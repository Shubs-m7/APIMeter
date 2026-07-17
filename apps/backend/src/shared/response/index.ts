import { Response } from "express";

export const success = (res: Response, data: any, message = "Success", meta?: any) => {
  res.status(200).json({
    success: true,
    message,
    data,
    meta,
  });
};

export const created = (res: Response, data: any, message = "Created", meta?: any) => {
  res.status(201).json({
    success: true,
    message,
    data,
    meta,
  });
};

export const error = (res: Response, message: string, statusCode = 400, errDetails?: any) => {
  res.status(statusCode).json({
    success: false,
    message,
    error: errDetails,
  });
};

