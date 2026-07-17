# Frontend Architecture Specification - APIMeter

**Project:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.1

---

## SECTION 1 — Architecture Philosophy

**Selected Architecture:** Feature-First Frontend Architecture

APIMeter utilizes a Feature-First structure where components, hooks, schemas, and services related to a specific domain are co-located in a dedicated module.

---

## SECTION 2 — Complete Folder Structure

```text
frontend/
├── src/
│   ├── features/               # FEATURE-FIRST MODULES (Core logic)
│   │   ├── auth/               # Auth components & hooks
│   │   ├── projects/           # Projects components & hooks
│   │   ├── api-keys/           # API Keys components & hooks
│   │   ├── api-requests/       # API Requests components & hooks (Displays as "Request Logs" in UI)
│   │   ├── analytics/          # Analytics charts & hooks
│   │   └── settings/           # Profile & Preferences components
```

---

## SECTION 3 — Feature Modules

### 1. Projects Module
*   **Responsibilities:** Managing Project environments.
*   **Public Interface:** `ProjectList`, `CreateProjectModal`, `useProjects()`.
*   **Schemas:** Zod schema updated to strictly validate URL-safe `slug` formats during creation.

### 2. API Keys Module
*   **Responsibilities:** Key generation, rotation, and revocation.
*   **Public Interface:** `ApiKeyTable`, `GenerateKeyModal`.
*   **Enums Handled:** Translates `ACTIVE`, `REVOKED`, and `EXPIRED` into corresponding Badge UI colors.

### 3. API Requests Module (UI Name: "Request Logs")
*   **Terminology Rule:** The frontend codebase strictly uses the module name `api-requests` and types like `ApiRequest` to map to the backend API. However, all UI rendering (Buttons, Page Titles, Navigation) must display the user-friendly string: **"Request Logs"**.

### 4. Settings Module
*   **Responsibilities:** Split into two distinct tabs/sub-modules:
    *   **Profile Settings:** Name, Email, Password, Avatar.
    *   **Application Preferences:** Theme (Light/Dark/System), Timezone, Date Format.

---

## SECTION 4 — State & Data Fetching

*   **TanStack Query:** Handles fetching projects, keys, and requests.
*   **Optimistic Updates:** When archiving a project (Status -> `ARCHIVED`), immediately remove it from the active list UI.

---

## SECTION 5 — FRONTEND DECISIONS (Architecture Decision Records)

*(Generated from Architecture Revision v1.1)*
*   **ADR-FE-1:** Module `request-logs` renamed to `api-requests`. **Reason:** Consistency with backend API. **Status:** Approved.
*   **ADR-FE-2:** UI continues displaying "Request Logs". **Reason:** Prevents user confusion between API Keys and API Requests. "Logs" is a recognizable industry standard for audit trails. **Status:** Approved.
*   **ADR-FE-3:** Projects require a `slug` input. **Reason:** To support future SEO/Vanity URLs. The frontend form will auto-generate the slug based on the project name, but allow manual overrides. **Status:** Approved.
*   **ADR-FE-4:** Settings UI split into distinct Profile and Preferences tabs. **Reason:** Improved UX and logical grouping of mutable state. **Status:** Approved.
*   **ADR-FE-5:** Badges map to `ACTIVE`, `REVOKED`, `EXPIRED`, and `ARCHIVED`. **Reason:** Synchronization with updated global Enums. **Status:** Approved.

---
*End of Frontend Architecture Specification*
