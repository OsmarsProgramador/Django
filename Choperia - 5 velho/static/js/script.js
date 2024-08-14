//static/js/script.js
// Código para inicializar o select2

$(document).ready(function() {
    $('.select2').select2();
});

// Lógica de troca de tema
function setTheme(theme) {
    if (theme === 'auto') {
    localStorage.removeItem('theme');
    } else {
    localStorage.setItem('theme', theme);
    }
    applyTheme();
}

function applyTheme() {
    let theme = localStorage.getItem('theme');
    let currentThemeIcon = document.getElementById('currentThemeIcon');
    let currentThemeName = document.getElementById('currentThemeName');
    let checkLight = document.getElementById('check-light');
    let checkDark = document.getElementById('check-dark');
    let checkAuto = document.getElementById('check-auto');

    checkLight.classList.add('d-none');
    checkDark.classList.add('d-none');
    checkAuto.classList.add('d-none');

    if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
    document.getElementById('navbar').classList.add('navbar-dark', 'bg-dark');
    document.getElementById('navbar').classList.remove('navbar-light', 'bg-light');
    currentThemeIcon.className = 'fa fa-moon-o';
    currentThemeName.textContent = 'Escuro';
    checkDark.classList.remove('d-none');
    } else if (theme === 'light' || (!theme && window.matchMedia('(prefers-color-scheme: light)').matches)) {
    document.documentElement.setAttribute('data-bs-theme', 'light');
    document.getElementById('navbar').classList.add('navbar-light', 'bg-light');
    document.getElementById('navbar').classList.remove('navbar-dark', 'bg-dark');
    currentThemeIcon.className = 'fa fa-sun-o';
    currentThemeName.textContent = 'Claro';
    checkLight.classList.remove('d-none');
    } else {
    document.documentElement.setAttribute('data-bs-theme', 'light');
    document.getElementById('navbar').classList.add('navbar-light', 'bg-light');
    document.getElementById('navbar').classList.remove('navbar-dark', 'bg-dark');
    currentThemeIcon.className = 'fa fa-adjust';
    currentThemeName.textContent = 'Automático';
    checkAuto.classList.remove('d-none');
    }
}

// Aplicar tema ao carregar a página
applyTheme();
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applyTheme);

// Para o htmx, para atualizar a lista de itens sem fechar o modal





