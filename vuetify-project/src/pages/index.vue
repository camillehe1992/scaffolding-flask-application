<template>
  <hello-world v-if="!isLogin" />
  <main-content v-else />
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();

const isLogin = localStorage.getItem("isLogin");

//
</script>
