<!--基本html代码区域-->
<template>
  <div class="general addBox">
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
                  <el-button style="width: 90px;" type="primary" @click="add('form')">添加</el-button>
                  <el-button style="width: 90px;" type="primary" @click="del('form')">删除</el-button>
              </el-form-item>
          </el-row>
      </el-form>
         
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
      add:function(formName){
        const self:any = this;
         self.$refs[formName].validate((valid) => {
          if (valid) {
            $.post('http://localhost:5000/addUser', {
                username: self.form.username,
                password: self.form.password
            })
            .then(res => {
              console.log(res)
              var code = res.code
              if(code==0) {
                alert('账号已存在');
              }
              if(code==1){
                  alert('保存成功');
              }
              else{
                  alert('保存失败')
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
      },
      del:function(formName){
        const self:any = this;
         self.$refs[formName].validate((valid) => {
          if (valid) {
            $.post('http://localhost:5000/deleteUser', {
                username: self.form.username,
                password: self.form.password
            })
            .then(res => {
              console.log(res)
              var code = res.code
              if(code==2) {
                alert('密码错误');
              }
              if(code==1){
                  alert('删除成功');
              }
              else{
                  alert('账号不存在')
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
      },

  },
})
</script>

<style lang='scss' scoped>
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
.addBox{
  position: relative;
  float:right;
  top:0%;
  right:5%;
}

</style>

