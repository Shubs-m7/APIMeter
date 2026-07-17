# Project Context

## Project Summary

APIMeter is a Secure API Key Management & Real-Time Usage Analytics Platform.

## Current Version

1.2

## Architecture Summary

Turborepo monorepo with pnpm workspaces.
Backend: Standalone Express.js + TypeScript REST API.
Frontend: Next.js Web Application.

## Tech Stack

- TypeScript
- pnpm
- Turborepo
- Express.js (Backend)
- Next.js (Frontend)
- Prisma (ORM) & PostgreSQL
- Zod (Validation)
- Pino (Logging)
- Vitest & Supertest (Testing)

## Folder Structure

- `apps/backend/`: Express.js backend application
- `apps/frontend/`: Next.js frontend application
- `packages/shared-types/`: Shared TypeScript types
- `packages/shared-utils/`: Shared utilities
- `packages/validation/`: Shared Zod schemas and validation helpers
- `packages/eslint-config/`: Shared ESLint config
- `packages/tsconfig/`: Shared TS config

## Current Sprint

Sprint 0 Roadmap:

- Task 0.1: Monorepo Foundation
- Task 0.2: Express Backend Foundation
- Task 0.3: Next.js Frontend Foundation
- Task 0.4: Shared Packages
- Task 0.5: PostgreSQL + Prisma
- Task 0.6: Authentication Foundation
- Task 0.7: Developer Tooling
- Task 0.8: Sprint Review

## Current Task

Task 0.2 - Express Backend Foundation (Updating Docs to v1.2)

## Development Rules

- Use production-grade naming.
- Use consistent formatting.
- Use clean folder organization.
- No unnecessary files.
- No feature implementation in Sprint 0.

## Coding Standards Summary

Strict TypeScript configurations and ESLint rules applied across the monorepo workspace. Express backend strictly follows feature-first modular architecture without traditional repository layers.
