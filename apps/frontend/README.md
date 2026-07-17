# APIMeter - Next.js Frontend

## Architecture

Next.js 16 (App Router) with Tailwind CSS v4, Shadcn UI, Zustand, and TanStack Query.

## Folder Structure

```
src/
  app/           # Next.js App Router pages and layouts
  assets/        # Static assets (logos, icons)
  components/    # Reusable UI components (Shadcn)
  config/        # Application config
  constants/     # Global constants
  features/      # Feature-specific modules
  hooks/         # Custom React hooks
  lib/           # Utilities (cn, etc)
  providers/     # React context providers
  services/      # API clients
  shared/        # Shared cross-domain types and utilities
  store/         # Zustand global stores
  styles/        # Global CSS
```

## Commands

- `pnpm dev`: Start development server
- `pnpm build`: Build production app
- `pnpm lint`: Run ESLint
- `pnpm typecheck`: Run TS type check
