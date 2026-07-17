import { z } from "zod";
export const CreateApiKeySchema = z.object({ name: z.string().min(3) });
