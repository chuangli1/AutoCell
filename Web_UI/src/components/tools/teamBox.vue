<template>
<div>
    <div v-if='isManager'  @click="isAddUser = !isAddUser" class="addIcon">
        <i :class="{ 'el-icon-plus': !isAddUser, 'el-icon-minus': isAddUser}"></i>
    </div>
    <add-user-box v-if='isAddUser' class='addBox'></add-user-box>
    <el-row>
    <el-col :span='8' v-for="(member,index) in members" :key='index'>
        <el-card  class="box-card teamBox">
            <div slot="header" class="clearfix">
                <i v-if="member.isManager" class="el-icon-star-on" style="color: #409EFF; padding-right:6px"></i>
                {{member.name}}
            </div>
            <div class="boxContent">
                <span class="Content"><i class="el-icon-message" style="padding-right:6px"></i>{{member.email?member.email:'未填写'}}</span>
                <span class="Content"><i class="el-icon-phone-outline" style="padding-right:6px"></i>{{member.phone?member.phone:'未填写'}}</span>
                <span class="Content"><i class="el-icon-suitcase" style="padding-right:6px"></i>{{member.office?member.office:'未填写'}}</span>
                <span class="Content"><i class="el-icon-location" style="padding-right:6px"></i>{{member.address?member.address:'未填写'}}</span>
            </div>
        </el-card>
    </el-col>
    </el-row>
    
</div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
import addUserBox from './addUserBox.vue'
export default Vue.extend({
    name:'teamBox',
    props:{
        members:Array
    },
    data(){
       return {
           isManager:sessionStorage.isManager==='true',
           isAddUser:false,
       }
    },
    components:{
        addUserBox
    },
    methods:{
        
    },
    created(){
        
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
}
.addBox{
    float:right;
}
.teamBox{
    margin: 10px;
    font-size:14px;
    .boxContent{
        .Content{
           display: block;
           margin: 5px;
        }
        
    }
}
</style>