<template>
  <div>
    <div>{{number}}</div>
    <div>
      <button @click="add">+</button>
      <button @click="minus">-</button>
      <router-view></router-view>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
export default Vue.extend({
  name: "lifa",
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