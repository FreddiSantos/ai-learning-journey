// Regras de mensagem de commit (Conventional Commits). Usado pelo workflow commitlint.yml.
export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    // O Dependabot escreve corpos com URLs longas; não vale reprovar o PR por isso.
    "body-max-line-length": [0],
    "footer-max-line-length": [0],
  },
};
