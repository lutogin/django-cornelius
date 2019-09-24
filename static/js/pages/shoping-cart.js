/**
 * Отрпавка сабмита.
 *
 * @param contactName
 * @param contactType
 * @param contactData
 * @returns {Promise<Response>}
 */
function sendBuyRequest(contactName, contactType, contactData) {
  data = {
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

// Метод подсчета общей стоимости
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
 * Форма подтверждения заказа.
 */
// Подсчитывает сумму выбраных товаров
document.addEventListener('DOMContentLoaded', () => {
  calculateTotalPrice();

  // Обработка клика подтверждение заказа
  // document.querySelector('#request-btn-submit').addEventListener('click', (evt) => {
  //   if(document.querySelector('form.request-from #contactName').value.length === 0 ||
  //     document.querySelector('form.request-from #contactData').value.length === 0)
  //   {
  //     evt.stopPropagation();
  //     return;
  //   }
  //   evt.preventDefault();
  //   const contactName = document.querySelector('#contactName').value;
  //   const contactType = document.querySelector('#contactType').value;
  //   const contactData = document.querySelector('#contactData').value;
  //
  //   sendBuyRequest(contactName, contactType, contactData)
  //     .then(() => {
  //       UIkit.modal(document.querySelector('#modal-request-buy')).hide();
  //       UIkit.notification({
  //         message: '<i class="fas fa-paper-plane"></i><span>&nbsp;Заявка отправлена, с вами свяжутся в ближайшее время</span>',
  //         status: 'primary',
  //         pos: 'bottom-right',
  //         timeout: 3000,
  //       });
  //     })
  //     .catch(err => console.error(err));
  // });
});
