// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== '') {
//     let cookies = document.cookie.split(';');
//     for (let i = 0; i < cookies.length; i++) {
//       let cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === (name + '=')) {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }


function addToCardBtn(url, csrftoken) {
  // let csrftoken = getCookie('csrftoken');

  fetch(url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  }).then(() => {
      UIkit.notification({
        message: '<i class="fas fa-shopping-cart"></i><span>&nbsp;Товар добавлен</span>',
        status: 'primary',
        pos: 'bottom-right',
        timeout: 3000,
      });
      document.querySelector('.shopping-cart_link').classList.add('animated', 'rubberBand');
    })
    .catch(err => console.error(err));
}
