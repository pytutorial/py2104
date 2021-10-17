<template>
  <div id="app" class="container mt-3">
    <h3>Đặt mua hàng trực tuyến</h3>
    <form id="fmt" @submit.prevent="orderProduct()">
      <table class="table">
        <tbody>
          <tr><th colspan="2"><h4>Thông tin sản phẩm</h4></th></tr>
          <tr>
            <th>Tên sản phẩm:</th>
            <td>{{product.name}}</td>
          </tr>
  
          <tr>
            <th>Đơn giá:</th>
            <td>{{product.price}} đ</td>
          </tr>
  
          <tr>
            <th>Số lượng:</th>
            <td>
              <input name="qty"
                class="form-control" style="width: 50px;" type="number" min="1" value="1">
              
              <span v-if="errors.qty" style="color:red">{{errors.qty[0]}}</span>
            </td>
          </tr>
  
          <tr><th colspan="2"><h4>Thông tin người mua hàng</h4></th></tr>
  
          <tr>
            <th>Họ và tên:</th>
            <td>
              <input name="customer_name" class="form-control">
              <span v-if="errors.customer_name" style="color:red">{{errors.customer_name[0]}}</span>
            </td>
          </tr>
  
          <tr>
            <th>Điện thoại:</th>
            <td>
              <input name="customer_phone" class="form-control">
              <span v-if="errors.customer_phone" style="color:red">{{errors.customer_phone[0]}}</span>
            </td>
          </tr>
  
          <tr>
            <th>Địa chỉ:</th>
            <td>
              <input name="customer_address" class="form-control">
              <span v-if="errors.customer_address" style="color:red">{{errors.customer_address[0]}}</span>
            </td>
          </tr>
          
        </tbody>
      </table>
      <button type="submit" class="btn btn-primary">Đặt mua</button>  
    </form>
  </div>
</template>
<script>
    export default {
      data: function(){
       return {
          id: null,
          product:{},
          errors: {}
        }
      },
      methods: {
        orderProduct: async function(){
          //alert('save');
          var data = new FormData(document.getElementById('fmt'));
          var url = 'http://127.0.0.1:8000/api/order-product/'+this.id;
          var resp = await fetch(url, {method: 'POST', body: data});
          if(resp.ok) {
            location.href = 'thank_you.html';
          }else{
            this.errors = await resp.json();
          }
        }
      },
      mounted: async function() {
        this.id = this.$route.params.id;
        var url = 'http://127.0.0.1:8000/api/product/'+this.id;
        var resp = await fetch(url);
        this.product = await resp.json();
      }
    }
  </script>