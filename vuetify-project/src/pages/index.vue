<template>
  <hello-world v-if="!isLogin" />
  <main-content v-else />
</template>

<script setup>
import { useStore } from "vuex";

const isLogin = localStorage.getItem("isLogin");

//
</script>
