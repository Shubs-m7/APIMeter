import dotenv from 'dotenv';
import { z } from 'zod';

// Load environment variables from .env if present
dotenv.config();

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']).default('development'),
  PORT: z.coerce.number().positive().int().default(3001),
  DATABASE_URL: z.string().url('DATABASE_URL must be a valid URL'),
  DIRECT_URL: z.string().url('DIRECT_URL must be a valid URL'),
  JWT_SECRET: z.string().min(32, 'JWT_SECRET must be at least 32 characters long'),
  JWT_REFRESH_SECRET: z.string().min(32, 'JWT_REFRESH_SECRET must be at least 32 characters long'),
  CLIENT_URL: z.string().url('CLIENT_URL must be a valid URL'),
  LOG_LEVEL: z.enum(['fatal', 'error', 'warn', 'info', 'debug', 'trace']).default('info'),
});

const _env = envSchema.safeParse(process.env);

if (!_env.success) {
  console.error('❌ Invalid backend environment variables:');
  const errors = _env.error.format();
  for (const [key, value] of Object.entries(errors)) {
    if ((key !== '_errors' && value && 'toArray' in value) || Array.isArray(value)) {
      // ZodFormattedError is typed strangely, this extracts the messages safely
      const messages = (value as any)._errors || value;
      console.error(`  - ${key}: ${messages}`);
    }
  }
  process.exit(1);
}

export const env = _env.data;
