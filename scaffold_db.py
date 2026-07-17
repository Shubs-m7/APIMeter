import os
import json

root = 'apps/backend'

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 1. Prisma schema
schema = '''generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")
  directUrl = env("DIRECT_URL")
}

// Models intentionally left blank for Sprint 0 - Task 0.5A
'''
write_file(os.path.join(root, 'prisma/schema.prisma'), schema)

# 2. Prisma seed
seed = '''// prisma/seed.ts
// Placeholder for future database seeding logic.
async function main() {
  console.log("Seeding database placeholder...");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });
'''
write_file(os.path.join(root, 'prisma/seed.ts'), seed)

# 3. Prisma README
readme = '''# Prisma Infrastructure

This folder contains the Prisma ORM configuration for APIMeter.

## Workflows

- **Generate Client:** pnpm prisma:generate
- **Apply Migrations:** pnpm prisma:migrate
- **Seed Database:** pnpm prisma:seed
- **Open Studio:** pnpm prisma:studio

## Environment Variables
Ensure DATABASE_URL and DIRECT_URL (for Neon) are present in your .env file.
'''
write_file(os.path.join(root, 'prisma/README.md'), readme)

# 4. Prisma client
prisma_client = '''import { PrismaClient } from "@prisma/client";
import { logger } from "./logger";

declare global {
  // eslint-disable-next-line no-var
  var prisma: PrismaClient | undefined;
}

export const prisma =
  global.prisma ||
  new PrismaClient({
    log: [
      { emit: "event", level: "query" },
      { emit: "event", level: "error" },
      { emit: "event", level: "info" },
      { emit: "event", level: "warn" },
    ],
  });

if (process.env.NODE_ENV !== "production") {
  global.prisma = prisma;
}

// Attach pino logger to Prisma events
prisma.("query" as never, (e: any) => {
  logger.debug({ query: e.query, params: e.params, duration: e.duration }, "Prisma Query");
});
prisma.("error" as never, (e: any) => {
  logger.error({ message: e.message, target: e.target }, "Prisma Error");
});
prisma.("info" as never, (e: any) => {
  logger.info({ message: e.message }, "Prisma Info");
});
prisma.("warn" as never, (e: any) => {
  logger.warn({ message: e.message }, "Prisma Warn");
});
'''
write_file(os.path.join(root, 'src/lib/prisma.ts'), prisma_client)

# Fix logger import in prisma.ts (it's actually in @/shared/logger)
prisma_client_fixed = prisma_client.replace('./logger', '@/shared/logger')
write_file(os.path.join(root, 'src/lib/prisma.ts'), prisma_client_fixed)

# 5. Database config
db_config = '''import { prisma } from "@/lib/prisma";
import { logger } from "@/shared/logger";

export const checkDatabaseHealth = async (): Promise<boolean> => {
  try {
    await prisma.\SELECT 1\;
    return true;
  } catch (error) {
    logger.error({ err: error }, "Database connection failed");
    return false;
  }
};
'''
write_file(os.path.join(root, 'src/config/database.ts'), db_config)

# 6. Add Error Classes
errors = '''
export class DatabaseConnectionError extends AppError {
  constructor(message = "Database connection failed") {
    super(message, 503, false);
  }
}

export class PrismaError extends AppError {
  constructor(message = "Database operation failed") {
    super(message, 500, false);
  }
}

export class DatabaseTimeoutError extends AppError {
  constructor(message = "Database operation timed out") {
    super(message, 504, false);
  }
}
'''
errors_file = os.path.join(root, 'src/shared/errors/index.ts')
with open(errors_file, 'a') as f:
    f.write(errors)

print("Scaffold complete.")
