import base from '@apimeter/eslint-config/base';

export default [
  ...base,
  {
    ignores: ['dist/**', 'node_modules/**', 'apps/**', 'packages/**', '.next/**'],
  },
];
