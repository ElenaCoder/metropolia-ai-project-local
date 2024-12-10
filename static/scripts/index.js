const form = document.getElementById("translateForm");
const resultDiv = document.getElementById("result");
const errorDiv = document.getElementById("error");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const text = document.getElementById("textToTranslate").value.trim();
    resultDiv.classList.add("d-none");
    errorDiv.classList.add("d-none");

    if (!text) {
        errorDiv.textContent = "Error: Input cannot be empty.";
        errorDiv.classList.remove("d-none");
        return;
    }

    resultDiv.textContent = "Translating...";
    resultDiv.classList.remove("d-none");

    try {
        const response = await fetch("/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text }),
        });
        const data = await response.json();

        if (response.ok) {
            resultDiv.textContent = `Translation: ${data.translated_text}`;
            resultDiv.classList.remove("alert-danger");
            resultDiv.classList.add("alert-success");
        } else {
            errorDiv.textContent = `Error: ${data.error}`;
            errorDiv.classList.remove("d-none");
        }
    } catch (error) {
        errorDiv.textContent = "Error: Unable to connect to the server.";
        errorDiv.classList.remove("d-none");
    }
});
