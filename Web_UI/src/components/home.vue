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
  }
});
</script>