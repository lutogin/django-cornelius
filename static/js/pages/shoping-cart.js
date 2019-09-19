/**
 * Удаление из корзины
 */
function removeFromCartBtn(url) {
  fetch(url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  }).then(() => {
      UIkit.notification({
        message: '<i class="fas fa-backspace"></i><span>&nbsp;Товар удален</span>',
        status: 'warning',
        pos: 'bottom-right',
        timeout: 3000,
      });

      // Удалим с таблици элемент
      document.querySelector(`#product_${id}`).parentNode.removeChild(document.querySelector(`#product_${id}`));
      calculateTotalPrice();
    })
    .catch(err => console.error(err));
}

function sendBuyRequest(contactName, contactType, contactData) {
  return fetch(`/buy-request?contactName=${contactName}&contactType=${contactType}&contactData=${contactData}`, { method: 'POST' });
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

  // Обработка клика
  document.querySelector('#request-btn-submit').addEventListener('click', (evt) => {
    if(document.querySelector('form.request-from #contactName').value.length === 0 ||
      document.querySelector('form.request-from #contactData').value.length === 0)
    {
      evt.stopPropagation();
      return;
    }
    evt.preventDefault();
    const contactName = document.querySelector('#contactName').value;
    const contactType = document.querySelector('#contactType').value;
    const contactData = document.querySelector('#contactData').value;

    sendBuyRequest(contactName, contactType, contactData)
      .then(() => {
        UIkit.modal(document.querySelector('#modal-request-buy')).hide();
        UIkit.notification({
          message: '<i class="fas fa-paper-plane"></i><span>&nbsp;Заявка отправлена, с вами свяжутся в ближайшее время</span>',
          status: 'primary',
          pos: 'bottom-right',
          timeout: 3000,
        });
      })
      .catch(err => console.error(err));
  });
});
