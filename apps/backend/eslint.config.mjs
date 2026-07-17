import backend from '@apimeter/eslint-config/backend';

export default [
  ...backend,
  {
    ignores: ['dist/**', 'node_modules/**'],
  },
];
