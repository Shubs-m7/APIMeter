# UI Specification - APIMeter

**Project:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.1

---

## SECTION 1 — Application Navigation

- **Public Navigation:** Minimal. Exists only on `/login` and `/register`.
- **Protected Navigation:** Composed of a fixed Desktop Sidebar and a Top Navigation bar.
- **Sidebar Structure:** Overview, Projects, API Keys, Request Logs, Settings.

_(Terminology Note: The sidebar explicitly says "Request Logs" to prioritize UX, despite the underlying data being API Requests)._

---

## SECTION 2 — Application Sitemap

```text
/
├── (auth)
│   ├── /login
│   └── /register
└── /dashboard (Authenticated Root)
    ├── /               (Dashboard Overview)
    ├── /projects
    │   └── /[slug]     (Project Details - URL uses slug)
    ├── /keys
    ├── /logs           (Request Logs)
    ├── /analytics
    └── /settings
```

---

## SECTION 3 — Projects Page

- **Create Dialog:** Modal triggered by the New Project button. Requires `name` (text input) and `slug` (text input, auto-generated from name but editable).
- **Status Badges:** Projects display a badge for `ACTIVE` or `ARCHIVED`.
- **Archive Dialog:** "Danger Zone" modal requiring the user to type the project name to confirm archiving (Soft Delete).

---

## SECTION 4 — API Keys Page

- **Table:** Columns: Name, Prefix (`apim_a1b2c3...`), Status (Badge), Last Used At, Actions.
- **Status Badges:** `ACTIVE` (Green), `REVOKED` (Red), `EXPIRED` (Yellow).
- **Generate Dialog:** Requests a `name`.
- **Success Modal (CRITICAL):** Upon creation, a modal displays the raw key ONLY ONCE. Uses a masked input box with a "Copy to Clipboard" button. Once closed, the key is gone forever. (This is strictly enforced to match the Backend ADR that keys are never stored in plaintext).

---

## SECTION 5 — Request Logs Page

- **UI Terminology:** The page title is "Request Logs".
- **Table:** Columns: Timestamp, Endpoint, Method, Status, Latency (ms), Key Prefix.
- **API Dependencies:** Internally maps to `GET /api/v1/projects/:projectId/requests`.

---

## SECTION 6 — Settings Page

The settings page is divided into two primary sections/tabs:

- **Profile Settings:**
  - Avatar Upload
  - Name Input
  - Email Input
  - Password Reset Form
- **Application Preferences:**
  - Theme (Radio Group: Light, Dark, System)
  - Timezone (Dropdown Menu)
  - Date Format (Dropdown Menu: YYYY-MM-DD, MM/DD/YYYY, etc.)

---

## SECTION 7 — UI DECISIONS (Architecture Decision Records)

_(Generated from Architecture Revision v1.1)_

- **ADR-UI-1:** Keep "Request Logs" naming convention. **Reason:** UX familiarity. **Status:** Approved.
- **ADR-UI-2:** Create Project Modal exposes `slug`. **Reason:** Gives the user control over their vanity URL. **Status:** Approved.
- **ADR-UI-3:** Settings split into Tabs. **Reason:** Prevents a massive scrolling settings page and logical categorization. **Status:** Approved.
- **ADR-UI-4:** Key Success Modal is blocking. **Reason:** Because the raw key is never stored, the user MUST acknowledge they have copied it before proceeding. **Status:** Approved.

---

_End of UI Specification Document_
