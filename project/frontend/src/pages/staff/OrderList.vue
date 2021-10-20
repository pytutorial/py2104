<template>
  <div class="container mt-3">
    <h4>Danh sách đơn hàng</h4>
    <div class="row my-3">
      <div class="col">
        <form id="fmt" @submit.prevent="searchOrder()">
          <input name="name" :value="name" class="form-control" placeholder="Tìm theo tên sản phẩm">
        </form>
      </div>
    </div>
    <table class="table table-bordered">
      <thead>
        <tr class="text-center">
          <th style="width: 20%;">Khách hàng</th>
          <th style="width: 20%;">Sản phẩm</th>
          <th style="width: 15%;">Số lượng</th>
          <th style="width: 15%;">Ngày đặt hàng</th>
          <th style="width: 20%;">Trạng thái</th>
          <th style="width: 10%;"></th>
        </tr>
      </thead>
      <tbody>        
        <tr v-if="items && items.length == 0">
          <td colspan="6">Không có đơn hàng nào</td>
        </tr>
        
        <tr v-for='(o,i) in items||[]' :key="i">
          <td>{{o.customer_name}}</td>
          <td>{{o.product_name}}</td>
          <td class="text-center">{{o.qty}}</td>
          <td class="text-center">{{o.order_date}}</td>
          <td>
            <span v-if="o.status==0"> Đang chờ giao hàng </span>
            <span v-else-if="o.status==1"> Đã giao hàng </span>
            <span v-else-if="o.status==2"> Đã hủy </span>            
          </td>
          <td class="text-center">
            <router-link class="btn btn-sm btn-secondary" :to='`/staff/order-detail/${o.id}`'>
              Xem
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>

    <b-pagination
      size="md"
      v-model="page"
      :total-rows="total"
      :per-page="pageSize"
    ></b-pagination>
    <label class="label">Tổng số : {{ total }} bản ghi</label>

  </div>
</template>

<script>

import { PAGE_SIZE, SERVER_URL} from "@/constants";
export default {
  data() {
    return {
      items: null,
      name: '',
      pageSize: PAGE_SIZE,
      page: 1,
      total: 0, 
    }
  },
  methods: {
    getData: async function(name, page) {
      this.name = name ?? '';
      this.page = page ?? 1;
      let url = `${SERVER_URL}/api/search-order?name=${this.name}&page=${this.page}`;
      let headers = {Authorization: 'Bearer ' + localStorage.getItem('token')};
      let resp = await fetch(url, {headers});
      let result = await resp.json();
      this.total = result.total;
      this.items = result.data;
    },
  
    searchOrder() {
      const data = new FormData(document.getElementById('fmt'));
      const name = data.get('name');
      this.getData(name, 1);
    }
  },
  watch: {
    page: function(){
      this.getData(this.name, this.page);
    }
  },

  mounted: function() {
    this.getData();
  }
};
</script>