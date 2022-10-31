<template>
  <q-page class="">
    <div class="q-pa-lg">
      <q-table
        title="Оперативный журнал"
        dense
        :rows="taskStore.taskList"
        :columns="columns"
        row-key="id"
        :pagination="pagination"
        :rows-per-page-options="[0]"
      >
        <template v-slot:body-cell-task_status="props">
          <q-td :props="props">
            <q-checkbox
              v-model="props.row.task_status"
              :color="props.value ? 'green' : 'red'"
              :disable="props.value"
            />
          </q-td>
        </template>
      </q-table>
    </div>
  </q-page>
</template>
  
  <script>
import { defineComponent } from "vue";
import { ref } from "vue";
// import { TableCheckBox } from "../components/TableCheckBox.vue";
import { useTaskStore } from "../stores/taskstore";

const columns = [
  {
    name: "number",
    align: "center",
    label: "№",
    field: "number",
    sortable: true,
  },
  {
    name: "dateStart",
    align: "center",
    label: "Время поступления",
    field: (taskList) => taskList.task_start.toLocaleString("ru"),
    sortable: true,
  },
  {
    name: "address",
    required: true,
    label: "Адрес дорожного объекта",
    align: "left",
    field: (taskList) => taskList.address,
    //format: val => `${val}`,
    sortable: true,
  },
  {
    name: "bug_description",
    label: "Описание неисправности",
    field: "bug_description",
    align: "left",
    sortable: true,
  },
  {
    name: "sender",
    label: "Кто передал",
    field: "sender",
    align: "left",
    sortable: true,
  },
  {
    name: "dispatcher",
    label: "Кто принял",
    field: "dispatcher",
    align: "left",
    sortable: true,
  },
  {
    name: "worker",
    label: "Исполнитель",
    field: "worker",
    align: "left",
    sortable: true,
  },
  {
    name: "job_description",
    label: "Выполненные работы",
    field: "job_description",
    align: "left",
    sortable: true,
  },
  {
    name: "job_doc_number",
    label: "Номер документа",
    field: "job_doc_number",
    align: "left",
    sortable: true,
  },
  {
    name: "task_end",
    label: "Время закрытия",
    field: "task_end",
    align: "left",
    sortable: true,
    sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
  },
  {
    name: "task_status",
    label: "Статус",
    field: "task_status",
    align: "left",
    sortable: true,
  },
];

const taskStore = useTaskStore();

export default defineComponent({
  components: {},
  name: "TasksPage",

  data() {
    return {
      roadObjects: [],
      columns,
      taskStore,
      pagination: ref({
        rowsPerPage: 30,
      }),
    };
  },

  computed: {},

  mounted() {
    taskStore.fetchTasks();
  },
});
</script>

<style>
tbody > tr:hover {
  background-color: rgba(0, 60, 95, 0.438);
  color: rgb(255, 255, 255);
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.185);
}
</style>

