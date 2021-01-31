<template>
<div>
    <div class="Rectangle-2">
        <span class="el-icon-search oval"></span>
        <input  @keyup.enter="searchItems" class="Search-Sheets" style="outline:none" placeholder="搜索数据" v-model="searchData"/>
        <span v-if="searchMode" @click="recoverSearch" class="el-icon-circle-close removeIcon"></span>
    </div>
        <table>
            <thead>
            <th v-for="(header,i) in headers" :key="i" @click="sorts(i)" :class="{'sortsure':(sortDirection[i]!=0)}">
                <span> {{header.text}} </span>
                <span  v-if='header.sortable'  class="sorticon" :class="{'el-icon-top': (sortDirection[i]===1||sortDirection[i]===0),
                'el-icon-bottom':(sortDirection[i]==-1),'sortsure':(sortDirection[i]!=0)}">
                </span>
            </th>
            </thead>
            <tbody>
                <tr  v-for="(item,i) in currentItems" :key="i">
                    <td v-for="(header,j) in headers"  :key="j">
                        <!-- <span>{{item[header.value]}}</span> -->
                        <slot :name='header.value' :item='item'>{{item[header.value]}}</slot>
                    </td>
                </tr>   
            </tbody>
        </table>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default  Vue.extend({
    name: 'epm2Table',
    props: {
        items: Array,
        headers: Array,
    },
    watch: {
        items: function(){
            const self:any=this
            if(self.items!=self.currentItems){
                self.currentItems = self.items;
                self.itemsCopy = self.items.slice();
                self.originItems = self.items.slice();
                for(let i = 0; i<self.headers.length; i++){
                    if(self.sortDirection[i]!==0){
                        self.sortsOrgin(i);
                        break;
                    }
                }
            }
        }
            
        },
    data(){
        return{
            sortName:'',
            currentItems: [],
            itemsCopy:[],
            sortDirection: [],
            searchData:'',
            searchMode:false,
            orginItems:[]
        };
    },
    created: function() {
        const self:any = this;
        self.currentItems = self.items;
        self.itemsCopy = self.items.slice();
        self.originItems = self.items.slice();
        for(let i = 0; i<self.headers.length; i++){
                self.sortDirection[i] = 0
        };
    },
    methods:{
        sortsOrgin: function(i){
            const self:any = this;
            self.sortName = self.headers[i].value;
            //self.itemsCopy = self.items.slice();
            self.currentItems = self.itemsCopy;
            if(self.sortDirection[i] === 1)
            {
              
              self.currentItems.sort(self.sortid);
            }
            else if(self.sortDirection[i] === -1)
            {
               self.currentItems.sort(self.sortid1);
            }

        },
        sorts: function(i){
            const self:any = this;

            self.currentItems = self.itemsCopy;
            self.sortName = self.headers[i].value;
            if(self.sortDirection[i] === 0){
              self.sortDirection[i] = 1;
              self.currentItems.sort(self.sortid);
              self.sortHead(i);
            }
            else if(self.sortDirection[i] === 1)
            {
               self.sortDirection[i] = -1;
               self.currentItems.sort(self.sortid1);
            }
            else{
                self.sortDirection[i] = 0;
                self.currentItems = self.originItems;
            }

        },
        sortid(item1,item2){   
            const self:any = this
            if(item1.isGroup&&(!item2.isGroup)) return -1;
            if(item2.isGroup&&(!item1.isGroup)) return 1;
            
            const a = item1[self.sortName];
            const b = item2[self.sortName];
            if(a>b) return 1;
            if(a===b) return 0;
            else return -1;
        },
        sortid1(item1,item2){  
            const self:any = this;
            if(item1.isGroup&&(!item2.isGroup)) return 1;
            if(item2.isGroup&&(!item1.isGroup)) return -1;
            const a = item1[self.sortName];
            const b = item2[self.sortName];
            if(a>b) return -1;
            if(a===b) return 0;
            else return 1;
        },
        sortHead(i){
            const self:any = this;
            for(let j = 0; j<self.headers.length; j++){
                
                if(j!==i) self.sortDirection[j] = 0;
            }
        },
        recoverSearch(){
            const self:any = this;
            self.currentItems =self.items.slice();
            self.itemsCopy = self.items.slice();
            self.originItems = self.itemsCopy.slice();
            for(let i = 0; i<self.headers.length; i++){
                if(self.sortDirection[i]!==0){
                    self.sortsOrgin(i);
                    break;
                }
            }
            self.searchData = '';
            self.searchMode = false;
        },
        searchItems(){
            const self:any = this;
            let searchItems:any = [];
            self.currentItems =self.items;
            self.itemsCopy =  self.items.slice();
            // if(self.searchData===''){
            //     for(let i = 0; i<self.headers.length; i++){
            //         if(self.sortDirection[i]!==0){
            //             self.sortsOrgin(i);
            //             break;
            //         }
            //     }
            //     return
            // }
            for(let i=0; i<self.currentItems.length; i++){
                    if(self.currentItems[i].isGroup){
                        self.currentItems[i]['sheets'].forEach(e => {
                            for(let j = 0; j<self.headers.length; j++){
                                if(e[self.headers[j].value]){
                                    if(e[self.headers[j].value].indexOf(self.searchData)!= -1){
                                        searchItems.push(e);
                                        break;
                                    }
                                }
                            }    
                        });
                    }
                    else{
                        for(let j = 0; j<self.headers.length; j++){
                            if(self.currentItems[i][self.headers[j].value]){
                                if(self.currentItems[i][self.headers[j].value].indexOf(self.searchData)!= -1){
                                    searchItems.push(self.currentItems[i]);
                                    break;
                                }
                            }
                        }
                    }
            }
            self.currentItems = searchItems;
            self.itemsCopy =  searchItems.slice();
            self.originItems = searchItems.slice();
            for(let i = 0; i<self.headers.length; i++){
                    if(self.sortDirection[i]!==0){
                        self.sortsOrgin(i);
                        break;
                    }
                }
            self.searchMode = true;
        }
    }

}
);
</script>
<style lang="scss" scoped>

table tbody {
    display: block;
    position: relative;
    top:0;
    bottom: 0px;
    left: 0px;
    // height: 480px;
    font-size:14px;
    overflow-y: auto;
}

table thead,
table tbody tr {
    display: table;
    width: 100%;
    table-layout: fixed; /**表格列的宽度由表格宽度决定，不由内容决定*/
}

thead th,
tbody td {
    width: 100%;
    padding-left: 6px;
}
td{
     white-space: nowrap;
}

table thead {
    width: calc( 100% - 1em);/*表头与表格垂直对齐*/
}

th{
    padding:2px 16px 16px 4px;
    font-size: 12px;
    background-color: #fff;
    color: #00000099;
    
}

tr{
   height: 48px;
   width: 100%;
   
}
td{
    padding-left: 16px;
    padding-right: 16px;
    
}
tr:hover{
    background-color:rgba($color: #333333, $alpha: 0.087);
}

.sorticon{
    visibility: hidden;
    font-size: 14px;
    padding: 4px;
}
th:hover{
    cursor:pointer;
    .sorticon{
        visibility: visible;
    }
}
.Rectangle-2 {
    width: 300px;
    height: 30px;
    margin: 2px 2px 0 8px;
    padding: 6px 6px;
    border-radius: 6px;
    background-color: #f6f6f6;
    position: fixed;
    top: 4px;
    right: 20px;
    z-index: 1000;
    .oval {
        width: 14px;
        height: 12px;
        padding-bottom: 5px;
        //margin: 0 0px 0px 0;
        border: solid 1.5px var(--black);
        position: relative;
        bottom: 3px;
    }
    .Search-Sheets {
        width: 240px;
        height: 16px;
        margin: 0 0 0 2px;
        font-family: Roboto;
        font-size: 12px;
        font-weight: normal;
        font-stretch: normal;
        font-style: normal;
        line-height: normal;
        letter-spacing: normal;
        color: #bbbbbb;
        background-color: #f6f6f6;
        border: none;
        padding-bottom: 5px;
        position: relative;
        bottom: 3px;
        :focus {
        outline: none;
        background-color: transparent;
    }
    }
    .removeIcon{
        width:14px;
        height: 14px;
        position: relative;
        bottom: 3px;
        color: rgb(99,99,99);


    }

}

.sortsure{
    visibility: visible;
    cursor:pointer;
    color: #000;
}
</style>