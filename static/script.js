// Select the chat form, input, and output elements
const chatForm = document.querySelector('#chat-form');
const chatInput = document.querySelector('#chat-input');
const chatOutput = document.querySelector('#chat-output');

// Function to add a message to the chat output
function addMessage(message, className) {
    // Create a new message element
    const messageElement = document.createElement('div');
    // Add the specified class name to the message element
    messageElement.classList.add('chat-message', className);
    // Set the inner HTML of the message element
    messageElement.innerHTML = `<p>${message}</p>`;
    // Append the message element to the chat output
    chatOutput.appendChild(messageElement);
    // Scroll the chat output to the bottom
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

// Function to send a message to the server and display the response
async function sendMessage(message) {
    // Add the user's message to the chat output
    addMessage(message, 'user-message');
    // Send the message to the server
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    });
    // Parse the response as JSON
    const data = await response.json();
    // Add the bot's response to the chat output
    addMessage(data.response, 'bot-message');
}

// Function to initiate a conversation with the server
async function initiateConversation() {
    // Send a request to initiate a conversation
    const response = await fetch('/initiate_conversation');
    // Parse the response as JSON
    const data = await response.json();
    // Add the bot's initial message to the chat output
    addMessage(data.response, 'bot-message');
}

// Add an event listener for form submission
chatForm.addEventListener('submit', event => {
    // Prevent the default form submission behavior
    event.preventDefault();
    // Get the value of the chat input field
    const message = chatInput.value;
    // Check if the message is not empty
    if (message.trim() !== '') {
        // Send the message to the server
        sendMessage(message);
        // Clear the chat input field
        chatInput.value = '';
    }
});

// Add an event listener for page load
window.addEventListener('load', () => {
    // Initiate a conversation with the server
    initiateConversation();
});
