# Prisma Infrastructure

This folder contains the Prisma ORM configuration for APIMeter.

## Workflows

- **Generate Client:** pnpm prisma:generate
- **Apply Migrations:** pnpm prisma:migrate
- **Seed Database:** pnpm prisma:seed
- **Open Studio:** pnpm prisma:studio

## Environment Variables

Ensure DATABASE_URL and DIRECT_URL (for Neon) are present in your .env file.
