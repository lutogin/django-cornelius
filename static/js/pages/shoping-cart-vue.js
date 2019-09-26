async function get_cart() {
  fetch('http://127.0.0.1:8000/cart/get-cart-api/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  })
  .then((res) => res.json())
  .then((data) => {
    return data;
  })
}
let products = get_cart();
console.log(products);

Vue.component('cart', {
  delimiters: ['${', '}'],
  props: ['products'],

  template: ['<div>',
                '<table class="uk-table uk-table-striped uk-table-hover uk-table-middle">',
                  '<caption></caption>',
                  '<tr :id="product.id"> v-for="product in products"',
                    '<td>',
                      '<a v-on:click="submit_cart">',
                        '<i class="fas fa-minus-circle"></i>',
                      '</a>',
                    '</td>',
                    '<td class="uk-table-link" width="100px">',
                      '<a href="">',
                        '<img width="80px" :src="product.img" :alt="product.title">',
                      '</a>',
                    '</td>',
                    '<td>${ product.title }</td>',
                    '<td>',
                      '<label for="p_quantity">Количетсво</label>',
                      '<input name="quantity-prod-" type="number" class="p_quantity" min="1" max="999" value="{{ item.quantity }}">',
                    '</td>',
                    '<td>',
                    '<label>',
                      '<input id="engr-prod-" class="uk-checkbox" type="checkbox" name="engr-prod-">',
                      'Выполнить гравировку',
                    '</label>',
                    '</td>',
                    '<td><span id="product-price" class="price">${ product.price }</span><span>₽</span></td>',
                  '</tr>',
                  '<tfooter>',
                    '<tr>',
                      '<td colspan="5">Предаварительная сумма заказа</td>',
                      '<td><span class="totalPrice"></span><span>₽</span></td>',
                    '</tr>',
                  '</tfooter>',
                '</table>',
                '<div class="uk-flex uk-flex-around">',
                  '<button class="uk-button uk-button-primary request" onclick="" uk-toggle="target: #modal-request-buy">Оставить заявку</button>',
                '</div>',
              '</div>'].join('')
});

const cart = new Vue({
  el: '#cart',
  data: {
    products: {'id': 1, 'title': 'afdsdfsd', 'img': '/sdfs/sdfs/sd.jpg', 'price': 222},
    msg: 'asdasdasda'
  },
  methods: {
    get_cart: function () {
      fetch('http://127.0.0.1:8000/cart/get_cart_api/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
        },
      })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
      })
    }
  }
});


