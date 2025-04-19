document.addEventListener("DOMContentLoaded", function () {
    // ------------------------------------------
    // Hamburger Menu Toggle
    // ------------------------------------------
    const menuIcon = document.getElementById("menu-icon");
    const navLinks = document.getElementById("nav-links");
    const bars = document.querySelectorAll(".menu-icon .bar");
  
    menuIcon?.addEventListener("click", function () {
      const isActive = navLinks.classList.toggle("active");
      menuIcon.setAttribute("aria-expanded", isActive);
      bars[0].style.transform = isActive ? "rotate(45deg) translate(5px, 5px)" : "rotate(0)";
      bars[1].style.opacity = isActive ? "0" : "1";
      bars[2].style.transform = isActive ? "rotate(-45deg) translate(5px, -5px)" : "rotate(0)";
    });
  
    document.addEventListener("click", function (event) {
      if (!navLinks.contains(event.target) && !menuIcon.contains(event.target)) {
        navLinks.classList.remove("active");
        menuIcon.setAttribute("aria-expanded", "false");
        bars.forEach(bar => {
          bar.style.transform = "rotate(0)";
          bar.style.opacity = "1";
        });
      }
    });
  
    navLinks?.addEventListener("click", function (event) {
      if (event.target.tagName === "A") {
        navLinks.classList.remove("active");
        menuIcon.setAttribute("aria-expanded", "false");
        bars.forEach(bar => {
          bar.style.transform = "rotate(0)";
          bar.style.opacity = "1";
        });
      }
    });
  
    // ------------------------------------------
    // Quantity Button Logic (+ / -)
    // ------------------------------------------
    document.querySelectorAll(".increase-qty").forEach(btn => {
      btn.addEventListener("click", () => {
        const input = btn.parentElement.querySelector(".item-qty");
        input.value = parseInt(input.value) + 1;
      });
    });
  
    document.querySelectorAll(".decrease-qty").forEach(btn => {
      btn.addEventListener("click", () => {
        const input = btn.parentElement.querySelector(".item-qty");
        const current = parseInt(input.value);
        if (current > 1) {
          input.value = current - 1;
        }
      });
    });
  
    // ------------------------------------------
    // AJAX Cart Add with Quantity
    // ------------------------------------------
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
          cookie = cookie.trim();
          if (cookie.startsWith(name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
    function updateCartCount(count) {
      const cartCount = document.getElementById("cart-count");
      if (cartCount) {
        cartCount.innerText = count;
      }
    }
  
    document.querySelectorAll('.add-to-cart').forEach(button => {
      button.addEventListener('click', function () {
        const menuItemId = button.dataset.id;
        const qtyInput = button.parentElement.querySelector('.item-qty');
        const quantity = parseInt(qtyInput?.value || "1");
  
        fetch('/cart/update/', {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
          },
          body: JSON.stringify({
            menu_item_id: menuItemId,
            action: 'add',
            quantity: quantity
          })
        })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              updateCartCount(data.cart_item_count);
            } else {
              console.warn("Server error:", data.error);
            }
          })
          .catch(error => {
            console.error("AJAX error:", error);
          });
      });
    });
  });
  