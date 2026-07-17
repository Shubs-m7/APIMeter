import { Request, Response, NextFunction } from 'express';

import { config } from '@/config/app';
import { logger } from '@/shared/logger';
import { error as errorResponse } from '@/shared/response';

export const errorMiddleware = (err: any, req: Request, res: Response, _next: NextFunction) => {
  const statusCode = err.statusCode || 500;
  const message = err.message || 'Internal server error';

  if (statusCode === 500) {
    logger.error({ err, reqId: req.reqId }, 'Unhandled exception');
  }

  errorResponse(res, message, statusCode, config.isDev ? err.stack : undefined);
};
