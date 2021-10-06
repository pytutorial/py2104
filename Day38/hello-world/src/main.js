import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'

Vue.config.productionTip = false

import Page1 from "./pages/Page1"
import Page2 from "./pages/Page2"
import Page3 from "./pages/Page3"

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
