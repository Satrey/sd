import { defineStore } from 'pinia';
import axios from 'axios';


export const useDispatchersStore = defineStore('dispatcherstore', {
  state: () => ({
    dispatchersList: []
  }),

  getters: {
    
  },

  actions: {
    async fetchDispatchers() {
      try {
        const data = await axios.get('http://localhost:8000/api/dispatchers')
          this.dispatchersList = data.data
        }
        catch (error) {
          alert(error)
          console.log(error)
      }
    }
  },
         
});