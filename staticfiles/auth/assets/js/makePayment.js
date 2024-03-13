const makePayment = document.getElementById('makePayment1')

// Send the payment and user details to the backend for final processing
function submitFormData(){

    var paymentDetails = {
        'paymentReference': Reference,
        'transactionReference': transactionR,
        'amount':amount
    }

    let url = '/process-payment/    '

    fetch(url, {
        method: 'POST',
        headers: {
            'content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'paymentDetails':paymentDetails})
    })
    .then((res) => res.json())
    .then((data) => {})
}

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

// Monnify payment SDK
function payWithMonnify() {
    var reference = 'Jobbot' + Math.floor((Math.random() * 1000000000) + 1)
    preProcessing(reference, amount)

    MonnifySDK.initialize({
        amount: amount,
        currency: "NGN",
        reference: reference,
        customerName: fullname,
        customerEmail: email,
        customerMobileNumber: phonenumber,
        apiKey: "MK_PROD_8ZAKFMZ5U4",
        contractCode: "139732582192",
        paymentDescription: "Subscribing to Jobbot Services",
        isTestMode: false,
        paymentMethods: ["CARD", "ACCOUNT_TRANSFER"],
        
        onComplete: function(response){
            //Implement what happens when transaction is completed.
            Reference = response['paymentReference']
            transactionR = response['transactionReference']

            // get access token
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
            })

            url = 'https://api.monnify.com/api/v1/transactions/query?paymentReference='+Reference
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
                if (data['requestSuccessful']){
                    if (data['responseBody']['paymentStatus'] == 'PAID') {
                        message = 'Transaction Successful   '
                        success = true
                        errorMessenger(message, success)
                        submitFormData()
                        window.location.href = domain+"/user-edit/"+user_id
                    }else{
                        message = 'Transaction Failed Do Try Again'
                        success = false
                        errorMessenger(message, success)
                    }
                }else{
                    message = 'Transaction Cancelled by the user, Do Try Again!'
                    success = false
                    errorMessenger(message, success)
                }
                console.clear()                
            })
        },
        onClose: function(data){
            //Implement what should happen when the modal is closed here
            console.clear()
        }
        
    });
}

function preProcessing(paymentReference, amount){

    let url = '/pre-process-payment/'

    fetch(url, {
        method: 'POST',
        headers: {
            'content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'paymentReference':paymentReference, 'amount':amount})
    })
    .then((res) => res.json())
    .then((data) => {})
}

makePayment.addEventListener('click', (e) =>{
    e.preventDefault()
    payWithMonnify()

})

