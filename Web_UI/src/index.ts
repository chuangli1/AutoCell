import Vue from 'vue'
import App from './App.vue'
import router from './router'
import * as ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import * as $ from 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
Vue.use(ElementUI)
// let div = document.createElement('div')
// div.id = 'app'
// div.textContent = 'webpack'

// document.body.appendChild(div)
new Vue({
    el: '#app',
    router,
    components: {App},
    template:'<App/>'
})