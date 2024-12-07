const form = document.getElementById("translate-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent the default form submission
    const textInput = document.getElementById("text-input").value;
    const resultElement = document.getElementById("result");

    try {
        const response = await fetch("/translate", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ text: textInput }),
        });

        const data = await response.json();

        if (response.ok) {
            resultElement.textContent = `Translation: ${data.translated_text}`;
        } else {
            resultElement.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        resultElement.textContent = `Error: Unable to connect to the server.`;
        console.error(error);
    }
});
