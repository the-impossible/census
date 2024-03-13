// get DOM element
const old = document.getElementById('old')
const password = document.getElementById('password')
const password1 = document.getElementById('password1')
const changeP = document.getElementById('changeP')
const changeE = document.getElementById('changeE')
const FieldFeedback = document.getElementById('FieldFeedback')
const emailFieldFeedback = document.getElementById('emailFieldFeedback')

emailField.addEventListener('keyup', (e) => {
    const emailVal = e.target.value.toLowerCase()

    if(emailVal.trim().length > 0) {

        fetch('/validate-email',{
            body: JSON.stringify({email:emailVal}),
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.email_error) {
                emailField.classList.add('is-invalid')
                emailFieldFeedback.innerHTML = data['email_error']
                changeE.disabled = true
            }else{
                emailField.classList.remove('is-invalid')
                emailField.classList.add('is-valid')
                changeE.disabled = false

            }
        })
    }
})

password.addEventListener('keyup', (e) => {
    let passwordVal = e.target.value

    if(passwordVal.length < 6){
        FieldFeedback.innerHTML = 'Passwords Too short!'
        changeP.disabled = true
    }else{
        FieldFeedback.innerHTML = ''
        changeP.disabled = false
    }
    
    if((passwordVal.length > 0) && (password1.value.length > 1)){
        if(password1.value != passwordVal){
            FieldFeedback.innerHTML = 'Passwords don\'t match!'
        }
        else{
            FieldFeedback.innerHTML = ''
            changeP.disabled = false
        }
        
    }
    

} )

password1.addEventListener('keyup', (e) => {
    let password1Val = e.target.value

    if(password1Val.length < 6){
        FieldFeedback.innerHTML = 'Passwords Too short!'
        changeP.disabled = true
    }else{
        FieldFeedback.innerHTML = ''
        changeP.disabled = false
    }

    if(password1Val.length > 0){
        if(password.value != password1Val){
            FieldFeedback.innerHTML = 'Passwords don\'t match!'
        }
        else{
            FieldFeedback.innerHTML = ''
            changeP.disabled = false
        }
    }
    
    

} )