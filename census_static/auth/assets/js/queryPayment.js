// get reQuery DOM element
const reQuery = document.getElementsByClassName('reQuery')
const spin = document.getElementsByClassName('spin')
const paymentID = document.getElementsByClassName('paymentID')
const color = document.getElementsByClassName('color')
const errorMessage = document.getElementById('errorMessage')

// Error messenger
// function for displaying payment error
function errorMessenger(message, success) {
    errorStatus.innerHTML = message
    if (success == true) {
        errorMessage.classList.remove('alert-danger')
        errorMessage.classList.add('alert-success')
    }else{
        errorMessage.classList.remove('alert-success')
        errorMessage.classList.add('alert-danger')
    }

    errorMessage.style.display = 'block'
    setTimeout(function(){
        errorMessage.style.display = 'none'
    }, 10000);
}

for(let i = 0; i < reQuery.length; i++){
	reQuery[i].addEventListener('click', (e) => {
		spin[i].classList.add('fa-spinner')
		let token
		fetch('https://api.monnify.com/api/v1/auth/login/', {
			method: 'POST',
			headers:{
					'Content-Type':'application/json',
					'Authorization':'Basic TUtfUFJPRF84WkFLRk1aNVU0OjVCWlVLODdGWU5HVzdGUUpORkI0VTNNV1ZOWTdETkpF'
			},
		})
		.then((res) => res.json())
		.then((data) => {
			token = data.responseBody.accessToken
			var paymentR = paymentID[i].innerHTML
			var index = i
			console.log(index)
			console.log(token)
			console.log(paymentR)
			queryPayment(token,  paymentR, index)            
		})

	})
}

function queryPayment (token, paymentR, index) {
     // Query monnify for payment
     let url = 'https://api.monnify.com/api/v1/transactions/query?paymentReference='+paymentR

     fetch(url, {
			method: 'GET',
			credentials: 'same-origin',
			mode: 'cors', 
			headers:{
				'Content-Type':'application/json',
				'Authorization':'Bearer' + token,
			},
     })
     .then((res) => res.json())
     .then((data) => {
        spin[index].classList.remove('fa-spinner')
        if (data['responseCode'] == '99'){
            color[index].innerHTML = 'failed'

            let url = '/update-payment/'

            fetch(url, {
                method: 'POST',
                headers: {
                    'content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
        
            body: JSON.stringify({'paymentReference':paymentID[index].innerHTML, 'amount':amount, 'status':'failed'})
        })
        .then((res) => res.json())
        .then((data) => {})
        var message = `Transaction Failed`
        var success = false
        errorMessenger(message, success)

         }else{
             var transaction_id = data['responseBody']['transactionReference']
             var status = data['responseBody']['paymentStatus'].toLowerCase()
             let url = '/update-payment/'
             fetch(url, {
                 method: 'POST',
                 headers: {
                     'content-Type': 'application/json',
                     'X-CSRFToken': csrftoken
                 },
                 body: JSON.stringify({'paymentReference':paymentID[index].innerHTML, 'amount':amount, 'transaction_id':transaction_id, 'status':status})
             })
             .then((res) => res.json())
             .then((data) => {})

             if (status == 'PAID'){
								color[index].classList.replace('bg-light-danger', 'bg-light-success')
								color[index].innerHTML = status
								var message = 'Transaction Confirmed!'
								var success = true
								errorMessenger(message, success)                    
 
             }else{
								color[index].innerHTML = status
								var message = `Transaction ${status}`
								var success = false
								errorMessenger(message, success)
             }
         }
     })
}