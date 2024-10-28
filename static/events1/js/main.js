// Form validation
document.addEventListener('DOMContentLoaded', function() {
    // Password validation for signup
    const signupForm = document.querySelector('form[action="/signup/"]');
    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            const password1 = document.getElementById('password1').value;
            const password2 = document.getElementById('password2').value;
            
            if (password1 !== password2) {
                e.preventDefault();
                alert("Passwords don't match!");
                return false;
            }
            
            if (password1.length < 8) {
                e.preventDefault();
                alert("Password must be at least 8 characters long!");
                return false;
            }
        });
    }

    // Search functionality with debounce
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let timeout = null;
        searchInput.addEventListener('input', function(e) {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                document.querySelector('.loader').style.display = 'block';
                this.closest('form').submit();
            }, 500);
        });
    }

    // Image preview for event creation/editing
    const imageInput = document.querySelector('input[type="file"]');
    if (imageInput) {
        imageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = document.createElement('img');
                    preview.src = e.target.result;
                    preview.style.maxWidth = '200px';
                    preview.style.marginTop = '10px';
                    
                    const container = imageInput.parentElement;
                    const oldPreview = container.querySelector('img');
                    if (oldPreview) {
                        container.removeChild(oldPreview);
                    }
                    container.appendChild(preview);
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // Confirm delete
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this event?')) {
                e.preventDefault();
            }
        });
    });

    // Date validation
    const dateInput = document.querySelector('input[type="date"]');
    if (dateInput) {
        dateInput.addEventListener('change', function(e) {
            const selectedDate = new Date(this.value);
            const today = new Date();
            
            if (selectedDate < today) {
                alert("Please select a future date!");
                this.value = '';
            }
        });
    }

    // Dynamic character count for description
    const descriptionInput = document.querySelector('textarea[name="description"]');
    if (descriptionInput) {
        const counter = document.createElement('div');
        counter.className = 'character-counter';
        descriptionInput.parentElement.appendChild(counter);

        descriptionInput.addEventListener('input', function() {
            const remaining = 1000 - this.value.length;
            counter.textContent = `${remaining} characters remaining`;
         });
    }
});

// Event Detail JavaScript
document.addEventListener("DOMContentLoaded", function() {
    const registerButton = document.getElementById("registerButton");
    const registrationForm = document.getElementById("registrationForm");
    const successModal = document.getElementById("successModal");
    const closeModal = document.querySelector(".close");

    registerButton.addEventListener("click", function() {
        registrationForm.style.display = "block";
    });

    closeModal.addEventListener("click", function() {
        successModal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target === successModal) {
            successModal.style.display = "none";
        }
    });

    const attendeeForm = document.getElementById("attendeeForm");
    attendeeForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(attendeeForm);
        fetch("/register-for-event/", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                successModal.style.display = "block";
                attendeeForm.reset();
            } else {
                alert("Registration failed. Please try again.");
            }
        })
        .catch(error => console.error(error));
    });
});