<template>
<div>
    <epm-2-table v-bind:items ="currentItems" :headers ="headers" v-if='isDataValid'>      
      <template v-slot:name={item}>
        <span :class="{'el-icon-film':item.Type==='video','el-icon-toilet-paper':item.Type==='number'}" class="icon"/>
        <span class="sheet-name">{{item.name}}</span>
      </template>
      <template v-slot:action={item}>
            <button class='actionBtn' v-if="item.Type==='video'" @click="dialogVisible = true">
                <span class="el-icon-video-play"></span>
            </button>
            <button class='actionBtn'>
                <span class="el-icon-download"></span>
            </button>
            <button class='actionBtn' v-if="item.isMe">
                <span class="el-icon-delete"></span>
            </button>
      </template> 
     </epm-2-table>
     <el-dialog
                :visible.sync="dialogVisible"
                width='680px'
                heigth="400px"
                top="15vh"
                :before-close="handleClose">
 
            <video-player  class="vjs-default-skin vjs-big-play-centered"
                          :options="playerOptions"
                          @play="onPlayerPlay($event)"
                          @pause="onPlayerPause($event)"
            >
            </video-player>
 
     </el-dialog>
</div>
</template>
<script lang="ts">
import Vue from 'vue'
import epm2Table from './tools/tableCard.vue'
import { videoPlayer } from 'vue-video-player' // video 插件
// import 'videojs-contrib-hls' // 引入hls
import 'video.js/dist/video-js.css'
import 'vue-video-player/src/custom-theme.css'

export default Vue.extend({
    name: 'dataManager',
    data(){
        return{
            currentItems:[],
            headers:[],
            isDataValid:false,
            dialogVisible: false,
            playerOptions:{
                    height: '360',
                    sources: [{
                        type: "rtmp/mp4",
                        src:'http://localhost:5000',
 
                    }],
                    techOrder: ['flash'],
                    autoplay: false,
                    controls: true,
                },

        }
    },

    components:{
        epm2Table,
        videoPlayer
    },
    methods:{
        onPlayerPlay:function () {
            
        },
        onPlayerPause:function () {
            
        },
    },
    created(){
        const self:any = this;
        self.headers = [
            {text:'名称', value: 'name',sortable: true},
            {text:'日期', value: 'date',sortable: true},
            {text:'', value: 'action',sortable: false},
        ];
        $.get('http://localhost:5000/videoGetAll').then(function(data){
            console.log(data);
            if(data.code=='1'){
                data.videoList.forEach(e => {
                    self.currentItems.push({
                        'name': e[1],
                        'date': e[3],
                        'Type':'video',
                        'action':'',
                        'isMe':e[2]===sessionStorage.username
                    })
                });
                console.log(self.currentItems);
                self.isDataValid = true;
            }
            else{
                self.$message.error('未知错误');
            }
        });
    }
})
</script>
<style lang='scss' scoped>
.actionBtn{
    border: none;
    outline: none;
    :hover{
        color: #409EFF;
    }
    :focus{
        outline: none;
    }
}

</style>