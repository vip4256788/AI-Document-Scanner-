const BASE_URL = "http://127.0.0.1:8000/api/v1";

const uploadBox = document.getElementById("uploadBox");
const fileInput = document.getElementById("fileInput");
const uploadContent = document.getElementById("uploadContent");
const loader = document.getElementById("loader");
const output = document.getElementById("output");

// Click Upload
uploadBox.addEventListener("click", () => {
    fileInput.click();
});

// Display file
function displayFile(file) {
    uploadContent.innerHTML = `
        <strong>📄 ${file.name}</strong><br>
        Size: ${(file.size / 1024).toFixed(2)} KB
    `;
}

// File Selection
fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        displayFile(fileInput.files[0]);
    }
});

// Drag Over
uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.classList.add("drag-over");
});

// Drag Leave
uploadBox.addEventListener("dragleave", () => {
    uploadBox.classList.remove("drag-over");
});

// Drop File
uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();

    uploadBox.classList.remove("drag-over");

    const files = e.dataTransfer.files;

    if (files.length > 0) {
        fileInput.files = files;
        displayFile(files[0]);
    }
});

// Loader
function showLoader(show) {
    loader.style.display = show ? "block" : "none";
}

// Scan API
async function scan() {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        showLoader(true);

        const response = await fetch(`${BASE_URL}/scan`, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        output.textContent =
            JSON.stringify(data, null, 2);

    } catch (error) {
        output.textContent =
            `❌ Error: ${error.message}`;
    } finally {
        showLoader(false);
    }
}

// Analyze API
async function analyze() {
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const prompt =
        document.getElementById("prompt").value.trim();

    const formData = new FormData();
    formData.append("file", file);

    try {
        showLoader(true);

        const url = prompt
            ? `${BASE_URL}/analyze?prompt=${encodeURIComponent(prompt)}`
            : `${BASE_URL}/analyze`;

        const response = await fetch(url, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        output.textContent =
            JSON.stringify(data, null, 2);

    } catch (error) {
        output.textContent =
            `❌ Error: ${error.message}`;
    } finally {
        showLoader(false);
    }
}