# Product Requirements Document (PRD)

**Project Name:** APIMeter
**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform
**Version:** 1.0.0
**Status:** Approved

---

## 1. PROJECT OVERVIEW

APIMeter is a cloud-based SaaS platform designed to solve the critical challenges of API key lifecycle management and usage tracking. It empowers developers and organizations to securely generate, rotate, and revoke API keys, organize them into distinct projects, and monitor API usage in real-time.
With an interface inspired by industry leaders like Stripe, Supabase, and Vercel, APIMeter delivers a modern, minimal, and highly secure developer experience. It provides deep analytical insights, audit trails, and granular control over API infrastructure, abstracting away the complexity of building custom API management systems.

## 2. PRIMARY USERS

- **Individual Developers:** Building side projects or integrating third-party APIs.
- **Freelancers:** Managing multiple client projects and requiring isolated API keys.
- **Startup Teams:** Needing shared access to API keys without compromising security.
- **Small Businesses:** Looking for out-of-the-box API management without enterprise costs.
- **SaaS Companies:** Requiring scalable infrastructure to track their own customers' API usage.
- **Agencies:** Handling diverse client portfolios securely.
- **Internal Engineering Teams:** Managing microservices and internal tool API access.

## 3. PROBLEM STATEMENT

**What problems do developers currently face?**
Developers often resort to hardcoding API keys, sharing them via insecure channels (like Slack or email), or building rudimentary, error-prone custom dashboards to track usage. Managing multiple environments (staging, production) across multiple projects quickly becomes a chaotic nightmare.

**What security risks exist?**

- **Key Leakage:** Accidental commits to public repositories or exposure in client-side code.
- **Lack of Rotation:** Keys remain active indefinitely because rotating them requires manual database updates and deployment coordination.
- **No Audit Trail:** When a key is compromised, there is no way to trace which developer generated it or when it was accessed.
- **Over-privileged Keys:** Keys often have global access rather than scoped permissions.

**What operational challenges exist?**

- **Usage Blind Spots:** No visibility into which keys are consuming the most resources.
- **Rate Limiting Complexity:** Implementing custom rate limiting per key is technically demanding.
- **Resource Drain:** Engineering hours are wasted building and maintaining internal admin panels instead of core product features.

**Why should APIMeter exist?**
APIMeter exists to democratize enterprise-grade API key management. It provides a secure, reliable, and aesthetically pleasing platform that allows developers to focus on building their product, knowing their API infrastructure is secure, auditable, and analytically tracked.

## 4. PRODUCT VISION

**The 3–5 Year Horizon:**
APIMeter will evolve from a standalone API key management dashboard into a comprehensive API Gateway and Developer Portal ecosystem.

- **Year 1-2:** Dominate key management and analytics. Become the default choice for modern SaaS startups.
- **Year 3-4:** Introduce intelligent threat detection (AI-driven anomaly detection for API usage spikes), automated rate limiting based on dynamic pricing tiers, and seamless integration with major cloud providers (AWS API Gateway, Cloudflare Workers).
- **Year 5:** Launch customizable Developer Portals where our customers can instantly generate API documentation, onboarding flows, and billing management for _their_ end-users, powered entirely by APIMeter's backend.

## 5. BUSINESS GOALS

- **Increase Security:** Provide a zero-trust model for API key generation and storage.
- **Simplify API Management:** Reduce the time it takes a developer to provision and distribute a new API key from hours to seconds.
- **Improve Monitoring:** Offer real-time insights to detect abuse or unoptimized API consumption instantly.
- **Reduce Operational Complexity:** Eliminate the need for companies to build internal admin dashboards.
- **Developer Experience (DX):** Achieve a Net Promoter Score (NPS) of 70+ by delivering a flawless, Vercel-like UI.
- **Scalability:** Support 10,000+ active projects and process 1B+ API logs monthly within the first year.

## 6. PRODUCT GOALS

- Deliver a seamless, sub-second latency dashboard experience.
- Ensure 100% secure storage of API keys (hashed/encrypted at rest).
- Provide actionable analytics that developers can actually understand without deep data science knowledge.
- Maintain a frictionless onboarding flow (time-to-first-key < 60 seconds).

## 7. SUCCESS METRICS (KPIs)

- **Daily Active Users (DAU):** Target 1,000 within 6 months.
- **Monthly Active Users (MAU):** Target 5,000 within 6 months.
- **Project Creation:** Average of 2.5 projects created per active user.
- **API Key Creation:** 10,000+ keys generated in the first quarter.
- **API Calls Tracked:** 100 Million requests processed and logged per month.
- **Average Session Duration:** < 3 minutes (indicating efficiency; users get in, get keys, and get out).
- **Retention:** 85% Month-over-Month retention rate.
- **Performance Targets:** P95 API response time < 50ms; Dashboard initial load < 1.5s.

## 8. USER PERSONAS

### 1. Solo Developer (Sam)

- **Goals:** Build and launch side projects quickly. Securely store third-party API keys (OpenAI, Stripe).
- **Pain Points:** Too many `.env` files scattered across different machines. No easy way to see if a side project is blowing up in API costs.
- **Motivations:** Speed, cost-efficiency, and modern DX.
- **Daily Workflow:** Commits code, deploys to Vercel, checks dashboard to ensure API isn't failing.
- **Technical Knowledge:** High. Prefers CLI and minimal UIs.

### 2. Startup Founder (Fiona)

- **Goals:** Ensure the company's proprietary API is secure. Track which beta customers are using the API the most.
- **Pain Points:** Developers are sharing keys in Slack. No central dashboard to show investors API traction.
- **Motivations:** Security compliance, business growth metrics, team collaboration.
- **Daily Workflow:** Reviews daily usage metrics, invites new engineers to the workspace, generates keys for B2B partners.
- **Technical Knowledge:** Medium. Needs visual charts and straightforward access controls.

### 3. Backend Engineer (Ben)

- **Goals:** Implement robust rate limiting and key validation in the company's microservices.
- **Pain Points:** Building custom API middleware is tedious. Rotating keys requires downtime.
- **Motivations:** Reliability, automation, API documentation.
- **Daily Workflow:** Writes API endpoints, integrates APIMeter SDK/API for validation, checks error logs.
- **Technical Knowledge:** Very High. Cares about API response times, SLA, and webhook integrations.

### 4. Engineering Manager (Elena)

- **Goals:** Enforce security policies across multiple teams. Audit who accessed what and when.
- **Pain Points:** No visibility into staging vs. production keys. Compliance audits (SOC2) are a nightmare.
- **Motivations:** Risk mitigation, compliance, team efficiency.
- **Daily Workflow:** Reviews audit logs, manages RBAC (Role-Based Access Control), revokes compromised keys.
- **Technical Knowledge:** High, but focused on architecture and process rather than writing code.

## 9. USER STORIES

**Authentication & Onboarding**

1. As a user, I want to sign up using GitHub so that I don't have to create a new password.
2. As a user, I want to sign up via email and password so that I have a traditional account.
3. As a user, I want to receive a verification email to secure my account.
4. As a user, I want to reset my password via email if I forget it.
5. As a user, I want to enable Two-Factor Authentication (2FA) so that my account is protected against unauthorized access.
6. As a user, I want to log out of all active sessions from my settings page.
7. As a user, I want to view my profile details (Name, Email, Avatar) in the dashboard.
8. As a user, I want to update my profile name and avatar.
9. As a user, I want to delete my account and purge all my data to comply with privacy laws.
10. As a user, I want to see a welcoming onboarding flow when I first log in to help me create my first project.

**Project Management** 11. As a developer, I want to create a new project so that I can group my API keys logically. 12. As a developer, I want to name my project and provide an optional description. 13. As a developer, I want to view a list of all my projects on the main dashboard. 14. As a developer, I want to edit a project's name and settings. 15. As a developer, I want to delete a project, which cascades to delete all associated keys and logs. 16. As a manager, I want to invite team members to a project via email. 17. As a manager, I want to assign roles (Admin, Viewer) to team members within a project. 18. As a manager, I want to remove a team member from a project. 19. As a user, I want to seamlessly switch between different projects using a top navigation dropdown. 20. As a user, I want to see a high-level summary of API usage for a project on its overview page.

**API Key Lifecycle** 21. As a developer, I want to generate a new API key with a single click. 22. As a developer, I want to assign a memorable name to an API key (e.g., "Mobile App Prod"). 23. As a developer, I want to define an expiration date for an API key so it automatically invalidates. 24. As a developer, I want to see the unmasked API key _only once_ immediately after creation for security. 25. As a developer, I want to easily copy the API key to my clipboard with a button click. 26. As a developer, I want to view a list of all active and revoked API keys in a project. 27. As a developer, I want to revoke an API key manually if I suspect it has been compromised. 28. As a developer, I want to seamlessly "roll" an API key (generate a new one while keeping the old one active for a grace period). 29. As a developer, I want to search for a specific API key by name or prefix. 30. As a developer, I want to filter the API key list by status (Active, Expired, Revoked).

**Usage & Analytics** 31. As a founder, I want to view a chart showing API requests over the last 24 hours, 7 days, and 30 days. 32. As a backend engineer, I want to see the total number of successful vs. failed API requests. 33. As a backend engineer, I want to view a detailed log table of every API request made using my keys. 34. As a backend engineer, I want the request log to show timestamp, IP address, endpoint, status code, and latency. 35. As a backend engineer, I want to filter request logs by specific API keys or status codes (e.g., show only 4xx errors). 36. As a manager, I want to export usage logs as a CSV file for compliance reporting. 37. As a founder, I want to see which specific API key is consuming the most requests (Top Consumers). 38. As a developer, I want real-time (or near real-time) updates on my analytics dashboard.

**System & Settings** 39. As a user, I want the dashboard to support Dark Mode for better eye comfort. 40. As a user, I want the interface to be fully responsive so I can revoke a key from my mobile phone in an emergency.

## 10. CORE FEATURES

### 10.1 Authentication & Authorization

- **Description:** Secure access to the APIMeter platform.
- **Business Value:** Protects user data and prevents unauthorized infrastructure access.
- **Priority:** Must Have
- **Dependencies:** Database (User table), Auth.js.
- **Acceptance Criteria:** Users can sign up, log in, manage sessions, and recover passwords securely. Passwords hashed via bcrypt.

### 10.2 Project Workspace

- **Description:** Logical separation of keys and logs.
- **Business Value:** Allows agencies and startups to organize data by environment (Staging vs. Prod) or client.
- **Priority:** Must Have
- **Dependencies:** Authentication.
- **Acceptance Criteria:** Users can create, edit, delete, and switch between projects seamlessly.

### 10.3 API Key Management Engine

- **Description:** Core CRUD operations for API keys.
- **Business Value:** The primary functionality of the product.
- **Priority:** Must Have
- **Dependencies:** Project Workspace, Cryptography module.
- **Acceptance Criteria:** Keys are securely generated with a prefix (e.g., `apm_live_...`). Full key is shown once. Keys can be revoked instantly.

### 10.4 Usage Analytics Dashboard

- **Description:** Visual representation of API consumption.
- **Business Value:** Provides immediate insights into system health and customer usage.
- **Priority:** Must Have
- **Dependencies:** Key Management, Request Logging API.
- **Acceptance Criteria:** Displays line charts for request volume, error rates, and top keys. Data is aggregatable by time periods.

### 10.5 Real-Time Activity & Request Logs

- **Description:** Detailed tabular view of incoming API requests.
- **Business Value:** Essential for debugging, auditing, and compliance.
- **Priority:** Should Have
- **Dependencies:** Analytics Dashboard.
- **Acceptance Criteria:** Searchable, filterable, and paginated table showing granular request details.

### 10.6 Team Collaboration (RBAC)

- **Description:** Inviting members and assigning permissions.
- **Business Value:** Enables B2B adoption and enterprise usage.
- **Priority:** Should Have
- **Dependencies:** Authentication, Projects.
- **Acceptance Criteria:** Owners can invite users via email. Viewers cannot create or revoke keys.

### 10.7 Dark Mode & Responsive UI

- **Description:** Aesthetically pleasing and mobile-friendly interface.
- **Business Value:** High Developer Experience (DX) standard.
- **Priority:** Must Have
- **Dependencies:** Shadcn UI, Tailwind CSS.
- **Acceptance Criteria:** UI toggles flawlessly between Light and Dark modes. Dashboard is fully usable on mobile devices.

## 11. FEATURE PRIORITIZATION (MoSCoW)

**Must Have:**

- User Registration / Login.
- Project Creation / Deletion.
- API Key Generation (Show once, hash in DB).
- API Key Revocation.
- Basic Analytics Dashboard (Total Requests, Error Rate).
- API Endpoint for validating keys (The core service).
- Dark Mode & Responsive UI.

**Should Have:**

- Detailed Request Logging table with Pagination.
- Filtering and Searching of Keys and Logs.
- Team Member Invites and Basic Roles.
- Key Expiration Dates.
- Key Prefixing (e.g., `apm_test_...`).

**Could Have:**

- API Key Rolling (Grace periods).
- CSV Export for Logs.
- Custom Rate Limiting per key.
- Webhooks for key revocation events.

**Won't Have (Version 1):**

- Advanced AI Anomaly Detection.
- Custom Domain Setup for Developer Portals.
- SAML / SSO Enterprise Login.
- Billing integrations for end-users.

## 12. BUSINESS RULES

1.  **Project Limits:** Free tier users are limited to 3 projects.
2.  **Key Limits:** Free tier users are limited to 10 active keys per project.
3.  **Key Visibility:** An API key is displayed in plain text _only once_ at the time of creation. It can never be retrieved again.
4.  **Key Storage:** Keys must be securely hashed (e.g., SHA-256) in the database. Only the prefix and last 4 characters are stored in plain text for UI identification.
5.  **Uniqueness:** API key hashes must be globally unique.
6.  **Deletions:** Deleting a project is a hard delete and cascades to all keys and logs. Revoking a key is a soft action (status change), but deleting a key purges it.
7.  **Ownership:** The user who creates a project is the `OWNER`. Ownership cannot be transferred in V1.
8.  **Validation:** All API endpoints must enforce strict input validation using Zod.

## 13. EDGE CASES

- **Authentication:** User attempts to sign up with an existing email via a different provider (OAuth vs. Credentials). Handled by account linking or rejecting duplicate emails.
- **Projects:** Two users attempt to name a project the exact same thing (Allowed, IDs are unique).
- **API Keys:** User clicks "Generate" twice rapidly (debounce UI, ensure idempotency).
- **API Keys:** User attempts to revoke an already revoked key (No-op, return 200).
- **Analytics:** User requests 1 year of data, causing DB strain (Enforce maximum date range of 30 days for V1).
- **Deletion:** User deletes a project while an API request is actively being processed (Validation API should fail gracefully with 401).
- **Rate Limiting:** A malicious user tries to brute force the login page or API key validation endpoint (IP-based rate limiting required).
- **Network Failures:** Database goes down (Display friendly 503 error page, do not expose stack trace).

## 14. NON-FUNCTIONAL REQUIREMENTS

- **Performance:** Dashboard SPA must become interactive in under 1.5 seconds. API Key validation endpoint must respond in < 50ms (P95).
- **Scalability:** Database must handle millions of log rows. (Requires proper indexing on `projectId` and `createdAt`).
- **Availability:** Target 99.9% uptime.
- **Security:** Follow OWASP Top 10. No exposed secrets.
- **Accessibility:** UI must meet WCAG 2.1 AA standards (contrast ratios, keyboard navigation, aria-labels).
- **Reliability:** Log insertion must not block API key validation (asynchronous logging).
- **Maintainability:** Strict adherence to Clean Architecture and SOLID principles. 100% TypeScript coverage.
- **Responsiveness:** Fluid grid layouts adapting from 320px (mobile) to 2560px (ultrawide).

## 15. SECURITY REQUIREMENTS

- **Password Security:** Passwords hashed using `bcrypt` with a minimum cost factor of 12. Minimum length 8 characters.
- **Authentication:** JWT or secure HTTP-only cookies via Auth.js.
- **Authorization:** Middleware checks on every API route to ensure user owns the `projectId` being accessed.
- **API Security:** CORS configured strictly. CSRF tokens for form submissions.
- **Session Security:** Sessions expire after 7 days. Password resets invalidate all active sessions.
- **Logging:** PII (Personally Identifiable Information) must never be stored in the request logs.
- **Audit Trails:** Every key creation, revocation, and project modification must be logged internally.
- **Rate Limiting:** Global rate limiting on public API endpoints (e.g., 100 req/min per IP for validation).
- **Input Validation:** Strict server-side Zod validation for all payloads. Reject unknown fields.

## 16. PERFORMANCE TARGETS

| Metric                      | Target       |
| :-------------------------- | :----------- |
| Dashboard Initial Load      | < 1.5s       |
| SPA Route Transitions       | < 200ms      |
| API Key Validation Endpoint | < 50ms (P95) |
| Analytics Query (30 days)   | < 800ms      |
| Log Search/Filter           | < 500ms      |

## 17. PRODUCT CONSTRAINTS

- **Time Constraints:** Version 1 must be MVP-ready in 4-6 weeks.
- **Technical Constraints:** Must deploy frontend and backend to Vercel (serverless constraints, execution timeouts). Database is Neon PostgreSQL (connection pooling required).
- **Budget Constraints:** Zero cost infrastructure for MVP (utilizing Vercel Free Tier, Neon Free Tier).
- **Deployment Constraints:** CI/CD pipeline must pass all linting and type checks before deployment.

## 18. FUTURE ROADMAP

- **Version 1.0 (Current):** Core Key Management, Basic Analytics, Projects.
- **Version 1.5:** Advanced Filtering, CSV Exports, Team Invites (RBAC).
- **Version 2.0:** Rate Limiting per API Key, Key Rolling, Webhooks.
- **Version 3.0:** Custom Developer Portals for end-users, Subscription Billing Integrations.
- **Future AI Features:** AI Anomaly Detection ("Unusual spike in API usage detected from IP block X").
- **Future Enterprise Features:** SAML/SSO, Custom Log Retention, VPC Peering.

## 19. COMPETITOR ANALYSIS

### Stripe Dashboard

- **Strengths:** Best-in-class UX/UI. Extremely clear key management (Test vs Live mode).
- **Weaknesses:** Not a standalone API product (tied to payments).
- **APIMeter Opportunity:** Replicate the "Test/Live" mode clarity and instant key rolling experience.

### Supabase

- **Strengths:** Excellent developer onboarding. Clean settings architecture.
- **Weaknesses:** API keys are tied heavily to their specific BaaS ecosystem.
- **APIMeter Opportunity:** Provide that same level of DX but agnostic to the backend database.

### Postman

- **Strengths:** Massive feature set for API testing.
- **Weaknesses:** Cluttered, bloated, desktop-heavy. Focuses on testing, not production key issuance.
- **APIMeter Opportunity:** Keep it minimal, web-first, focusing purely on management and monitoring.

### Unique Selling Points (USPs) for APIMeter

1.  **Laser-focused:** Does one thing (API Keys) exceptionally well. No bloat.
2.  **Design-first:** A dashboard that developers are proud to look at.
3.  **Instant Setup:** Deployable and usable in seconds.

## 20. ASSUMPTIONS

1.  Developers are comfortable managing their environment variables to connect to APIMeter.
2.  Vercel Serverless functions can handle the expected API validation load without severe cold-start penalties affecting the 50ms target.
3.  Neon PostgreSQL's serverless connection pooling will efficiently manage connections from Vercel.
4.  Users will initially prefer a hosted SaaS solution over self-hosting.

## 21. RISKS

- **Technical Risks:** Vercel cold starts slowing down API key validation. (Mitigation: Edge functions or keeping functions warm).
- **Business Risks:** Developers might just build their own simple key table instead of using APIMeter. (Mitigation: Focus heavily on the Analytics and DX value proposition).
- **Security Risks:** A vulnerability in our key hashing logic could expose customer infrastructure. (Mitigation: Strict adherence to established crypto libraries, external audits).
- **Scalability Risks:** Storing millions of request logs could bloat the Postgres database quickly. (Mitigation: Implement partitioning on the `RequestLog` table or plan migration to a time-series DB like ClickHouse later).

## 22. OUT OF SCOPE (Version 1)

- SAML / SSO integration.
- GraphQL API support (REST only for V1).
- Monetization / Billing engine (Free to use initially).
- Time-series database integration (Postgres will be used for V1 logs).
- Custom domains.
- AI features.

---

_End of Document_
