#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define PI 3.14

int main()
{
    int r = 15;
    float p = 2 * PI * r;
    float a = PI * pow(r, 2);

    printf("Le rayon du cercle est : %d unité(s) \n", r);
    printf("Le périmètre du cercle est : %f unité(s) \n", p);
    printf("L'aire du cercle est : %f unité(s)² \n", a);
    return EXIT_SUCCESS;
}