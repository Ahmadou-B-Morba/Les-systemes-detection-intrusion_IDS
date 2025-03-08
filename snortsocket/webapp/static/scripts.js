document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch alerts from the Flask API endpoint
    function fetchAlerts() {
        fetch('/alerts')
            .then(response => response.json())
            .then(data => {
                const alertList = document.getElementById('alert-list');
                alertList.innerHTML = ''; // Clear existing alerts

                data.forEach(alert => {
                    const listItem = document.createElement('li');
                    listItem.textContent = alert;
                    listItem.classList.add('alert');
                    alertList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching alerts:', error));
    }

    // Fetch alerts initially and then every 5 seconds
    fetchAlerts();
    setInterval(fetchAlerts, 5000);
});
