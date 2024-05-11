import { createMemoryHistory, createRouter } from "vue-router";

import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";

const routes = [
	{
		path: "/",
		name: "Home",
		component: Login,
	},
	{
		path: "/login",
		name: "Login",
		component: Login,
	},
	{
		path: "/register",
		name: "Register",
		component: Register,
	},
];

const router = createRouter({
	history: createMemoryHistory(),
	routes,
});

export default router;
