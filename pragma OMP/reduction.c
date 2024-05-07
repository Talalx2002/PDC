#include <stdio.h>
#include <omp.h>

double start_time, end_time;
static long num_step = 100000;
double step;

int main() {
    int i;
    double x, pi, sum = 0.0;
    start_time = omp_get_wtime();
    step = 1.0 / (double)num_step;

    #pragma omp parallel for reduction(+:sum)
    for (i = 0; i < num_step; i++) {
        x = (i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x);
    }
    end_time = omp_get_wtime();
	
	pi = step * sum;

    printf("VALUE of PI is %lf\n", pi);
    printf("TIME OF EXECUTION IS %lf seconds\n", end_time - start_time);
    printf("time of start %lf seconds\n",start_time);
    printf("TIME of end IS %lf seconds\n",end_time);

    return 0;
}
