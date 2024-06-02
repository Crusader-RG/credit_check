const creditCheck = (num) => {
    // make array from num input
    arr = Array.from(num.toString()).map(Number)
    let sum = 0
    // loop through array and double every other
    for (i = 0; i < arr.length; i += 2){
        arr[i] = arr[i] * 2
    }
    // loop through array and sum the digits of numbers greater than 9
    for (i = 0; i < arr.length; i++){
        if (arr[i] > 9){
            arr[i] = (Math.floor(arr[i] / 10)) + (arr[i] % 10)
        }
    }
    // loop through array and sum array
    for (i = 0; i < arr.length; i++){
        sum += arr[i]
    }
    // % 10 check for validity
    if (sum % 10 === 0){
        return 'Valid'
    } else {
        return "Invalid"
    }
    
}


console.log(creditCheck(5541808923795240))