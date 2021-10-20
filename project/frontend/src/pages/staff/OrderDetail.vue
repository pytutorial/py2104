<template>
  <div class="container mt-3">
    <h4>Thông tin đơn hàng</h4>
    <table class="table">
      <tbody>
        <tr>
          <th style="width:30%">Tên khách hàng:</th>
          <td>{{order.customer_name}}</td>
        </tr>
        <tr>
          <th>Điện thoại khách hàng:</th>
          <td>{{order.customer_phone}}</td>
        </tr>
        <tr>
          <th>Địa chỉ khách hàng:</th>
          <td>{{order.customer_address}}</td>
        </tr>
        <tr>
          <th>Sản phẩm:</th>
          <td>{{order.product_name}}</td>
        </tr>
        <tr>
          <th>Số lượng:</th>
          <td>{{order.qty}}</td>
        </tr>
        <tr>
          <th>Đơn giá:</th>
          <td>{{order.price_unit}} đ</td>
        </tr>
        <tr>
          <th>Tổng tiền:</th>
          <td>{{order.price_unit * order.qty}} đ</td>
        </tr>
        <tr>
          <th>Ngày đặt hàng:</th>
          <td>{{order.order_date}}</td>
        </tr>
        <tr v-if="order.status==1">
          <th>Ngày giao hàng</th>
          <td>{{order.deliver_date}}</td>
        </tr>
        <tr>
          <th>Trạng thái:</th>
          <td>
            <span v-if="order.status==0"> Đang chờ giao hàng </span>
            <span v-else-if="order.status==1"> Đã giao hàng </span>
            <span v-else-if="order.status==2"> Đã hủy </span> 
          </td>
        </tr>
      </tbody>
    </table>
    
    <router-link class="btn btn-secondary mr-2" to="/staff/order-list">
      Quay lại
    </router-link>
    <template v-if="order.status==0">
      <button class="btn btn-primary mr-2" type="button" @click="confirmOrder()">
        Xác nhận đơn hàng đã được giao
      </button>
      <button class="btn btn-danger" type="button" @click="cancelOrder()">
        Hủy đơn hàng
      </button>
    </template>
  </div>
</template>

<script>
import { SERVER_URL} from "@/constants";
export default {
  data() {
    return{
      id: null,
      order: {}
    }
  },
  methods: {
    confirmOrder: async function() {
      if(!confirm('Xác nhận đơn hàng đã được giao?')){
        return;
      }
      
      let headers = {Authorization: 'Bearer ' + localStorage.getItem('token')};

      let resp = await fetch(`${SERVER_URL}/api/confirm-order/${this.id}`,  {headers, method: 'POST'});

      if(resp.ok){
        this.$router.push('/staff/order-list');
      }else{
        alert('Thao tác thực hiện không thành công');
      }

    },

    cancelOrder: async function() {
      if(!confirm('Hủy đơn hàng này?')) {
        return;
      }
      
      let headers = {Authorization: 'Bearer ' + localStorage.getItem('token')};
      
      let resp = await fetch(`${SERVER_URL}/api/cancel-order/${this.id}`, {headers, method: 'POST'});

      if(resp.ok){
        this.$router.push('/staff/order-list');
      }else{
        alert('Thao tác thực hiện không thành công');
      }
    }
  },

  mounted: async function() {    
    this.id = this.$route.params.id;
    let headers = {Authorization: 'Bearer ' + localStorage.getItem('token')};
    let resp = await fetch(`${SERVER_URL}/api/view-order/${this.id}`, {headers});
    this.order = await resp.json();
  }
};
</script>