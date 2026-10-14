---
name: database-design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Database Design

> **Learn to THINK, not copy SQL patterns.**

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `database-selection.md` | PostgreSQL vs Neon vs Turso vs SQLite | Choosing database |
| `database-security.md` | SQL Injection, RLS, SSL & Secret Hardening | Hardening data layer |
| `orm-selection.md` | Drizzle vs Prisma vs Kysely | Choosing ORM |
| `schema-design.md` | Normalization, PKs, relationships | Designing schema |
| `indexing.md` | Index types, composite indexes | Performance tuning |
| `optimization.md` | N+1, EXPLAIN ANALYZE | Query optimization |
| `migrations.md` | Safe migrations, serverless DBs | Schema changes |

---

## 🔒 Database Security & Hardening (Critical)

1. **SQL Injection Prevention:**
   - NEVER use string concatenation or template literals (`$queryRawUnsafe("... ${input}")`).
   - ALWAYS use parameterized queries or type-safe ORMs (Prisma, Drizzle, Kysely).
2. **Row Level Security (RLS):**
   - In PostgreSQL / Supabase, every public table MUST have RLS enabled (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY;`).
   - Never expose `service_role` key in frontend code; keep it strictly in serverless/backend endpoints.
3. **Data Protection & PII:**
   - Passwords must be hashed with `bcrypt`/`argon2` (never plaintext or MD5/SHA1).
   - Sensitive fields (`password_hash`, `tokens`, `internal_notes`) must be excluded from public API responses (`select: { password: false }`).
4. **Connection Pooling & SSL:**
   - Production connections MUST enforce `sslmode=require`.
   - Use connection poolers (PgBouncer, Neon pooling) to prevent connection starvation (DDoS vulnerability).
5. **Zero-Downtime Safe Migrations:**
   - Never drop columns without a 2-phase migration (expand and contract).
   - Add nullable columns or provide defaults to prevent locking large tables.

---

## ⚠️ Core Principle

- ASK user for database preferences when unclear
- Choose database/ORM based on CONTEXT
- Don't default to PostgreSQL for everything
- Security first: validate inputs, enforce RLS, protect credentials

---

## Decision Checklist

Before designing schema:

- [ ] Asked user about database preference?
- [ ] Chosen database for THIS context?
- [ ] Considered deployment environment?
- [ ] Row Level Security (RLS) configured?
- [ ] SQL Injection vector eliminated (prepared statements)?
- [ ] SSL connection enabled (`sslmode=require`)?
- [ ] Planned index strategy?
- [ ] Defined relationship types?

---

## Anti-Patterns

❌ Default to PostgreSQL for simple apps (SQLite may suffice)
❌ Raw SQL queries with string interpolation
❌ Exposing Supabase `service_role` in Vite/React client
❌ Storing plain passwords or weak hashes
❌ Leaving tables without RLS in Supabase/PostgreSQL
❌ Skip indexing on foreign keys
❌ Use SELECT * in production
❌ Store JSON when structured data is better
❌ Ignore N+1 queries
