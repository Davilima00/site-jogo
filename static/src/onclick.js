async function pulo() {
    try {
        const response = await fetch("/onclick", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: "Hello from the frontend!" }),
        });

        if (!response.ok) {
            console.error("Erro na requisição:", response.status, response.statusText);
            return;
        }

        const result = await response.json();
        console.log(result);


    } catch (error) {
        console.error("Erro durante o fetch:", error);
    }
}


