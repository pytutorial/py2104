<template>
  <div class="container mt-5">
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
          <p class="mb-2">
            <input
              v-model="categoryId"
              value="1"
              type="radio"
              name="categoryId"
            />
            Acer
          </p>
          <p class="mb-2">
            <input
              v-model="categoryId"
              value="2"
              type="radio"
              name="categoryId"
            />
            Asus
          </p>
          <p class="mb-2">
            <input
              v-model="categoryId"
              value="3"
              type="radio"
              name="categoryId"
            />
            Lenovo
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
            v-for="product in productList"
            class="col-4"
            style="padding-bottom: 50px"
          >
            <a :href="'product_detail.html?id=' + product.id">
              <img width="100%" :src="getImageUrl(product)" />
              <div style="position: absolute; bottom: 0">
                <p class="mb-1">{{ product.name }}</p>
                <p class="mb-1">
                  <i style="font-size: 14px">Giá bán :</i>
                  <b>{{ product.price }} ₫</b>
                </p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>