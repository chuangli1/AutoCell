<template>
  <div>
    <div v-if='isManager'><span class="addUser" @click="addUser">+</span></div>
    <add-user-box v-if='isAddUser' class='addBox'></add-user-box>  
    <div id='monitor' class="monitor">
      <monitor></monitor>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import monitor from './monitor.vue';
import addUserBox from './tools/addUserBox.vue'

export default Vue.extend({
  name: "home",
  data() {
    return {
      number: 0,
      isAddUser: false,
      isManager:false
    }
  },
  components:{
    addUserBox,
    monitor,
  },
  methods: {
    addUser(){
      const self:any = this;
      self.isAddUser = !self.isAddUser;
    },
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
    sessionStorage.isManager==='true'?self.isManager = true:self.isManager = false;
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
  .addUser{
  position: absolute;
  cursor: pointer;
  top:-1.5%;
  left:95%;
  font-size:36px;
}
</style>