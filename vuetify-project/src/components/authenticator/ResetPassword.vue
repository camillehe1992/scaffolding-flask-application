<template>
  <v-card-text>
    <v-card-title> Reset Password </v-card-title>
    <v-form
      v-show="resetToggle"
      v-model="sendCodeForm"
      @submit.prevent="sendCode"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Email</div>

      <v-text-field
        v-model="email"
        :readonly="loading"
        :rules="[required]"
        placeholder="Enter Email"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
        clearable
      ></v-text-field>

      <div
        v-if="!status?.success"
        class="pb-2 text-red text-caption text-decoration-none"
      >
        {{ status?.msg }}
      </div>

      <v-card-actions>
        <v-btn
          :disabled="!sendCodeForm"
          :loading="loading"
          type="submit"
          size="large"
          variant="tonal"
          block
          @click="sendCode"
        >
          Send Code
        </v-btn>
      </v-card-actions>
      <div class="center-button">
        <v-btn @click="$emit('toReset')" variant="text">
          Back to Sign In
        </v-btn>
      </div>
    </v-form>

    <v-form
      v-show="!resetToggle"
      v-model="resetPasswordForm"
      @submit.prevent="resetPassword"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Code *</div>

      <v-text-field
        v-model="code"
        :readonly="loading"
        :rules="[required]"
        placeholder="Enter Code"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
        clearable
      ></v-text-field>

      <div
        class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
      >
        New Password
      </div>

      <v-text-field
        v-model="password"
        :readonly="loading"
        :rules="[required]"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        placeholder="Enter Password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
        clearable
      ></v-text-field>

      <div
        class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
      >
        Confirm Password
      </div>

      <v-text-field
        v-model="confirmedPassword"
        :readonly="loading"
        :rules="[required]"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        placeholder="Confirm Password"
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

      <v-card-actions>
        <v-btn
          :disabled="!resetPasswordForm"
          :loading="loading"
          type="submit"
          class="mb-8"
          size="large"
          variant="tonal"
          block
        >
          Submit
        </v-btn>
      </v-card-actions>

      <div class="center-button">
        <v-btn @click="sendCode" variant="text"> Resend Code </v-btn>
      </div>
    </v-form>
  </v-card-text>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ref } from "vue";

const router = useRouter();
const store = useStore();

const resetToggle = ref(true);
const visible = ref(false);

const sendCodeForm = ref(null);
const resetPasswordForm = ref(null);

const code = ref(null);
const email = ref(null);
const password = ref(null);
const confirmedPassword = ref(null);
const loading = ref(false);
const status = ref(null);

const sendCode = async () => {
  if (!resetToggle.value) {
    resetToggle.value = true;
    email.value = null;
  }
  if (!sendCodeForm.value) return;
  loading.value = true;

  const params = {
    email: email.value,
  };

  // const res = await store.dispatch("user/sendCode", params);
  const res = {
    success: true,
    msg: "Email is sent!",
  };
  loading.value = false;
  status.value = res;
  if (res.success) {
    resetToggle.value = false;
    sendCodeForm.value = null;
  }
};

const resetPassword = () => {
  if (!resetPasswordForm.value) return;
  loading.value = true;

  if (password.value !== confirmedPassword.value) {
    status.value = {
      success: false,
      msg: "The password is invalid!",
    };
    return;
  }

  const params = {
    code: code.value,
    email: email.value,
    password: password.value,
  };

  // const res = await store.dispatch("user/resetPassword", params);
  const res = {
    success: true,
    msg: "",
  };
  loading.value = false;
  status.value = res;

  if (res.success) {
    resetToggle.value = false;
  }
};

const required = (v) => {
  return !!v || "Field is required";
};
</script>

<style lang="scss" scoped>
.center-button {
  text-align: center;
  margin-top: 10;
}
</style>
