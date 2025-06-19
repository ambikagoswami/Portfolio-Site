/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../templates/**/*.html",   // sabhi Django HTML templates
    "../../**/*.py",               // sabhi python files (views.py, etc.)
    "../../**/*.js",               // agar tum js me bhi tailwind use kr rahe ho
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
