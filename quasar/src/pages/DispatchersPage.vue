<template>
    <q-page class="">
      <div class="q-pa-lg">
          <q-table class="pa-lg"
            title = 'Список действующих диспетчеров организации'
            dense
            :rows="dispatchersStore.dispatchersList"
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
  import { useDispatchersStore } from "../stores/dispatchersstore"
  
  const columns = [
    { name: 'number', align: 'center', label: '№', field: 'id', sortable: true },
    {
      name: 'last_name',
      required: true,
      label: 'Фамилия',
      align: 'left',
      field: dispatchersList => dispatchersList.last_name,
      format: val => `${val}`,
      sortable: true
    },
    { name: 'first_name', label: 'Имя', field: 'first_name', align: 'left', sortable: true},
    { name: 'middle_name', label: 'Отчество', field: 'middle_name', align: 'left', sortable: true, sort: (a, b) => parseInt(a, 10) - parseInt(b, 10) },
    { name: 'mobile_phone_number', label: 'Номер мобильного телефона', field: 'phone_number', align: 'left', sortable: true},
    { name: 'mobile_phone_number', label: 'Номер рабочего телефона', field: 'phone_number_worked', align: 'left', sortable: true},
  ]

  const dispatchersStore = useDispatchersStore()
  
  export default defineComponent({
    name: 'DispatchersPage',
  
    data() {
      return {
        dispatchersStore,
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
  
    mounted() {
        dispatchersStore.fetchDispatchers()
    },
  
  
  })
  </script>

<style>
tbody > tr:hover {
  background-color: rgba(0, 60, 95, 0.438);
  color: rgb(255, 255, 255);
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.185);
}
</style>