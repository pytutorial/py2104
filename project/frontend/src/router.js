import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/pages/Home'
import ViewProduct from '@/pages/ViewProduct'
import OrderProduct from '@/pages/OrderProduct'
import ThankYou from '@/pages/ThankYou'
import Login from '@/pages/Login'
Vue.use(VueRouter);

const routes = [
    {path: '/', component: Home, meta:{page:1}},
    {path: '/view-product/:id', component: ViewProduct, meta:{page:1}},
    {path: '/order-product/:id', component: OrderProduct, meta:{page:1}},
    {path: '/thank-you', component: ThankYou, meta:{page:1}},
    {path: '/login', component: Login},
]

const router = new VueRouter({routes})
export default router;