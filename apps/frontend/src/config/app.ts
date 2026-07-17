import { env } from './env';

export const APP_CONFIG = {
  name: env.NEXT_PUBLIC_APP_NAME,
  version: '1.2',
  apiUrl: env.NEXT_PUBLIC_API_URL,
};
