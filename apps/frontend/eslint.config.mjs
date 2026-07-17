import frontend from '@apimeter/eslint-config/frontend';

export default [
  ...frontend,
  {
    ignores: ['.next/**', 'dist/**', 'node_modules/**'],
  },
];
