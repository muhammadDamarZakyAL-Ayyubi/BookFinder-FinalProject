// ================== THEME TOGGLE ==================
const toggleBtn = document.getElementById("themeToggle");

// Load theme from local storage
if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light");
}

// Toggle theme
toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {
        localStorage.setItem("theme", "light");
        toggleBtn.innerHTML = "🌙"; 
    } else {
        localStorage.setItem("theme", "dark");
        toggleBtn.innerHTML = "☀️";
    }
});

// Set correct icon on load
toggleBtn.innerHTML = document.body.classList.contains("light") ? "🌙" : "☀️";


// ================== SMOOTH HOVER BOOK CARDS ==================
document.querySelectorAll(".book-card").forEach(card => {
    card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.transform = `translateY(-8px) scale(1.02)`;
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "translateY(0) scale(1)";
    });
});

