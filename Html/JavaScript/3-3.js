let secondiTotali = 12560;

let ore = Math.floor(secondiTotali / 3600);

let minuti = Math.floor((secondiTotali % 3600) / 60);

let secondi = secondiTotali % 60;

console.log(ore + " ore, " + minuti + " minuti e " + secondi + " secondi");
