<template>
<div class = "row">
   <div class = "col-sm-9">   
       <img src = 'http://localhost:5000/video' width="640px" height="480px">
       <el-card style="width: 640px;height:230px">
           <div slot="header" style="margin-left:6px; width: 640px">
               <span><i style="padding-right:6px" class="el-icon-s-tools"></i>位移台控制</span>
           </div>
           <div class="stageCard">
               <div class="movetop"><i  class="el-icon-caret-top"></i></div>
               <span>
                    <div style="display:inline" class="moveleft"><i  class="el-icon-caret-left"></i></div>
                    <div style="display:inline" class="fBtn">
                        <el-button type="info" style="width:30px;">
                            <span style="position:relative; left:-4px; boarder:none">F</span>
                            </el-button>
                        </div>
                    <div style="display:inline" class="moveright"><i  class="el-icon-caret-right"></i></div>
               </span>
               <div class="movebottom"><i  class="el-icon-caret-bottom"></i></div>
           </div>
           <div class="general" style="float:right;position:relative; bottom:130px;right:250px; height:140px; width:100px;">
                <span class="title">Z轴移动</span>
                <div style="margin:10px"><el-button type="info" icon="el-icon-top"></el-button></div>
                <div style="margin:10px"><el-button type="info" icon="el-icon-bottom"></el-button></div>
            </div>
            <div style="float:left; position:relative; bottom:140px; left:10px; height:140px; width:200px; font-size:14px">
                <div style="margin-bottom:10px">
                    运动步长：
                    <el-select style="margin-top:10px" v-model="stepValue" placeholder="请选择运动步长">
                        <el-option
                            v-for="item in stepOptions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div style="margin-top:10px">
                    运动速度：
                    <el-select style="margin-top:10px" v-model="speedValue" placeholder="请选择运动速度">
                        <el-option
                            v-for="item in speedOptions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </div>
            </div>
        
       </el-card>
   </div>
   <div class = "col-sm-3">
       <el-card style="margin:0px 10px">
           <div slot="header" style="margin-left:6px">
               <span><i style="padding-right:6px" class="el-icon-video-camera"></i>视频录制</span>
           </div>
           <div class="recordCard">
               <span @click="recordStart()" v-if="recordStatus===0"><i class="el-icon-video-play"></i>开始录制</span>
               <span @click="recordStop()" v-if="recordStatus===1"><i  class="el-icon-video-pause"></i>正在录制</span>
               <span v-if="recordStatus===2"><i  class="el-icon-success"></i>完成录制</span>
               <span @click="recordRe()"><i  class="el-icon-refresh-left"></i>重新录制</span>
               <span @click="recordSave()"><i  class="el-icon-s-release"></i>保存录制</span>
           </div>
       </el-card>
   </div>
</div>
</template>
<script lang="ts">
declare let $:any;
import Vue from 'vue'
export default Vue.extend({
    name:'monitor',
    data(){
        return {
            recordStatus: 0,
            videoName:'',
            myDate: new Date(),
            stepOptions:[
                {
                    label:'1 mm',
                    value:0
                },
                {
                    label:'2 mm',
                    value:1
                },
                {
                    label:'3 mm',
                    value:2
                },
                {
                    label:'4 mm',
                    value:3
                }
            ],
            stepValue:1,
            speedOptions:[
                {
                    label:'1 mm/s',
                    value:0
                },
                {
                    label:'2 mm/s',
                    value:1
                },
                {
                    label:'3 mm/s',
                    value:2
                },
                {
                    label:'4 mm/s',
                    value:3
                }
            ],
            speedValue:1

        }

    },
    methods:{
       recordStart(){
            const self:any = this;
            self.$prompt('请输入视频文件名', '视频录制', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputPattern: /^[\s\S]{1,200}$/,
                inputErrorMessage: '视频文件名长度不能超过200个'
                }).then(({ value })=>{
                   $.post('http://localhost:5000/videoRecordStart',{videoName: value}).then(data=>{
                       if(data.code===1){
                            self.videoName = value;
                            self.recordStatus = 1;
                            self.$message({
                                message: '开始成功',
                                type: 'success'
                            });
                       }
                       else{
                           self.$message.error('未知错误');
                       }
                   })
                }).catch(() => {
                self.$message({
                    type: 'info',
                    message: '取消输入'
                }); });
       },
       recordStop(){
           const self:any = this;
           $.post('http://localhost:5000/videoRecordStop').then(data=>{
                if(data.code===1){
                        self.recordStatus = 2;
                        self.$message({
                            message: '结束成功',
                            type: 'success'
                        });
                }
                else{
                    self.$message.error('未知错误');
                }
            });
       },
       recordRe(){
           const self:any = this;
            if(self.recordStatus!==2){
                self.$notify({
                    title: '警告',
                    message: '尚未录制视频，请录制完视频后操作',
                    type: 'warning'
                    });
                return;}
           self.recordStatus = 0;
       },
       recordSave(){
            const self:any = this;
            if(self.recordStatus!==2){
                self.$notify({
                    title: '警告',
                    message: '请录制完视频后操作',
                    type: 'warning'
                    });
                return;}
            $.post('http://localhost:5000/videoRecordSave',{userName:sessionStorage.username,
            videoName:self.videoName,videoDate:self.myDate.toLocaleString()
            }).then(data=>{
                if(data.code===1){
                        self.recordStatus = 0;
                        self.$message({
                            message: '保存成功',
                            type: 'success'
                        });
                }
                else{
                    self.$message.error('未知错误');
                }
            });
       }
    }
    
})
</script>
<style lang="scss" scoped>
.recordCard{
    cursor: pointer;
    font-size: 14px;
    i{
        padding-bottom: 10px;
        margin: 6px;
        padding-right:4px

    }
    span{
        display: block;
    }
    span:hover{
         color: #409EFF;
    }
    
}
.stageCard{
    position: relative;
    left:400px;
    bottom: 36px;
    height: 140px;
    width:200px;
    cursor: pointer;
    color: #999;
   .movetop{
       font-size: 50px;
       position: relative;
       left:50px;
       top:28px;
       :hover{
           color: #409EFF;
       }
   }
    .moveleft{
       font-size: 50px;
       position: relative;
       left:0px;
       :hover{
           color: #409EFF;
       }
   }
   .fBtn{
       position: relative;
       left:0px;
       bottom: 13px;
   }
    .moveright{
       font-size: 50px;
       position: relative;
       left:0px;
       :hover{
           color: #409EFF;
       }
   }
    .movebottom{
       font-size: 50px;
       position: relative;
       left:51px;
       bottom:30px;
       :hover{
           color: #409EFF;
       }
   }
}
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