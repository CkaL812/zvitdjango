document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector(".menu-button");
    const menuContainer = document.querySelector(".menu-container");

    if (menuButton && menuContainer) {
        menuButton.addEventListener("click", (e) => {
            e.preventDefault();
            menuContainer.classList.toggle("active");
        });

        // Клік поза меню — закрити
        document.addEventListener("click", (e) => {
            if (
                !menuContainer.contains(e.target) &&
                !menuButton.contains(e.target)
            ) {
                menuContainer.classList.remove("active");
            }
        });
    }
});



