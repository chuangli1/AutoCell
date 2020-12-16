<template>
<div>
    <epm-2-table v-bind:items ="currentItems" :headers ="headers" v-if='isDataValid'>      
      <template v-slot:name={item}>
        <span :class="{'el-icon-film':item.Type==='video','el-icon-toilet-paper':item.Type==='number'}" class="icon"/>
        <span class="sheet-name">{{item.name}}</span>
      </template>
      <template v-slot:action={item}>
            <button class='actionBtn' v-if="item.Type==='video'" @click="videoPlay(item.name)">
                <span class="el-icon-video-play"></span>
            </button>
            <button class='actionBtn' @click="downloadVideo(item.name)"> 
                <span class="el-icon-download"></span>
            </button>
            <button class='actionBtn' v-if="item.isMe">
                <span class="el-icon-delete"></span>
            </button>
      </template> 
     </epm-2-table>
     <el-dialog
                :visible.sync="dialogVisible"
                @close='videoPlayStop'
                width='680px'
                heigth="480px"
                top="15vh"
                >
                <img :src="videoSrc" width="640px" height="480px">
     </el-dialog>
</div>
</template>
<script lang="ts">
declare let $:any;
import Vue from 'vue'
import epm2Table from './tools/tableCard.vue'


export default Vue.extend({
    name: 'dataManager',
    data(){
        return{
            currentItems:[],
            headers:[],
            isDataValid:false,
            dialogVisible: false,
            videoSrc:'0'
        }
    },

    components:{
        epm2Table
    },
    methods:{
        videoPlay(video_name){
           const self:any = this;
           self.dialogVisible = true;
           self.videoSrc = 'http://localhost:5000/videoPlay?video_name='+video_name+'.avi';

        },
        videoPlayStop(){
           const self:any = this;
           self.dialogVisible = false;
           self.videoSrc = 0;

        },
        downloadVideo (video_name) {
            const self:any = this;
             let url = 'http://localhost:5000/videoDownload?video_name='+video_name+'.avi'
             window.open(url);
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