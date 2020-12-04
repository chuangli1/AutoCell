<!--基本html代码区域-->
<template>
<div  class="back">
  <div class="login">
      <el-form ref="form" :model="form" status-icon :rules="rules2" label-width="0px">
          <el-row type="flex" justify="center">
              <el-form-item prop="username">
                  <el-input placeholder='账户' v-model="form.username"></el-input>
              </el-form-item>
          </el-row>
          <el-row type="flex" justify="center">
              <el-form-item prop="password">
                  <el-input placeholder='密码' v-model="form.password"></el-input>
              </el-form-item>
          </el-row>
          <el-row type="flex" justify="center">
              <el-form-item>
                  <el-button style="width: 200px;" type="primary" @click="submit('form')">登录</el-button>
              </el-form-item>
          </el-row>
      </el-form>
         
  </div>
  </div>
</template>

<!--数据存贮交互，事件控制地区-->
<script lang='ts'>
declare let $:any;
import Vue from 'vue'
export default Vue.extend({
  name: 'login',
  data () {
    const self:any = this;
     var validateuser = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入用户名'));
        } else {
          if (self.form.checkPass !== '') {
            self.$refs.form.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          callback();
        }
      };
    return {
        form:{
            name:'',
            password:'',
        },
        rules2: {
          userName: [
            { validator: validateuser, trigger: 'blur' }
          ],
          password: [
            { validator: validatePass, trigger: 'blur' }
          ],
          
        }
    };
  },
  methods:{
      /*提交进行判断的函数 */
      submit:function(formName){
        const self:any = this;
         self.$refs[formName].validate((valid) => {
          if (valid) {
            $.post('http://localhost:5000/login', {
                username: self.form.username,
                password: self.form.password
            })
            .then(res => {
              console.log(res)
              var code = res.code
              if(code==0) {
                alert('账号不存在');
              }
              else if(code==2){
                  alert('密码错误');
              }
              else if(code==3){
                // 未记住登录
                //localStorage.clear();
                sessionStorage.isUser = true;
                sessionStorage.isManager = true;
                sessionStorage.username = self.form.username;
                self.$router.push({path: '/home'});
              }
              else{
                sessionStorage.isUser = true;
                sessionStorage.isManager = false;
                sessionStorage.username = self.form.username;
                self.$router.push({path: '/home'});
              }
            })
            .catch(error => {
                    console.log(error);
                })
          } else {
            alert('密码或者账号不完整');
            console.log('error submit!!');
            return false;
          }
        })
      }
  },
})
</script>
<style scoped>
.login{
  position: absolute;
  top:40%;
  left:calc(50% - 100px);
}
.back{
  background-color: gray;
  width: 100%;
  height:95%;
}
</style>
