/*
- ref
http://www.gdep.jp/page/view/251
- compile
nvcc -o matrix_cpu.exe matrix_cpu.cu
- run
./matrix_cpu.exe
*/

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>


/* define n square matrix size */
#define MATRIX_SIZE 1024


int main(int argc, char** argv)
{
    unsigned int col_idx, row_idx, scan_idx;
    int* matA;
    int* matB;
    int* matC;

    time_t Start, Stop;

    matA = (int*)malloc(sizeof(int) * MATRIX_SIZE * MATRIX_SIZE);
    matB = (int*)malloc(sizeof(int) * MATRIX_SIZE * MATRIX_SIZE);
    matC = (int*)malloc(sizeof(int) * MATRIX_SIZE * MATRIX_SIZE);

    for (col_idx = 0; col_idx < MATRIX_SIZE; col_idx++) {
        for (row_idx = 0; row_idx < MATRIX_SIZE; row_idx++) {
            matA[col_idx * MATRIX_SIZE + row_idx] = rand() % (MATRIX_SIZE * MATRIX_SIZE);
            matB[col_idx * MATRIX_SIZE + row_idx] = rand() % (MATRIX_SIZE * MATRIX_SIZE);
            matC[col_idx * MATRIX_SIZE + row_idx] = 0;
        }
    }

    time(&Start);

    for (col_idx = 0; col_idx < MATRIX_SIZE; col_idx++) {
        for (row_idx = 0; row_idx < MATRIX_SIZE; row_idx++) {
            for (scan_idx = 0; scan_idx < MATRIX_SIZE; scan_idx++) {
                matC[col_idx + MATRIX_SIZE + row_idx] += matA[col_idx * MATRIX_SIZE + scan_idx] * matB[scan_idx * MATRIX_SIZE + row_idx];
            }
        }
    }

    time(&Stop);

    printf("Processing time: %f (sec)\n", (double)(Stop - Start));

    free(matA);
    free(matB);
    free(matC);

    return 0;
}
