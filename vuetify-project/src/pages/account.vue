<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card align="center">
          <template v-slot:prepend>
            <div>
              <v-avatar
                v-if="user?.avatar"
                size="72px"
                color="grey-darken-3"
                :image="user?.avatar"
              ></v-avatar>
              <v-avatar v-else size="108px" color="cyan-darken-3">
                <v-icon size="72px" icon="mdi-account-circle"></v-icon>
              </v-avatar>
            </div>
          </template>

          <v-card-title>
            {{ user?.username }}
          </v-card-title>

          <v-card-subtitle>
            {{ user?.email }}
          </v-card-subtitle>

          <v-card-text
            >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod.</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-card>
          <v-card-text>
            <div class="font-weight-bold ms-1 mb-2">Today</div>

            <v-timeline align="start" density="compact">
              <v-timeline-item
                v-for="message in messages"
                :key="message.time"
                :dot-color="message.color"
                size="x-small"
              >
                <div class="mb-4">
                  <div class="font-weight-normal">
                    <strong>{{ message.from }}</strong> @{{ message.time }}
                  </div>

                  <div>{{ message.message }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="9">
        <v-card>
          <v-tabs
            v-model="tab"
            align-tabs="center"
            color="deep-purple-accent-4"
          >
            <v-tab :value="1">Landscape</v-tab>
            <v-tab :value="2">City</v-tab>
            <v-tab :value="3">Abstract</v-tab>
          </v-tabs>

          <v-tabs-window v-model="tab">
            <v-tabs-window-item v-for="n in 3" :key="n" :value="n">
              <v-container fluid>
                <v-row>
                  <v-col v-for="i in 6" :key="i" cols="12" md="4">
                    <v-img
                      :lazy-src="`https://picsum.photos/10/6?image=${
                        i * n * 5 + 10
                      }`"
                      :src="`https://picsum.photos/500/300?image=${
                        i * n * 5 + 10
                      }`"
                      height="205"
                      cover
                    ></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-tabs-window-item>
          </v-tabs-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
import { useStore } from "vuex";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const store = useStore();
const router = useRouter();

const user = ref(null);

const tab = ref(null);

const messages = ref([
  {
    from: "You",
    message: `Sure, I'll see you later.`,
    time: "10:42am",
    color: "deep-purple-lighten-1",
  },
  {
    from: "John Doe",
    message: "Yeah, sure. Does 1:00pm work?",
    time: "10:37am",
    color: "green",
  },
  {
    from: "You",
    message: "Did you still want to grab lunch today?",
    time: "9:47am",
    color: "deep-purple-lighten-1",
  },
]);

onMounted(async () => {
  user.value = await fetchUser();
});
const token = localStorage.getItem("token");

const fetchUser = async () => {
  try {
    return await store.dispatch("user/getUser", { token });
  } catch (error) {
    router.push({ name: "/login" });
  }
};
</script>
<style lang="scss"></style>
