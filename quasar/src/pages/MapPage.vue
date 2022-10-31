<template>
    <q-page class="flex flex-center">
        <q-card id="map-card" class="shadow-14">
            <div id = "map" class="shadow-14">
            </div>
        </q-card>
    </q-page>
</template>
 
<script>
import { Map, View } from 'ol';
import { Tile as TileLayer } from 'ol/layer';
import { OSM } from 'ol/source';
import {useGeographic} from 'ol/proj';
import { ref } from 'vue'

useGeographic();

export default {
    name: 'MapPage',
    mounted() {
        this.map = new Map({
            target: 'map',
            layers: [
                new TileLayer({
                    source: new OSM(),
                    name: 'OSM'
                })
            ],
            view: new View({
                center: [65.5272, 57.1522],
                zoom: 15
            })
        });
 
        // Mutate the map object or change the map state
        // this.$store.commit('setMap', this.map);
        
 
    }
}
</script>
 
<style scoped>
#map{
    height: 91vh;
    width: auto;
    margin: 0;
    padding: 0;
}

#map-card {
    height: 93vh;
    width: 87.5vw;
    margin: 0;
    padding: 10px;
}
</style>