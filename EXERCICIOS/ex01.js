let n1 = 1
let n2 = 34

function sum(a, b) {
    
    if (a < 10) {
        sum(12, n2)
        return
    }
    let res = a + b
    console.log(res)
}

sum(n1, n2)