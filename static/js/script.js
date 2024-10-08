function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    const chatOutput = document.getElementById("chat-output");

    const userBubble = document.createElement("div");
    userBubble.className = "chat-bubble user";
    userBubble.innerText = userInput;
    chatOutput.appendChild(userBubble);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
 
        const botBubble = document.createElement("div");
        botBubble.className = "chat-bubble bot";
        botBubble.innerText = data.response;
        chatOutput.appendChild(botBubble);

        chatOutput.scrollTop = chatOutput.scrollHeight;
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    document.getElementById("user-input").value = "";
}

