async function sendMessage() {
    const message = document.getElementById('message').value;
    if (!message) return alert("Ingresa un mensaje");

    await fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({text: message})
    });

    document.getElementById('message').value = '';
}