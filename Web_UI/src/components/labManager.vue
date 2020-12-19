<template>
<div>
    <div class="general" style="position:relative; top:5px; min-height:300px">
        <span class="title"><span><i style="padding-right:6px" class="el-icon-refresh"></i>多试剂切换系统控制</span></span>
        <lab-box v-if="regantTasks" :tasks="regantTasks" taskType="regant"></lab-box>
    </div>
     <div class="general" style="margin-top:20px; min-height:300px">
        <span class="title"><span><i style="padding-right:6px" class="el-icon-monitor"></i>监视系统控制</span></span>
        <lab-box  v-if="monitorTasks" :tasks="monitorTasks" taskType="monitor"></lab-box>
    </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
import labBox from './tools/labBox.vue'
declare let $:any;
export default Vue.extend({
    name: 'labManager',
    data() {
        return{
           regantTasks:[],
           monitorTasks:[],
           userName:''
        }

    },
    components:{
        labBox
    },
    methods:{

    },
    created(){
       const self:any = this;
       self.userName = sessionStorage.username;
        $.get('http://localhost:5000/loadTasks?type=regant').then(function(data){
           data.tasks.forEach(e => {
                self.regantTasks.push({
                    id:e[0],
                    name:e[1],
                    username:e[2],
                    date:e[3],
                    valves:e[4],
                    time:e[5].split(','),
                    pres:e[6],
                    interval:e[7].split(','),
                    access:self.userName===e[2]
                })
            });
        });
        $.get('http://localhost:5000/loadTasks?type=monitor').then(function(data){
            data.tasks.forEach(e => {
                self.monitorTasks.push({
                    id:e[0],
                    name:e[1],
                    username:e[2],
                    date:e[3],
                    time:e[4].split(','),
                    interval:e[5].split(','),
                    access:self.userName===e[2]
                })
            });
        });
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