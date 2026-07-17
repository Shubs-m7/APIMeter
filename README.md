# APIMeter

**Tagline:** Secure API Key Management & Real-Time Usage Analytics Platform

## Project Overview

APIMeter is a scalable platform designed to manage API keys and track usage in real-time. It provides developers and administrators with deep insights into their API's performance and usage constraints.

## Architecture

This project is structured as a **Turborepo** monorepo using **pnpm**. 

### Folder Structure

```text
apimeter/
├── apps/
│   ├── backend/         (Node.js / Express or Next.js API placeholder)
│   └── frontend/        (Web Application placeholder)
├── packages/
│   ├── shared-types/    (TypeScript types and interfaces)
│   ├── shared-utils/    (Common helper functions)
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

## Development Workflow

We use standard Turborepo commands for development:
- `pnpm dev`: Start all apps in development mode.
- `pnpm build`: Build all apps and packages.
- `pnpm lint`: Run ESLint across the workspace.
- `pnpm typecheck`: Run TypeScript compilation check.
- `pnpm test`: Run tests.
