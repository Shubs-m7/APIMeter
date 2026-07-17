# APIMeter - Express Backend

## Architecture

Standalone Express.js 5 API in TypeScript.

## Folder Structure

```
src/
  app.ts           # Express application configuration
  server.ts        # Server entry point
  config/          # Environment variables and constants
  middleware/      # Global middleware (errors, request IDs)
  shared/          # Shared utilities (errors, logger, response)
  modules/         # Feature-first domain modules (empty for now)
  utils/           # Helper functions
  types/           # TypeScript definitions
```

## Commands

- `pnpm dev`: Start the server in development mode using `tsx`
- `pnpm build`: Compile TypeScript to `dist/`
- `pnpm start`: Run the compiled server
- `pnpm typecheck`: Run TypeScript compilation check
- `pnpm lint`: Run ESLint
- `pnpm clean`: Remove `dist/`

## Development Workflow

1. Environment variables are validated on startup via Zod.
2. Ensure you have `NODE_ENV=development` to enable pretty logging.
