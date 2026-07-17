# APIMeter (v1.2)

**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform

## Project Overview

APIMeter is a scalable platform designed to manage API keys and track usage in real-time. It provides developers and administrators with deep insights into their API's performance and usage constraints.

## Architecture

This project is structured as a **Turborepo** monorepo using **pnpm**.

### Folder Structure

```text
apimeter/
├── apps/
│   ├── backend/         (Standalone Express.js / TypeScript API)
│   └── frontend/        (Next.js Web Application)
├── packages/
│   ├── shared-types/    (TypeScript types and interfaces)
│   ├── shared-utils/    (Common helper functions)
│   ├── validation/      (Shared Zod schemas & helpers)
│   ├── eslint-config/   (Shared ESLint configurations)
│   └── tsconfig/        (Shared TypeScript configurations)
├── docs/                (Project documentation)
├── .ai/                 (AI context and logs)
├── docker/              (Dockerfiles and compose configs)
├── scripts/             (Utility scripts)
└── .github/workflows/   (CI/CD pipelines)
```

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v20+)
- [pnpm](https://pnpm.io/) (v9+)

### Installation

1. Install dependencies:
   ```bash
   pnpm install
   ```
2. Run the development server:
   ```bash
   pnpm dev
   ```

## Tech Stack

- **Language:** TypeScript
- **Package Manager:** pnpm
- **Monorepo Tool:** Turborepo
- **Backend:** Express.js, Prisma ORM, PostgreSQL, Zod, Pino, Helmet
- **Frontend:** Next.js
- **Testing:** Vitest, Supertest

## Sprint 0 Roadmap

- **Task 0.1:** Monorepo Foundation
- **Task 0.2:** Express Backend Foundation
- **Task 0.3:** Next.js Frontend Foundation
- **Task 0.4:** Shared Packages
- **Task 0.5:** PostgreSQL + Prisma
- **Task 0.6:** Authentication Foundation
- **Task 0.7:** Developer Tooling
- **Task 0.8:** Sprint Review

## Development Workflow

We use standard Turborepo commands for development:

- `pnpm dev`: Start all apps in development mode.
- `pnpm build`: Build all apps and packages.
- `pnpm lint`: Run ESLint across the workspace.
- `pnpm typecheck`: Run TypeScript compilation check.
- `pnpm test`: Run Vitest tests across the workspace.

## Git Workflow & Commit Standards

This repository enforces strict code quality and commit message standards through Git hooks (Husky).

### Git Hooks

- **pre-commit**: Formats staged files (`prettier`), lints staged files (`eslint --fix`), and performs a workspace-wide typecheck (`pnpm run typecheck`). The commit will abort if any errors are encountered.
- **commit-msg**: Enforces the Conventional Commits specification for all commit messages.

### Commit Message Format

Commits must follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>
```

**Examples:**

- `feat(auth): add login endpoint`
- `fix(api): resolve validation bug`
- `docs(readme): update setup guide`
- `refactor(database): simplify Prisma client`
- `test(auth): add login integration tests`
- `chore(tooling): update ESLint`

### Bypassing Hooks

_Warning: Bypassing hooks is heavily discouraged and should only be used in emergencies to unblock critical production issues._

To bypass the hooks, append the `--no-verify` flag to your commit command:

```bash
git commit -m "fix(critical): emergency patch" --no-verify
```

## Testing Philosophy

APIMeter utilizes **Vitest** as the core test runner for both Frontend and Backend, maximizing mono-repo compatibility and speed.

### Backend Testing (`apps/backend/tests`)

- **Unit Tests**: Focus on utility functions, error classes, and isolated pure logic.
- **Integration Tests**: Leverage `supertest` to test complete API flows without needing to deploy the server.
- **Coverage**: V8 coverage enabled across `src/**`.

### Frontend Testing (`apps/frontend/tests`)

- **Unit Tests**: Component isolation testing utilizing `React Testing Library` (RTL) over `jsdom`.
- **Custom Renderers**: All custom hooks and providers are wrapped natively via `test-utils.tsx`.

### Running Tests

- `pnpm test`: Execute all tests in the workspace (single run).
- `pnpm test:watch`: Run all tests in interactive watch mode (perfect for TDD).
- `pnpm test:coverage`: Generate a comprehensive V8 coverage report for the workspace.
