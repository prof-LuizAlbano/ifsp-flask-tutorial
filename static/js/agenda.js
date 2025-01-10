// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to all elements with the delete class
    document.querySelectorAll('.delete-item').forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            
            // Get the href from the link
            const deleteUrl = this.getAttribute('href');            
            const confirmed = confirm('Tem certeza que deseja excluir este item?');
            
            // If user confirms, proceed with deletion
            if (confirmed) {
                window.location.href = deleteUrl;
            }
        });
    });
});