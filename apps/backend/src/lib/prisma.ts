import { PrismaClient } from "@prisma/client";
import { logger } from "@/shared/logger";

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
prisma.$on("query" as never, (e: any) => {
  logger.debug({ query: e.query, params: e.params, duration: e.duration }, "Prisma Query");
});
prisma.$on("error" as never, (e: any) => {
  logger.error({ message: e.message, target: e.target }, "Prisma Error");
});
prisma.$on("info" as never, (e: any) => {
  logger.info({ message: e.message }, "Prisma Info");
});
prisma.$on("warn" as never, (e: any) => {
  logger.warn({ message: e.message }, "Prisma Warn");
});
