let numero = 5; 

console.log("Tabellina del " + numero + " (con for):");
for (let i = 1; i <= 10; i++) {
    console.log(numero + " x " + i + " = " + (numero * i));
}

let numero2 = 5;
let i = 1;

console.log("Tabellina del " + numero2 + " (con while):");
while (i <= 10) {
    console.log(numero2 + " x " + i + " = " + (numero2 * i));
    i++;
}
