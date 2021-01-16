#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>

// Definition du type Point
struct Point
{
    int X;
    int Y;
};

typedef struct Point Point;

int main()
{
    // Déclarer deux variables ptA et ptB de types Point
    Point ptA, ptB;
    // Initialiser ptA à (0,0)
    ptA.X = 0;
    ptA.Y = 0;
    // Initialiser ptB à (10,10)
    ptB.X = 10;
    ptB.Y = 10;

    // Calculer la distance entre ptA et ptB.
    float distance = 0;
    distance = sqrt(pow((ptB.X - ptA.X), 2) + pow((ptB.Y - ptA.Y), 2));

    assert(distance == sqrt(200));

    return EXIT_SUCCESS;
}