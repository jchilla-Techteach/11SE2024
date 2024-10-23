document.getElementById('loadContent').addEventListener('click', () => {
    document.getElementById('studyMaterials').innerHTML = `
        <h2>Study Materials</h2>
        <ul>
            <li>Mathematics</li>
            <li>Physics</li>
            <li>Chemistry</li>
        </ul>
    `;
});

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('service-worker.js')
            .then((registration) => {
                console.log('Service Worker registered with scope:', registration.scope);
            })
            .catch((error) => {
                console.error('Service Worker registration failed:', error);
            });
    });
}
