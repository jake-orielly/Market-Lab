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

function prettyPrint(given) {
    if (given == undefined) {
        console.error('prettyPrint given undefined input')
        return '';
    }
    let arr = given.split('_')
    for (let i = 0; i < arr.length; i++)
        arr[i] = arr[i].substr(0,1).toUpperCase() + arr[i].substr(1);
    return arr.join(' ');
}