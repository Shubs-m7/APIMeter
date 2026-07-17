import { z } from 'zod';

const envSchema = z.object({
  NEXT_PUBLIC_API_URL: z.string().url('NEXT_PUBLIC_API_URL must be a valid URL'),
  NEXT_PUBLIC_APP_NAME: z.string().min(1, 'NEXT_PUBLIC_APP_NAME is required'),
});

const _env = envSchema.safeParse({
  NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  NEXT_PUBLIC_APP_NAME: process.env.NEXT_PUBLIC_APP_NAME,
});

if (!_env.success) {
  console.error('❌ Invalid frontend environment variables:');
  const errors = _env.error.format();
  for (const [key, value] of Object.entries(errors)) {
    if ((key !== '_errors' && value && 'toArray' in value) || Array.isArray(value)) {
      const messages = (value as any)._errors || value;
      console.error(`  - ${key}: ${messages}`);
    }
  }

  // Throw an error rather than process.exit to allow Next.js to handle the error gracefully during build or CSR
  throw new Error('Invalid frontend environment variables');
}

export const env = _env.data;
