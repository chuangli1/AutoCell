<!--基本html代码区域-->
<template>
  <div class="firstdemo">
      <el-form ref="form" :model="form" status-icon :rules="rules2" label-width="100px">
           <el-row type="flex" justify="center">
              <el-col :span="4">
                  <el-form-item label-width="80px">
                    <h2 class="title">用户登录</h2>
                  </el-form-item>
              </el-col>
          </el-row>
          <el-row type="flex" justify="center">
              <el-col :span="6">
                  <el-form-item label="账户：" prop="username">
                      <el-input v-model="form.username"></el-input>
                  </el-form-item>
              </el-col>
          </el-row>
          <el-row type="flex" justify="center">
              <el-col :span="6">
                  <el-form-item label="密码：" prop="password">
                      <el-input v-model="form.password"></el-input>
                  </el-form-item>
              </el-col>
          </el-row>
          <el-row type="flex" justify="center">
                  <el-form-item>
                      <el-button style="width: 200px;" type="primary" @click="submit('form')">提交</el-button>
                  </el-form-item>
          </el-row>
          <el-row style="text-align: center;margin-left:80px">
                <el-link type="primary" @click="register()">还没账号，立即注册</el-link>
            </el-row>
      </el-form>
         
  </div>
</template>

<!--数据存贮交互，事件控制地区-->
<script lang='ts'>
declare let $:any;
import Vue from 'vue'
export default Vue.extend({
  name: 'firstdemo',
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
            $.get('http://localhost:3000/api/login', {
              params: {
                username: self.form.username,
                password: self.form.password
              }
            })
            .then(res => {
              console.log(res)
              console.log(res.data.mydata)
              var code = res.data.statusCode
              var msg = res.data.msg
              if(code==200) {
                alert('登录中');
                $.get('http://localhost:3000/api/video', {
                params: {
                username: self.form.username
                }
               })
                .then(resv => {
                self.$router.push({name: 'index',params: { mydata: res.data.mydata,myvideo:resv.data.myvideo}});
                })
              }
              else{
                  alert('密码错误');
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
