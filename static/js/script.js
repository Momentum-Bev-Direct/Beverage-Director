console.log('js linked wubba')

const slider = document.querySelector('#ounce-slider')

const ounceOutput = document.querySelector('#ounce-pour')
const pourPriceOutput = document.querySelector('#price-per-pour')
ounceOutput.innerHTML = slider.value

slider.oninput = function () {
    ounceOutput.innerHTML = this.value;
}