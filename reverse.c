#include <stdio.h>
#include<string.h>
int main(void) {
	char str[20];
	printf("\nEnter the string:");
	gets(str);
	int n=strlen(str);
	for(int i=n-1;i>=0;i--)
	printf("%c",str[i]);
	return 0;
}
