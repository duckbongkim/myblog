// console.log(1);
// setTimeout(delayPrint, 1000);
// console.log(3);

// function delayPrint(){
//     console.log(2)
// }


const myPromise = new Promise((resolve, reject)=> {

    const condition = true;
    if (condition) {
        resolve('성공');
    } else {
        reject('실패');
    }

});

myPromise.then(res => {
    console.log(res)
}).catch(err=>{
    console.error(err)
})