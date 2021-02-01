// 
// Изменение хедера при скролле
// 
let header = document.querySelector('.header-wrap');
if (header) {
    let headerOnScroll = function () {
        if (pageYOffset === 0) {
            header.classList.add('header-light');
        }
        else{
            header.classList.remove('header-light');
        }
    }
    window.addEventListener('scroll', headerOnScroll);
    
    // 
    // Дропдаун юзера
    // 
    
    let header__user = document.querySelector('.header__user');
    let header__dropdown = document.querySelector('.header__dropdown');
    let onHeaderUserHover = function () {
        header__user.classList.add('header__user-active');
        header__dropdown.classList.remove('dn');
    }
    let onHeaderUserMouseLeave = function () {
        header__user.classList.remove('header__user-active');
        header__user.removeEventListener('mouseenter', onHeaderUserHover);
        header__user.removeEventListener('mouseleave', onHeaderUserMouseLeave);
        setTimeout(function(){
            header__dropdown.classList.add('dn');
            header__user.addEventListener('mouseenter', onHeaderUserHover);
            header__user.addEventListener('mouseleave', onHeaderUserMouseLeave);
        }, 300)
    }
    if (header__user) {
        header__user.addEventListener('mouseenter', onHeaderUserHover);
    }
    if (header__user) {
        header__user.addEventListener('mouseleave', onHeaderUserMouseLeave);
    }
}


// 
// Слайдер
// 

let curSlider = 1;
let slider = document.querySelector('.cards');
if (slider) {
    let prevButton = document.querySelector('.button__prev');
    let lastButton = document.querySelector('.lastbutton');
    let nextButton = document.querySelector('.button__next');
    let count = document.querySelectorAll('.card').length;
    let onNextButtonClick = function () {
        if (curSlider < count) {
            curSlider++;
            callSlide(curSlider);
        }
    }
    let onPrevButtonClick = function () {
        if (curSlider > 1) {
            curSlider--;
            callSlide(curSlider);
        }
    }
    nextButton.addEventListener('click', onNextButtonClick);
    prevButton.addEventListener('click', onPrevButtonClick);
    let progressText = document.querySelector('.progresstext');
    let progressBar = document.querySelector('.progressing');
    let callSlide = function (curSlider) {
        slider.style.transform = `translateX(-${(curSlider - 1) * 685 }px)`;
        progressText.textContent = `${curSlider} / ${count}`;
        progressBar.style.width = `${curSlider / count * 100}%`;
        if (curSlider === count) {
            progressBar.style.width = `calc(${curSlider / count * 100}% + 50px)`;
            lastButton.classList.remove('dn');
        }
        else{
            lastButton.classList.add('dn');
        }
        if (curSlider === 1) {
            prevButton.classList.add('button__circle-disabled');
        }
        else{
            prevButton.classList.remove('button__circle-disabled');
        }
    }
    callSlide(curSlider);
}

 