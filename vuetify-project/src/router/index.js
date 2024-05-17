/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router/auto";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
});

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = Boolean(localStorage.getItem("isLoggedIn") ?? "false");
//   console.log(`isLoggedIn ${isLoggedIn}`);

//   if (!isLoggedIn) next({ name: "/" });
//   else next();
// });

export default router;
