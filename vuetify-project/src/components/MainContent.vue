<template>
  <v-container class="mx-auto" width="100%" v-if="user">
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click="rail = false"
    >
      <v-list>
        <v-list-item :title="user?.username" :subtitle="user?.username" nav>
          <template v-slot:prepend>
            <div class="pr-2">
              <v-avatar
                v-if="user.avatar"
                color="grey-darken-3"
                :image="user.avatar"
              ></v-avatar>
              <v-avatar v-else color="cyan-darken-3">
                <v-icon icon="mdi-account-circle"></v-icon>
              </v-avatar>
            </div>
          </template>
          <template v-slot:append>
            <v-btn
              icon="mdi-chevron-left"
              variant="text"
              @click.stop="rail = !rail"
            ></v-btn>
          </template>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item
          prepend-icon="mdi-folder"
          title="My Files"
          value="myfiles"
        ></v-list-item>
        <v-list-item
          prepend-icon="mdi-account-multiple"
          title="Shared with me"
          value="shared"
        ></v-list-item>
        <v-list-item
          prepend-icon="mdi-star"
          title="Starred"
          value="starred"
        ></v-list-item>
      </v-list>
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

const drawer = ref(true);
const rail = ref(false);
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
