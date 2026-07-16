import { defineStore } from 'pinia';
import axios from 'axios';
import type { Match } from '../model/Match';

export const useMatchStore = defineStore('matchStore', {
    state: () => ({
        match: null as Match | null,
        isLoading: false,
        error: null as string | null,
    }),

    actions: {
        async fetchMatch() {
            this.isLoading = true;
            this.error = null;
            try{
                const response = await axios.get<Match>('http://localhost:8000/api/match');
                this.match = response.data;
            }catch(error: any){
                console.error('Error fetching match:', error);
                this.error = " || 'An error occurred while fetching the match.'";
            }finally {
                this.isLoading = false;}
            }
    }
});