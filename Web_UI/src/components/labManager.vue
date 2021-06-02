<template>
<div>
    <div class="general" style="position:relative; top:5px; min-height:300px">
        <span class="title"><span><i style="padding-right:6px" class="el-icon-refresh"></i>多试剂切换系统控制</span></span>
        <lab-box v-if="taskFlag==1" :activeList="activeRegantList" taskType="regant"></lab-box>
    </div>
     <div class="general" style="margin-top:20px; min-height:300px">
        <span class="title"><span><i style="padding-right:6px" class="el-icon-monitor"></i>监视系统控制</span></span>
        <lab-box  v-if="taskFlag==1"  :activeList="activeMonitorList" taskType="monitor" :locations='locations'></lab-box>
    </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
import labBox from './tools/labBox.vue'
declare let $:any;
export default Vue.extend({
    name: 'labManager',
    props:{refresh:Boolean},
    data() {
        return{
           regantTasks:[],
           monitorTasks:[],
           userName:'',
           activeregantList:[],
           activemonitorList:[],
           taskFlag:0,
           locations:[]

        }

    },
    watch:{
        refresh: function(){
            const self:any = this;
            self.refreshData();
        }
    },
    components:{
        labBox
    },
    methods:{
        refreshData(){
            const self:any = this;
            $.post('/getLocation',{username:sessionStorage.username}).then(data=>{
                if(data.code===1){
                     self.locations = data.locationList.map(n=>{
                        return {
                            id:n[0],
                            name:n[1],
                            angle:n[3],
                            line:n[4]
                        }
                    });                  
                }
                else{
                    self.$message.error('未知错误');
                }
            });
        }

    },
    created(){
       const self:any = this;
        $.get('/loadTaskList').then(data=>{
            self.activeMonitorList = data.taskList.filter(d=>{return d[3]==='monitor'}).map(d=>{return [d[1],d[2]]});
            self.activeRegantList = data.taskList.filter(d=>{return d[3]==='regant'}).map(d=>{return [d[1],d[2]]});
            self.taskFlag++;
            self.refreshData();
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