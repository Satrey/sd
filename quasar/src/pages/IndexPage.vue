<template>
  <q-page>
    <div class="q-pa-lg">
      <q-table
        title="Список светофорных объектов"
        dense
        :rows="roadObjects.objects"
        :columns="columns"
        row-key="id"
        :pagination="pagination"
        :rows-per-page-options="[15, 30, 45, 60]"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";

const columns = [
  {
    name: "number",
    align: "center",
    label: "№",
    field: "id",
    sortable: true,
  },
  {
    name: "name",
    required: true,
    label: "Адрес дорожного объекта",
    align: "left",
    field: "name",
    sortable: true,
  },
  { name: "lat", label: "Широта", field: "lat", align: "left", sortable: true },
  {
    name: "lon",
    label: "Долгота",
    field: "lon",
    align: "left",
    sortable: true,
  },
  {
    name: "regime_description",
    label: "Описание",
    field: "regime_description",
    align: "left",
    sortable: true,
  },
];

export default defineComponent({
  name: "IndexPage",

  data() {
    return {
      roadObjects: [],
      columns,

      fixed: ref(false),

      pagination: ref({
        rowsPerPage: 30,
      }),
    };
  },

  methods: {
    loadData() {
      // Загрузка данных о существующих дорожных объектах
      this.$axios
        .get("http://api.tgt72.ru/api/v3/trafficlight/")
        .then((response) => {
          this.roadObjects = response.data;
          console.log(this.roadObjects);
        })
        .catch(() => {
          console.log(console.error());
        });
    },
  },

  mounted() {
    this.loadData();
  },
});
</script>

<style lang="css">
tbody > tr:hover {
  background-color: rgba(0, 60, 95, 0.438);
  color: rgb(255, 255, 255);
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.185);
}
</style>