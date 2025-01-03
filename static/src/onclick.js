async function pulo() {
    const response = await fetch("/onclick", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: "Hello from the frontend!" })
    });
    const result = await response.json();
    console.log(result.message);
}


