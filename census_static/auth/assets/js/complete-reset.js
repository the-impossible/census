const password = document.getElementById('password')
const password1 = document.getElementById('password1')
const btnSubmit = document.getElementById('btnSubmit')
const form = document.getElementById('form')
const passwordFieldFeedback = document.getElementById('passwordFieldFeedback')
const password1FieldFeedback = document.getElementById('password1FieldFeedback')

// automatically disable the submit button

password.addEventListener('keyup', (e) => {
    passwordVal = e.target.value

    if (passwordVal.length < 6) {
        passwordFieldFeedback.innerHTML = "password too short"
        password.classList.add('is-invalid')
    }else{
        password.classList.remove('is-invalid')
        password.classList.add('is-valid')
        passwordFieldFeedback.innerHTML = ""
    }
})

password1.addEventListener('keyup', (e) => {
    passwordVal = e.target.value

    if (passwordVal != password.value) {
        password1FieldFeedback.innerHTML = "password don't match"
        password1.classList.add('is-invalid')
    }else{
        password1.classList.remove('is-invalid')
        password1.classList.add('is-valid')
        password1FieldFeedback.innerHTML = ""
    }
})

btnSubmit.addEventListener('click', (e) => {
    e.preventDefault();
    if (password.value == '' && password1.value == ''){
        password.classList.add('is-invalid')
        password1.classList.add('is-invalid')
    }else if(password.value != password1.value) {
        passwordFieldFeedback.innerHTML = "password don't match"
    }else if(password.value.length < 6) {
        passwordFieldFeedback.innerHTML = "password too short"
    }else {
        form.submit()
    }
})