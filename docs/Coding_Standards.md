# Engineering Coding Standards - APIMeter

**Project:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.1

---

## SECTION 1 — Folder Naming

Folder names must be lowercase and use `kebab-case`. Never abbreviate folder names.

*   `modules/` (Feature boundaries)
    *   `api-requests/` (Standardized domain for raw logs)
    *   `projects/`
    *   `api-keys/`
*   `lib/` (Shared internal libraries)
*   `validators/` (Zod schemas)

---

## SECTION 2 — Security Standards

*   **API Key Hashing (CRITICAL):** Plaintext API Keys must NEVER be stored in the database. Incoming API keys must be hashed using SHA-256 and compared against the `hashedKey` stored in the database.
*   **Password Hashing:** Use `bcryptjs` or `argon2`. Never store plain-text passwords.
*   **JWT Handling:** Store session tokens in `HttpOnly`, `Secure`, `SameSite=Lax` cookies.

---

## SECTION 3 — Coding Standards Decisions (Architecture Decision Records)

*(Generated from Architecture Revision v1.1)*
*   **ADR-CODE-1:** Security standards mandated to include key hashing. **Reason:** To align with Backend security constraints preventing plaintext API key storage. **Status:** Approved.
*   **ADR-CODE-2:** Module naming `api-requests` strictly mandated. **Reason:** Domain alignment. **Status:** Approved.

---
*End of Engineering Coding Standards Document*
