const emailField = document.getElementById('id_email')
const emailFieldFeedback = document.getElementById('emailFieldFeedback')

const passwordField = document.getElementById('id_password')
const passwordFieldFeedback = document.getElementById('passwordFieldFeedback')

const usernameField = document.getElementById('id_username')
const usernameFieldFeedback = document.getElementById('usernameFieldFeedback')

const tooglePassword = document.getElementById('tooglePassword')

const form = document.getElementById('form')
const btnSubmit = document.getElementById('btnSubmit')


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
        if (usernameVal.length < 10 || usernameVal.length > 10 ) {
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
    e.preventDefault();
    if (passwordField.value == '' && emailField.value =='' && usernameField.value ==''){
        emailField.classList.add('is-invalid')
        passwordField.classList.add('is-invalid')
        usernameField.classList.add('is-invalid')
    }else if (passwordField.className == 'form-control mb-2 is-invalid'){
        passwordField.classList.add('is-invalid')
    }else if (emailField.className == 'form-control mb-2 is-invalid') {
        emailField.classList.add('is-invalid')
    }else if (usernameField.className == 'form-control mb-2 is-invalid') {
        usernameField.classList.add('is-invalid')
    }else {
        form.submit()
    }
})