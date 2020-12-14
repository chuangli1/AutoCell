<template>
    <epm-2-table v-bind:items ="currentItems" :headers ="headers" v-if='isDataValid'>
          
      <!-- <template v-slot:name={item}>
          <span> {{item.name}}</span> -->
           <!-- <router-link :to="`/${item.routerLink}/${item.id}${item.routerLink==='report'||item.routerLink==='dashboard'? '/false':''}`"
                            v-if="!item.isGroup" :key="item.id">
                <span class="nameIcon pictureIcon" :class="icon"/>
                <a class="sheet-name">{{item.name}}</a>
            </router-link>
            <div v-else @click="openFolder(item)">
                <span class="nameIcon pictureIcon folderIcon"/>
                <a class="sheet-name">{{item.name}}</a>
            </div> -->
      <!-- </template> -->
      <!-- <template v-slot:action={item}>
            <button class='actionBtn' v-if="!item.isGroup">
                <span class="glyphicon glyphicon-trash"></span>
            </button>
            <button class='actionBtn' v-if="!item.isGroup && item.routerLink ==='sheet2'">
                <span class="glyphicon glyphicon-copy"></span>
            </button>
            <button class='actionBtn' v-if="!item.isGroup && item.routerLink !=='freeSheet'">
                <span class="glyphicon glyphicon-edit"></span>
            </button>
      </template>  -->

     </epm-2-table>
</template>
<script lang="ts">
import Vue from 'vue'
import epm2Table from './tools/tableCard.vue'
export default Vue.extend({
    name: 'dataManager',
    data(){
        return{
            currentItems:[],
            headers:[],
            isDataValid:false

        }
    },

    components:{
        epm2Table
    },
    methods:{

    },
    created(){
        const self:any = this;
        self.headers = [
            {text:'名称', value: 'name',sortable: true},
            {text:'日期', value: 'date',sortable: true},
            {text:'', value: 'action',sortable: false},
        ];
        $.get('http://localhost:5000/videoGet',{"user_name":"1"}).then(function(data){
            console.log(data);
            if(data.code=='1'){
                data.videoList.forEach(e => {
                    self.currentItems.push({
                        'name': e[1],
                        'date': e[3],
                        'isGroup':false,
                        'action':''
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

</style>