let form = document.getElementById("form");
let formSubmitBtn = document.getElementById("form-submit");
let formName = document.getElementById("form-name");
let formEmail = document.getElementById("form-email");
let formMessage = document.getElementById("form-message");
let resendMessage = true;

const showPassword = document.querySelector(".show-password");
if (showPassword) {
  showPassword.addEventListener("click", () => {
    const passwordInput = document.querySelector("#password-input");
    if (passwordInput.type == "password") {
      passwordInput.type = "text";
      showPassword.classList.remove("fa-eye");
      showPassword.classList.add("fa-eye-slash");
    } else {
      passwordInput.type = "password";
      showPassword.classList.remove("fa-eye-slash");
      showPassword.classList.add("fa-eye");
    }
  });
}

const formSubmitBtn = document.querySelector("#submit-form");

if (formSubmitBtn && resendMessage) {
  formSubmitBtn.addEventListener("click", (e) => {
    e.preventDefault();
    resendMessage = false;

    // Build formData object.
    let formData = new FormData();
    formData.append("name", formName.value);
    formData.append("email", formEmail.value);
    formData.append("message", formMessage.value);

    fetch("/", {
      body: formData,
      method: "post",
      credentials: "same-origin",
      headers: {
        "X-CSRFToken": csrftoken,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        function changeToF(element) {
          if (element.parentElement.classList.contains("has-success")) {
            element.parentElement.classList.remove("has-success");
            element.parentElement.classList.add("has-danger");
          } else {
            element.parentElement.classList.add("has-danger");
          }
        }
        function changeToS(element) {
          if (element.parentElement.classList.contains("has-danger")) {
            element.parentElement.classList.remove("has-danger");
            element.parentElement.classList.add("has-success");
          } else {
            element.parentElement.classList.add("has-success");
          }
        }
        function clearInputs() {
          formName.parentElement.classList.remove("has-danger");
          formEmail.parentElement.classList.remove("has-danger");
          formMessage.parentElement.classList.remove("has-danger");
          formName.parentElement.classList.remove("has-success");
          formEmail.parentElement.classList.remove("has-success");
          formMessage.parentElement.classList.remove("has-success");
          document.getElementById("name-error").innerHTML = "";
          document.getElementById("email-error").innerHTML = "";
          document.getElementById("message-error").innerHTML = "";
        }

        if (data.success) {
          formName.value = "";
          formEmail.value = "";
          formMessage.value = "";
          clearInputs();
          resendMessage = false;
          document.getElementById("modal-toggle").click();
        } else {
          resendMessage = true;
          if (data.errors.name) {
            changeToF(formName);
            document.getElementById(
              "name-error"
            ).innerHTML = `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> ${data.errors.name}</small>`;
          } else {
            changeToS(formName);
            document.getElementById("name-error").innerHTML = "";
          }

          if (data.errors.email) {
            changeToF(formEmail);
            document.getElementById(
              "email-error"
            ).innerHTML = `<small class="error-text"><i class="fa fa-exclamation-triangle"></i> ${data.errors.message}</small>`;
          } else {
            changeToS(formMessage);
            document.getElementById("message-error").innerHTML = "";
          }
        }
      });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.querySelector("#theme-toggle");

  themeToggle.addEventListener("change", function () {
    if (this.checked) {
      document.documentElement.setAttribute("data-theme", "dark");
    } else {
      document.documentElement.setAttribute("data-theme", "light");
    }
  });
});
