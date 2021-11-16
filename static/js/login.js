const inputContainers = document.querySelectorAll(".app-input");

inputContainers.forEach((container) => {
    const input = container.querySelector("input");
    const events = ["focus", "blur"];

    events.forEach((event) => {
        input.addEventListener(event, () => {
            if (!input.value) {
                toggleClass(container, "input-active");
            }
        });
    });
});

function toggleClass(element, className) {
    const isActive = element.classList.contains(className);

    if (isActive) {
        element.classList.remove(className);
    } else {
        element.classList.add(className);
    }
}

$(".toggle-password").click(function() {
    $(this).toggleClass("fa-eye-slash");
    input = $(this).parent().find("input");
    if (input.attr("type") == "password") {
        input.attr("type", "text");
    } else {
        input.attr("type", "password");
    }
});

const submitButton = document.querySelector('.app-login-button');
submitButton.disabled = true
function isEmpty() {
    let username = document.getElementById('id_username').value;
    let password = document.getElementById('id_password').value;

    if (username.length > 7 && password.length > 7) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }
}