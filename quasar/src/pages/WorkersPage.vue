<template>
    <q-page class="">
      <div class="">
          <q-table class="q-pa-sm q-ma-sm"
            title = 'Список сотрудников'
            dense
            :rows="filteredWorkers"
            :columns="columns"
            row-key="name"
            :pagination="pagination"
            :rows-per-page-options="[30]"
          />
      </div>
    </q-page>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import { ref } from 'vue'
  import { useWorkersStore } from "../stores/workersstore"

  const workersStore = useWorkersStore()
  
  const columns = [
    { name: 'number', align: 'center', label: '№', field: 'id', sortable: true },
    {
      name: 'last_name',
      required: true,
      label: 'Фамилия',
      align: 'left',
      field: dispatchers => dispatchers.last_name,
      format: val => `${val}`,
      sortable: true
    },
    { name: 'first_name', label: 'Имя', field: 'first_name', align: 'left', sortable: true},
    { name: 'middle_name', label: 'Отчество', field: 'middle_name', align: 'left', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
    { name: 'job_title', label: 'Должность', field: 'job_title', align: 'left', sortable: true},
    { name: 'mobile_phone_number', label: 'Номер мобильного телефона', field: 'phone_number', align: 'left', sortable: true},
    { name: 'mobile_phone_number', label: 'Номер рабочего телефона', field: 'phone_number_worked', align: 'left', sortable: true},
  ]
  
  export default defineComponent({
    name: 'WorkersPage',
    
    // Фильтр search из MainLayout.vue для сортировки таблицы
    props: {
        search: String,
    },

    data() {
      return {
        workersStore,
        columns,

        pagination: ref({
            rowsPerPage: 30
        })
      }
    },
  
    methods: {
      loadData() {
        // Загрузка данных о существующих дорожных объектах
        this.$axios.get('http://localhost:8000/api/objects')
        .then((response) => {
          this.roadObjects = response.data
          console.log(this.roadObjects)
        })
        .catch(() => {
          console.log(console.error())
        })
  
        // Загрузка оперативного журнала
        this.$axios.get('http://localhost:8000/api/tasks')
        .then((response) => {
          this.tasks = response.data
          console.log(this.tasks)
        })
        .catch(() => {
          console.log(console.error())
        })
  
        // Загрузка данных о работниках выполняющих текущие заявки
        this.$axios.get('http://localhost:8000/api/workers')
        .then((response) => {
          this.workers = response.data
          console.log(this.workers)
        })
        .catch(() => {
          console.log(console.error())
        })
  
        // Загрузка данных о 
        this.$axios.get('http://localhost:8000/api/dispatchers')
        .then((response) => {
          this.dispatchers = response.data
          console.log(this.dispatchers)
        })
        .catch(() => {
          console.log(console.error())
        })
      },
    },

    computed: {
        // Фильтрует таблицу светофорных объектов по полю name 
        filteredWorkers() {
            return this.workersStore.workersList.filter(elem => elem.last_name.toLowerCase().indexOf(this.search.toLowerCase()) !== -1)    
        },
    },
  
    mounted() {
      workersStore.fetchWorkers()
    },
  
  
  })
  </script>