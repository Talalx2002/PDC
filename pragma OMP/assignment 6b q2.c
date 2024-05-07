#include <stdio.h>
#include <omp.h>
#include<time.h>

int main() {
    int rows = 260; // Number of rows (you can adjust this)
    int cols = 260; // Number of columns (you can adjust this)

    // Declare five 2D arrays
    int array1[rows][cols];
    int array2[rows][cols];
    int array3[rows][cols];
    int array4[rows][cols];
    int array5[rows][cols];

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
//            scanf("%d", &array1[i][j]);
				array1[i][j] = i+j*2;
				array2[i][j] = i+j*3;
				array3[i][j] = i+j*4;
				array4[i][j] = i+j*5;
				array5[i][j] = i+j*6;		
        }
    }
    // Compute the sum of corresponding elements
    int sum[rows][cols];
    int sums = 0 ;
    double start_time, end_time;
    start_time = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            sum[i][j] += array1[i][j] + array2[i][j] + array3[i][j] + array4[i][j] + array5[i][j];
        }
    }
    end_time = omp_get_wtime();
//    printf("sum is %d \n", sums);
    printf("TIME OF EXECUTION IS %lf seconds\n", end_time - start_time);
    printf("time of start %lf seconds\n",start_time);
    printf("TIME of end IS %lf seconds\n",end_time);
     
    // Display the sum
    printf("Sum of corresponding elements:\n");
//    for (int i = 0; i < rows; ++i) {
//        for (int j = 0; j < cols; ++j) {
//            printf("%d ", sum[i][j]);
//        }
//        printf("\n");
//    }

    return 0;
}
