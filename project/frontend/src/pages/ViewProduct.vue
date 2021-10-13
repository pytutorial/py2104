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
        <a href='index.html' class="btn btn-secondary">Quay lại</a>
        <a :href='`order_product.html?id=${product.id}`' class="btn btn-primary">Mua hàng</a>
      </div>
    </div>
  </div>
</template>