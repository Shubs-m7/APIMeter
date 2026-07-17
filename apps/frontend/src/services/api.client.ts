import axios from 'axios';

export const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api/v1',
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
