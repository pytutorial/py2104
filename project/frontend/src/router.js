import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/pages/Home'
Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home, meta:{page:1}},
]

const router = new VueRouter({routes})
export default router;