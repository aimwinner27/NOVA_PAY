async function sendPayment(){

let recipient = document.getElementById("recipient").value;
let amount = document.getElementById("amount").value;

const response = await fetch("http://127.0.0.1:8000/process-payment",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
amount: parseInt(amount),
recipient: recipient
})

});

const data = await response.json();

document.getElementById("result").innerHTML = data.message;

}