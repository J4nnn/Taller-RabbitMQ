async function fetchMessages() {
    const response = await fetch('/messages');
    const messages = await response.json();
    
    const list = document.getElementById('messages');
    list.innerHTML = '';
    messages.forEach(msg => {
        const li = document.createElement('li');
        li.textContent = `${msg.producer}: ${msg.message}`;
        list.appendChild(li);
    });
}

setInterval(fetchMessages, 3000);
