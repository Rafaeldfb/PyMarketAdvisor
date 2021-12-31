
function settings() {
    
    var select = document.getElementById('selectUpdate');
    var nameBlock = document.getElementById('nameBlock');
    var pwdBlock = document.getElementById('pwdBlock');
    var btn = document.getElementById('updateBtn');

    if (select.value == 'changeName') {
        nameBlock.classList.remove('d-none');
        nameBlock.classList.add('d-block');

        if (pwdBlock.classList.contains('d-block')) {
            pwdBlock.classList.remove('d-block');
            pwdBlock.classList.add('d-none');
        };

        btn.removeAttribute('disabled');
    } else if (select.value == 'changePwd') {
        pwdBlock.classList.remove('d-none');
        pwdBlock.classList.add('d-block');

        if (nameBlock.classList.contains('d-block')) {
            nameBlock.classList.remove('d-block');
            nameBlock.classList.add('d-none');
        };

        btn.removeAttribute('disabled');
    };
};