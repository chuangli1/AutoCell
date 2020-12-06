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
      number: 0
    }
  },
  methods: {
      add() {
          const self:any = this;
          let number: number = this.number + 1
          self.number = number
          $.get('/get',function(data){
            alert(data);
          })
          //self.$router.push('/home')
      },
      minus() {
          const self:any = this;
          let number: number = this.number - 1
          self.number = number
          self.$router.push('/')
      }
  }
});
</script>
<style scoped>
.title{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align:center; 
  background-color:wheat; 
  height:5%;
  position: sticky;
}

</style>
