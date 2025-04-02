document.addEventListener('DOMContentLoaded', function() {
  const characterDiv = document.getElementById('character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => {
      if(!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then((data) => {
      characterDiv.textContent = data.name;
    })
    .catch((error) => {
      console.error('Error fetching character:', error);
      characterDiv.textContent = 'Error loading character';
    });
});
