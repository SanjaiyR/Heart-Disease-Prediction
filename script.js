document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input, select");

    inputs.forEach(input => {
        input.addEventListener("input", function() {
            input.style.borderColor = input.checkValidity() ? "#ccc" : "red";
        });
    });
});
