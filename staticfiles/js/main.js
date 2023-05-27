const theme = {
    'light-theme': 'dark-theme',
    'dark-theme': 'light-theme'
}
window.onload = function() {
    let themeData = JSON.parse(localStorage.getItem('themeData'))
    if(!themeData) {
        return;
    }
    else {
       changeTheme(themeData.contentContainerId) 
    }
};
const changeLanguage = (context) => {
    context.language = document.getElementById('slider-language').checked ? 'pl' : 'en'
    context.submit()
}
const changeTheme = (contentContainerId) => {
    const data = {};
    const darkModeCheckbox = document.getElementById('slider');
    let contentContainer;

    if(contentContainerId) {
        contentContainer = document.getElementById(contentContainerId);
        if(contentContainer) return;
        contentContainer = document.getElementById(theme[contentContainerId]);
        contentContainer.id = contentContainerId;
        contentContainerId === 'dark-theme' ? darkModeCheckbox.checked = true : darkModeCheckbox.checked = false;
        return;
    }
    if(darkModeCheckbox.checked) {
        contentContainer = document.getElementById('light-theme');
        data.contentContainerId = contentContainer.id = 'dark-theme'
    }
    else {
        contentContainer = document.getElementById('dark-theme');
        data.contentContainerId = contentContainer.id = 'light-theme'
    }
    localStorage.setItem('themeData', JSON.stringify(data))
}