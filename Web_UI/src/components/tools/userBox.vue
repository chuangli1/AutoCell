<template>
<div>
   <div class="addIcon">
        <i class="el-icon-refresh-left"></i>
   </div>
   <div class="userContent">
       <div class="Content" style="color: #409EFF;"><i class="el-icon-s-custom" style="padding-right:6px"></i>用户：
      {{user.name}}</div>
      <div class="Content"><i class="el-icon-message" style="padding-right:6px"></i>邮箱：
         <input  v-model="user.email" :placeholder="user.email?user.email:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-phone-outline" style="padding-right:6px"></i>电话：
         <input v-model="user.phone" :placeholder="user.phone?user.phone:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-suitcase" style="padding-right:6px"></i>工作：
         <input  v-model="user.office" :placeholder="user.office?user.office:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-location" style="padding-right:6px"></i>地址：
         <input  v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-lock" style="padding-right:6px"></i>新的密码：
         <input v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-lock" style="padding-right:6px"></i>确认密码：
         <input  v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
      </div>
   </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
   name:'userBox',
   props:{
      user:Object
   },
   data(){
      
   },
   methods:{

   }

})
</script>
<style lang='scss' scoped>
.addIcon{
    cursor: pointer;
    text-align: right;
    height: 6px;
    padding: 0 0px;
    font-size: 18px;
    position: relative;
    top: -15px;
    :hover{
       color: #409EFF;
    }
}
.userContent{
   font-size:16px;
   margin: 10px;
   .Content{
      display: block;
      margin-bottom: 10px;
   }
   input{
      font-size: 12px;
        width:300px;
        height: 25px;
        outline: none;
        border-radius: 3px;
        color: #bbbbbb;
        background-color: #f6f6f6;
        border:none
   }
}
</style>