// =====================================
// GPS Tracker Dashboard
// =====================================

// ---------------------
// Create map
// ---------------------
const map = L.map("map").setView([14.5995, 120.9842], 13);

L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        attribution: "&copy; OpenStreetMap contributors"
    }
).addTo(map);

// ---------------------
// Marker & Route
// ---------------------
const marker = L.marker([14.5995, 120.9842]).addTo(map);

const route = L.polyline([], {
    color: "blue",
    weight: 5
}).addTo(map);

// ---------------------
// Sidebar Elements
// ---------------------
const latitudeText = document.getElementById("latitude");
const longitudeText = document.getElementById("longitude");
const pointsText = document.getElementById("points");
const updatedText = document.getElementById("updated");
const statusText = document.getElementById("status");
const clearButton = document.getElementById("clearButton");

// ---------------------
// API Calls
// ---------------------
async function getLatestLocation() {

    const response = await fetch("/location/latest");
    return await response.json();

}

async function getAllLocations() {

    const response = await fetch("/locations");
    return await response.json();

}

async function clearHistory() {

    await fetch("/locations", {
        method: "DELETE"
    });

}

// ---------------------
// Dashboard Update
// ---------------------
async function updateDashboard() {

    try {

        const latest = await getLatestLocation();
        const locations = await getAllLocations();

        // No data
        if (!latest || latest.message) {

            latitudeText.textContent = "--";
            longitudeText.textContent = "--";
            pointsText.textContent = "0";
            updatedText.textContent = "--";
            statusText.textContent = "🟢 Waiting...";

            route.setLatLngs([]);

            return;
        }

        // Sidebar
        latitudeText.textContent = Number(latest.latitude).toFixed(6);
        longitudeText.textContent = Number(latest.longitude).toFixed(6);
        pointsText.textContent = locations.length;
        updatedText.textContent = latest.timestamp;
        statusText.textContent = "🟢 Live";

        // Marker
        marker.setLatLng([
            latest.latitude,
            latest.longitude
        ]);

        // Center map
        map.setView([
            latest.latitude,
            latest.longitude
        ]);

        // Route
        const points = locations
            .slice()
            .reverse()
            .map(location => [
                location.latitude,
                location.longitude
            ]);

        route.setLatLngs(points);

    } catch (error) {

        console.error(error);

        statusText.textContent = "🔴 Offline";

    }

}

// ---------------------
// Button
// ---------------------
clearButton.addEventListener("click", async () => {

    if (!confirm("Clear all saved locations?")) {
        return;
    }

    await clearHistory();

    marker.setLatLng([14.5995, 120.9842]);
    route.setLatLngs([]);

    updateDashboard();

});

// ---------------------
// Auto Refresh
// ---------------------
updateDashboard();

setInterval(updateDashboard, 2000);