<template>
<div class = "row">
   <div class = "col-sm-9">
       <el-card style="margin:0px 10px;color:#FFFFFF;  background: rgba(255, 255, 255, 0); position:absolute; top:5px">
           <div slot="header" style="margin-left:6px;">
               <span><i style="padding-right:6px" class="el-icon-odometer"></i>环境监测</span>
           </div>
           <div class="envCard">
               <span><i  class="el-icon-data-line"></i>实时温度：{{Temp}}</span>
               <span><i  class="el-icon-magic-stick"></i>实时CO2：{{CO2}}</span>
           </div>
       </el-card>
       <div style="margin:0px 10px;color:#FFFFFF;  background: rgba(255, 255, 255, 0); position:absolute; top:5px; right:20px">
            <el-button @click="isSwitch = true" type="primary" style="margin-right: 16px;">
            阀门控制
            </el-button>
            <el-popover
                placement="bottom"
                title=""
                max-width="300"
                trigger="click">
            <div style="width:100%">
                <div style="display:inline-block;vertical-align:top">
                    <div style="margin-right: 50px" v-for="(location,index) in locations" :key='index'>
                        <el-tooltip :content="`转盘角度:${location.angle},直线位置:${location.line}`" placement="bottom">
                            <el-radio
                                style="margin:5px"
                                @change="locationChange"
                                v-model="optLocation" :label="index" border size="medium">
                                {{location.name}}
                            </el-radio>
                        </el-tooltip>
                        <i @click="deleteLocation(index)" class="el-icon-delete" style="cursor:pointer;margin:0 10px 0 10px"></i>
                        <el-button @click="editLocation(index)" type="primary" icon="el-icon-edit" circle></el-button>
                    </div>
                    <el-button @click="addLocation()" type="primary" icon="el-icon-plus" circle></el-button>
                        
                </div>
            </div>
                <el-button slot="reference" type="primary">更新位置</el-button>
            </el-popover>
       </div>
       <img src = '/video' width="100%">
   </div>
   <div class = "col-sm-3">
        <el-card>
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
         <el-card>
            <div slot="header" style="margin-left:6px">
                <span><i style="padding-right:6px" class="el-icon-video-camera"></i>对焦控制</span>
            </div>
            <div class="recordCard">
                <div style="margin:0 0 5px 5px">
                    <el-button type="info" icon="el-icon-bangzhu" @click="focus('auto','up')">对焦</el-button>
                </div>
                <div class="general" style="margin:14px 0 0 0; height:120px; width:100px;">
                    <span class="title">手动控制</span>
                    <div style="margin:0 5px"><el-button type="info" icon="el-icon-top" @click="focus('hand','up')"></el-button></div>
                    <div style="margin:10px 5px 0 5px"><el-button type="info" icon="el-icon-bottom" @click="focus('hand','down')"></el-button></div>
                </div>
            </div>
         </el-card>
   </div>
   <el-drawer
        title="位置编辑"
        :visible.sync ="locationVisible"
        direction="ltr"
        :format="format"
        size="25%"
        :modal="false">
        <el-input placeholder="" v-model="myLocationName">
            <template slot="prepend">自定义位置名称：</template>
        </el-input>
        <div class="card" style="text-align:center">
            <div style="margin-bottom:10px">转盘位置设定</div>
            <div>
             <el-progress :percentage="percentageAngle" :format="format" type="circle" :stroke-width="20"></el-progress>
            </div>
            <div style="margin:10px;">
                <el-select v-model="stepAngle" placeholder="请选择" style="width:100px">
                    <el-option
                        v-for="item in optionsAngle"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
                <el-button-group style="margin:10px;">
                    <el-button icon="el-icon-minus" @click="decreaseAngle"></el-button>
                    <el-button icon="el-icon-plus" @click="increaseAngle"></el-button>
                </el-button-group>
            </div>
        </div>
        <div class="card" style="text-align:center">
            <div style="margin-bottom:10px">直线位置设定</div>
            <el-progress  :text-inside="true"  :format="formatLine" :stroke-width="20" :percentage="percentageLine"></el-progress>
            <div style="margin:10px;">
                <el-select v-model="stepLine" placeholder="请选择" style="width:100px">
                    <el-option
                        v-for="item in optionsLine"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
                <el-button-group style="margin:10px;">
                    <el-button icon="el-icon-minus" @click="decreaseLine"></el-button>
                    <el-button icon="el-icon-plus" @click="increaseLine"></el-button>
                </el-button-group>
            </div>
         </div>
        <div style="float:right;margin:30px 10px 30px 0;">
            <el-button @click="locationVisible = false">取 消</el-button>
            <el-button type="primary" @click="locationSave">确 定</el-button>
        </div>
    </el-drawer>
    <el-drawer
        title="阀门控制"
        style="overflow:auto"
        :visible.sync="isSwitch"
        :modal='false'
        direction="ltr"
        size="25%"
    >
        <div class="card">
            <div style="text-align:center;margin-bottom:10px">阀门开关</div>
            <el-checkbox-group 
                v-model="valvesChecked"
                style="margin-left:10%"
                :min="0">
                <el-checkbox v-for="valve in valves" :label="valve" :key="valve">{{valve}}</el-checkbox>
            </el-checkbox-group>
        </div>
        <div class="card">
            <div style="text-align:center">压力设定</div>
            <div style="text-align:center;margin:0 20px 0 20px">
            <el-slider
                v-model="presValue"
                height="100px">
            </el-slider>
            <el-input-number v-model="presValue"  :min="0" :max="100"></el-input-number>
            </div>
        </div>
        <div style="float:right;margin-top:30px;margin-right:10px">
            <el-button @click="isSwitch = false">取 消</el-button>
            <el-button type="primary" @click="switchSave">确 定</el-button>
        </div>
    </el-drawer>
</div>
</template>
<script lang="ts">
declare let $:any;
import Vue from 'vue'
export default Vue.extend({
    name:'monitor',
    data(){
        return {
            presValue:0,
            isSwitch:false,
            myLocationName:'',
            valves:['阀门1','阀门2','阀门3','阀门4','阀门5','阀门6','阀门7','阀门8'],
            valvesChecked:[],
            recordStatus: 0,
            videoName:'',
            Temp:37,
            CO2:400,
            myDate: new Date(),
            optLocation:'1',
            locations:[
                {name:'位置1: 芯片1',id:'1',angle:10,line:40},
                {name:'位置2: 芯片2',id:'2',angle:40,line:50}],
            locationVisible:false,
            percentageAngle:50,
            optionsAngle:[
                {label:'1°',value:1/3.6},
                {label:'3.6°',value:1},
                {label:'36°',value:10},
                {label:'75°',value:25},
                {label:'180°',value:50},
            ],
            optionsLine:[
                {label:'1cm',value:10},
                {label:'0.1cm',value:1},
                {label:'0.01cm',value:0.1},
                {label:'2cm',value:20},
            ],
            stepAngle:10,
            percentageLine:50,
            stepLine:10,
            editID:-1,
            getSensor:null

        }
    },
    methods:{
        switchSave(){
            const self:any = this;
            console.log(self.valvesChecked[0][2],self.presValue)
            const presData = {
                valveChecked:self.valvesChecked.map(e=>e[2]),
                presValue:self.presValue
            }
            $.post('/valveControl',presData).then((data)=>{
                if(data.code===1){
                    self.$message({
                        message: '阀门调整成功',
                        type: 'success'
                    });
                }
                else{
                    self.$message.error('未知错误, 请重试');
                }

            })

        },
        focus(way,dir){
            const self:any = this;
            // if(way==='auto'&&!self.autoFocus) return;
            // if(way==='hand'&&self.autoFocus){
            //     self.$notify({
            //             title: '警告',
            //             message: '请先关闭自动对焦!',
            //             type: 'warning'
            //     });
            // return;}
            $.post('/focus',{way:way,direction:dir}).then(data=>{
            })
        },
        locationChange(index){
            const self:any = this;
            let location = self.locations[index];
            $.post('/changeLocation',{angle:location.angle,
            line:location.line}).then(data=>{
                if(data.code===1){
                        self.$message({
                            message: '位置改变成功',
                            type: 'success'
                        });
                        //if(self.autoFocus) self.foucs('auto','up')
                }
                else{
                    self.$message.error('未知错误, 请重试');
                }
            });


        },
        addLocation(){
            const self:any = this;
            self.editLocation(-1)
        },
        editLocation(index){
            const self:any = this;
            self.editID = index;
            if(index!==-1){
                self.percentageLine = self.locations[index].line;
                self.percentageAngle = self.locations[index].angle;
                self.myLocationName = self.locations[index].name.split(':')[1];
            }
            else{
                self.myLocationName = '';
            }
            self.locationVisible = true;

        },
        getLocations(){
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
                    self.$message.error('未知错误, 请重试');
                }
            });

        },
        deleteLocation(index){
            const self:any = this;
            let location = self.locations.splice(index,1)[0];
            $.post('/deleteLocation',{username:sessionStorage.username,
            id:location.id}).then(data=>{
                if(data.code===1){
                        self.$message({
                            message: '保存成功',
                            type: 'success'
                        });
                        self.$emit('refreshLocations')
                }
                else{
                    self.$message.error('未知错误, 请重试');
                }
            });

        },
        locationSave(){
            const self:any = this;
            if(self.editID===-1){
                let id = self.locations.length>0?Number(self.locations[self.locations.length-1].id)+1:1;
                let newLocation = {
                    username:sessionStorage.username,
                    name:'位置'+id+': '+self.myLocationName,
                    angle:self.percentageAngle,
                    line:self.percentageLine
                }
                self.locations.push(newLocation);
                $.post('/addLocation',newLocation).then(data=>{
                        if(data.code===1){
                                self.$message({
                                    message: '保存成功',
                                    type: 'success'
                                });
                                self.$emit('refreshLocations');
                                self.getLocations();
                        }
                        else{
                            self.$message.error('未知错误, 请重试');
                        }
                });        
            }
            else{
                self.locations[self.editID].angle = self.percentageAngle;
                self.locations[self.editID].line = self.percentageLine;
                self.locations.push({});
                self.locations.pop();
                let id = self.locations[self.editID].id
                $.post('/updateLocation',{username:sessionStorage.username,
                id:id,angle:self.percentageAngle,line:self.percentageLine}).then(data=>{
                        if(data.code===1){
                                self.$message({
                                    message: '修改成功',
                                    type: 'success'
                                });
                        }
                        else{
                            self.$message.error('未知错误, 请重试');
                        }
                });   
            };
            self.locationVisible = false;
        },
        increaseAngle() {
            const self:any = this;
            if (self.percentageAngle > 100) return;
            self.percentageAngle += self.stepAngle;
            if (self.percentageAngle > 100) {
                self.percentageAngle = 100;
            }
            $.post('/stage',{type:'angle',angle:Math.floor(360*self.percentageAngle)/100}).then(data=>{

            })
        },
        increaseLine() {
            const self:any = this
	    if (self.percentageLine > 100) return;
            self.percentageLine += self.stepLine;
            if (self.percentageLine > 100) {
                self.percentageLine = 100;
            };
            $.post('/stage',{type:'line',line:Math.floor(200*self.percentageLine)/100}).then(data=>{

            })
        },
        format(percentage) {
            return `${Math.floor(360*percentage)/100}°`;
        },
        formatLine(percentage) {
            return `${Math.floor(percentage*200)/100} mm`;
        },
        decreaseAngle() {
            const self:any = this;
	    if (self.percentageAngle < 0) return;
            self.percentageAngle -= self.stepAngle;
            if (self.percentageAngle < 0) {
                self.percentageAngle = 0;
            }
            $.post('/stage',{type:'angle',angle:Math.floor(360*self.percentageAngle)/100}).then(data=>{

            })
        },
        decreaseLine() {
            const self:any = this;
            self.percentageLine -= self.stepLine;
	    if (self.percentageAngle < 0) return;
            if (self.percentageLine < 0) {
                self.percentageLine = 0;
            }
            $.post('/stage',{type:'line',line:Math.floor(200*self.percentageLine)/100}).then(data=>{

            })
        },
        recordStart(){
            const self:any = this;
            self.$prompt('请输入视频文件名', '视频录制', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputPattern: /^[\s\S]{1,200}$/,
                inputErrorMessage: '视频文件名长度不能超过200个'
                }).then(({ value })=>{
                    $.post('/videoRecordStart',{videoName: value}).then(data=>{
                        if(data.code===1){
                            self.videoName = value;
                            self.recordStatus = 1;
                            self.$message({
                                message: '开始成功',
                                type: 'success'
                            });
                        }
                        else{
                            self.$message.error('未知错误, 请重试');
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
            $.post('/videoRecordStop').then(data=>{
                if(data.code===1){
                        self.recordStatus = 2;
                        self.$message({
                            message: '结束成功',
                            type: 'success'
                        });
                }
                else{
                    self.$message.error('未知错误, 请重试');
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
            $.post('/videoRecordSave',{userName:sessionStorage.username,
            videoName:self.videoName,videoDate:self.myDate.toLocaleString()
            }).then(data=>{
                if(data.code===1){
                        self.recordStatus = 0;
                        self.$message({
                            message: '保存成功',
                            type: 'success'
                        });
                        self.$emit('refreshData')
                }
                else{
                    self.$message.error('未知错误, 请重试');
                }
            });
        },
        getSensors(){
            const self:any = this;
            $.get('/sensor').then(data=>{
                if(data.code===1){
                        self.Temp = data.data[2].toFixed(2)+' C';
                        self.CO2 = (data.data[0]/10000).toFixed(2)+' %';
                }
                
            })

        }
    },
    created(){
        const self:any = this;
        self.getLocations();
	self.getSensors();	
        self.getSensor = setInterval(()=>{self.getSensors()},30000)
    },
    beforeDestroy() {
      const self:any = this;
      clearInterval(self.getSensor);
    }
    
})
</script>
<style>
.el-drawer.ltr{
    overflow: auto;
}

</style>
<style lang="scss" scoped>
.card{
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    margin: 10px;
    padding: 15px;
}
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
.envCard{
    cursor: pointer;
    font-size: 12px;
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
    height: 140px;
    width:200px;
    cursor: pointer;
    color: #999;
    position: relative;
    bottom: 30px;
    left:20px;
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
    margin-bottom: 6px;
    margin-top: 6px;
    font-size: 12px;
    .title {
        position: absolute;
        top: -12px;
        font-size: 14px;
        background-color: #ffffff;
        padding: 0 5px;
    }
}
</style>