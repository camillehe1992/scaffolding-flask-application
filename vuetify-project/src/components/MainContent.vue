<template>
  <v-container class="mx-auto" width="100%" v-if="user">
    <v-navigation-drawer>
      <v-list>
        <v-list-item
          prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
          :subtitle="user?.email"
          :title="user?.email"
        >
          <template v-slot:append>
            <v-btn icon="mdi-menu-down" size="small" variant="text"></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list :lines="false" density="compact" nav>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :value="item"
          color="primary"
        >
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block @click="logout()"> Logout </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-main style="height: 354px"></v-main>
  </v-container>
</template>
<script setup>
import { useStore } from "vuex";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const items = [
  { text: "My Files", icon: "mdi-folder" },
  { text: "Shared with me", icon: "mdi-account-multiple" },
  { text: "Starred", icon: "mdi-star" },
  { text: "Recent", icon: "mdi-history" },
  { text: "Offline", icon: "mdi-check-circle" },
  { text: "Uploads", icon: "mdi-upload" },
  { text: "Backups", icon: "mdi-cloud-upload" },
];

const store = useStore();
const router = useRouter();

const user = ref(null);

onMounted(async () => {
  user.value = await fetchUser();
});
const token = localStorage.getItem("token");

const fetchUser = async () => {
  try {
    return await store.dispatch("user/getUser", { token });
  } catch (error) {
    router.push({ name: "/" });
  }
};

const logout = () => {
  localStorage.removeItem("isLogin");
  localStorage.removeItem("token");
  router.push("/login");
};
</script>
<style lang=""></style>
