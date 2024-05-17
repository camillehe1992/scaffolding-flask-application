<template>
  <div v-if="isLoggedIn">
    <h1 class="title">Hello Todos</h1>
    <todos />
    <v-btn
      variant="tonal"
      size="large"
      color="black"
      block
      rounded="lg"
      @click="signout"
    >
      Sign Out
    </v-btn>
  </div>
  <authenticator v-else />
</template>

<script setup>
const isLoggedIn = localStorage.getItem("isLoggedIn");

const signout = () => {
  localStorage.clear();
  location.reload();
};
//
</script>

<style lang="scss" scoped>
.title {
  text-align: center;
  line-height: 100px;
}
</style>
