<template>
    <div class="q-pa-md">
      <div class="q-gutter-sm">      
        <q-checkbox />
      </div>
    </div>
</template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    setup () {
      return {
        green: ref(false),
        red: ref(false),
        cyan: ref(true)
      }
    }
  }
  </script>
  