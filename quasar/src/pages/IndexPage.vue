<template>
  <q-page>
    <div class="q-pa-lg">
      <q-table
        title="Список светофорных объектов"
        dense
        :rows="filteredObjects"
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
import { useObjectsStore } from '../stores/objectsstore'

// Задаем колонки которые будут в таблице, а так же их формат.
const columns = [
  {
    name: "number",
    align: "center",
    label: "№",
    field: "id",
    sortable: true,
  },
  // Поле для базы PostgreSQL
  // {
  //   name: "name",
  //   required: true,
  //   label: "Адрес дорожного объекта",
  //   align: "left",
  //   field: "address",
  //   sortable: true,
  // },
  // Поле для API tgt
  { 
    name: "name",
    required: true,
    label: "Адрес дорожного объекта",
    align: "left",
    field: "name",
    sortable: true,
  },
  // Поле для базы PostgreSQL
  // { name: "lat", label: "Широта", field: "latitude", align: "left", sortable: true },
  // Поле для API tgt
  { name: "lat", label: "Широта", field: "lat", align: "left", sortable: true },
  // Поле для базы PostgreSQL
  // {
  //   name: "lon",
  //   label: "Долгота",
  //   field: "longitude",
  //   align: "left",
  //   sortable: true,
  // },
  { name: "lon", label: "Широта", field: "lon", align: "left", sortable: true },
  // Поле для базы PostgreSQL
  // {
  //   name: "regime_description",
  //   label: "Описание",
  //   field: "description",
  //   align: "left",
  //   sortable: true,
  // },
  // Поле для API tgt
  {
    name: "regime_description",
    label: "Описание",
    field: "regime_description",
    align: "left",
    sortable: true,
  },
];

// Подключаем хранилище светофорных объектов
const roadObjectsStore = useObjectsStore()


export default defineComponent({
  name: "IndexPage",

   // Фильтр search из MainLayout.vue для сортировки таблицы
  props: {
    search: String,
  },


  data() {
    return {
      roadObjectsStore,
      columns,
      fixed: ref(false),
      pagination: ref({
        rowsPerPage: 30,
      }),
    };
  },

  // watch: {
  //   search() {
  //     //console.log('Search', this.search)
  //     this.filter = this.search
  //     //console.log('Fiilter', this.filter)
  //   }
  // },


  computed: {
    
    // Фильтрует таблицу светофорных объектов по полю name 
    filteredObjects() {
      return this.roadObjectsStore.roadObjectsList.filter(elem => elem.name.toLowerCase().indexOf(this.search.toLowerCase()) !== -1)    
    }
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

    printData(arg) {
      console.log(arg)
    },  
  },

  mounted() {
    // Загружаем данные в хранилище светофорных объектов
    roadObjectsStore.fetchRoadObjects();
    // console.log(this.roadObjectsStore.roadObjectsList)
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