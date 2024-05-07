#include <omp.h>
main()
{
	#pragma omp parallel
	{
		#pragma omp sections
			{
			#pragma omp section
				(void) funcA();
					#pragma omp section
						(void) funcB();
										} /*-- End of sections block --*/
												} /*-- End of parallel region --*/
													}/*-- End of Main Program --*/

void funcA()
{
	printf("In funcA: this section is executed by thread %d\n", omp_get_thread_num());
}
void funcB() 
{
printf("In funcB: this section is executed by thread %d\n", omp_get_thread_num());
}