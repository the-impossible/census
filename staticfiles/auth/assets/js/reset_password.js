const emailField = document.getElementById('email')
const emailFieldFeedback = document.getElementById('emailFieldFeedback')
const btnSubmit = document.getElementById('btnRecover')

// automatically disable the submit button
btnSubmit.disabled = true

emailField.addEventListener('keyup', (e) => {
    let emailVal = e.target.value.toLowerCase()
    if (emailVal.length > 0) {
        fetch('/validate-email', {
            body: JSON.stringify({email:emailVal}),
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            }
         })
         .then((res) => res.json())
         .then((data) => {
             console.clear()
            if (data['email_error'] === 'Email already taken'){
            emailField.classList.remove('is-invalid')
            emailField.classList.add('is-valid')
            btnSubmit.disabled = false
            }else{
            btnSubmit.disabled = true
            emailField.classList.remove('is-valid')
            emailField.classList.add('is-invalid')
            emailFieldFeedback.innerHTML = 'Email does not exists'
            }
        })
    }
})

