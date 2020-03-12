#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_matrix.h>
int main()
{
	float m[3][3]={{1, 0.67, 0.33}, {0.45, 1, 0.55},{0.67, 0.33, 1}}, U[3][3], L[3][3];
	gsl_matrix *M = gsl_matrix_alloc(3,3);
	gsl_permutation *q = gsl_permutation_alloc(3);
	int i, j;
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			gsl_matrix_set(M,i,j,m[i][j]);
		}
	}
	int n;
	gsl_linalg_LU_decomp(M, q, &n);
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%f\t",gsl_matrix_get(M,i,j));
		}
		printf("\n");
	}	
	
	
	//Getting L
	printf("L:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(j>i)
			{ 
				L[i][j]=0.0;
				printf("0.000000\t");
			}
			else if(i==j)
			{ 
				L[i][j]=1.000000; 
				printf("1.000000\t");
					
			}
			else
			{ 
				L[i][j]=gsl_matrix_get(M,i,j); 
				printf("%f\t",L[i][j]);
			}
		}
		printf("\n");
	}


	//Getting U
	printf("U:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(j<i)
			{
				U[i][j]=0.0;
				printf("0.000000\t");
			}
			else
			{
				U[i][j]=gsl_matrix_get(M,i,j);
				printf("%f\t",U[i][j]);
			}
		}
		printf("\n");
	}


	//CHECKING THE DECOMPOSITION
	float LU[3][3];
	int k=0;
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			LU[i][j]=0;
			for(k=0;k<3;k++)
			{
				LU[i][j]+=L[i][k]*U[k][j];
			}
		}
	}
	printf("M:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%f\t",m[i][j]);
		}
		printf("\n");
	}
	
	printf("LU:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%f\t",LU[i][j]);
		}
		printf("\n");
	}
	
	gsl_permutation_free(q);
	gsl_matrix_free(M);
	return 0;
}
