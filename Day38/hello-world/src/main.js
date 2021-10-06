import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

Vue.config.productionTip = false

const Page1 = {template: `<h3>Trang chủ</h3>`};
const Page2 = {template: `<h3>Trang 2</h3>`};
const Page3 = {template: `<h3>Trang 3</h3>`};

Vue.use(VueRouter);
const routes = [
  {path: '/', component: Page1, meta:{page:1}},
  {path: '/page-2', component: Page2, meta:{page:2}},
  {path: '/page-3', component: Page3, meta:{page:3}}
];

new Vue({
  render: h => h(App),
  router: new VueRouter({routes})
}).$mount('#app')
