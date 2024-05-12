import globals from "globals";

import path from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";
import pluginJs from "@eslint/js";

// mimic CommonJS variables -- not needed if using CommonJS
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({baseDirectory: __dirname, recommendedConfig: pluginJs.configs.recommended});

const config = [
  ...compat.extends("airbnb-base"),
  {
    files: ["**/*.js"],
    languageOptions: {
      sourceType: "commonjs",
      parserOptions: { ecmaVersion: "latest" },
    },
  },
  {
    languageOptions: { globals: { ...globals.node, ...globals.jest, }},
    rules: {
      "no-console": "off",
      "no-plusplus": "off",
      "no-param-reassign": ["error", { "props": false }],
      "no-multi-spaces": ["error", { "ignoreEOLComments": true }],
      "no-multiple-empty-lines": ["error", {"max": 2, "maxEOF": 1, "maxBOF": 0}],
      'no-restricted-syntax': [
        "error",
        {
          selector: 'LabeledStatement',
          message: 'Labels are a form of GOTO; using them makes code confusing and hard to maintain and understand.',
        },
        {
          selector: 'WithStatement',
          message: '`with` is disallowed in strict mode because it makes code impossible to predict and optimize.',
        },
      ],
    }
  },
  {
    ignores: [
      "eslint.config.mjs",
      "jest.config.js",
      "template.js",
    ],
  }
];

export default config;
