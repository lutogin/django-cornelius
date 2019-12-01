const HOST = 'http://0.0.0.0:8000';

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
async function cartRequest(cart_event, p_id) {
  const ADD_TO_CARD = 'add';
  const DEL_FROM_CARD = 'rm';

  if (cart_event !== ADD_TO_CARD && cart_event !== DEL_FROM_CARD) {
    alert(`Wrong cart event! (${cart_event})`);
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

  try {
    const res = await fetch(`${HOST}/cart/${url[cart_event]}/${p_id}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  });
  const data = await res.json();
  const cart_counter = document.querySelector('.header_cart__counter');
    switch (cart_event) {
      case ADD_TO_CARD:
        cart_counter.innerText = data.counter;
        if(!cart_counter.classList.contains('active')) {
          cart_counter.classList.add('active');
        }
        break;

      case DEL_FROM_CARD:
        document.querySelector(`#product-${p_id}`).remove();
        if(+data.counter > 0) {
          cart_counter.innerText = data.counter;
        } else {
          cart_counter.classList.remove('active');
          cart_counter.innerText = 0;
        }

        calculateTotalPrice();
        break;
    }

    UIkit.notification({
      message: msg[cart_event],
      status: 'primary',
      pos: 'bottom-right',
      timeout: 3000,
    });
  } catch (e) {
    console.error(e);
  }


}

/**
 * Метод отправки запроса.
 *
 * @param {string} url
 * @param {string} method
 * @param {obj} data
 * @returns {Promise<Response>}
 */
function makeReq(url, method, data) {

  return fetch(url, {
    method: method,
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(data)
  });
}
