#!/usr/bin/env bash
# Database bootstrap for ai_service. Must run as a Postgres SUPERUSER.
#
# - dev: mounted into /docker-entrypoint-initdb.d/, runs once when the pg_data volume is empty.
# - CI:  run explicitly with PGHOST/PGPASSWORD set (see .github/workflows/ci.yml).
#
# Why a superuser script: pgvector's vector.control has no `trusted = true`, so only a superuser can
# CREATE EXTENSION vector. The app and its migrations run as the limited role `mirra_ai` (B3 5-2:
# one DB user per schema). See docs/plans/skeleton.md section 8.1.
#
# Note: no `set -u` / `exit` here, because the postgres entrypoint may *source* this file.
set -eo pipefail

: "${POSTGRES_USER:?POSTGRES_USER is required}"
: "${POSTGRES_DB:?POSTGRES_DB is required}"
: "${AI_DB_PASSWORD:?AI_DB_PASSWORD is required}"
AI_DB_USER="${AI_DB_USER:-mirra_ai}"
AI_TEST_DB="${AI_TEST_DB:-${POSTGRES_DB}_test}"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v ai_user="$AI_DB_USER" -v ai_pass="$AI_DB_PASSWORD" -v test_db="$AI_TEST_DB" <<'SQL'
-- Role for ai_service (idempotent).
SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', :'ai_user', :'ai_pass')
WHERE NOT EXISTS (SELECT FROM pg_roles WHERE rolname = :'ai_user') \gexec

-- Separate database for integration tests (migration tests downgrade to base).
SELECT format('CREATE DATABASE %I', :'test_db')
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = :'test_db') \gexec
SQL

for db in "$POSTGRES_DB" "$AI_TEST_DB"; do
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$db" \
    -v ai_user="$AI_DB_USER" -v db="$db" <<'SQL'
-- CONNECT + CREATE lets mirra_ai create (and own) its schema `ai`; nothing else.
SELECT format('GRANT CONNECT, CREATE ON DATABASE %I TO %I', :'db', :'ai_user') \gexec
CREATE EXTENSION IF NOT EXISTS vector;
SQL
done

echo "init-ai: role ${AI_DB_USER}, databases ${POSTGRES_DB} and ${AI_TEST_DB}, extension vector ready"
