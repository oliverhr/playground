# Algorithms with Javascript


Linter configuration: `eslint.config.mjs`
```
export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "commonjs",
      parserOptions: { ecmaVersion: 'latest' },
      globals: globals.node,
    },
  },
  {
    rules: {
      "no-param-reassign": ["error", { "props": false }],
    }
  },
  ...compat.extends("airbnb-base"),
];

```


eslint ignored files: `.eslintignore`
```
node_modules/
/**/node_modules/*

eslint.config.mjs
```
