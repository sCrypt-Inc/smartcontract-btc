export function generateRandomHex(length) {
    const characters = '0123456789abcdef'
    let hex = ''

    for (let i = 0; i < length * 2; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length)
        hex += characters.charAt(randomIndex)
    }

    return hex
}
