#include <stdio.h>

// just for reference
int fib_recursive(int n){
	if(n<=1)
		return n;
	return fib_recursive(n-2)+fib_recursive(n-1);
}

int fib(int n){
	int x=0;int y=1;
	int tmp;
	for(int i=0;i<n;i++){
		y+=x;
		tmp=x;
		x=y;
		y=tmp;
	}
	return x;
}

int main(){
	for(int i=0;i<10;i++){
		printf("%i %i %i\n",i,fib(i),fib_recursive(i)); //matches
	}
	int i=0x43b;
	printf("%i %i\n",0x43b,fib(0x43b)); //overflow
	// printf("%i\n",fib_recursive(0x43b)); runs forever
}