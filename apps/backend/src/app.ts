import compression from 'compression';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import express from 'express';
import helmet from 'helmet';
import pinoHttp from 'pino-http';

import { checkDatabaseHealth } from '@/config/database';
import { errorMiddleware } from '@/middleware/error.middleware';
import { notFoundMiddleware } from '@/middleware/not-found.middleware';
import { requestIdMiddleware } from '@/middleware/request-id.middleware';
import { logger } from '@/shared/logger';
import { success } from '@/shared/response';

const app = express();

app.use(requestIdMiddleware);
app.use(pinoHttp({ logger, customProps: (req) => ({ reqId: req.reqId }) }));
app.use(helmet());
app.use(cors());
app.use(compression());
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/health', async (_req, res) => {
  const isDbHealthy = await checkDatabaseHealth();
  success(res, {
    status: 'ok',
    database: isDbHealthy ? 'connected' : 'disconnected',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV,
  });
});

app.use(notFoundMiddleware);
app.use(errorMiddleware);

export default app;
