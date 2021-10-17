<template>
  <div>
      Trang dành riêng cho nhân viên
  </div>
</template>
<script>
export default{
  mounted: function() {
    if(!localStorage.getItem('token')){
      this.$router.push('/login');
    }
  }
}
</script>
