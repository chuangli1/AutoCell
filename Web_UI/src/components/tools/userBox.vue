<template>
<div>
   <div class="addIcon">
      <el-button size='small' type="primary" icon="el-icon-refresh-left" @click="updateUser">更新</el-button>
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
         <input v-model="password0" placeholder="********" type='password'/>
      </div>
      <div class="Content"><i class="el-icon-lock" style="padding-right:6px"></i>确认密码：
        
         <input  v-model="password1" placeholder="********" type='password'/>
      </div>
   </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
export default Vue.extend({
   name:'userBox',
   props:{
      user:Object
   },
   data(){
      return{
         password0:'',
         password1:'',
      }
   },
   methods:{
       updateUser(){
          const self:any = this;
          let data = {
              user_id: self.user.id,
              user_password:self.password0===self.password1&&self.password0!=''?self.password0:'',
              user_mail:self.user.email,
              user_phone:self.user.phone,
              user_office:self.user.office,
              user_address:self.user.address
          }
          if(!self.testF(data)) self.$message.error('输入格式错误');
          else
            $.post('http://localhost:5000/updateUser',data).then(data=>{
               if(data.code === 0){
                  self.$message.error('未知错误');
               }
               else{
                     self.$message({
                        message: '更新成功',
                        type: 'success'
                     });
               }
            })
       },
       testF(data){
          const mailTest = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/;
          const phoneTest = /^((\d{11})|(\d{3,4}-)*(\d{7,8})+(-\d{1,4})*|(\d{5}))$/;
          if(!data.user_mail.match(mailTest)) return false;
          if(!data.user_phone.match(phoneTest)) return false;
          return true;
       }
   }

})
</script>
<style lang='scss' scoped>
.addIcon{
    cursor: pointer;
    outline:none;
    text-align: right;
    height: 6px;
    padding: 0 0px;
    font-size: 18px;
    position: relative;
    top: -8px;
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
        color: #524949;
        background-color: #f6f6f6;
        border:none
   }
}
</style>