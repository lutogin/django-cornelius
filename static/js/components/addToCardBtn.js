function addToCardBtn(url) {
  fetch(url, { method: 'POST' })
    .then(() => {
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
