<template>
  <v-app-bar image="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
    <template v-slot:image>
      <v-img
        gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
      ></v-img>
    </template>

    <template v-slot:prepend>
      <v-app-bar-nav-icon icon="$vuetify" href="/"></v-app-bar-nav-icon>
    </template>

    <v-app-bar-title>Login Demo Application</v-app-bar-title>

    <v-spacer></v-spacer>

    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-inline-block social-link text-black"
    >
      <v-btn>{{ item.title }} </v-btn>
    </a>

    <v-menu min-width="200px" rounded>
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props">
          <v-avatar>
            <span v-if="user?.initials">{{ user?.initials }}</span>
            <v-icon v-else icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </v-btn>
      </template>
      <v-card>
        <v-card-text>
          <div class="mx-auto text-center">
            <v-avatar color="secondary">
              <span v-if="user?.initials" class="text-h5">{{
                user?.initials
              }}</span>
              <v-icon v-else icon="mdi-account-circle"></v-icon>
            </v-avatar>
            <h3>{{ user?.username }}</h3>
            <p class="text-caption mt-1">
              {{ user?.email }}
            </p>
            <v-divider class="my-3"></v-divider>
            <v-btn variant="text" rounded @click="editAccount()">
              Edit Account
            </v-btn>
            <v-divider class="my-3"></v-divider>
            <v-btn variant="text" rounded @click="signout()"> Log Out </v-btn>
          </div>
        </v-card-text>
      </v-card>
    </v-menu>
  </v-app-bar>
</template>

<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();

const user = computed(() => store.state.user.currentUser);

const items = [
  { href: "/login", title: "login", title: "Log In" },
  { href: "/signup", title: "signup", title: "Sign Up" },
];

const editAccount = () => {
  router.push({ name: "/account" });
};

const signout = () => {
  localStorage.clear();
  router.push({ name: "/login" });
};
</script>
<style lang=""></style>
