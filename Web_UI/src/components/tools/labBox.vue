<template>
  <div>
    <div class="addIcon"><span @click="addTask"><i class="el-icon-plus"></i></span></div>
    <el-card v-for="(task,index) in tasks" :key='index' class="box-card labBox">
        <div slot="header" class="clearfix">
            <span>{{task.name}}</span>
            <span style="float: right; padding: 3px 0">
                <i v-if='task.access' class="el-icon-delete icon" @click="deleteTask(task.id)"></i>
                <i v-if='task.access' class="el-icon-edit-outline icon" @click="editTask(task.id)"></i>
            </span>
        </div>
        <div>
            <div>
            <i class="el-icon-warning-outline"></i>
            </div>
            <div style="float: right; padding: 3px 0;font-size:14px">{{task.des}}</div>
        </div>
    </el-card>
    <el-dialog
        :visible.sync="dialogVisible"
        @close='closeEdit'
        width='680px'
        heigth="480px"
        top="15vh"
        >
        <div>
           <el-input placeholder="请输入内容" v-model="taskNew.name">
                <template slot="prepend">任务名：</template>
           </el-input>
           <el-input placeholder="请输入数字" v-model="taskNew.time[0]" class="input-with-select">
               <template slot="prepend">开始时间：</template>
                <template slot="append">小时后</template>
           </el-input>
           <el-input placeholder="请输入数字" v-model="taskNew.time[1]" class="input-with-select">
               <template slot="prepend">结束时间：</template>
                <template slot="append">小时后</template>
           </el-input>
           <el-input placeholder="请输入数字" v-model="taskNew.time[0]" class="input-with-select">
               <template slot="prepend">任务间隔：</template>
                <template slot="append">小时</template>
           </el-input>
           <el-input v-if="taskType==='regant'" placeholder="请输入数字" v-model="taskNew.time[1]" class="input-with-select">
               <template slot="prepend">阀门开启时间：</template>
                <template slot="append">秒</template>
           </el-input>
           <el-input v-if="taskType==='monitor'" placeholder="请输入数字" v-model="taskNew.time[1]" class="input-with-select">
               <template slot="prepend">视频录制时间：</template>
                <template slot="append">秒</template>
           </el-input>
          
        </div>
     </el-dialog>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    name:'labBox',
    props:{
        tasks:Array,
        taskType:String
    },
    data(){
        return{
           dialogVisible:false,
           taskNew:{
               name:'',
               time:[0,0],
               interval:[0,0]


           }
        }
    },
    methods:{
        deleteTask(id){

        },
        editTask(id){
           const self:any = this;
           self.dialogVisible = true;
        },
        addTask(){
            const self:any = this;
            self.dialogVisible = true;
            if(self.taskType==='regant'){
              alert(1)
            }
        },
        closeEdit(){
            const self:any = this;
            self.dialogVisible = false;
            self.$message.error('未保存！');
        }
    },
    created(){

    }
    
})
</script>
<style lang='scss' scoped>
 .addIcon{
        text-align: right;
        height: 6px;
        padding: 0 0px;
        font-size: 18px;
        position: relative;
        top: -15px;

}
.labBox{
    padding:10px 10px 10px;
    :hover  .icon{
       color: #409EFF;
    }
}
</style>
