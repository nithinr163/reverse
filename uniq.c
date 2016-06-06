#include <stdio.h>

int main(void) {
	int arr[100],dup[20],a,n,i,j,k=0,c=1,p=0;
	printf("\nEnter the no. of elements:");
	scanf("%d",&n);
	printf("\nEnter the elements:");
	for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	for (i = 0; i < n; ++i)
    {
        for (j = i + 1; j < n; ++j)
        {
            if (arr[i] > arr[j])
            {
                a =  arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }
    for(i=0;i<n;i+=c)
    {
    	for(j=i+1,p=0,c=1;j<n;j++)
    	{
    		if(arr[i]==arr[j])
    		{
    			++c;
    			++p;
    		}
    	}
    	if(p==0)
    		printf("\n Unique element:%d",arr[i]);
    	
    }
    return 0;
}
