// script.js

// Open Register Popup
document.querySelector('.btn-register').addEventListener('click', function() {
  document.getElementById('register-popup').style.display = 'flex';
});

// Open Login Popup (from Register popup)
document.getElementById('login-link').addEventListener('click', function(e) {
  e.preventDefault(); // Prevent default anchor behavior
  document.getElementById('register-popup').style.display = 'none';
  document.getElementById('login-popup').style.display = 'flex';
});

// Open Register Popup (from Login popup)
document.getElementById('register-link').addEventListener('click', function(e) {
  e.preventDefault(); // Prevent default anchor behavior
  document.getElementById('login-popup').style.display = 'none';
  document.getElementById('register-popup').style.display = 'flex';
});

// Close Register Popup
document.getElementById('close-register-popup').addEventListener('click', function() {
  document.getElementById('register-popup').style.display = 'none';
});

// Close Login Popup
document.getElementById('close-login-popup').addEventListener('click', function() {
  document.getElementById('login-popup').style.display = 'none';
});

// Close the popup if the user clicks outside of it
window.addEventListener('click', function(event) {
  if (event.target === document.getElementById('register-popup')) {
    document.getElementById('register-popup').style.display = 'none';
  }
  if (event.target === document.getElementById('login-popup')) {
    document.getElementById('login-popup').style.display = 'none';
  }
});
// Close the popup if the user clicks the "x" button