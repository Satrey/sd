import { defineStore } from 'pinia';
import axios from 'axios';


export const useTaskStore = defineStore('taskstore', {
  state: () => ({
    taskList: []
  }),

  getters: {
    
  },

  actions: {
    async fetchTasks() {
      try {
        const data = await axios.get('http://localhost:8000/api/tasks')
          this.taskList = data.data
        }
        catch (error) {
          alert(error)
          console.log(error)
      }
    }
  },
         
});