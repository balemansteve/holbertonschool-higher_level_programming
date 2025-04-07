document.querySelector('#toggle_header').addEventListener('click', function () {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
    } else {
        header.classList.replace('green', 'red');
    }
});
