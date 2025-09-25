
const input = require('read-line-sync')
const b1 = +input.question('Bim1: ')
const b2 = +input.question('Bim2: ')

let media = (b1 * 2 + b2 * 3) / 5


console.log (`Média = ${media}`)

if(media >= 60) {
    console.log('Aprovado(a)')
} else {
    console.log('Avaliação final')
}