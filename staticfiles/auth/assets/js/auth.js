const emailField = document.getElementById('id_email')
const emailFieldFeedback = document.getElementById('emailFieldFeedback')

const passwordField = document.getElementById('id_password')
const passwordFieldFeedback = document.getElementById('passwordFieldFeedback')

const NumberField = document.getElementById('id_phoneNumber')
const NumberFieldFeedback = document.getElementById('NumberFieldFeedback')

const fullNameField = document.getElementById('id_fullname')
const fullNameFieldFeedback = document.getElementById('fullnameFieldFeedback')

const usernameField = document.getElementById('id_username')
const usernameFieldFeedback = document.getElementById('usernameFieldFeedback')

const tooglePassword = document.getElementById('tooglePassword')

const form = document.getElementById('form') 
const btnSubmit = document.getElementById('btnSubmit')

const condition = document.getElementById('condition') 

btnSubmit.disabled = true
condition.addEventListener('click', (e) => {
    if (condition.checked == true){
        btnSubmit.type = "submit";
        btnSubmit.disabled = false
    }else{
        btnSubmit.disabled = true
    }
})

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
                
            }else{
                emailField.classList.remove('is-invalid')
                emailField.classList.add('is-valid')
            }
        })
    }
})

usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value

    if(usernameVal.length > 0) {
        if (usernameVal.length < 4 ) {
            usernameField.classList.add('is-invalid')
            usernameFieldFeedback.innerHTML = 'Seem wrong'
        }else{

            fetch('/validate-username',{
                body: JSON.stringify({username:usernameVal}),
                method: 'POST',
                headers: {
                    'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                if (data.username_error) {
                    usernameField.classList.add('is-invalid')
                    usernameFieldFeedback.innerHTML = data['username_error']
                    
                }else{
                    usernameField.classList.remove('is-invalid')
                    usernameField.classList.add('is-valid')
                }
            })
        }  
    }
})

NumberField.addEventListener('keyup', (e) => {
    const phoneVal = e.target.value

    if(phoneVal.length > 0) {

        fetch('/validate-number',{
            body: JSON.stringify({phone:phoneVal}),
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            },
        })
        .then((res) => res.json())
        .then((data) => {
            
            if (data.number_error) {
                NumberField.classList.add('is-invalid')
                NumberFieldFeedback.innerHTML = data['number_error']
                
            }else {
                NumberField.classList.remove('is-invalid')
                NumberField.classList.add('is-valid')
            }
        })
    }
})

fullNameField.addEventListener('keyup', (e) => {
    fullNameVal = e.target.value

    if (fullNameVal.length < 4 ) {
        fullNameField.classList.add('is-invalid')
        fullNameFieldFeedback.innerHTML = 'Seem wrong'

    }else {
        fullNameField.classList.remove('is-invalid')
        fullNameField.classList.add('is-valid')

    }

})

tooglePassword.addEventListener('click', (e) => {
    if (tooglePassword.className == 'fa fa-eye-slash') {
        tooglePassword.classList.remove('fa-eye-slash')
        passwordField.setAttribute('type', 'text')
        tooglePassword.classList.add('fa-eye')
    }else{
        tooglePassword.classList.remove('fa-eye')
        passwordField.setAttribute('type', 'password')
        tooglePassword.classList.add('fa-eye-slash')
    }
})

passwordField.addEventListener('keyup', (e) => {
    passwordVal = e.target.value

    if (passwordVal.length < 6) {
        passwordField.classList.add('is-invalid')
        passwordFieldFeedback.innerHTML = 'Password should be at least 6 characters'
    }else {
        passwordField.classList.remove('is-invalid')
        passwordField.classList.add('is-valid')

    }
})

btnSubmit.addEventListener('click', (e) => {
    if (passwordField.value != '' && fullNameField.value != '' && NumberField.value != '' && emailField.value !='' && usernameField.value !=''){
        form.submit()
    }else{
        if (passwordField.value == ''){
            passwordField.classList.add('is-invalid')
        }else{
            passwordField.classList.remove('is-invalid')
            passwordField.classList.add('is-valid')
        }
    
        if (fullNameField.value == ''){
            fullNameField.classList.add('is-invalid')
        }else{
            fullNameField.classList.remove('is-invalid')
            fullNameField.classList.add('is-valid')
        }
    
        if (NumberField.value == ''){
            NumberField.classList.add('is-invalid')
        }else{
            NumberField.classList.remove('is-invalid')
            NumberField.classList.add('is-valid')
        }
    
        if (usernameField.value == ''){
            usernameField.classList.add('is-invalid')
        }else{
            usernameField.classList.remove('is-invalid')
            usernameField.classList.add('is-valid')
        }
    
        if (emailField.value == ''){
            emailField.classList.add('is-invalid')
        }else{
            emailField.classList.remove('is-invalid')
            emailField.classList.add('is-valid')
        }
    }
})