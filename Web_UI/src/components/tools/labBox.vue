<template>
  <div>
    <div class="addIcon"><span @click="addTask"><i class="el-icon-plus"></i></span></div>
    <el-card v-for="(task,index) in tasks" :key='index' class="box-card labBox">
        <div slot="header" class="clearfix">
            <span style="display:inline-block;margin-top:17px"><el-switch v-model="task.isActive" :active-text=task.name :disabled=!task.access @change='changeStatus($event,task)'></el-switch></span>
            <span v-if='task.isActive' style="display:inline-block;margin-top:17px">上次开启时间：{{task.activeDate}}</span>
            <span style="float: right; padding: 3px 0">
                <i v-if='task.access' class="el-icon-delete icon" @click="deleteTask(task.id)"></i>
                <el-button type="primary" icon="el-icon-edit" circle v-if='task.access' class="icon" @click="editTask(task)"></el-button>
            </span>
        </div>
        <div style="font-size:14px">
            <div>
                <i class="el-icon-warning-outline">任务开始时间：{{task.time[0]}}分钟后</i>
                <i class="el-icon-warning-outline">任务结束时间：{{task.time[1]}}分钟后</i>
                <i class="el-icon-warning-outline">任务执行间隔：{{task.interval[0]}}分钟</i>
                <i class="el-icon-warning-outline">单次任务时间：{{task.interval[1]}}秒</i>
            </div>
            <div v-if="taskType==='regant'">
                 <i class="el-icon-warning-outline">阀门开启：{{task.valves}}</i>
                 <i class="el-icon-warning-outline">压力大小：{{task.pres}}</i>
            </div>
            <div v-else>
                 <i class="el-icon-warning-outline">成像位置：{{task.location}}</i>
            </div>
            <div style="float: right; padding: 3px 0;font-size:14px">{{task.username+'于'+task.date+'创建'}}</div>
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
                <template slot="append">分钟后</template>>
           </el-input>
           <el-input placeholder="输入大于开始时间的整数" v-model="taskNew.time[1]" class="input-with-select inputSub">
               <template slot="prepend">结束时间：</template>
                <template slot="append">分钟后</template>
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
           <div v-if="taskType==='monitor'">
            <el-input placeholder="输入整数" v-model="taskNew.interval[1]" class="input-with-select inputSub">
                <template slot="prepend">单次录制时间：</template>
                    <template slot="append">秒</template>
            </el-input>
            <div class="general inputSub">
                    <span class="title">成像位置设定</span>
                    <el-checkbox-group 
                        v-model="locationChecked"
                        :min="1">
                        <el-checkbox v-for="(location,index) in locations" :label="location.id" :key="index**2+1">{{location.name}}</el-checkbox>
                    </el-checkbox-group>
            </div>
           </div>
          
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
        activeList:Array,
        taskType:String,
        locations:Array
    },
    data(){
        return{
           dialogVisible:false,
           valves:['valve1','valve2','valve3','valve4','valve5','valve6','valve7','valve8'],
           valvesChecked:[],
           locationChecked:[],
           presValue:0,
           taskNew:{
               name:'',
               time:[0,0],
               interval:[0,0]
           },
           myDate:new Date(),
           editId:-1,
           tasks:[]
        }
    },
    methods:{
        deleteTask(id){
            const self:any = this;
            const dataD = {
                'type':self.taskType,
                'task_id':id
            }
             $.post('/deleteTask',dataD).then(function(data){
                if(data.code === 0){
                    self.$message.error('未知错误');
                }
                else{
                    self.$message({
                        message: '删除成功',
                        type: 'success'
                    });
                    self.tasks.splice(self.tasks.findIndex(e => e.id === id), 1) 
                }
            });
            if(self.activeList.findIndex(d=>d[0]===id)!==-1){
            $.post('/deleteTaskList',{task_id:id, task_type:self.taskType}).then(data=>{
                if(data.code === 0){
                        self.$message.error('未知错误');
                    }
                else{
                        self.$message({
                            message: '任务关闭成功',
                            type: 'success'
                        });
                        self.activeList.splice(self.activeList.findIndex(d=>d[0]===id),1);
                    }
                        
                });
            }
        },
        editTask(task){
           const self:any = this;
           if(task.isActive){
               self.$notify({
                    title: '警告',
                    message: 'Please close this Task!!!!',
                    type: 'warning'
                    });
                return;
           }
           self.taskNew = {
               name:task.name,
               time:task.time.slice(),
               interval:task.interval.slice(),
           }
           if(self.taskType==='regant'){
               self.presValue = task.pres;
               self.valvesChecked = []
               for(let i=0; i<task.valves.length; i++){
                   self.valvesChecked.push(self.valves[parseInt(task.valves[i])-1]);
               }
           }
           else{
               console.log(task)
               self.locationChecked = task.location.slice();
           }
           self.editId = task.id;
           self.dialogVisible = true;

        },
        reload(){
            const self:any = this;
            let tasks:any = [];
            if(self.taskType==='regant'){
                $.get('/loadTasks?type='+self.taskType).then(function(data){
                data.tasks.forEach(e => {
                    tasks.push({
                        id:e[0],
                        name:e[1],
                        username:e[2],
                        date:e[3],
                        valves:e[4].split(''),
                        time:e[5].split(','),
                        pres:e[6],
                        interval:e[7].split(','),
                        access:sessionStorage.username===e[2]||sessionStorage.isManager==='true',
                        isActive:false,
                        activeDate:-1
                    })
                    });
                    for(let e of tasks){
                        let t = self.activeList.findIndex(d=>d[0]===e.id)
                        if(t!==-1) {e.isActive = true;e.activeDate=e[1]}
                    }
                    self.tasks = tasks;
                });
            }
            else{
                 $.get('/loadTasks?type='+self.taskType).then(function(data){
                data.tasks.forEach(e => {
                    tasks.push({
                        id:e[0],
                        name:e[1],
                        username:e[2],
                        date:e[3],
                        time:e[4].split(','),
                        interval:e[5].split(','),
                        location:e[6]===""?[]:e[6].split(',').map(n=>Number(n)),
                        access:sessionStorage.username===e[2]||sessionStorage.isManager==='true',
                        isActive:false,
                        activeDate:-1
                    })
                    });
                    for(let e of tasks){
                        let t = self.activeList.findIndex(d=>d[0]===e.id)
                        if(t!==-1) {e.isActive = true;e.activeDate=e[1]}
                    }
                    self.tasks = tasks;
                });
            }
   
        },
        addTask(){
            const self:any = this;
            self.taskNew = {
               name:'',
               time:[0,0],
               interval:[0,0],
           }
           self.valvesChecked = [];
           self.presValue = 0;
           self.editId = -1;
           self.dialogVisible = true;

        },
        testTask(data){
            const self:any = this;
            if(data.task_name===''||isNaN(self.taskNew.interval[0])||isNaN(self.taskNew.interval[1])||isNaN(self.taskNew.time[0])||isNaN(self.taskNew.time[1])
            ||parseInt(self.taskNew.time[1])<=parseInt(self.taskNew.time[0])||parseInt(self.taskNew.interval[0])===0||parseInt(self.taskNew.interval[1])===0||
            parseInt(self.taskNew.interval[0])>=parseInt(self.taskNew.time[1])-parseInt(self.taskNew.time[0])){
                return false;
            }
            if(self.taskType==='regant'&&(!self.valvesChecked||self.presValue==0)) return false;
            else return true;
        },
        changeStatus(status,task){
            const self:any = this;
            if(status){
                 $.post('/addTaskList',{type:self.taskType,task_id:task.id,list_date:self.myDate.toLocaleString()}).then(data=>{
                      if(data.code === 0){
                            self.$message.error('未知错误');
                            task.isActive = !status;
                        }
                        else{
                            self.$message({
                                message: '任务开启成功',
                                type: 'success'
                            });
                            task.activeDate = self.myDate.toLocaleString();
                            self.activeList.push([task.id,self.myDate.toLocaleString()]);
                        }
                });
            }
            else{
                $.post('/deleteTaskList',{task_id:task.id, task_type:self.taskType}).then(data=>{
                      if(data.code === 0){
                            self.$message.error('未知错误');
                            task.isActive = !status;
                        }
                        else{
                            self.$message({
                                message: '任务关闭成功',
                                type: 'success'
                            });
                            task.activeDate = -1;
                            self.activeList.splice(self.activeList.findIndex(d=>d===task.id),1);
                        }
                });
            }
        },
        saveTask(){
            const self:any = this;
            self.dialogVisible = false;
            const url = (self.editId===-1)?'/addTask':'/updateTask';
            if(self.taskType==='regant'){
              let val = '';
              self.valvesChecked.forEach(e => {
                  val = val+e[5];
              });
              let data:any = {
                  type:'regant',
                  task_name:self.taskNew.name,
                  task_date:self.myDate.toLocaleString(),
                  task_interval:self.taskNew.interval[0].toString()+','+self.taskNew.interval[1].toString(),
                  task_time:self.taskNew.time[0].toString()+','+self.taskNew.time[1].toString(),
                  task_valve:val,
                  task_pres:self.presValue,
                  task_username:sessionStorage.username
              }
              if(self.editId!==-1) data.task_id = self.editId;
              if(self.testTask(data)){
                  $.post(url,data).then(function(data){
                        if(data.code === 0){
                            self.$message.error('未知错误');
                        }
                        else{
                            self.$message({
                                message: (self.editId===-1)?'添加成功':'修改成功',
                                type: 'success'
                            });
                            self.reload()
                        }
                    });
               }
               else {
                     self.$message.error('输入错误！');
               }
            }
            else{
                let data:any = {
                  type:'monitor',
                  task_name:self.taskNew.name,
                  task_date:self.myDate.toLocaleString(),
                  task_interval:self.taskNew.interval[0].toString()+','+self.taskNew.interval[1].toString(),
                  task_time:self.taskNew.time[0].toString()+','+self.taskNew.time[1].toString(),
                  task_username:sessionStorage.username,
                  task_location:self.locationChecked.join(',')
              }
              if(self.editId!==-1) data.task_id = self.editId;
              if(self.testTask(data)){
                  $.post(url,data).then(function(data){
                        if(data.code === 0){
                            self.$message.error('未知错误');
                        }
                        else{
                            self.$message({
                                message: (self.editId===-1)?'添加成功':'修改成功',
                                type: 'success'
                            });
                            self.reload()
                           
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
        const self:any = this;
        let tasks:any = [];
        if(self.taskType==='regant'){
            $.get('/loadTasks?type='+self.taskType).then(function(data){
            data.tasks.forEach(e => {
                tasks.push({
                    id:e[0],
                    name:e[1],
                    username:e[2],
                    date:e[3],
                    valves:e[4].split(''),
                    time:e[5].split(','),
                    pres:e[6],
                    interval:e[7].split(','),
                    access:sessionStorage.username===e[2]||sessionStorage.isManager==='true',
                    isActive:false,
                    activeDate:-1
                })
                });
                for(let e of tasks){
                    let t = self.activeList.findIndex(d=>d[0]===e.id)
                    if(t!==-1) {e.isActive = true;e.activeDate=self.activeList[t][1]}
                }
                self.tasks = tasks;
            });
        }
        else{
            $.get('/loadTasks?type='+self.taskType).then(function(data){
            data.tasks.forEach(e => {
                tasks.push({
                    id:e[0],
                    name:e[1],
                    username:e[2],
                    date:e[3],
                    time:e[4].split(','),
                    interval:e[5].split(','),
                    location:e[6]===""?[]:e[6].split(',').map(n=>Number(n)),
                    access:sessionStorage.username===e[2]||sessionStorage.isManager==='true',
                    isActive:false,
                    activeDate:-1
                })
                });
                for(let e of tasks){
                    let t = self.activeList.findIndex(d=>d[0]===e.id)
                    if(t!==-1) {e.isActive = true;e.activeDate=self.activeList[t][1]}
                }
                self.tasks = tasks;
            });
        }
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
    :hover{
       color: #409EFF;
    }

}
.labBox{
    padding:10px 10px 10px;
    :hover  .icon{
       color: #409EFF;
       margin-right: 10px;
       cursor:pointer;
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
