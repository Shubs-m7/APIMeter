import { Request, Response, NextFunction } from 'express';

import { NotFoundError } from '@/shared/errors';

export const notFoundMiddleware = (req: Request, _res: Response, next: NextFunction) => {
  next(new NotFoundError(`Cannot find ${req.method} ${req.originalUrl} on this server`));
};
