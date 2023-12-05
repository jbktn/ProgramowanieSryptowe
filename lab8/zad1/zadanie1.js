funkcja_zwrotna = () => {
    let tekstWartosc = document.getElementById('pole_tekstowe').value;
    let numerycznaWartosc = document.getElementById('pole_liczbowe').value;

    let typTekstowejWartosci = typeof tekstWartosc;
    let typNumerycznejWartosci = typeof numerycznaWartosc;

    console.log(`${tekstWartosc}:${typTekstowejWartosci}`);
    console.log(`${numerycznaWartosc}:${typNumerycznejWartosci}`);
    }

executeCodeFourTimes = () => {
    for (let i = 0; i < 4; i++) {
        const inputValue = window.prompt("Podaj wartość:");
        const inputType = typeof inputValue;
        console.log(`Wczytana wartość: ${inputValue}, typ wczytanej wartości: ${inputType}`);
    }
}

/*console.log('Tekst 1');
window.alert('Tekst 2');
document.write('Tekst 3');*/