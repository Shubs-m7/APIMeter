import { describe, it, expect } from 'vitest';

import { createTestServer } from '../utils/test-server';

describe('Health Endpoint', () => {
  it('should return 200 and healthy status', async () => {
    const server = createTestServer();
    const response = await server.get('/health');

    expect(response.status).toBe(200);
    expect(response.body.success).toBe(true);
    expect(response.body.data.status).toBe('ok');
    expect(response.body.data.environment).toBe('test');
  });

  it('server should handle 404 for unknown routes', async () => {
    const server = createTestServer();
    const response = await server.get('/unknown-route');

    expect(response.status).toBe(404);
  });
});
