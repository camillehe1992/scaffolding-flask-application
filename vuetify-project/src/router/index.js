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

router.beforeEach((to, from, next) => {
  const isLogin = Boolean(localStorage.getItem("isLogin") ?? "false");
  if (to.name !== "/login" && to.name !== "/register" && !isLogin)
    next({ name: "/login" });
  else next();
});

export default router;
