function miniMaxSum(arr) {
    let totalSum = arr.reduce((acc, curr) => acc + curr, 0);
    let minNum = Math.min(...arr);
    let maxNum = Math.max(...arr);
    
    let minSum = totalSum - maxNum;
    let maxSum = totalSum - minNum;
    
    console.log(minSum + " " + maxSum);
}
const input = "1 2 3 4 5";
const arr = input.split(" ").map(Number);


miniMaxSum(arr);