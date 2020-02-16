function roundTo(num,decimals) {
    let tenPow = Math.pow(10,decimals);
    let result = parseInt(num * tenPow) / tenPow;
    result = '' + result;
    if (result.indexOf('.') == -1) {
        result += '.'
        for (let i = 0; i < decimals; i++)
            result += '0'
    }
    else {
        while (result.split('.')[1].length < decimals)
            result += '0';
    }
    return result;
}