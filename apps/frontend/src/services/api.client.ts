import axios from 'axios';

import { env } from '@/config/env';

export const apiClient = axios.create({
  baseURL: env.NEXT_PUBLIC_API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor placeholder
apiClient.interceptors.request.use((config) => {
  return config;
});

// Response interceptor placeholder
apiClient.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error),
);
