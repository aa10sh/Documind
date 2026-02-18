// Change this when deploying to AWS
const BASE_URL = "http://127.0.0.1:8000/api";


// Upload Document
async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const status = document.getElementById("uploadStatus");

    if (!fileInput.files.length) {
        status.innerText = "Please select a file.";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        status.innerText = "Uploading...";

        const response = await fetch(`${BASE_URL}/upload`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        status.innerText = "✅ " + data.message;

    } catch (error) {
        status.innerText = "❌ Upload failed.";
        console.error(error);
    }
}



// Chat With Document
async function askQuestion() {
    const input = document.getElementById("questionInput");
    const chatBox = document.getElementById("chatBox");

    const question = input.value.trim();

    if (!question) return;

    // Show user message
    chatBox.innerHTML += `<p><b>You:</b> ${question}</p>`;

    input.value = "";

    try {
        const response = await fetch(`${BASE_URL}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        chatBox.innerHTML += `<p><b>AI:</b> ${data.answer}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<p style="color:red;"><b>Error:</b> Could not get response</p>`;
        console.error(error);
    }
}
