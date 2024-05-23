document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    // Function to show error messages
    function showError(errorElement, errorMessage) {
        const error = document.querySelector("." + errorElement);
        error.classList.add("display-error");
        error.innerHTML = errorMessage;
    }

    // Function to clear error messages
    function clearError() {
        const errors = document.querySelectorAll(".error");
        errors.forEach(error => {
            error.innerHTML = "";
            error.classList.remove("display-error");
        });
    }

    // Function to handle form submission
    function handleSubmit(event) {
        clearError(); // Clear previous errors before validation

        const taskid = document.getElementById("taskid");
        const tasktitle = document.getElementById("tasktitle");
        const teachername = document.getElementById("teachername");
        const description = document.getElementById("description");
        const createdby = document.getElementById("createdby");

        let isValid = true;

        if (taskid.value === "") {
            showError("Taskid-error", "Invalid Task id, it cannot be empty.");
            isValid = false;
        } else if (taskid.value.length > 10) {
            showError("Taskid-error", "Invalid Task id, it cannot be greater than 10 characters.");
            isValid = false;
        }

        if (tasktitle.value === "") {
            showError("title-error", "Invalid Task Title, it cannot be empty.");
            isValid = false;
        } else if (tasktitle.value.length > 55) {
            showError("title-error", "Invalid Task Title, it cannot be greater than 55 characters.");
            isValid = false;
        }

        if (teachername.value === "") {
            showError("TName-error", "Invalid Teacher Name, it cannot be empty.");
            isValid = false;
        } else if (teachername.value.length > 55) {
            showError("TName-error", "Invalid, it cannot be greater than 55 characters.");
            isValid = false;
        }

        if (description.value.length > 160) {
            showError("des-error", "Invalid Description, it cannot be greater than 160 characters.");
            isValid = false;
        }

        if (createdby.value === "") {
            showError("admin-error", "Invalid admin name, it cannot be empty.");
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    }

    // Attach event listener to form submission
    form.addEventListener("submit", handleSubmit);
});
