while true {
    if let message = readLine() {
        if message == "END" {
            break
        }
        let reversedMessage = String(message.reversed())
        print(reversedMessage)
    }
}
