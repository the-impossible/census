// Get Dom Element for filtering
const ajaxInput = document.getElementById('ajaxInput')
const noResult = document.getElementById('noResult')
const hideDataTable = document.getElementById('hideDataTable')
const postInput = document.getElementById('postInput')
const catOptions = document.getElementById('catOptions')
const requestOutput = document.getElementById('requestOutput')

// Get Dom Element for mailing
const invite = document.getElementsByClassName('invite')
const form_user_id = document.getElementsByClassName('user_id')
const mail = document.getElementById('mail')
const form_date = document.getElementById('date')
const form_time = document.getElementById('time')
const errorMessage = document.getElementById('errorMessage')
const errorStatus = document.getElementById('errorStatus')
// const form_job_id = document.getElementById('job_id')

// Add eventListener to catOptions
catOptions.addEventListener('change', (e) =>{
    console.log('e', e.target.value)
    fetch('',{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'category':e.target.value})
    })
    .then((res) => res.json())
    .then((data) => {
        if(data.length > 0) {
            ajaxInput.innerHTML += ''
            postInput.style.display = 'none'
            noResult.style.display = 'none'
            hideDataTable.style.display = 'block'
            requestOutput.style.display = 'block'
            var result =''
            data.forEach((element, id) => {
                result += `<tr>
                                <th scope="row">${id+1}</th>
                                <td><a href="/admin_user_details/${element.user__id} ">${element.user__fullname}</a></td>
                                <td>${element.job_types}</td>
                                <td><button class="btn btn-primary invite" data-toggle="modal" data-target="#exampleModal"><i class="fa fa-envelope"> <span class="user_id" style="display: none;">${element.user__id}</span> </i> Invite</button></td>
                            </tr>`
            }) 
            ajaxInput.innerHTML = result                   
        }
        else{
            hideDataTable.style.display = 'none'
            requestOutput.style.display = 'none'
            noResult.style.display = 'block'
        }
    })
})

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
        mail.onclick = function () {
            console.log('making request')
            let date = form_date.value
            let time = form_time.value
            let name = catOptions.value
            let user_id = form_user_id[i].innerHTML
            if(form_date.value == ''){
                errorMessenger('Schedule date is empty', false)
            }else if(form_time.value == ''){
                errorMessenger('Schedule Time is empty', false)
            }else {
                console.log('fetching')
                fetch('/admin_make_quick_invitation',{
                    method: 'POST',
                    headers: {
                        'Content-Type':'application/json',
                        'X-CSRFToken': csrftoken,
                    },
                    body: JSON.stringify({'date':date, 'time':time, 'user_id':user_id, 'name':name})
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
        }
    })
}