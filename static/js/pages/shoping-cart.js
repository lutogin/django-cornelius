/**
 * Цена гравировки.
 * @type {number}
 */
const ENGRAVING_PRICE = 500;

/**
 * Пересчитывает общую стоимость.
 */
function calculateTotalPrice() {
  let priceses = document.querySelectorAll('.price');
  let quantity = document.querySelectorAll('.p_quantity');
  let totalPrice = 0;
  priceses.forEach((item, index) => {
    totalPrice += parseInt(item.textContent) * parseInt(quantity[index].value);
  });
  document.querySelector('.totalPrice').textContent = totalPrice;

  // Блокировать кнопку, в случае если с корзины удалено все
  if (totalPrice === 0) {
    document.querySelector('button.request').setAttribute('disabled', 'true');
  } else {
    document.querySelector('button.request').removeAttribute('disabled')
  }
}

/**
 * Отработка checkbox с гравировкой.
 *
 * @param pid ID продукта
 */
function addEngraving(pid) {
  let product_price_el = document.querySelector(`#product-${pid} #product-price`);
  let price = +product_price_el.innerText;
  let chk_box = document.querySelector(`#engr-product-${pid}`);
  if (chk_box.checked) {
    product_price_el.innerText = price + ENGRAVING_PRICE;
  } else {
    product_price_el.innerText = price - ENGRAVING_PRICE;
  }

  calculateTotalPrice();
}

/**
 * Отрпавка сабмита.
 *
 * @param contactName
 * @param contactType
 * @param contactData
 * @returns {Promise<Response>}
 */
function submitRequest(contactName, contactType, contactData) {
  let data = {
    'contactName': contactName,
    'contactType': contactType,
    'contactData': contactData
  };

  return fetch('http://127.0.0.1:8000/cart/submit/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(data)
  });
}

/**
 * Форма подтверждения заказа.
 */
document.addEventListener('DOMContentLoaded', () => {
  calculateTotalPrice();

  // Обработка клика подтверждение заказа
  document.querySelector('#confirm-order-form').addEventListener('submit', (evt) => {
    if(document.querySelector('#confirm-order-form #contactName').value.length === 0 ||
      document.querySelector('#confirm-order-form #contactData').value.length === 0)
    {
      evt.stopPropagation();
      return;
    }
    evt.preventDefault();

    UIkit.modal(document.querySelector('#modal-request-buy')).hide();
    UIkit.modal(document.querySelector('#modal-submit-buy')).show();
    UIkit.notification({
      message: "Спасибо!",
      status: 'primary',
      pos: 'bottom-right',
      timeout: 3000,
    });

    const contactName = document.querySelector('#contactName').value;
    const contactType = document.querySelector('#contactType').value;
    const contactData = document.querySelector('#contactData').value;
    submitRequest(contactName, contactType, contactData)
      .then((res) => res.json())
      .then((data) => {

        setTimeout(() => {
          window.location.href = (data['url'])
        }, 3000)
      })
      .catch(err => console.error(err));
  });
});
