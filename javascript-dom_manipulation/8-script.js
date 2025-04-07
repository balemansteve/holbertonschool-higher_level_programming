document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#hello').textContent = data.hello;
        });
});
