#include <stdio.h>
#include <cuda.h>

__global__ void factorialKernel(int* d_in, long* d_out) {
    int idx = threadIdx.x;
    int n = d_in[idx];
    long result = 1;

    for (int i = 1; i <= n; ++i) {
        result *= i;
    }

    d_out[idx] = result;
}

int main() {
    int h_in[5] = {1, 2, 3, 4, 5}; // Example numbers
    long h_out[5];
    int *d_in;
    long *d_out;

    // Allocate memory on GPU
    cudaMalloc((void**)&d_in, 5 * sizeof(int));
    cudaMalloc((void**)&d_out, 5 * sizeof(long));

    // Transfer data from CPU to GPU
    cudaMemcpy(d_in, h_in, 5 * sizeof(int), cudaMemcpyHostToDevice);

    // Launch kernel
    factorialKernel<<<1, 5>>>(d_in, d_out);

    // Transfer data back from GPU to CPU
    cudaMemcpy(h_out, d_out, 5 * sizeof(long), cudaMemcpyDeviceToHost);

    // Print results
    for (int i = 0; i < 5; ++i) {
        printf("Factorial of %d is %ld\n", h_in[i], h_out[i]);
    }

    // Free GPU memory
    cudaFree(d_in);
    cudaFree(d_out);

    return 0;
}
