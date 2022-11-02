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
        const data = await api.get('http://api.tgt72.ru/api/v3/trafficlight/')  //('http://localhost:8000/api/objects') //http://api.tgt72.ru/api/v3/trafficlight/
          let res = data.data
          this.roadObjectsList = res.objects
          console.log('Запрос Axios из store ', this.roadObjectsList)
        }
        catch (error) {
          alert(error)
          console.log(error)
      }
    }
  },
         
});