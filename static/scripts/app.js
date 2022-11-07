
// Get the current year digits
const d = new Date();
document.getElementById("current-year").innerHTML = d.getFullYear();


let defaultOption = document.querySelector('.defaultOption');
let UnorderedList = document.querySelector('.ul');

defaultOption.onclick = function(){
    UnorderedList.classList.toggle('active');
}
function selectOption(listItem){
    let value = listItem.innerHTML;
    defaultOption.innerHTML= value;
    UnorderedList.classList.toggle('active');
}