let currentUser = "Vous";

function sendMessage() {
    const input = document.getElementById('message-input');
    const content = input.value.trim();
    
    if (!content) return;

    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            author: currentUser,
            content: content
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            addMessageToUI(data.message);
            input.value = '';
        }
    });
}

function addMessageToUI(msg) {
    const chatArea = document.getElementById('chat-area');
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message';
    msgDiv.innerHTML = `
        <strong>${msg.author}</strong> <small>${msg.time}</small><br>
        ${msg.content}
    `;
    chatArea.appendChild(msgDiv);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function switchServer(server) {
    window.location.href = `/server/${server}`;
}

function createServer() {
    const name = prompt("Nom du nouveau serveur ?");
    if (name) {
        alert(`Serveur "${name}" créé ! (simulation)`);
    }
}

// Auto scroll
window.onload = () => {
    const chatArea = document.getElementById('chat-area');
    if (chatArea) chatArea.scrollTop = chatArea.scrollHeight;
};
