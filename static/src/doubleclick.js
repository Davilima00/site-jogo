async function doubleclick() {
    const response = await fetch("/doubleclick", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: "Hello from the frontend!" })
    });
    const result = await response.json();
    console.log(result.message);
}
