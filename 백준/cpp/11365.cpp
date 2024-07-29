#include <iostream>
#include <string>

int main() {
    std::string message;

    while (true) {
        std::getline(std::cin, message);

        if (message == "END") {
            break;
        }

        for (int i = message.length() - 1; i >= 0; i--) {
            std::cout << message[i];
        }
        std::cout << std::endl;
    }

    return 0;
}
