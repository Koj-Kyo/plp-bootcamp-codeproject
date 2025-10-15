// TeleHealth Connect - Main JavaScript

// Auto-dismiss flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideOut 0.3s';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
});

// Add slide out animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Form validation for registration
const registerForm = document.getElementById('registerForm');
if (registerForm) {
    registerForm.addEventListener('submit', function(e) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        if (password !== confirmPassword) {
            e.preventDefault();
            showAlert('Passwords do not match!', 'danger');
            return false;
        }

        if (password.length < 6) {
            e.preventDefault();
            showAlert('Password must be at least 6 characters long!', 'danger');
            return false;
        }

        return true;
    });
}

// Form validation for booking
const bookingForm = document.getElementById('bookingForm');
if (bookingForm) {
    bookingForm.addEventListener('submit', function(e) {
        const appointmentDate = document.getElementById('appointment_date').value;
        const appointmentTime = document.getElementById('appointment_time').value;

        if (!appointmentDate || !appointmentTime) {
            e.preventDefault();
            showAlert('Please select both date and time for your appointment!', 'danger');
            return false;
        }

        // Check if appointment is in the future
        const selectedDateTime = new Date(appointmentDate + 'T' + appointmentTime);
        const now = new Date();

        if (selectedDateTime <= now) {
            e.preventDefault();
            showAlert('Appointment must be scheduled for a future date and time!', 'danger');
            return false;
        }

        return true;
    });

    // Set minimum date to today
    const dateInput = document.getElementById('appointment_date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.min = today;
    }
}

// Helper function to show custom alerts
function showAlert(message, type) {
    const flashContainer = document.querySelector('.flash-messages') || createFlashContainer();

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.innerHTML = `
        <span class="alert-message">${message}</span>
        <button class="alert-close" onclick="this.parentElement.remove()">×</button>
    `;

    flashContainer.appendChild(alertDiv);

    // Auto dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.style.animation = 'slideOut 0.3s';
        setTimeout(() => {
            alertDiv.remove();
        }, 300);
    }, 5000);
}

// Create flash container if it doesn't exist
function createFlashContainer() {
    const container = document.createElement('div');
    container.className = 'flash-messages';
    document.body.appendChild(container);
    return container;
}

// Phone number formatting
const phoneInputs = document.querySelectorAll('input[type="tel"]');
phoneInputs.forEach(input => {
    input.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 0) {
            if (value.length <= 3) {
                value = `(${value}`;
            } else if (value.length <= 6) {
                value = `(${value.slice(0, 3)}) ${value.slice(3)}`;
            } else {
                value = `(${value.slice(0, 3)}) ${value.slice(3, 6)}-${value.slice(6, 10)}`;
            }
        }
        e.target.value = value;
    });
});

// Search form auto-submit on filter change (optional enhancement)
const searchForms = document.querySelectorAll('.search-form');
searchForms.forEach(form => {
    const selects = form.querySelectorAll('select');
    selects.forEach(select => {
        select.addEventListener('change', function() {
            // Optional: Auto-submit on filter change
            // Uncomment the line below if you want instant filtering
            // form.submit();
        });
    });
});

// Confirmation dialogs for destructive actions
const deleteButtons = document.querySelectorAll('.btn-danger[type="submit"]');
deleteButtons.forEach(button => {
    button.closest('form').addEventListener('submit', function(e) {
        if (!button.hasAttribute('data-confirmed')) {
            e.preventDefault();
            if (confirm('Are you sure you want to perform this action?')) {
                button.setAttribute('data-confirmed', 'true');
                this.submit();
            }
        }
    });
});

// Dynamic form field highlighting
const formControls = document.querySelectorAll('.form-control');
formControls.forEach(control => {
    control.addEventListener('focus', function() {
        this.style.borderColor = 'var(--primary-color)';
        this.style.boxShadow = '0 0 0 3px rgba(37, 99, 235, 0.1)';
    });

    control.addEventListener('blur', function() {
        this.style.borderColor = '';
        this.style.boxShadow = '';
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Loading state for forms
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn && !submitBtn.hasAttribute('data-loading')) {
            submitBtn.setAttribute('data-loading', 'true');
            submitBtn.disabled = true;
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Loading...';

            // Reset after 10 seconds as a failsafe
            setTimeout(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
                submitBtn.removeAttribute('data-loading');
            }, 10000);
        }
    });
});

// Add active class to current nav link
const currentLocation = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    if (link.getAttribute('href') === currentLocation) {
        link.style.color = 'var(--primary-color)';
        link.style.fontWeight = '600';
    }
});

// Console log for development
console.log('TeleHealth Connect - Application loaded successfully');
