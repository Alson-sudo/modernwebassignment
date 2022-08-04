var nav = document.querySelector('nav');
window.addEventListener('scroll', function(){
if(window.pageYOffset >100){
    nav.classList.add('bg-dark', 'shadow');
}
else{

nav.classList.remove('bg-dark', 'shadow');

}
})
function headAche(){
    nav.classList.add('bg-dark', 'shadow');
}


//$(document).ready(function(){
//$('#toggle').click(function(){
//
//let x = $('#toggle').val()
//if(x=='show'){
//    $('nav').classList.add('bg-dark', 'shadow')
//    $(this).val('hide')
//}
//else if(x=='hide'){
//$('nav').classList.remove('bg-dark', 'shadow')
//$(this).val('show')
//}
//})
//})
