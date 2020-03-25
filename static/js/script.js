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
console.log('pre-fetch')

fetch('/api/spirit')
    .then(function(response) {return response.json()})
    .then(function (data) {
        console.log(data)
    })

// fetch('https://swapi.co/api/people/?page=3')
//   .then(function (response) { return response.json()})
//   .then(function (data) {
//     console.log(data)
//     starWarsCharacters = data
//     const character = starWarsCharacters.results[9]
//     const characterHeading = document.createElement('h1')
//     characterHeading.innerText = character.name
//     container.appendChild(characterHeading)
//     characterHeading.classList.add('name-heading')
//     const speciesKey = document.createElement('h2')
//     speciesKey.innerText = 'species'
//     container.appendChild(speciesKey)
//     speciesKey.classList.add('key')

//     return starWarsCharacters.results[9].species[0]