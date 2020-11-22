import Router from 'vue-router'
import Vue from 'vue'
import home from '../components/home.vue'
import login from '../components/login.vue'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/home',
            name: 'home',
            component: home
        },
        {
            path: '/',
            name: 'login',
            component: login
        },
    ]

})