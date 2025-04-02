document.addEventListener('DOMContentLoaded', function() {
  const addItemDiv = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');

  addItemDiv.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});
