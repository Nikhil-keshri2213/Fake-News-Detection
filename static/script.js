// JavaScript to handle form submission and display prediction result

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const textarea = document.querySelector("textarea");
    const predictionDiv = document.getElementById("prediction");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        const newsText = textarea.value.trim();
        if (!newsText) {
            predictionDiv.textContent = "Please enter some news text.";
            predictionDiv.style.color = "red";
            return;
        }

        predictionDiv.textContent = "Processing...";
        predictionDiv.style.color = "#fff";

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({ message: newsText }),
            });

            if (response.ok) {
                const result = await response.text();
                predictionDiv.textContent = `Prediction: ${result}`;
                predictionDiv.style.color = "#fff";
            } else {
                predictionDiv.textContent = "Error processing your request. Please try again.";
                predictionDiv.style.color = "red";
            }
        } catch (error) {
            console.error("Error:", error);
            predictionDiv.textContent = "An unexpected error occurred. Please try again later.";
            predictionDiv.style.color = "red";
        }
    });
});
