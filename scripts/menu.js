document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const navLinks = document.getElementById("nav-links");
    const bars = document.querySelectorAll(".menu-icon .bar");

    // Toggle the navigation menu and animate the hamburger icon
    menuIcon.addEventListener("click", function () {
        const isActive = navLinks.classList.toggle("active");

        // Update ARIA attribute for accessibility
        menuIcon.setAttribute("aria-expanded", isActive);

        // Animate the hamburger icon
        if (isActive) {
            // Transform into an "X"
            bars[0].style.transform = "rotate(45deg) translate(5px, 5px)";
            bars[1].style.opacity = "0";
            bars[2].style.transform = "rotate(-45deg) translate(5px, -5px)";
        } else {
            // Revert to hamburger icon
            bars[0].style.transform = "rotate(0) translate(0, 0)";
            bars[1].style.opacity = "1";
            bars[2].style.transform = "rotate(0) translate(0, 0)";
        }
    });

    // Close the navigation menu when clicking outside
    document.addEventListener("click", function (event) {
        const isClickInsideMenu = navLinks.contains(event.target);
        const isClickOnMenuIcon = menuIcon.contains(event.target);

        if (!isClickInsideMenu && !isClickOnMenuIcon) {
            navLinks.classList.remove("active");
            menuIcon.setAttribute("aria-expanded", "false");

            // Revert the hamburger icon
            bars[0].style.transform = "rotate(0) translate(0, 0)";
            bars[1].style.opacity = "1";
            bars[2].style.transform = "rotate(0) translate(0, 0)";
        }
    });

    // Close the menu when a link is clicked (optional)
    navLinks.addEventListener("click", function (event) {
        if (event.target.tagName === "A") {
            navLinks.classList.remove("active");
            menuIcon.setAttribute("aria-expanded", "false");

            // Revert the hamburger icon
            bars[0].style.transform = "rotate(0) translate(0, 0)";
            bars[1].style.opacity = "1";
            bars[2].style.transform = "rotate(0) translate(0, 0)";
        }
    });
});