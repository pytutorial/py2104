<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-6">
        <img width="100%" :src='product.image' />
      </div>
      <div class="col-6 pt-5">
        <h4>{{product.name}}</h4>
        <table class="table">
          <tbody>
            <tr>
              <th>Hãng sản xuất:</th>
              <td>{{product.category_name}}</td>
            </tr>
            <tr>
              <th>Giá bán:</th>
              <td>{{product.price}} ₫</td>
            </tr>
          </tbody>
        </table>
        <router-link to='/' class="btn btn-secondary mr-2">Quay lại</router-link>
        <router-link :to='`/order-product/${product.id}`' class="btn btn-primary">Mua hàng</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { SERVER_URL} from "@/constants";
export default {
  data: function() {
    return {
      product: {}
    }
  },
  mounted: async function() {
    var id = this.$route.params.id;
    var url = `${SERVER_URL}/api/product/${id}`;
    var resp = await fetch(url);
    this.product = await resp.json();
  }
}
</script>
