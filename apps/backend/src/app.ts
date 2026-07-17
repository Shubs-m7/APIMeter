import express from "express";
import cors from "cors";
import helmet from "helmet";
import compression from "compression";
import cookieParser from "cookie-parser";
import pinoHttp from "pino-http";
import { logger } from "@/shared/logger";
import { requestIdMiddleware } from "@/middleware/request-id.middleware";
import { notFoundMiddleware } from "@/middleware/not-found.middleware";
import { errorMiddleware } from "@/middleware/error.middleware";
import { success } from "@/shared/response";

const app = express();

app.use(requestIdMiddleware);
app.use(pinoHttp({ logger, customProps: (req) => ({ reqId: req.reqId }) }));
app.use(helmet());
app.use(cors());
app.use(compression());
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/health", (_req, res) => {
  success(res, {
    status: "ok",
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV,
  });
});

app.use(notFoundMiddleware);
app.use(errorMiddleware);

export default app;

