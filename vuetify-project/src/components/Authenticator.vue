<template>
  <v-card v-if="!reset" min-width="60vh">
    <v-tabs v-model="tab" fixed-tabs>
      <v-tab text="Sign In" value="signin"></v-tab>
      <v-tab text="Create Account"></v-tab>
    </v-tabs>

    <v-card-text>
      <v-tabs-window v-model="tab" value="create-account">
        <v-tabs-window-item value="signin">
          <login @to-reset="reverseReset" />
        </v-tabs-window-item>

        <v-tabs-window-item value="create-account">
          <create-account />
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-text>
  </v-card>
  <v-card v-else min-width="65vh">
    <reset-password @to-reset="reverseReset" />
  </v-card>
</template>

<script setup>
import { ref } from "vue";
const reset = ref(false);
const tab = ref(null);

const reverseReset = () => (reset.value = !reset.value);
</script>

<style lang="scss" scoped></style>
