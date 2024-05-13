<template>
  <hello-world v-if="isLogin" />
  <login v-else />
</template>

<script setup>
import { ref } from "vue";
import login from "./login.vue";

const isLogin = ref(false);

//
</script>
