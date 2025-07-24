function checkStatus() {
    fetch('/check')
        .then(response => response.json())
        .then(data => {
            const statusDiv = document.getElementById('status');
            if (data.status === "Intruder") {
                statusDiv.textContent = "⚠️ Intruder Detected!";
                statusDiv.style.color = "red";
            } else {
                statusDiv.textContent = "✅ Safe";
                statusDiv.style.color = "lime";
            }
        });
}

setInterval(checkStatus, 3000);