<template>
  <div style="height:100%">
    <div class='title'>
      <span>AutoCell System</span>
    </div>
    <div class="body">
      <router-view></router-view>
    </div>
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
  height:6%;
  position: fixed;
  top:0;
  z-index: 1000;
}
.body{
   position: relative;
   top:6%;
   height: 94%;
}

</style>
