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
 * Универсальный метод для запроса к корзине.
 *
 * @param url
 * @param type_msg
 */
function cartRequest(url, type_msg) {
  const ADD_TO_CARD = 'add';
  const DEL_FROM_CARD = 'del';

  $msg = '<i class="fas fa-shopping-cart"></i><span>&nbsp;</span>';
  if (type_msg === ADD_TO_CARD) {
    $msg = '<i class="fas fa-shopping-cart"></i><span>&nbsp;Товар добавлен</span>';
  } else if (type_msg === DEL_FROM_CARD) {
    $msg = '<i class="fas fa-backspace"></i><span>&nbsp;Товар удален</span>';
  }

  fetch(url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
  }).then(() => {
      UIkit.notification({
        message: $msg,
        status: 'primary',
        pos: 'bottom-right',
        timeout: 3000,
      });
    }).catch(err => console.error(err));
}
