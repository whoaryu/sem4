const myform = document.querySelector('#my-form')
const nameInput = document.querySelector('#name')
const emailInput = document.querySelector('#email')
const msg = document.querySelector('.msg')
const userList = document.querySelector('#users')

myform.addEventListener('submit',onsubmit);

function onsubmit(e){
    e.preventDefault();

    if(nameInput.value=='' || emailInput.value=='')
        {
            msg.classList.add('error')
            msg.innerHTML = "Please enter all"

        }
    else{
        console.log(`name ${nameInput.value} email ${emailInput.value}`)
        const li = document.createElement('li')
        li.appendChild(document.createTextNode(`name ${nameInput.value} email ${emailInput.value}`))

        userList.appendChild(li);
        nameInput.value=''
        emailInput.value=''
    }
}
