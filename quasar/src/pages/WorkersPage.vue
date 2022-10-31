<template>
    <q-page class="">
      <div class="q-pa-lg">
          <q-table
            title = 'Список сотрудников'
            :rows="workers"
            :columns="columns"
            row-key="name"
            :pagination="pagination"
            :rows-per-page-options="[0]"
          />
      </div>
    </q-page>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import { ref } from 'vue'
  
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
    { name: 'mobile_phone_number', label: 'Номер мобильного телефона', field: 'phone_number', align: 'left', sortable: true},
    { name: 'mobile_phone_number', label: 'Номер рабочего телефона', field: 'phone_number_worked', align: 'left', sortable: true},
  ]
  
  export default defineComponent({
    name: 'WorkersPage',
  
    data() {
      return {
        workers: [],
        columns,

        pagination: ref({
            rowsPerPage: 15
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
  
    mounted() {
      this.loadData()
    },
  
  
  })
  </script>