/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router/auto";
const isAuthenticated = false;

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
});

router.beforeEach((to, from, next) => {
  if (to.name !== "/login" && to.name !== "/register" && !isAuthenticated)
    next({ name: "/login" });
  else next();
});

export default router;
