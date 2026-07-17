import { Request, Response, NextFunction } from 'express';

import { generateId } from '@/utils/generate-id';

export const requestIdMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const reqId = req.headers['x-request-id'] || generateId();
  req.reqId = reqId as string;
  res.setHeader('X-Request-Id', reqId);
  next();
};
