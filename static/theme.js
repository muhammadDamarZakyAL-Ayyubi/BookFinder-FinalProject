const btn = document.getElementById("toggle-theme");
const body = document.body;

btn.addEventListener("click", () => {
    body.classList.toggle("light");
    body.classList.toggle("dark");

    btn.textContent = body.classList.contains("light") ? "☀️" : "🌙";
});
