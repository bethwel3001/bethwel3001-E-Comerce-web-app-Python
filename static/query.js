// Get the elements
const hamburgerMenu = document.getElementById('hamburger-menu');
const navLinks = document.querySelector('.nav-links');
const closeMenu = document.getElementById('close-menu');

// Open the navbar when hamburger menu is clicked
hamburgerMenu.addEventListener('click', () => {
  navLinks.classList.add('open');  // Add 'open' class to show the menu
  closeMenu.style.display = 'block'; // Show the close button (X)
});

// Close the navbar when the 'X' button is clicked
closeMenu.addEventListener('click', () => {
  navLinks.classList.remove('open');  // Remove 'open' class to hide the menu
  closeMenu.style.display = 'none';   // Hide the close button (X)
});
