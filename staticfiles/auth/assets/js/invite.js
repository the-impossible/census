const invite = document.getElementsByClassName('invite')
const form_user_id = document.getElementsByClassName('user_id')
const mail = document.getElementById('mail')
const form_date = document.getElementById('date')
const form_time = document.getElementById('time')
const errorMessage = document.getElementById('errorMessage')
const errorStatus = document.getElementById('errorStatus')
const form_job_id = document.getElementById('job_id')

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

for(let i = 0; i < invite.length; i++){
    invite[i].addEventListener('click', (e) => {
        console.log('i was click', i)
        mail.onclick = function () {
            console.log('making request')
            let date = form_date.value
            let time = form_time.value
            let job_id = form_job_id.value
            let user_id = form_user_id[i].innerHTML

            fetch('/admin_make_invitation',{
                method: 'POST',
                headers: {
                    'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({'date':date, 'time':time, 'user_id':user_id, 'id':job_id})
            })
            .then((res) => res.json())
            .then((data) => {
                console.log(data)
                if (data['True']){
                    message = data['message']
                    success = true
                    errorMessenger(message, success)
                }else{
                    message = data['message']
                    success = false
                    errorMessenger(message, success)
                }
            })
        }
    })
}