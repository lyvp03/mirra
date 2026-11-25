# ADR 0003: Catalog built from real photos (ACCESSORY slot, 4:5 images, on-model try-on input)

- Status: accepted (2026-11-24)
- Context: seed data `ai_service/data/seed/mirra-data.zip`; replaces the "AI-generated images"
  approach (`generate_images.py`, `gen.ps1`, 120 self-generated products, now archived in
  `mirra-data/_archive`).

## Context

The design assumed a self-generated catalog of 120 products with flat-lay images in 2:3. The real
catalog was built from real product photos instead:

- 193 products, 1008 SKUs (`MR###-C#-size`), 339 WebP images at 720×900 (4:5).
- Per category: blouses 51, tees 7, knitwear 6, pants 18, skirts 25, dresses 73, jackets 2,
  shoes 3, bags 8, jumpsuit 0 (the category exists but is empty).
- Every photo shows a model wearing the item. There are **no flat-lay images**.
- A photo of a model wearing a matching set (top + pants/skirt) becomes 2 products that share the
  image. Several angles of the same item and color become one product with images `-1/-2/-3`,
  and the front view is the primary image.
- Product names are English brand-style names, `<female first name> <type>` (Lily Mini Dress).
  A top and its matching bottom share the first name (Aurelia Top, Aurelia Pants). A descriptive
  Vietnamese name `name_vi` is kept for search.
- Sizes: clothing S–XL, shoes 35–39 (new chart `nu_giay`, by foot length), bags Freesize.

Several design rules no longer fit this data: the slot list, the 2:3 image ratio, the
Vietnamese-only content rule, and above all BR15 / UC17.4, which require a flat-lay image before
try-on can be enabled. Under that rule no real product could ever be tried on.

## Decision

1. **New slot `ACCESSORY`** in `categories.slot` (shoes, bags). Accessories never go into a set
   (BR20), and `try_on_enabled` is always false for them. That gives 10 seeded categories:
   `ao-so-mi-ao-kieu`, `ao-thun-croptop`, `ao-len-cardigan` (TOP); `quan`, `chan-vay` (BOTTOM);
   `dam-vay-lien`, `jumpsuit` (ONE_PIECE); `ao-khoac` (OTHER); `giay-dep`, `tui-xach` (ACCESSORY).
2. **Image ratio 4:5** (was 2:3), source images kept uncropped. Design System token
   `image-ratio` = 4/5.
3. **`products.name_vi varchar(200) NULL`**: shown as a secondary label and folded into
   `search_documents.content`. `products.name` holds the English brand name.
4. **No `view` column** in `product_images`. `position` orders the images within a color, and
   `position = 0` is the front view and primary image. The `view` field exists only in the seed
   manifest.
5. **On-model photos are valid try-on input.** For a color, the try-on reference image is the
   FLAT_LAY image if there is one, otherwise the MODEL image with the lowest `position`.
   `product_images.kind` keeps `MODEL, FLAT_LAY`, and FLAT_LAY becomes optional.
   - BR15 / UC17.4: a color must have a try-on reference image (flat-lay *or* model photo).
   - The error code stays `FLAT_LAY_REQUIRED` to avoid churning B5. It now also covers
     "accessory category".
   - `GET /internal/v1/variants` field `flat_lay_url` is renamed to **`tryon_image_url`**. No
     code used the old name yet.
   - B2 sequence `hasFlatLayForEachColor` is renamed to `hasTryOnImageForEachColor`.
6. **Set try-on (UC32.1)**: if both items share the same reference image (a matching set shot in
   one photo), that image is sent as is. Otherwise `OutfitComposer.compose(top, bottom)` merges the
   two reference images as before. `SetImageJobRunner` makes that choice. The `OutfitComposer`
   signature does not change.
7. **Try-on provider benchmark (B9)** gets a high-weight criterion: the provider must accept a
   garment photo worn by a model (e.g. FASHN) and pick the right item, including out of a set photo.
8. **Seed mapping**: `products.price` = `compare_at_price_vnd` if set, otherwise `price_vnd`. A
   product with `compare_at_price_vnd` gets one `promotions` row with `sale_price` = `price_vnd`.
9. **`product_variants.color_hex varchar(7) NULL`**, `CHECK color_hex ~ '^#[0-9a-f]{6}$'`: the swatch
   color. The seed copies it from the catalog. All 1008 SKUs pass the CHECK, and each
   (product, color) pair has exactly one hex value.
10. **`weight_gram` default per category** (seed only, no schema change). The catalog has no weights,
    and B4 requires `CHECK > 0` because BR11 shipping fees depend on it. Grams: ao-so-mi-ao-kieu 200,
    ao-thun-croptop 180, ao-len-cardigan 350, quan 400, chan-vay 300, dam-vay-lien 350, jumpsuit
    450, ao-khoac 600, giay-dep 700, tui-xach 500. Staff can edit them later (UC17.3).
11. **Jackets are an outer layer, not a set top.** BR20 used to list "áo khoác" (jackets) as a top,
    but the data has always given `ao-khoac` slot `OTHER` ("lớp ngoài phối cùng outfit"). BR20 is
    now aligned with the data: set tops are slot TOP only (blouses, tees, knitwear), and jackets
    never go into a set. The alternative, moving `ao-khoac` to TOP, was rejected because it would
    mean changing the seed data and a jacket over bare skin is not a realistic try-on.

## Changes applied

The sources in `../mirra-export/*.md` were edited and `docs/design/` was regenerated with
`scripts/split_design.py`:

| Doc | Change |
| --- | --- |
| B1 | BR20 excludes accessories and jackets (slot TOP/BOTTOM only); UC17.1 name fields; UC17.3 image rules; UC17.4 try-on reference; UC32.1 set reference image; UC12 reference image |
| B2 | OutfitComposer, Product, ProductImage descriptions; UC17.4 sequence; UC32 text |
| B3 | ICoreInternal description |
| B4 | `slot` CHECK + ACCESSORY; `products.name`, `name_vi`; `try_on_enabled`; `product_variants.color_hex`, `weight_gram` note; `product_images.kind`, `position` + note; `search_documents.content`; section 7 rows; section 8.3 seed rows (categories, size charts, catalog, default weights) |
| B5 | `PUT /admin/products/{id}/try-on` 409 text; `/variants` → `tryon_image_url`; `FLAT_LAY_REQUIRED` meaning |
| B6 | `SetImageJobRunner` skips composition when images are shared |
| B7 | `try_on_enabled` comment; `start_tryon` check; category slug example |
| B8 | 2:3 → 4:5 (three places) |
| B9 | Benchmark criterion + comparison row; test data description |
| B8 mockup exports (`mirra-export/mockups/*.html`) | Unpacked the gzip+base64 bundles: `--image-ratio` 2/3 → 4/5, the placeholder comment, the try-on dropzone, the "Tỉ lệ 4:5" caption (50 entries in 6 files) |
| [Design System Mirra](https://claude.ai/artifact/9b6hjNcuM5S8zNuxjJwZ1h) (v8) | `image-ratio` token 4/5; README imagery rule and product naming rule; ProductCard, ProductsCard, OutfitCard (BR20) READMEs; TryOnPanel and Cover previews |
| [Mirra B8 Mockups](https://claude.ai/artifact/JcW5sBZNfPepKtmZzRZwhU) canvas (v38) | `ds/mirra/tokens.css` and `tokens.json`; `screens.css` comment; S21 dropzone; A04 caption |

## Consequences / not done here

- `seed.py` (Postgres + MinIO) is written in the code phase against the real ORM. It applies
  decisions 8–10.
- Mockup screens still show sample text from the old catalog (names like "Đầm Ngắn Linh Lan", and
  the slot dropdown in A04 without ACCESSORY or a `name_vi` field). They only illustrate the layout
  and are left as they are.
