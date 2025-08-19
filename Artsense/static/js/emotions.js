

// Wait 5 seconds, then show input field
setTimeout(() => {
    document.getElementById('inputSection').style.display = 'block';
    document.getElementById('emotionInput').focus();
}, 5000);

// Handle submit
document.getElementById('submitBtn').addEventListener('click', function () {
    const input = document.getElementById('emotionInput');
    const word = input.value.trim();

    if (!word) {
        alert("Please enter a word.");
        return;
    }

    // Hide input
    document.getElementById('inputSection').style.display = 'none';

    // Show success
    document.getElementById('confirmation').style.display = 'block';

    // Show Next and Statics buttons
    document.getElementById('actionButtons').style.display = 'block';
});