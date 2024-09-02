function showSubmenu(id) {
    var submenu = document.getElementById(id);
    submenu.style.display = "block";
}

function hideSubmenu(id) {
    setTimeout(function() {
        var submenu = document.getElementById(id);
        if (!submenu.matches(':hover')) { // olcutar al sacar el raton 
            submenu.style.display = "none";
        }
    }, 200); // retraso para desaparecer 
}
