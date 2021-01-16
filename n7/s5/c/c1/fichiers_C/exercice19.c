#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc >= 2)
    {
        printf("Les arguments sont : \n");
        for (int i = 1; i < argc - 1; i++)
        {
            printf("%s ; ", argv[i]);
        }
        printf("%s\n", argv[argc - 1]);
    }
    else
    {
        printf("Il n'y a pas d'argument.\n");
    }
    return EXIT_SUCCESS;
}