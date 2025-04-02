document.getElementById('toggle_header').addEventListener('click', function() {
  const header = document.querySelector('header');
  if (header.classList.contains('#FF0000')) {
    header.classList.remove('#FF0000');
    header.classList.add('#00FF00');
  } else {
    header.classList.remove('#00FF00');
    header.classList.add('#FF0000');
  }
});
