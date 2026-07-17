import os
import json
import re

root = 'apps/backend'

# 1. package.json scripts
pkg_path = os.path.join(root, 'package.json')
with open(pkg_path, 'r') as f:
    pkg = json.load(f)

pkg['scripts'].update({
    'prisma:generate': 'prisma generate',
    'prisma:migrate': 'prisma migrate dev',
    'prisma:studio': 'prisma studio',
    'prisma:push': 'prisma db push',
    'prisma:seed': 'tsx prisma/seed.ts',
    'db:reset': 'prisma migrate reset',
    'db:status': 'prisma migrate status'
})

# Make sure prisma/seed is mapped in package.json to avoid Prisma missing it
pkg['prisma'] = {
    'seed': 'tsx prisma/seed.ts'
}

with open(pkg_path, 'w') as f:
    json.dump(pkg, f, indent=2)


# 2. .env
env_path = os.path.join(root, '.env')
env_content = '''PORT=3000
NODE_ENV=development
DATABASE_URL="postgresql://user:password@localhost:5432/apimeter?schema=public"
DIRECT_URL="postgresql://user:password@localhost:5432/apimeter?schema=public"
'''
with open(env_path, 'w') as f:
    f.write(env_content)


# 3. src/config/env.ts
env_ts_path = os.path.join(root, 'src/config/env.ts')
with open(env_ts_path, 'r') as f:
    env_ts = f.read()

if 'DATABASE_URL' not in env_ts:
    env_ts = env_ts.replace('z.object({', 'z.object({\n  DATABASE_URL: z.string().url(),\n  DIRECT_URL: z.string().url().optional(),')
    with open(env_ts_path, 'w') as f:
        f.write(env_ts)

# 4. src/app.ts health endpoint update
app_ts_path = os.path.join(root, 'src/app.ts')
with open(app_ts_path, 'r') as f:
    app_ts = f.read()

# Add import if missing
if 'checkDatabaseHealth' not in app_ts:
    app_ts = 'import { checkDatabaseHealth } from "@/config/database";\n' + app_ts
    
    # Replace the health endpoint
    health_old = '''app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});'''
    health_new = '''app.get("/health", async (req, res) => {
  const isDbHealthy = await checkDatabaseHealth();
  res.status(200).json({ 
    status: "ok",
    database: isDbHealthy ? "connected" : "disconnected"
  });
});'''
    app_ts = app_ts.replace(health_old, health_new)
    
    with open(app_ts_path, 'w') as f:
        f.write(app_ts)

print("Update complete")
