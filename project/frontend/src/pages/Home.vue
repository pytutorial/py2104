<template>
  <div id="app" class="container mt-5">
    <div class="row">
      <div class="col-3" style="border: 1px solid #ddd; border-radius: 4px">
        <div class="form-group mt-4">
          <label><b>Tên sản phẩm:</b></label>
          <input
            v-model="name"
            class="form-control"
            placeholder="Nhập tên sản phẩm cần tìm"
          />
        </div>

        <div class="form-group">
          <label><b>Hãng sản xuất:</b></label>
          <p class="mb-2">
            <input
              v-model="categoryId"
              value=""
              type="radio"
              name="categoryId"
            />
            Tất cả
          </p>
          <p class="mb-2" v-for="category in categoryList" :key="category.id">
            <input
              v-model="categoryId"
              :value="category.id"
              type="radio"
              name="categoryId"
            />
            {{category.name}}
          </p>
        </div>

        <div class="form-group">
          <label><b>Mức giá:</b></label>
          <p class="mb-2"><input type="radio" name="priceRangeId" /> Tất cả</p>
          <p class="mb-2">
            <input type="radio" name="priceRangeId" /> Dưới 10 triệu
          </p>
          <p class="mb-2">
            <input type="radio" name="priceRangeId" /> Từ 10-20 triệu
          </p>
          <p class="mb-2">
            <input type="radio" name="priceRangeId" /> Trên 20 triệu
          </p>
        </div>

        <button class="btn btn-primary mb-4" @click="search">Tìm kiếm</button>
      </div>
      <div class="col-9">
        <div class="row">
          <div
            :key="product.id"
            v-for="product in productList"
            class="col-4"
            style="padding-bottom: 50px"
          >
            <router-link :to="'/view-product/' + product.id">
              <img width="100%" :src="getImageUrl(product)" />
              <div style="position: absolute; bottom: 0">
                <p class="mb-1">{{ product.name }}</p>
                <p class="mb-1">
                  <i class='product-price'>Giá bán :</i>
                  <b>{{ product.price }} ₫</b>
                </p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .product-price {
    font-size: 14px;
  }
</style>

<script> 
import { SERVER_URL} from "@/constants";
export default {
  data: function() {
    return {
        productList:[],
        name: '',
        categoryId: '',
        serverUrl: SERVER_URL,
        categoryList: []
    }
  },

  methods: {
    getImageUrl: function(product){
      return this.serverUrl + product.image;
    },

    getCategoryList: async function() {
      var resp = await fetch(this.serverUrl + '/api/category');
      this.categoryList = await resp.json();
    },

    search: async function() {
      var url = this.serverUrl + '/api/get-product-list?name='+this.name;
      var resp = await fetch(url);
      var result = await resp.json();
      console.log(result);
      this.productList = result;
    }
  },

  mounted: async function() {
    this.getCategoryList();
    this.search();
  }
}
</script>