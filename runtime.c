#include <stdio.h>
#define DEBUG  1

static int read_count =0;
int read_int(void);
void print_int(int);

int read_int(){
    int x =0;
    // if(DEBUG){
    //     return 1;
    // }
    // scanf("%d",&x);
    // return x;
    return 1;
}

void print_int(int x){
    printf("%d", x);
}