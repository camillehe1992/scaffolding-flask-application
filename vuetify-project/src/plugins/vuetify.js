/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import "@mdi/font/css/materialdesignicons.css";
import "@/styles/settings.scss";

// Composables
import { createVuetify } from "vuetify";

const myCustomLightTheme = {
  dark: false,
  color: {
    background: "#F5F5F5",
  },
};

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  theme: {
    defaultTheme: "light",
    themes: {
      myCustomLightTheme,
    },
  },
});
