import Vue from 'vue'
import Lifa from './lifa.vue'
import router from './router'
let div = document.createElement('div')
div.id = 'app'
div.textContent = 'webpack'

document.body.appendChild(div)
new Vue({
    el: '#app',
    router,
    render: (h) => h(Lifa)
})