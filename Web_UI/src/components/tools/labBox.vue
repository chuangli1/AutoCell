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
            <div style="float: right; padding: 3px 0;font-size:14px">{{task.username}}</div>
        </div>
    </el-card>
    <el-dialog
        :visible.sync="dialogVisible"
        width='480px'
        heigth="450px"
        top="15vh"
        >
        <div class="inputBox">
           <el-input placeholder="输入任务名" v-model="taskNew.name" >
                <template slot="prepend">任务名：</template>
           </el-input>
           <el-input placeholder="输入小于24的整数" v-model="taskNew.time[0]" class="input-with-select inputSub">
               <template slot="prepend">开始时间：</template>
                <template slot="append">分钟</template>>
           </el-input>
           <el-input placeholder="输入大于开始时间的整数" v-model="taskNew.time[1]" class="input-with-select inputSub">
               <template slot="prepend">结束时间：</template>
                <template slot="append">分钟</template>
           </el-input>
           <el-input placeholder="请输入小于总时间的整数" v-model="taskNew.interval[0]" class="input-with-select inputSub">
               <template slot="prepend">任务间隔：</template>
               <template slot="append">分钟</template>
           </el-input>
           <div v-if="taskType==='regant'" class="inputSub">
           <el-input v-if="taskType==='regant'" placeholder="输入整数" v-model="taskNew.interval[1]" class="input-with-select">
               <template slot="prepend">单次开启时间：</template>
                <template slot="append">秒</template>
           </el-input>
           <div class="general inputSub">
               <span class="title">阀门开关及压力设定</span>
               <el-checkbox-group 
                    v-model="valvesChecked"
                    :min="1">
                    <el-checkbox v-for="valve in valves" :label="valve" :key="valve">{{valve}}</el-checkbox>
                </el-checkbox-group>
                <el-slider
                    v-model="presValue"
                    show-input>
                </el-slider>
            </div>
           </div>
           <el-input v-if="taskType==='monitor'" placeholder="输入整数" v-model="taskNew.interval[1]" class="input-with-select inputSub">
               <template slot="prepend">单次录制时间：</template>
                <template slot="append">秒</template>
           </el-input>
          
        </div>
        <div style="text-align:right" class="inputSub">
                  <el-button style="width: 90px;" type="primary" @click="saveTask">确认</el-button>
                  <el-button style="width: 90px;" type="primary" @click="closeEdit">取消</el-button>
          </div>
     </el-dialog>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
export default Vue.extend({
    name:'labBox',
    props:{
        tasks:Array,
        taskType:String
    },
    data(){
        return{
           dialogVisible:false,
           valves:['valve1','valve2','valve3','valve4','valve5','valve6','valve7','valve8'],
           valvesChecked:['valve1','valve2'],
           presValue:0,
           taskNew:{
               name:'',
               time:[0,0],
               interval:[0,0]
           },
           myDate:new Date(),
        }
    },
    methods:{
        deleteTask(id){

        },
        editTask(id){
           const self:any = this;
           self.dialogVisible = true;
           self.add = false;
        },
        addTask(){
            const self:any = this;
            self.dialogVisible = true;
            self.add = true;
        },
        teskTask(data){
            const self:any = this;
            if(data.task_name===''||isNaN(self.taskNew.interval[0])||isNaN(self.taskNew.interval[1])||isNaN(self.taskNew.time[0])||isNaN(self.taskNew.time[1])
            ||self.taskNew.time[1]<=self.taskNew.time[0]||self.taskNew.interval[0]===0||self.taskNew.interval[1]===0||self.taskNew.interval[0]>=self.taskNew.time[1]-self.taskNew.time[0]
            ||self.taskNew.interval[1]>=self.taskNew.time[1]-self.taskNew.time[0]||self.presValue==0){
                return false;
            }
            else return true;
            

        },
        saveTask(){
            const self:any = this;
            self.dialogVisible = false;
            const url = self.add?'http://localhost:5000/addTask':'http://localhost:5000/updateTask';
            if(self.taskType==='regant'){
              let val = '';
              self.valvesChecked.forEach(e => {
                  val = val+e[5];
              });
              let data = {
                  type:'regant',
                  task_name:self.taskNew.name,
                  task_date:self.myDate.toLocaleString(),
                  task_interval:self.taskNew.interval[0].toString()+','+self.taskNew.interval[1].toString(),
                  task_time:self.taskNew.time[0].toString()+','+self.taskNew.time[1].toString(),
                  task_valve:val,
                  task_pres:self.presValue,
                  task_username:sessionStorage.username
              }
              if(self.teskTask(data)){
                  $.post(url,data).then(function(data){
                        if(data.code === 0){
                            self.$message.error('未知错误');
                        }
                        else{
                            self.$message({
                                message: '添加成功',
                                type: 'success'
                            });
                            //self.reloadInfo().reverse()
                        }
                    });
               }
               else {
                     self.$message.error('输入错误！');
               }
            }
            else{
                let data = {
                  type:'monitor',
                  task_name:self.taskNew.name,
                  task_date:self.myDate.toLocaleString(),
                  task_interval:self.taskNew.interval[0].toString()+','+self.taskNew.interval[1].toString(),
                  task_time:self.taskNew.time[0].toString()+','+self.taskNew.time[1].toString(),
                  task_username:sessionStorage.username
              }
              if(self.teskTask(data)){
                  $.post(url,data).then(function(data){
                        if(data.code === 0){
                            self.$message.error('未知错误');
                        }
                        else{
                            self.$message({
                                message: '添加成功',
                                type: 'success'
                            });
                            //self.reloadInfo().reverse()
                        }
                    });
              }
              else {
                   self.$message.error('输入错误！');
              }
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
.inputSub{
    margin-top: 10px;
}
.general{
    border: 1px solid #bbbbbb;
    border-radius: 6px;
    padding: 23px 16px 16px 16px;
    position: relative;
    margin-bottom: 20px;
    margin-top: 25px;
    font-size: 16px;
    .title {
        position: absolute;
        top: -12px;
        font-size: 14px;
        background-color: #ffffff;
        padding: 0 8px;
    }
}
</style>
