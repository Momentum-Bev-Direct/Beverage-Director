console.log('js linked wubba')

const slider = document.querySelector('#ounce-slider')

const ounceOutput = document.querySelector('#ounce-pour')
const pourPriceOutput = document.querySelector('#pour-price')
ounceOutput.innerHTML = slider.value
const costOfGoodsOutput = document.querySelector('#cost-of-goods-value')
const menuPriceOutput = document.querySelector('#menu-price-value')
const targetCostPercent = document.querySelector('#target-cost-value')
let pricePerOunce = .50


slider.oninput = function () {
    ounceOutput.innerHTML = this.value;
    pourPriceOutput.innerHTML = (this.value * pricePerOunce).toFixed(2)
    costOfGoodsOutput.innerHTML = pourPriceOutput.innerHTML
    menuPriceOutput.innerHTML = (costOfGoodsOutput.innerHTML / (targetCostPercent.value / 100)).toFixed(2)

    
}

