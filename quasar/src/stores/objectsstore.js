import { defineStore } from 'pinia';
import { api } from '../boot/axios';


export const useObjectsStore = defineStore('objectsstore', {
  state: () => ({
    roadObjectsList: [],
  }),

  getters: {
    
  },

  actions: {
    async fetchRoadObjects() {
      try {
        const data = await api.get('http://localhost:8000/api/objects') //('http://localhost:8000/api/objects') //http://api.tgt72.ru/api/v3/trafficlight/
          this.roadObjectsList = data.data
          console.log('Запрос Axios из store ', this.roadObjectsList)
        }
        catch (error) {
          alert(error)
          console.log(error)
      }
    }
  },
         
});