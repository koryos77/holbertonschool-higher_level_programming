document.addEventListener('DOMContentLoaded', function() {
	const titleDiv = document.getElementById('list_movies');

	fetch('https://swapi-api.hbtn.io/api/films/?format=json')
		.then((response) => {
			if(!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		})
		.then((data) => {
			titleDiv.textContent = data.name;
		})
		.catch((error) => {
			console.error('Error fetching title:', error);
			titleDiv.textContent = 'Error loading title';
		});
});
