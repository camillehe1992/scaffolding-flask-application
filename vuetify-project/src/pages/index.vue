<template>
  <hello-world v-if="isLogin" />
  <login v-else />
</template>

<script setup>
import login from "./login.vue";

const isLogin = Boolean(localStorage.getItem("isLogin") ?? "false");

//
</script>
