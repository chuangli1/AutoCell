<template>
  <div>
    <div style="text-align:center">
      AutoCell Cloud System 1.0
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
