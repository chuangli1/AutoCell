<template>
   <div class="userContent">
      <div class="Content"><i class="el-icon-message" style="padding-right:6px"></i>邮箱：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.email" :placeholder="user.email?user.email:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-phone-outline" style="padding-right:6px"></i>电话：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.phone" :placeholder="user.phone?user.phone:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-suitcase" style="padding-right:6px"></i>工作：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.office" :placeholder="user.office?user.office:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-location" style="padding-right:6px"></i>地址：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-lock" style="padding-right:6px"></i>新的密码：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
      </div>
      <div class="Content"><i class="el-icon-lock" style="padding-right:6px"></i>确认密码：
         <input style="dispaly:inline; width:300px; size:small" v-model="user.address" :placeholder="user.address?user.address:'未填写'"/>
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
.userContent{
   font-size:16px;
   .Content{
      display: block;
   }
}
</style>