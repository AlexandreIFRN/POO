//1º) Calcule o volume de um cilindro dada a sua altura (h) e o seu raio (r) pela fórmula:
var raio = Number(prompt("Digite o raio (r):").replace(",", "."));
var altura = Number(prompt("Digite a altura (h):").replace(",", "."));
function volume_cilindro(raio, altura) {
    return Math.PI * (raio * raio) * altura;
}
console.log(volume_cilindro(raio, altura).toFixed(2));
alert("Volume = ".concat(volume_cilindro(raio, altura).toFixed(2)));
