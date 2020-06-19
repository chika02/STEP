#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

void print_array(int n, double A[n][n]){
    
    for (int i=0; i<n; i++){
        printf("[");
        for (int j=0; j<n; j++){
            printf("%f ",A[i][j]);
        }
        printf("]\n");
    }
    printf("\n");
    return;
}

void array_generator(int n, double A[n][n]){

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            A[i][j] = rand()*1.0/RAND_MAX;
        }
    }
    return;
}

void product_c(int n, double A[n][n], double B[n][n], double C[n][n]){
    
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            double sum = 0;
            for (int k=0; k<n; k++){
                sum += A[i][k]*B[k][j];
            }
            C[i][j] = sum;
        }
    }
    return;
}

int measure_time(n){

    double A[n][n];
    double B[n][n];
    double C[n][n];
    array_generator(n, A);
    array_generator(n, B);

    struct timeval t1,t2;
    gettimeofday(&t1, NULL);
    product_c(n, A, B, C);
    gettimeofday(&t2, NULL);

    return t2.tv_usec - t1.tv_usec;

}

int main (int argc, char** argv){

    srand(time(NULL));
    const char* path = "time_c.csv";
    FILE* fp = fopen(path, "w");

    int m = 10;
    double ave = 0;
    for (int n=1; n<100; n++){
        for (int i=0; i<m; i++){
            ave += measure_time(n)*1.0/m;
        }
        fprintf(fp, "%d  %lf\n", n, ave);
    }
    
    return 0;
}