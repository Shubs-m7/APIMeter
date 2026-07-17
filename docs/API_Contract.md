# REST API Contract - APIMeter

**Project:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.1

---

## SECTION 1 — API OVERVIEW

This document serves as the exact contract for all HTTP communication between the Next.js Client (or external consumers) and the Next.js API Routes (`/api/v1/*`).

*   **Base URL:** `https://api.apimeter.com/api/v1` (Production) / `http://localhost:3000/api/v1` (Local)
*   **Data Format:** JSON exclusively.
*   **Terminology Note:** The UI may use the term "Request Logs", but all internal APIs strictly use `/requests` to represent raw API Request data.

---

## SECTION 2 — CORE STANDARDS

| Concept | Standard |
| :--- | :--- |
| **Methods** | `GET` (Read), `POST` (Create), `PATCH` (Partial Update), `DELETE` (Archive/Remove). |
| **Idempotency** | Repeating a `DELETE` request on an already deleted resource returns `200 OK`, not `404`. |
| **Authentication** | Session-based (NextAuth) for dashboard APIs. Bearer token for Edge Validation API. |
| **Pagination** | `limit` (max 100), `page` (Offset) for Projects. `limit`, `cursor` for API Requests. |
| **Search Standard** | Query parameters (e.g., `?q=searchterm`). |

---

## SECTION 3 — STANDARD RESPONSE FORMAT

All API responses strictly adhere to a consistent wrapper format to simplify frontend parsing.

**Standard Success Response (2xx)**
```json
{
  "success": true,
  "data": { ... },
  "meta": {
    "pagination": { "total": 100, "page": 1, "limit": 10 }
  },
  "timestamp": "2026-07-16T12:00:00.000Z",
  "requestId": "req_abc123"
}
```

---

## SECTION 4 — PROJECT MODULE

### Create Project
*   **Method / URL:** `POST /api/v1/projects`
*   **Request Schema:** `{ "name": "string", "slug": "string(unique, url-safe)", "description": "string?" }`
*   **Response:** `201 Created`, Project object.

### List Projects
*   **Method / URL:** `GET /api/v1/projects`
*   **Response:** `200 OK`, Array of Projects (Includes `status: ACTIVE | ARCHIVED`).

### Delete (Archive) Project
*   **Method / URL:** `DELETE /api/v1/projects/:id`
*   **Response:** `200 OK`. Soft deletes project (changes status to `ARCHIVED`).

---

## SECTION 5 — API KEY MODULE

### Generate Key
*   **Method / URL:** `POST /api/v1/projects/:projectId/keys`
*   **Request Schema:** `{ "name": "string" }`
*   **Response:** `201 Created`. **CRITICAL:** Returns `{ "apiKey": { "id": "...", "status": "ACTIVE" }, "rawKey": "apim_..." }`. This is the ONLY time `rawKey` is ever transmitted.

### List Keys
*   **Method / URL:** `GET /api/v1/projects/:projectId/keys`
*   **Response:** `200 OK`. Array of Keys (Includes `lastUsedAt`, excludes plain-text key entirely).

### Revoke Key
*   **Method / URL:** `PATCH /api/v1/projects/:projectId/keys/:keyId/revoke`
*   **Response:** `200 OK`. Updates status to `REVOKED`.

### Edge Validation (Internal API)
*   **Method / URL:** `POST /api/v1/validate`
*   **Request:** `Authorization: Bearer apim_...`
*   **Process:** The backend hashes the incoming Bearer token and compares it against `hashedKey` in the DB.
*   **Response:** `200 OK` (Valid) or `401 Unauthorized` (Invalid/Revoked/Expired).

---

## SECTION 6 — API REQUEST MODULE (Formerly Request Logs)

### List Requests
*   **Method / URL:** `GET /api/v1/projects/:projectId/requests`
*   **Query Params:** `?limit=50&cursor=cuid123`
*   **Response:** `200 OK`. Array of `ApiRequest` objects.

---

## SECTION 7 — ANALYTICS MODULE

*(Note: Analytics are served via an Aggregation Layer that safely queries API Requests without exposing raw rows).*

### Dashboard Summary
*   **Method / URL:** `GET /api/v1/projects/:projectId/analytics/summary`
*   **Response:** `200 OK`. `{ "totalRequests": 1500, "errorRate": 2.5, "avgLatency": 45 }`

---

## SECTION 8 — ACTIVITY LOG MODULE

### List Timeline
*   **Method / URL:** `GET /api/v1/projects/:projectId/activity`
*   **Response:** `200 OK`. Array of audit events matching `{ "entityType": "...", "entityId": "...", "action": "...", "actorId": "...", "metadata": {}, "timestamp": "..." }`.

---

## SECTION 9 — SETTINGS MODULE

### Update Profile Settings
*   **Method / URL:** `PATCH /api/v1/settings/profile`
*   **Request Schema:** `{ "name": "string?", "email": "string?", "password": "string?", "avatar": "string?" }`
*   **Response:** `200 OK`.

### Update Application Preferences
*   **Method / URL:** `PATCH /api/v1/settings/preferences`
*   **Request Schema:** `{ "theme": "light|dark|system", "timezone": "string", "dateFormat": "string" }`
*   **Response:** `200 OK`.

---

## SECTION 10 — API DECISIONS (Architecture Decision Records)

*(Generated from Architecture Revision v1.1)*
*   **ADR-API-1:** Rename route `/logs` to `/requests`. **Reason:** Internal terminology alignment. **Status:** Approved.
*   **ADR-API-2:** `rawKey` explicitly isolated in the POST response. **Reason:** Enforces standard that keys are never fetchable after creation. **Status:** Approved.
*   **ADR-API-3:** Projects require a `slug` payload. **Reason:** SEO/URL friendly routing in the dashboard. **Status:** Approved.
*   **ADR-API-4:** Settings split into `/profile` and `/preferences`. **Reason:** Separation of concerns. Security updates (Profile) vs UX updates (Preferences). **Status:** Approved.

---
*End of REST API Contract*
