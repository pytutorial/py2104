import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/pages/Home'
import ViewProduct from '@/pages/ViewProduct'
Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home, meta:{page:1}},
    {path: '/view-product/:id', component: ViewProduct, meta:{page:1}},
]

const router = new VueRouter({routes})
export default router;