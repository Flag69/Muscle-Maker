const API_URL = "http://127.0.0.1:8000"

export async function generate_program(filters) {
    const response = await fetch(API_URL + "/workout", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(filters)
    })
    const data = await response.json()
    return data
}

export async function generate_pdf(workout) {

    const response = await fetch(API_URL + "/workout/pdf", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(workout)
    })

    if (!response.ok) {
        throw new Error("Failed to generate PDF")
    }

    const blob = await response.blob()

    const url = window.URL.createObjectURL(blob)

    const link = document.createElement("a")
    link.href = url
    link.download = "muscle-maker-workout.pdf"

    link.click()

    window.URL.revokeObjectURL(url)
}