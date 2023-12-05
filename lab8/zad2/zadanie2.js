sum = (x,y) => {
    return x+y;
}

sum_strings = (a) => {
    let sum = 0;
    for (let str of a) {
        if (/^\d{1,3}$/.test(str.slice(0, 3))) {
            sum += parseInt(str, 10);
        }
    }
    return sum;
}

digits = (s) => {
    let oddSum = 0;
    let evenSum = 0;
  
    for (let char of s) {
        if (/[0-9]/.test(char)) {
            const digit = parseInt(char, 10);  
            if (digit % 2 === 0) {
                evenSum += digit;
            } else {
                oddSum += digit;
            }
        }
    } 
    return [oddSum, evenSum];
}

letters = (s) => {
    let lowercaseCount = 0;
    let uppercaseCount = 0;  
    for (let char of s) {
        if (/[a-z]/.test(char)) {
            lowercaseCount++;
        } else if (/[A-Z]/.test(char)) {
            uppercaseCount++;
        }
    }  
    return [lowercaseCount, uppercaseCount];
}