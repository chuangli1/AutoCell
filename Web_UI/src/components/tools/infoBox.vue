<template>
  <div>
    <div class="addIcon"><span @click="addInfo"><i class="el-icon-plus"></i></span></div>
    
    <el-card v-for="(info,index) in infos" :key='index' class="box-card infoBox">
        <div slot="header" class="clearfix">
            <span>{{info[1]}}</span>
            <span style="float: right; padding: 3px 0">
                <i v-if='info[1]===userName||isManager' class="el-icon-delete deleteIcon" @click="deleteInfo(info[0])"></i>
            </span>
        </div>
        <div>
            <div>
            <i class="el-icon-warning-outline"></i>
            <span style="font-size:14px">{{info[2]}}</span>
            </div>
            <div style="float: right; padding: 3px 0;font-size:14px">{{info[3].split(' ')[0]}}</div>
        </div>
        </el-card>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
declare let $:any;
export default Vue.extend({
    name:'infoBox',
    data(){
        return{
           infos:[],
           myDate: new Date(),
           userName:'',
           isManager:false
        }
    },
    methods:{
        addInfo(){
            const self:any = this;
            self.$prompt('请输入留言', '留言', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                inputPattern: /^[\s\S]{1,200}$/,
                inputErrorMessage: '留言字数不能超过200个'
                }).then(({ value }) => {
                    const infoData = {
                    'info_user':self.userName,
                    'info_content':value,
                    'info_date': self.myDate.toLocaleString()
                    };
                    $.post('http://localhost:5000/addInfo',infoData).then(function(data){
                        if(data.code === 0){
                            self.$message.error('未知错误');
                        }
                        else{
                            self.$message({
                                message: '添加成功',
                                type: 'success'
                            });
                            self.reloadInfo().reverse()
                        }
                    });
                }).catch(() => {
                self.$message({
                    type: 'info',
                    message: '取消输入'
                });       
            });
        },
        deleteInfo(ID){
            const self:any = this;
            const infoData = {
                  'info_id':ID,
            }
             $.post('http://localhost:5000/deleteInfo',infoData).then(function(data){
                if(data.code === 0){
                    self.$message.error('未知错误');
                }
                else{
                    self.$message({
                        message: '删除成功',
                        type: 'success'
                    });
                    self.reloadInfo().reverse()
                }
            });
        },
        reloadInfo(){
            const self:any = this;
            $.get('http://localhost:5000/loadInfos').then(function(data){
            self.infos = data.infos.reverse();
        });
        }
    },
    created(){
        const self:any = this;
        self.userName = sessionStorage.username;
        self.isManager = (sessionStorage.isManager == 'true')? true:false;
        $.get('http://localhost:5000/loadInfos').then(function(data){
            self.infos = data.infos.reverse();
        });
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
        top: -34px;

}
.infoBox{
    padding:10px 10px 10px;
    :hover  .deleteIcon{
       color: #409EFF;
    }
    .leaveName{
       padding:0;
       font-size: 14px;
       display: block;
       text-align: right;
    }
}

</style>
<style>
.el-card__header{
    padding:3px 10px 3px !important;

}
.el-card{
    padding:0px !important;
    margin: 10px 0px;
}
.el-card__body{
    padding:6px 10px 6px !important;
}
</style>