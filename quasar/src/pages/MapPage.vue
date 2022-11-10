<template>
  <q-page class="flex flex-center">
    <q-card id="map-card" class="shadow-14">
      <div id="map" class="shadow-14"></div>
    </q-card>
  </q-page>
</template>
 
<script>
import { Map, View, Feature } from "ol";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { OSM, Vector as VectorSource } from "ol/source";
import { useGeographic, fromLonLat } from "ol/proj";
import { Point } from "ol/geom";
import { Circle, Fill, Icon, Stroke, Style, Text } from "ol/style";
import { ref } from "vue";

import { useObjectsStore } from "src/stores/objectsstore";

import "ol/ol.css";

useGeographic();
const store = useObjectsStore();

const iconFeature = new Feature({
  geometry: new Point([]),  // 65.564400266641, 57.15661500269
});

const pointStyle = new Style({
  image: new Circle({
    radius: 7,
    fill: new Fill({
      color: "red",
    }),
    stroke: new Stroke({
      color: "black",
      width: 1,
    }),
  }),
});

iconFeature.setStyle([pointStyle /*iconStyle*/]);

export default {
  name: "MapPage",

  data() {
    return {
      map: null,
      iconFeature: null,
      center: null,
      store,
      lon: 65.564400266641,
      lat: 57.15661500269,
    };
  },

  methods: {
    initMap() {

        console.log("Hi from init map function");
        iconFeature.setGeometry(new Point([this.lon, this.lat]));

      //   const iconFeature = new Feature({
      //     geometry:  new Point([65.5272, 57.1522]),
      //   });
      //   const iconStyle = new Style({
      //     image: new Icon({
      //       anchor: [0.5, 1],
      //       src: "assets/traffic-lights.png",
      //     }),
      //     text: new Text({
      //       text: "World\nText",
      //       font: "bold 30px Calibri,sans-serif",
      //       fill: new Fill({
      //         color: "black",
      //       }),
      //       stroke: new Stroke({
      //         color: "white",
      //         width: 2,
      //       }),
      //     }),
      //   });

        const vectorSource = new VectorSource({
            features: [iconFeature],
        });

        const vectorLayer = new VectorLayer({
            source: vectorSource,
        });

        const rasterLayer = new TileLayer({
            source: new OSM(),
        });

        const map = new Map({
            layers: [rasterLayer, vectorLayer],
            target: "map",
            view: new View({
                center: [65.5272, 57.1522],
                zoom: 14,
            }),
        });
    },
  },

  mounted() {
    this.initMap();

    // this.$store.commit('setMap', this.map);
    // this.map.getView().setCenter(ol.proj.transform([long, lat], 'EPSG:4326', 'EPSG:3857'));
  },
};
</script>
 
<style scoped>
#map {
  height: 90vh;
  width: auto;
}

#map-card {
  height: 100%;
  width: 100%;
  padding: 10px;
  margin: 5px;
  /*background-color: rgba(17, 17, 17, 0.644);*/
}
</style>