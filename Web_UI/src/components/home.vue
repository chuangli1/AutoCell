<template>
  <div style="height:100%">
    <div class="home" style="height:100%;">
      <div class="row" style="height:100%;">
        <div class="left-area col-sm-3">
          <div>
            <i class="el-icon-bell"></i>
            <span>留言板</span>
          </div>
          <div class="info">
           <info-box></info-box>
          </div>
        </div>
        <div class="right-area col-sm-9">
          <el-tabs v-model="activeName">
            <el-tab-pane label="实时监控" name="first">
              <div id='monitor' class="monitor">
                <monitor @refreshData="refreshData=!refreshData" @refreshLocations="refreshLocations=!refreshLocations"></monitor>
              </div>
            </el-tab-pane>
            <el-tab-pane label="实验配置" name="second">
              <lab-manager :refresh='refreshLocations'></lab-manager>
            </el-tab-pane>
            <el-tab-pane label="数据管理" name="third">
              <data-manager :refresh="refreshData"></data-manager>
            </el-tab-pane>
            <el-tab-pane label="用户设置" name="fourth">
              <user-manager></user-manager>
            </el-tab-pane>
          </el-tabs>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import monitor from './monitor.vue';
import addUserBox from './tools/addUserBox.vue'
import infoBox from './tools/infoBox.vue'
import dataManager from './dataManager.vue'
import labManager from './labManager.vue'
import userManager from './userManager.vue'

export default Vue.extend({
  name: "home",
  data() {
    return {
      number: 0,
      isAddUser: false,
      isManager:false,
      activeName:'first',
      refreshData:false,
      refreshLocations:false
    }
  },
  components:{
    addUserBox,
    monitor,
    infoBox,
    dataManager,
    labManager,
    userManager
  },
  methods: {
    addUser(){
      const self:any = this;
      self.isAddUser = !self.isAddUser;
    },
    handleClick(tab, event) {
        console.log(tab, event);
    },
  },
  created(){
    const self:any = this;
    if(!sessionStorage.isUser) self.$router.push({path:'/'})
    sessionStorage.isManager==='true'?self.isManager = true:self.isManager = false;
  }
});
</script>
<style lang="scss" scoped>

  .home{
    margin: 20px;
  }
  .left-area{
    margin-top: 10px;
      .info{
        // border: 1px solid #bbbbbb;
        // border-radius: 6px;
        margin-top:8px;
        min-height: 90%;
        width: auto;
      }
  }
  .right-area{
      width:100%;
  }
</style>