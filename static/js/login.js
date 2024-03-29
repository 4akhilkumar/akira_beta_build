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
    if (input.prop("type") == "password") {
        input.prop("type", "text");
    } else {
        input.prop("type", "password");
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

$('.app-login-button').click(function() {
    $(this).prop('disabled', true);
    $('.app-input input').prop('readonly', true);
    $('.toggle-password').remove();
    if ($('#id_password').prop('type') != 'password') {
        $('#id_password').prop('type', 'password');
    }
    $(this).html('<i class="fas fa-spinner fa-spin"></i>');
    $(this).closest('form').submit();
});