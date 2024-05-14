<template>
  <div class="pa-12">
    <v-card
      class="mx-auto px-6 py-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <v-form v-model="form" @submit.prevent="onSubmit">
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>

        <v-text-field
          v-model="email"
          :readonly="loading"
          :rules="[required]"
          density="compact"
          placeholder="Email address"
          prepend-inner-icon="mdi-email-outline"
          variant="outlined"
          clearable
        ></v-text-field>

        <div
          class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
        >
          Password
        </div>

        <v-text-field
          v-model="password"
          :readonly="loading"
          :rules="[required]"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="visible = !visible"
          clearable
        ></v-text-field>

        <div
          v-if="status?.type == 'failed'"
          class="pb-2 text-red text-caption text-decoration-none"
        >
          {{ status?.message }}
        </div>

        <v-btn
          :disabled="!form"
          :loading="loading"
          type="submit"
          class="mb-8"
          color="blue"
          size="large"
          variant="tonal"
          block
        >
          Sign Up
        </v-btn>

        <v-card-text class="text-center">
          <a class="text-blue text-decoration-none" href="/login">
            <v-icon icon="mdi-chevron-left"></v-icon> Log in
          </a>
        </v-card-text>
      </v-form>
    </v-card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
const visible = ref(false);

const form = ref(null);
const email = ref(null);
const password = ref(null);
const loading = ref(false);
const status = ref(null);

const router = useRouter();
const store = useStore();

const onSubmit = () => {
  if (!form.value) return;
  loading.value = true;

  const params = {
    username: email.value,
    email: email.value,
    password: password.value,
  };

  store
    .dispatch("user/signup", params)
    .then((res) => {
      if (res.success) {
        status.value = {
          message: res.msg,
          type: "succeed",
        };
        router.push({ name: "/" });
      } else {
        status.value = {
          message: res.msg,
          type: "failed",
        };
      }
    })
    .catch((e) => {
      console.log(e);
    })
    .finally(() => {
      loading.value = false;
    });
};

const required = (v) => {
  return !!v || "Field is required";
};
</script>
