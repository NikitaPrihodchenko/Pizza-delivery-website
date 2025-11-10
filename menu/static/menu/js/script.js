document.addEventListener("DOMContentLoaded", function() {
  const buttons = document.querySelectorAll(".category-btn");
  const cards = document.querySelectorAll(".product-card");

  buttons.forEach(btn => {
      btn.addEventListener("click", () => {
          const category = btn.getAttribute("data-category");

          buttons.forEach(b => b.classList.remove("active"));
          btn.classList.add("active");

          cards.forEach(card => {
              if (card.getAttribute("data-cat") === category || category === "all") {
                  card.style.display = "block";
              } else {
                  card.style.display = "none";
              }
          });
      });
  });
});
