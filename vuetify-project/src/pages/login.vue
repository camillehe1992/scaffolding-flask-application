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

          <a
            class="text-caption text-decoration-none text-blue"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
          >
            Forgot login password?</a
          >
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
          Log In
        </v-btn>

        <v-card-text class="text-center">
          <a class="text-blue text-decoration-none" href="/register">
            Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
          </a>
        </v-card-text>
      </v-form>
    </v-card>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
const visible = ref(false);

const form = ref(null);
const email = ref(null);
const password = ref(null);
const loading = ref(false);
const status = ref(null);

const router = useRouter();

const onSubmit = () => {
  if (!form.value) return;
  loading.value = true;

  const url = "http://localhost:5000/api/login";
  const params = {
    email: email.value,
    password: password.value,
  };

  axios
    .post(url, params)
    .then((r) => {
      if (r.data.success) {
        status.value = {
          message: r.data.msg,
          type: "succeed",
        };
        router.push({ name: "/" });
      } else {
        status.value = {
          message: r.data.msg,
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
