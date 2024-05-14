document.getElementById("logQueryForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const searchParams = new URLSearchParams(formData).toString();

    fetch(`/search?${searchParams}`)
        .then(response => response.json())
        .then(data => displaySearchResults(data))
        .catch(error => console.error("Error fetching search results:", error));
});

function displaySearchResults(results) {
    const searchResultsDiv = document.getElementById("searchResults");
    searchResultsDiv.innerHTML = "";

    if (results.length === 0) {
        searchResultsDiv.textContent = "No logs found matching the criteria.";
    } else {
        results.forEach(log => {
            const logDiv = document.createElement("div");
            logDiv.classList.add("log");
            logDiv.textContent = JSON.stringify(log, null, 2);
            searchResultsDiv.appendChild(logDiv);
        });
    }
}
