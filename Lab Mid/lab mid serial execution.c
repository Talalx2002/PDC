//SERIAL EXECUTION

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define SIZE 250
#define EVEN_COUNT 100

void initialize_array(int arr[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            arr[i][j] = rand() % 1000; // Random values between 0 and 999
        }
    }
}

void find_even_numbers(int A[SIZE][SIZE], int B[SIZE][SIZE], int C[SIZE][SIZE], int D[EVEN_COUNT]) {
    int count = 0;

    for (int i = 0; i < SIZE && count < EVEN_COUNT; i++) {
        for (int j = 0; j < SIZE && count < EVEN_COUNT; j++) {
            if (A[i][j] % 2 == 0 && count < EVEN_COUNT) {
                D[count++] = A[i][j];
            }
            if (B[i][j] % 2 == 0 && count < EVEN_COUNT) {
                D[count++] = B[i][j];
            }
            if (C[i][j] % 2 == 0 && count < EVEN_COUNT) {
                D[count++] = C[i][j];
            }
        }
    }
}

void print_array(int arr[EVEN_COUNT]) {
    for (int i = 0; i < EVEN_COUNT; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE];
    int D[EVEN_COUNT];

    srand(time(NULL)); // Seed for random number generation

    initialize_array(A);
    initialize_array(B);
    initialize_array(C);

    find_even_numbers(A, B, C, D);

    print_array(D);

    return 0;
}
