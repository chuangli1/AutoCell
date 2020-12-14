<template>
  <div style="height:100%">
    <div class="container home" style="height:100%">
      <div class="row" style="height:100%">
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
                <monitor></monitor>
              </div>
            </el-tab-pane>
            <el-tab-pane label="实验配置" name="second">配置管理</el-tab-pane>
            <el-tab-pane label="数据管理" name="third">
              <data-manager></data-manager>
            </el-tab-pane>
            <el-tab-pane label="用户设置" name="fourth">
              <div v-if='isManager'  @click="addUser" class="addUser">
                <i :class="{ 'el-icon-plus': !isAddUser, 'el-icon-minus': isAddUser}"></i>
              </div>
              <add-user-box v-if='isAddUser' class='addBox'></add-user-box>
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

export default Vue.extend({
  name: "home",
  data() {
    return {
      number: 0,
      isAddUser: false,
      isManager:false,
      activeName:'first'
    }
  },
  components:{
    addUserBox,
    monitor,
    infoBox,
    dataManager
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
  .addUser{
    cursor: pointer;
    text-align: right;
    font-size:16px;
  }
  .addBox{
      float:right;
    }
  .home{
    margin-top: 10px;
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
      width:70%;
  }
</style>