import pino, { LoggerOptions } from 'pino';

import { config } from '@/config/app';

const options: LoggerOptions = {
  level: config.logLevel,
};

if (config.isDev) {
  options.transport = {
    target: 'pino-pretty',
    options: {
      colorize: true,
      translateTime: 'SYS:standard',
    },
  };
}

export const logger = pino(options);
