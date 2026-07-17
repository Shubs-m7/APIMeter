import { prisma } from "@/lib/prisma";
import { logger } from "@/shared/logger";

export const checkDatabaseHealth = async (): Promise<boolean> => {
  try {
    await prisma.$queryRaw`SELECT 1`;
    return true;
  } catch (error) {
    logger.error({ err: error }, "Database connection failed");
    return false;
  }
};
