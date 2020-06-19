#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int array_generator(int n, float A[n][n]){

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            A[i][j] = rand()*1.0/RAND_MAX;
        }
    }
    return 0;
}



int main (int argc, char** argv){

    if (argc != 2) {
        fprintf(stderr, "usage: ./comparison <number>\n");
        exit(1);
    }
    int n = atoi(argv[1]);
    if (n == 0) {
        fprintf(stderr, "error: invalid character detected\n");
        exit(1);
    }

    srand(time(NULL));

    float A[n][n];
    float B[n][n];
    array_generator(n, A);
    array_generator(n, B);
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf("%f ",A[i][j]);
        }
        printf("\n");
    }
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf("%f ",B[i][j]);
        }
        printf("\n");
    }

}