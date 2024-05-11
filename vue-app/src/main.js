import { createApp } from "vue";
import App from "./App.vue";
import "./style.css";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import router from "./router";

createApp(App)
	.use(router)
	.use(ElementPlus, { size: "small", zIndex: 3000 })
	.mount("#app");
