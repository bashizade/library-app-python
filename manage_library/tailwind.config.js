/** @type {import('tailwindcss').Config} */
const themes = require("daisyui/src/theming/themes");
module.exports = {
    content: [
        './**/templates/*.html',
        './**/templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [require("daisyui")],
    daisyui: {
        themes: ['light', 'dark','lemonade'],
    },
}

