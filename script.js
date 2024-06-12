document.getElementById('progress-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const date = document.getElementById('date').value;
    const notes = document.getElementById('notes').value;

    if (date && notes) {
        const log = document.getElementById('log');
        const logEntry = document.createElement('li');
        logEntry.textContent = `${date}: ${notes}`;
        log.appendChild(logEntry);

        document.getElementById('progress-form').reset();
    } else {
        alert('Please fill in both fields.');
    }
});
