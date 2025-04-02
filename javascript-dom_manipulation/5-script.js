document.addEventListener('DOMContentLoaded', function() {
  const updateHeaderDiv = document.getElementById('update_header');
  const header = document.querySelector('header');

  updateHeaderDiv.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
  });
});
