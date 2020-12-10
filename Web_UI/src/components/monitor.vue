<template>
<div class = "row">
   <div class = "col-sm-9">   
       <img src = 'http://localhost:5000/video' width="640px" height="360px">
       <el-card style="width: 640px">
           <div slot="header" style="margin-left:6px; width: 640px">
               <span><i style="padding-right:6px" class="el-icon-s-tools"></i>位移台控制</span>
           </div>
           <div class="stageCard">
               <div class="move"><i  class="el-icon-caret-top"></i></div>
               <span>
                    <div style="display:inline" class="move"><i  class="el-icon-caret-left"></i></div>
                    <div style="display:inline">
                        <el-button type="info" style="width:30px; heigth:30px">
                            <span style="position:relative; left:-4px; boarder:none">F</span>
                            </el-button>
                        </div>
                    <div style="display:inline" class="move"><i  class="el-icon-caret-right"></i></div>
               </span>
               <div class="move"><i  class="el-icon-caret-bottom"></i></div>
           </div>
       </el-card>
   </div>
   <div class = "col-sm-3">
       <el-card style="margin-top:0px">
           <div slot="header" style="margin-left:6px">
               <span><i style="padding-right:6px" class="el-icon-video-camera"></i>视频录制</span>
           </div>
           <div class="recordCard">
                <span  v-if="recordStatus===0"><i class="el-icon-video-play"></i>开始录制</span>
               <span v-if="recordStatus===1"><i  class="el-icon-video-pause"></i>正在录制</span>
               <span v-if="recordStatus===2"><i  class="el-icon-video-success"></i>完成录制</span>
               <span><i  class="el-icon-refresh-left"></i>重新录制</span>
               <span><i  class="el-icon-s-release"></i>保存录制</span>
           </div>
       </el-card>
   </div>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    name:'monitor',
    data(){
        return {
            recordStatus: 0
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
   .move{
       font-size: 50px;
   }
}
</style>