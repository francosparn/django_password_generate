// Variables
let refresh = document.querySelector('#refresh')
let copy = document.querySelector('#copy')
let password = document.querySelector('#password')

// Events
refresh.addEventListener('click', refreshPassword)
copy.addEventListener('click', copyPassword)

// Functions
function refreshPassword(e){
    e.preventDefault()
    location.reload()
}

function copyPassword(e){
    e.preventDefault()
    password.select()
    document.execCommand('copy')
}
