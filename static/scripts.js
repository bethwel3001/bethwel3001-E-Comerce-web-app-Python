// Toggle between light/dark mode
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const themeIcon = document.querySelector('.theme-toggler');
    themeIcon.textContent = body.classList.contains('dark-mode') ? '🌞' : '🌙';
  }
  
  // Toggle Login/Sign-up form visibility
  function toggleLoginForm() {
    const form = document.getElementById('login-form');
    form.style.display = form.style.display === 'flex' ? 'none' : 'flex';
  }
  