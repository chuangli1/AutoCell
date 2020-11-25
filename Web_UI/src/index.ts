import Vue from 'vue'
import App from './App.vue'
import router from './router'
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