// Get the markAsDoneBtn and add event listener
document.getElementById('markAsNotDoneBtn').addEventListener('click', function() {
    // Get the task ID from the data attribute
    const taskId = this.getAttribute('data-task-id');
    
    // Make the fetch request with the correct URL
    fetch(`/task/${taskId}/mark_as_not_done/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',  // Ensure CSRF token is included for security
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Task marked as Not done');
            window.history.back();
        } else {
            alert('Failed to update task status');
        }
    });
});

document.getElementById('cancelBtn').addEventListener('click', function() {
    window.history.back();
});
