#include <stdio.h>

static int read_count =0;

int read_int(){
    return read_count+=1;
}