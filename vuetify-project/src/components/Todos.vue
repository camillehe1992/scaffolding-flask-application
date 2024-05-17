<template>
  <div>
    <h1>My todos</h1>
    <div>
      <v-btn variant="tonal" size="large" color="black" block rounded="lg">
        + new
      </v-btn>
    </div>

    <v-list
      lines="one"
      rounded="lg"
      density="compact"
      border="xs"
      min-width="75vh"
    >
      <v-list-item
        v-for="item in items"
        :key="item.id"
        :title="item.name"
        @click="removeTodo(item.id)"
      ></v-list-item>
    </v-list>

    <div>
      🥳 App successfully hosted. Try creating a new todo.
      <br />
      <a
        href="https://docs.amplify.aws/gen2/start/quickstart/nextjs-pages-router/"
      >
        Review next steps of this tutorial.
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const items = ref([
  {
    name: "Learn Vue!!!",
    id: 1,
  },
  {
    name: "Go Shopping",
    id: 2,
  },
  {
    name: "Learn AWS",
    id: 3,
  },
]);

const removeTodo = (id) => {
  console.log(id);
};
</script>

<style lang="scss" scoped>
h1 {
  padding: 10px 0;
}
.v-btn {
  margin-bottom: 10px;
}
.v-list {
  padding: 0;
  margin-bottom: 10px;
  border: 1px solid currentColor;
}
.v-list-item:not(:last-child) {
  border-bottom: 1px solid currentColor;
}
</style>
