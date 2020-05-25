# Este Ejemplo fue tomado del libro de Georgia Weidman

#include <stdio.h>
int main(int argc, char *argv[])
{
    if(argc < 2)
    {
        printf("%s\n", "Pase su nombre como argumento");
        return 0;
    }
    else
    {
                printf("Hola %s\n", argv[1]);
                return 0;
    }
}
