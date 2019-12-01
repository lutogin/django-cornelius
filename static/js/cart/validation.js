const schema = {
  tel: /^[0-9]{10}$/,
  viber: /^\+?[0-9]{9,15}$/,
  telegram: /^(@?[A-z_.-]{3,}|\+?[0-9]{9,16})$/,
  skype: /^[A-z0-9_-]+$/,
  hangouts: /^[A-z0-9_@]+$/,
  VK: /^(((https:\/\/)?vk\.com\/)?[A-z0-9_.]+)$/,
  email: /^[A-z0-9._]+@[A-z]+\.[A-z]{2,4}$/
};

/**
 * Валидация.
 * @param data        DOM обьект с датой.
 * @param schema      Регулярное вырожение.
 * @param form        DOM обьект формы.
 * @param submitBtn   DOM обьект с кнопкой сабмита.
 */
function validation(data, schema, form, submitBtn) {
  if(data.value.match(schema)) {
    form.validity = true;
    data.classList.add('uk-form-success');
    submitBtn.removeAttribute('disabled');
  } else {
    form.validity = false;
    data.classList.remove('uk-form-success');
    data.classList.add('uk-form-danger');
    submitBtn.setAttribute('disabled', 'disabled');
  }
}

/**
 * Слушатель для проверки формы.
 */
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector('form#confirm-order-form.validation');
  const select = form.querySelector('#contact_type');
  const data = form.querySelector('#contact_data');
  const submitBtn = form.querySelector('#request-btn-submit');

  if (data.value !== '') {
    validation(data, schema[select.value], form, submitBtn);
  }

  data.addEventListener('input', () => {
    if (data.value !== '') {
      validation(data, schema[select.value], form, submitBtn);
    // } else {
    //   data.classList.remove('uk-form-success');
    //   data.classList.remove('uk-form-danger');
    }
  });

  form.addEventListener('change', () => {
    data.classList.remove('uk-form-success');
    data.classList.remove('uk-form-danger');
    if (data.value !== '') {
      validation(data, schema[select.value], form, submitBtn);
    }
  });

  form.addEventListener('submit', (evt) => {
    validation(data, schema[select.value], form, submitBtn);
    if (!form.validity) {
      evt.preventDefault();
    }
  })
});