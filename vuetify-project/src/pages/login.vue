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
          v-if="!status?.success"
          class="pb-2 text-red text-caption text-decoration-none"
        >
          {{ status?.msg }}
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
          <a class="text-blue text-decoration-none" href="/signup">
            Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
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

const onSubmit = async () => {
  if (!form.value) return;
  loading.value = true;

  const params = {
    email: email.value,
    password: password.value,
  };

  const res = await store.dispatch("user/login", params);
  if (res.success) {
    router.push({ name: "/" });
  }
  status.value = res;
  loading.value = false;
};

const required = (v) => {
  return !!v || "Field is required";
};
</script>
