import fs from 'fs-extra';
import { argv } from 'node:process';
import { readFileSync } from 'node:fs';
import { readFile } from 'node:fs/promises';
import readline from 'node:readline';
import { exec } from 'node:child_process';

function sync() {
    let data = Number(readFileSync("./data.txt"));
    data++;
    console.log(data);
    fs.writeFileSync("./data.txt", String(data));
}

async function async() {
    let data = Number(await readFile("./data.txt"));
    data++;
    console.log(data);
    fs.writeFile("./data.txt", String(data));
}

function commands() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.on('line', (line) => {
        exec(line, (error, stdout) => {
            if (error) {
                console.error(`Błąd wykonania komendy: ${error}`);
                return;
            }
            console.log(stdout);
        });
    });
    
}

console.clear();
console.log("\t\x1B[34mProgram start\x1B[0m");
if (argv[2] === "--sync") {
    console.log(`\x1B[31mSynchroniczny odczyt pliku "${argv[1]}"\x1B[0m`);
    sync();
}
else if (argv[2] === "--async") {
    console.log(`\x1B[31mAsynchroniczny odczyt pliku "${argv[1]}"\x1B[0m`);
    async();
}
else {
    commands();
}
console.log("\t\x1B[34mProgram stop\x1B[0m");