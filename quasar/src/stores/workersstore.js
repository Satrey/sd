import { defineStore } from 'pinia';
import { api } from '../boot/axios';


export const useWorkersStore = defineStore('workerstore', {
  state: () => ({
    workersList: [],
  }),

  getters: {
    
  },

  actions: {
    async fetchWorkers() {
      try {
        const data = await api.get('http://localhost:8000/api/workers')
          this.workersList = data.data
        }
        catch (error) {
          alert(error)
          console.log(error)
      }
    }
  },
         
});