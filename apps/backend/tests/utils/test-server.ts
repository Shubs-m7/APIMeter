import supertest from 'supertest';

import app from '@/app';

export const createTestServer = () => {
  return supertest(app);
};
