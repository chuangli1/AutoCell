<template>
<div>
    <div class="general" style="position:relative; top:5px; min-height:300px">
        <span class="title"><span><i style="padding-right:6px" class="el-icon-refresh"></i>多试剂切换系统控制</span></span>
        <lab-box :tasks="regantTasks" taskType="regant"></lab-box>
    </div>
     <div class="general" style="margin-top:20px; min-height:300px">
                <span class="title"><span><i style="padding-right:6px" class="el-icon-monitor"></i>监视系统控制</span></span>
    </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
import labBox from './tools/labBox.vue'
export default Vue.extend({
    name: 'labManager',
    data() {
        return{
           regantTasks:[{
              name:'任务1',
              id:1,
              des:'dhfljlegjlwe',
              access:true
           },{
              name:'任务1',
              id:1,
              des:'dhfljlegjlwe',
              access:true
           },{
              name:'任务1',
              id:1,
              des:'dhfljlegjlwe',
              access:true
           },
           {
              name:'任务1',
              id:1,
              des:'dhfljlegjlwe',
              access:true
           }]
        }
    },
    components:{
        labBox
    },
    methods:{

    },
    created(){

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