/**
 * Возвращает значение cookie по ключу.
 *
 * @param name  Ключ
 * @returns {null}
 */
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

/**
 * Универсальный метод для запросов работы с корзиной.
 *
 * @param {string} cart_event   Тип события(add/rm)
 * @param {string} p_id         ID продукта.
 */
function cartRequest(cart_event, p_id) {
  const ADD_TO_CARD = 'add';
  const DEL_FROM_CARD = 'rm';

  if (cart_event !== ADD_TO_CARD && cart_event !== DEL_FROM_CARD) {
    console.error(`Wrong cart event! (${cart_event})`);
    return;
  }

  // Адреса запросов.
  const url = {
    'add': 'add',
    'rm': 'remove',
  };
  // Сообщения.
  const msg = {
    'add': '<i class="fas fa-shopping-cart"></i><span>&nbsp;Товар добавлен</span>',
    'rm': '<i class="fas fa-backspace"></i><span>&nbsp;Товар удален</span>'
  };


  current_url = url[cart_event];
  console.log(current_url);
  fetch(`http://127.0.0.1:8000/cart/${url[cart_event]}/${p_id}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  }).then(() => {
      UIkit.notification({
        message: msg[cart_event],
        status: 'primary',
        pos: 'bottom-right',
        timeout: 3000,
      });
    })
    .catch(err => console.error(err));
}

