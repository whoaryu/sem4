/*As a logistics manager for an e-commerce company, you are responsible for optimizing the travel times of delivery trucks moving between multiple warehouses in a city. The road network is complex, and you need to find the most time-efficient routes for all pairs of warehouses.
Input:
The number of warehouses in the city.
A weighted directed graph representing the road network between warehouses.
The weight of each edge represents the travel time between warehouses.
Output:
A matrix showing the shortest travel times between all pairs of warehouses.*/

// floydwarshall

#include <stdio.h>
#define v 10
void floyd_warshall(int a[v][v], int n)
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (a[i][j] > a[i][k] + a[k][j])
                {
                    a[i][j] = a[i][k] + a[k][j];
                }
            }
        }
    }
    printf("All Pairs Shortest Path is :\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    int a[v][v];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    floyd_warshall(a, n);
}
