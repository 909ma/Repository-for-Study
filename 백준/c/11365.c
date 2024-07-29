#include <stdio.h>
#include <string.h>

int main() {
    char message[500];
    while(1){
        scanf(" %[^\n]", message);

        if(strcmp(message, "END") == 0){
            break;
        }

        for (int i = strlen(message) - 1; i >= 0; i--){
            printf("%c", message[i]);
        }
        printf("\n");
    }
    return 0;
}

// scanf(" %[^\n]", message);는 공백을 포함한 문자열을 입력받기 위해 사용됩니다. 앞의 공백은 이전 입력의 남은 개행 문자를 무시하게 합니다.
