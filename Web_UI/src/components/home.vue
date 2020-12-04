<template>
  <div>

    <div>{{number+100}}</div>
    <div>
      <button @click="add">+</button>
      <button @click="minus">-</button>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
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
      },
      minus() {
          const self:any = this;
          let number: number = this.number - 1
          self.number = number
      }
  },
  created(){
    const self:any = this;
    if(!sessionStorage.isUser) self.$router.push({path:'/'})
  }
});
</script>
<style lang="scss" scoped>
  .general {
            border: 1px solid #bbbbbb;
            border-radius: 6px;
            padding: 16px;
            position: relative;
            margin-bottom: 16px;
            margin-top: 24px;
            font-size: 14px;
            .title {
                position: absolute;
                top: -12px;
                font-size: 18px;
                background-color: #ffffff;
                padding: 0 8px;
            }
  }
</style>