/*
- ref
http://www.gdep.jp/page/view/251
http://hidemon-memo.blogspot.jp/2014/10/cuda.html
- compile
export PATH=/usr/local/cuda-8.0/bin:$PATH
nvcc -I /usr/local/cuda-8.0/samples/common/inc -o matrix_gpu.exe matrix_gpu.cu
- run
./matrix_gpu.exe
*/


#include <stdio.h>
// #include <malloc.h>
#include <stdlib.h>
// #include <time.h>
// #include <cutil_inline.h>
#include <helper_cuda.h>
#include <helper_functions.h>


#define MATRIX_SIZE 1024
#define BLOCK_SIZE 16


__global__ void
matrixMul(int* inMatrixA, int* inMatrixB, int* inMatrixC);


int main(int argc, char** argv)
{
    unsigned int matrixSize = sizeof(unsigned int) * MATRIX_SIZE * MATRIX_SIZE;

    int* hMatrixA;
    int* hMatrixB;
    int* hMatrixC;

    hMatrixA = (int*)malloc(matrixSize);
    hMatrixB = (int*)malloc(matrixSize);

    /* init */
    unsigned int col_idx, row_idx;
    for (col_idx = 0; col_idx < MATRIX_SIZE; col_idx++) {
        for (row_idx = 0; row_idx < MATRIX_SIZE; row_idx++) {
            hMatrixA[col_idx * MATRIX_SIZE + row_idx] = rand() % (MATRIX_SIZE * MATRIX_SIZE);
            hMatrixB[col_idx * MATRIX_SIZE + row_idx] = rand() % (MATRIX_SIZE * MATRIX_SIZE);
        }
    }

    /* device variable */
    int* dMatrixA;
    int* dMatrixB;
    int* dMatrixC;

    /* device memory */
    // cutilSafeCall(cudaMalloc((void**)&dMatrixA, matrixSize));
    // cutilSafeCall(cudaMemcpy(dMatrixA, hMatrixA, matrixSize, cudaMemcpyHostToDevice));
    // cutilSafeCall(cudaMalloc((void**)&dMatrixB, matrixSize));
    // cutilSafeCall(cudaMemcpy(dMatrixB, hMatrixB, matrixSize, cudaMemcpyHostToDevice));
    // cutilSafeCall(cudaMalloc((void**)&dMatrixC, matrixSize));
    checkCudaErrors(cudaMalloc((void**)&dMatrixA, matrixSize));
    checkCudaErrors(cudaMemcpy(dMatrixA, hMatrixA, matrixSize, cudaMemcpyHostToDevice));
    checkCudaErrors(cudaMalloc((void**)&dMatrixB, matrixSize));
    checkCudaErrors(cudaMemcpy(dMatrixB, hMatrixB, matrixSize, cudaMemcpyHostToDevice));
    checkCudaErrors(cudaMalloc((void**)&dMatrixC, matrixSize));

    /* block size & grid size */
    dim3 block(BLOCK_SIZE, BLOCK_SIZE);
    dim3 grid(MATRIX_SIZE / BLOCK_SIZE, MATRIX_SIZE / BLOCK_SIZE);

    /* start timer */
    // unsigned int timer = 0;
    // CUT_SAFE_CALL(cutCreateTimer(&timer));
    // CUT_SAFE_CALL(cutStartTimer(timer));
    cudaEvent_t start;
    cudaEvent_t stop;
    checkCudaErrors(cudaEventCreate(&start));
    checkCudaErrors(cudaEventCreate(&stop));
    checkCudaErrors(cudaEventRecord(start, NULL)); // start

    /* start kernel */
    matrixMul<<<grid, block>>>(dMatrixA, dMatrixB, dMatrixC);
    cudaThreadSynchronize();

    /* secure mem & trancerate memory from device */
    hMatrixC = (int*)malloc(matrixSize);
    // cutilSafeCall(cudaMemcpy(hMatrixC, dMatrixC, matrixSize, cudaMemcpyDeviceToHost));
    checkCudaErrors(cudaMemcpy(hMatrixC, dMatrixC, matrixSize, cudaMemcpyDeviceToHost));


    /* stop timer */
    // CUT_SAFE_CALL(cutStoptimer(timer));
    // printf("Processing time: %f (msec)\n", cutGetTimerValue(timer));
    // CUT_SAFE_CALL(cutDeleteTimer(timer));
    checkCudaErrors(cudaEventRecord(stop, NULL));
    checkCudaErrors(cudaEventSynchronize(stop));
    float msecTotal = 0.0f;
    checkCudaErrors(cudaEventElapsedTime(&msecTotal, start, stop));
    printf("Processing time: %f (msec)\n", msecTotal);

    /* release host, device memory */
    free(hMatrixA);
    free(hMatrixB);
    free(hMatrixC);
    // cutilSafeCall(cudaFree(dMatrixA));
    // cutilSafeCall(cudaFree(dMatrixB));
    // cutilSafeCall(cudaFree(dMatrixC));
    checkCudaErrors(cudaFree(dMatrixA));
    checkCudaErrors(cudaFree(dMatrixB));
    checkCudaErrors(cudaFree(dMatrixC));

    /* endroll */
    cudaThreadExit();
    exit(1);
}


__global__ void
matrixMul(int* inMatrixA, int* inMatrixB, int* inMatrixC) {
    unsigned int col_idx = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int row_idx = blockIdx.y * blockDim.y + threadIdx.y;
    unsigned int scan_idx;
    unsigned int target = 0;

    for (scan_idx = 0; scan_idx < MATRIX_SIZE; scan_idx++) {
        target += inMatrixA[col_idx * MATRIX_SIZE + scan_idx] * inMatrixB[scan_idx * MATRIX_SIZE + row_idx];
        __syncthreads();
    }
    inMatrixC[col_idx * MATRIX_SIZE + row_idx] = target;
}
