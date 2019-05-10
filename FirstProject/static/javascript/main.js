var profile_data = document.getElementsByClassName('profile-container')[0];
var profile_popup = document.getElementsByClassName('profile-popup')[0];
var links = profile_popup.children;
function Click_Handler() {
    if (profile_popup.classList.contains('hidden')){
        profile_popup.classList.remove('hidden');
        Animation.Animate(links,1500,200)
    } else {
        profile_popup.classList.add('hidden');
        Animation.StopAnimation()
    }
}
profile_data.addEventListener('click', Click_Handler);

