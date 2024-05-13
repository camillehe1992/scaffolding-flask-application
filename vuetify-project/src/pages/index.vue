<template>
  <hello-world v-if="isLogin" />
  <login v-else />
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex/types/index.js";
import login from "./login.vue";

const store = useStore();

const isLogin = computed(() => store.state.user.isLogin);

//
</script>
