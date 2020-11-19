import login from '../components/login.vue'
import Vue from 'vue'
import Router from 'vue-router'
import home from '../components/home.vue'

Vue.use(Router);

 export default new Router({
     routes:[
        {
            path:'/',
            component: login,
            name: 'login'
        },
        {
            path:'/home',
            component: home,
            name: 'home'
        }
     ]
 })

