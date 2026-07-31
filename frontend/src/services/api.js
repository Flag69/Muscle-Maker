const API_URL = "http://127.0.0.1:8000"

export async function generate_program() {
    const response = await fetch(API_URL + "/workout")
    const data = await response.json()
    return data
}
