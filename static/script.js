function fetchHaiku() {
    fetch('/haiku')
        .then(response => response.json())
        .then(data => {
            document.getElementById('haiku').textContent = data.haiku;
        })
        .catch(err => {
            console.error(err);
            alert('Error fetching haiku.');
        });
}
