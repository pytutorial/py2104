<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary p-0">
      <div class="navbar-nav">
        <router-link class="nav-item nav-link" :class="{active: $route.meta.page==1}" to="/staff/order-list">Quản lý đơn hàng</router-link>
        <router-link class="nav-item nav-link" :class="{active: $route.meta.page==2}" to="/staff/product-list">Quản lý sản phẩm</router-link>
        <router-link class="nav-item nav-link" :class="{active: $route.meta.page==3}" to="/staff/category-list">Quản lý nhóm sản phẩm</router-link>
      </div>
      
      <ul class="navbar-nav ml-auto">
        <li class="nav-item dropdown no-arrow">
          <a class="nav-link dropdown-toggle p-0" data-toggle="dropdown" href="#">
            <img class="rounded-circle" style="width:60px" src="https://raw.githubusercontent.com/pytutorial/html_samples/master/css_bootstrap/user.svg">
          </a>
          <div class="dropdown-menu dropdown-menu-right">
            <a class="dropdown-item" href="#">
              Thông tin tài khoản
            </a>
            <div class="dropdown-divider"></div>
            <a @click="logout()" class="dropdown-item" href="#">
              Đăng xuất
            </a>
          </div>
        </li>
      </ul>
    </nav>

    <router-view></router-view> 

    <div class="container mt-3" v-if="$route.path=='/staff/'||$route.path=='/staff'">
      Trang dành cho nhân viên cửa hàng
    </div>
  </div>
</template>
<script>
export default{
  methods: {
    logout: function() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  },
  mounted: function() {
    if(!localStorage.getItem('token')){
      this.$router.push('/login');
    }
  }
}
</script>
