<template>
<div>
    <div class="general" style="margin-top:20px; min-height:300px">
        <span class="title"><i style="padding-right:6px"  class="el-icon-user"></i>团队成员</span>
        <team-box :members="members" v-if="setFlag"></team-box>
    </div>
    <div class="general" style="margin-top:20px; min-height:300px">
        <span class="title"><i style="padding-right:6px"  class="el-icon-user-solid"></i>个人设置</span>
        <user-box :user="user"  v-if="setFlag"></user-box>
    </div>
</div> 
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
import teamBox from './tools/teamBox.vue'
import userBox from './tools/userBox.vue'
export default Vue.extend({
    name:'userManager',
    data(){
        return{
             members:[],
             user:{},
             setFlag: false
        }
    },
    components:{
        teamBox,
        userBox
    },
    methods:{

    },
    created(){
        const self:any = this;
        $.get('http://localhost:5000/loadTeam').then(data=>{
            data.members.forEach(e => {
                self.members.push({
                    'name':e[0],
                    'isManager':e[5]===0
                });
            });
            self.user = self.members.filter(d=>d.name===sessionStorage.username)[0];
            self.setFlag = true;
        })
    }
})
</script>
<style lang='scss' scoped>
.general{
    border: 1px solid #bbbbbb;
    border-radius: 6px;
    padding: 16px 16px 0px 16px;
    padding-bottom: 0px;
    position: relative;
    margin-bottom: 16px;
    margin-top: 6px;
    font-size: 12px;
    .title {
        position: absolute;
        top: -12px;
        font-size: 14px;
        background-color: #ffffff;
        padding: 0 8px;
    }
}
</style>