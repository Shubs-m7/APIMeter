import os
import json

root = 'packages'

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def write_json(path, data):
    write_file(path, json.dumps(data, indent=2))

# 1. tsconfig
tsconfig_dir = os.path.join(root, 'tsconfig')
write_json(os.path.join(tsconfig_dir, 'package.json'), {
  'name': '@apimeter/tsconfig',
  'version': '1.0.0',
  'private': True,
  'files': ['base.json', 'node.json', 'next.json', 'strict.json']
})
write_file(os.path.join(tsconfig_dir, 'README.md'), '# @apimeter/tsconfig\n\nShared TypeScript configurations for the workspace.')
write_json(os.path.join(tsconfig_dir, 'base.json'), {
  'compilerOptions': {
    'target': 'ES2022',
    'module': 'ESNext',
    'moduleResolution': 'Bundler',
    'lib': ['ES2022'],
    'esModuleInterop': True,
    'strict': True,
    'skipLibCheck': True,
    'forceConsistentCasingInFileNames': True,
    'resolveJsonModule': True
  }
})
write_json(os.path.join(tsconfig_dir, 'node.json'), {
  'extends': './base.json',
  'compilerOptions': {
    'moduleResolution': 'NodeNext',
    'module': 'NodeNext',
    'target': 'ES2022'
  }
})
write_json(os.path.join(tsconfig_dir, 'next.json'), {
  'extends': './base.json',
  'compilerOptions': {
    'lib': ['dom', 'dom.iterable', 'esnext'],
    'allowJs': True,
    'noEmit': True,
    'isolatedModules': True,
    'jsx': 'preserve',
    'plugins': [{'name': 'next'}]
  }
})
write_json(os.path.join(tsconfig_dir, 'strict.json'), {
  'extends': './base.json',
  'compilerOptions': {
    'noUncheckedIndexedAccess': True,
    'exactOptionalPropertyTypes': True,
    'noImplicitOverride': True,
    'noFallthroughCasesInSwitch': True,
    'noUnusedLocals': True,
    'noUnusedParameters': True
  }
})

# 2. eslint-config
eslint_dir = os.path.join(root, 'eslint-config')
write_json(os.path.join(eslint_dir, 'package.json'), {
  'name': '@apimeter/eslint-config',
  'version': '1.0.0',
  'private': True,
  'main': 'base.js',
  'files': ['base.js', 'frontend.js', 'backend.js']
})
write_file(os.path.join(eslint_dir, 'README.md'), '# @apimeter/eslint-config\n\nShared ESLint configurations.')
write_file(os.path.join(eslint_dir, 'base.js'), 'module.exports = {};\n')
write_file(os.path.join(eslint_dir, 'frontend.js'), 'module.exports = {};\n')
write_file(os.path.join(eslint_dir, 'backend.js'), 'module.exports = {};\n')

# 3. config
config_dir = os.path.join(root, 'config')
write_json(os.path.join(config_dir, 'package.json'), {
  'name': '@apimeter/config',
  'version': '1.0.0',
  'private': True,
  'main': 'src/index.ts',
  'scripts': { 'typecheck': 'tsc --noEmit' },
  'devDependencies': { 'typescript': '^5.0.0', '@apimeter/tsconfig': 'workspace:*' }
})
write_json(os.path.join(config_dir, 'tsconfig.json'), {
  'extends': '@apimeter/tsconfig/strict.json',
  'compilerOptions': { 'baseUrl': '.', 'outDir': 'dist' },
  'include': ['src']
})
write_file(os.path.join(config_dir, 'README.md'), '# @apimeter/config\n\nApplication-wide constants.')
write_file(os.path.join(config_dir, 'src/constants/index.ts'), 'export const APP_NAME = \"APIMeter\";\nexport const API_VERSION = \"v1\";\nexport const DEFAULT_PAGE_SIZE = 20;\n')
write_file(os.path.join(config_dir, 'src/routes/index.ts'), 'export const PUBLIC_ROUTES = [\"/login\"];\nexport const PROTECTED_ROUTES = [\"/dashboard\"];\n')
write_file(os.path.join(config_dir, 'src/api/index.ts'), 'export const API_PREFIX = \"/api/v1\";\n')
write_file(os.path.join(config_dir, 'src/metadata/index.ts'), 'export const SEO_TITLE = \"APIMeter Dashboard\";\n')
write_file(os.path.join(config_dir, 'src/env/index.ts'), 'export const ENV_KEYS = [\"NODE_ENV\", \"PORT\"];\n')
write_file(os.path.join(config_dir, 'src/index.ts'), 'export * from \"./constants\";\nexport * from \"./routes\";\nexport * from \"./api\";\nexport * from \"./metadata\";\nexport * from \"./env\";\n')

# 4. shared-types
types_dir = os.path.join(root, 'shared-types')
write_json(os.path.join(types_dir, 'package.json'), {
  'name': '@apimeter/shared-types',
  'version': '1.0.0',
  'private': True,
  'main': 'src/index.ts',
  'scripts': { 'typecheck': 'tsc --noEmit' },
  'devDependencies': { 'typescript': '^5.0.0', '@apimeter/tsconfig': 'workspace:*' }
})
write_json(os.path.join(types_dir, 'tsconfig.json'), {
  'extends': '@apimeter/tsconfig/strict.json',
  'compilerOptions': { 'baseUrl': '.', 'outDir': 'dist' },
  'include': ['src']
})
write_file(os.path.join(types_dir, 'README.md'), '# @apimeter/shared-types\n\nReusable TypeScript types.')
write_file(os.path.join(types_dir, 'src/common/index.ts'), 'export type Timestamp = string | number | Date;\nexport type Identifier = string;\n')
write_file(os.path.join(types_dir, 'src/api/index.ts'), 'export interface ApiResponse<T> { success: boolean; data?: T; error?: any; }\n')
write_file(os.path.join(types_dir, 'src/auth/index.ts'), 'export interface UserDTO { id: string; email: string; }\n')
write_file(os.path.join(types_dir, 'src/projects/index.ts'), 'export interface ProjectDTO { id: string; name: string; }\n')
write_file(os.path.join(types_dir, 'src/analytics/index.ts'), 'export interface AnalyticsDTO { totalRequests: number; }\n')
write_file(os.path.join(types_dir, 'src/pagination/index.ts'), 'export interface Pagination { page: number; limit: number; total: number; }\n')
write_file(os.path.join(types_dir, 'src/index.ts'), 'export * from \"./common\";\nexport * from \"./api\";\nexport * from \"./auth\";\nexport * from \"./projects\";\nexport * from \"./analytics\";\nexport * from \"./pagination\";\n')

# 5. shared-utils
utils_dir = os.path.join(root, 'shared-utils')
write_json(os.path.join(utils_dir, 'package.json'), {
  'name': '@apimeter/shared-utils',
  'version': '1.0.0',
  'private': True,
  'main': 'src/index.ts',
  'scripts': { 'typecheck': 'tsc --noEmit' },
  'dependencies': { 'clsx': '^2.1.0', 'tailwind-merge': '^2.2.0' },
  'devDependencies': { 'typescript': '^5.0.0', '@apimeter/tsconfig': 'workspace:*' }
})
write_json(os.path.join(utils_dir, 'tsconfig.json'), {
  'extends': '@apimeter/tsconfig/strict.json',
  'compilerOptions': { 'baseUrl': '.', 'outDir': 'dist' },
  'include': ['src']
})
write_file(os.path.join(utils_dir, 'README.md'), '# @apimeter/shared-utils\n\nPure TypeScript utility functions.')
write_file(os.path.join(utils_dir, 'src/string.ts'), 'export const capitalize = (str: string) => str.charAt(0).toUpperCase() + str.slice(1);\n')
write_file(os.path.join(utils_dir, 'src/sleep.ts'), 'export const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));\n')
write_file(os.path.join(utils_dir, 'src/cn.ts'), 'import { clsx, type ClassValue } from \"clsx\";\nimport { twMerge } from \"tailwind-merge\";\nexport function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)); }\n')
write_file(os.path.join(utils_dir, 'src/index.ts'), 'export * from \"./string\";\nexport * from \"./sleep\";\nexport * from \"./cn\";\n')

# 6. validation
val_dir = os.path.join(root, 'validation')
write_json(os.path.join(val_dir, 'package.json'), {
  'name': '@apimeter/validation',
  'version': '1.0.0',
  'private': True,
  'main': 'src/index.ts',
  'scripts': { 'typecheck': 'tsc --noEmit' },
  'dependencies': { 'zod': '^3.22.0' },
  'devDependencies': { 'typescript': '^5.0.0', '@apimeter/tsconfig': 'workspace:*' }
})
write_json(os.path.join(val_dir, 'tsconfig.json'), {
  'extends': '@apimeter/tsconfig/strict.json',
  'compilerOptions': { 'baseUrl': '.', 'outDir': 'dist' },
  'include': ['src']
})
write_file(os.path.join(val_dir, 'README.md'), '# @apimeter/validation\n\nReusable Zod schemas.')
write_file(os.path.join(val_dir, 'src/common/index.ts'), 'import { z } from \"zod\";\nexport const IdentifierSchema = z.string().uuid();\n')
write_file(os.path.join(val_dir, 'src/auth/index.ts'), 'import { z } from \"zod\";\nexport const LoginSchema = z.object({ email: z.string().email(), password: z.string().min(8) });\n')
write_file(os.path.join(val_dir, 'src/projects/index.ts'), 'import { z } from \"zod\";\nexport const CreateProjectSchema = z.object({ name: z.string().min(3) });\n')
write_file(os.path.join(val_dir, 'src/api-keys/index.ts'), 'import { z } from \"zod\";\nexport const CreateApiKeySchema = z.object({ name: z.string().min(3) });\n')
write_file(os.path.join(val_dir, 'src/settings/index.ts'), 'import { z } from \"zod\";\nexport const UpdateProfileSchema = z.object({ name: z.string() });\n')
write_file(os.path.join(val_dir, 'src/index.ts'), 'export * from \"./common\";\nexport * from \"./auth\";\nexport * from \"./projects\";\nexport * from \"./api-keys\";\nexport * from \"./settings\";\n')

print("Success")
