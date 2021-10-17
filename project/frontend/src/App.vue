<template>
  <div>
    <app-staff v-if="$route.path.startsWith('/staff')"></app-staff>
    <router-view v-else></router-view>
  </div>
</template>
<script>
import AppStaff from './AppStaff.vue';
export default {
  components:{
    AppStaff
  }
}
</script>
