//1º) Calcule o volume de um cilindro dada a sua altura (h) e o seu raio (r) pela fórmula:

let raio: number   = Number(prompt("Digite o raio (r):")!.replace(",", "."));
let altura: number = Number(prompt("Digite a altura (h):")!.replace(",", "."));



function volume_cilindro(raio: number, altura: number): number {
    return Math.PI * (raio*raio) * altura
}

console.log(volume_cilindro(raio, altura).toFixed(2));
alert(`Volume = ${volume_cilindro(raio, altura).toFixed(2)}`);

