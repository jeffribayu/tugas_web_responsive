
  const slider = document.querySelector('.product-slider');
  const productCards = document.querySelectorAll('.product-card');

  let scrollAmount = 0;

  function scrollRight() {
    scrollAmount += productCards[0].offsetWidth + 20;
    if (scrollAmount > slider.scrollWidth - slider.offsetWidth) {
      scrollAmount = slider.scrollWidth - slider.offsetWidth;
    }
    slider.scrollTo({
      left: scrollAmount,
      behavior: 'smooth',
    });
  }

  function scrollLeft() {
    scrollAmount -= productCards[0].offsetWidth + 20;
    if (scrollAmount < 0) {
      scrollAmount = 0;
    }
    slider.scrollTo({
      left: scrollAmount,
      behavior: 'smooth',
    });
  }
