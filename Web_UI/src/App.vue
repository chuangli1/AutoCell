<template>
  <div style="height:100%">
    <div class='title'>
      <span>AutoCell Cloud System 1.0</span>
    </div>
      <router-view></router-view>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
export default Vue.extend({
  name: "App",
  data() {
    return {
      isManager: 0
    }
  },
  methods: {
  }
});
</script>
<style scoped>
.title{
  width:100%;
  display: flex;

  align-items: center;
  text-align: center;
  justify-content: center;
  flex-direction: column;
  background-color:#75B0ED; 
  height:5%;
  position: sticky;
  top:0%;
  z-index: 1000;
}

</style>
