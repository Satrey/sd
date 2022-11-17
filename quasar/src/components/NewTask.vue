<template>
  <div class="q-pa-md">
    <div class="q-gutter-sm">
      <div class="col-12">Номер заявки: {{}}</div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
import { useTaskStore } from "../stores/taskstore";

const taskStore = useTaskStore();

export default defineComponent({
  components: {},
  name: "NewTasks",

  props: {
    search: String,
  },

  data() {
    return {
      taskStore,
    };
  },

  computed: {},

  mounted() {},
});
</script>

<style></style>
