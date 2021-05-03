#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define DEBUG  1

//memory
intptr_t free_ptr;
intptr_t from_end;
int heap_size = (1<<12);

int64_t* from_space_end;
int64_t* root_stack_ptr;

void init_mem();
int64_t read_int(void);
void initialize();
void collect(uint64_t, uint64_t);

//print functions
void print_value(uint64_t val, uint64_t ty);

extern uint64_t T_Unit;
extern uint64_t  T_S64;
extern uint64_t  T_Bool; 
extern uint64_t T_Vector;


void init_mem(){
    free_ptr = (intptr_t)malloc(heap_size);
    if(!free_ptr){
        fprintf(stderr, "cannot init_mem\n");
        exit(1);
    }
    from_end = free_ptr * heap_size;
    return;
}   

int64_t read_int(){
    int x =0;
    // if(DEBUG){
    //     return 1;
    // }
    // scanf("%d",&x);
    // return x;
    return 1;
}

void print_unit(){
    printf("%s", "Unit");
    return;
}

void print_int(int x){
    printf("%d", x);
    return;
}

void print_bool(int x){
    printf("%s", x ? "true": "false");
    return;
}

void print_vector(uint64_t *val);
void print_vector(uint64_t *val){
    uint64_t *ty = (uint64_t*)val[0];
    printf("Vector[");
    for(uint8_t i =0; i < ty[1]; i++){
        print_value(ty[2+i], val[1+i]);
        if(i != ty[1]){
            printf(" ");
        }
    }
    printf("]");
    return;
}

void print_value(uint64_t ty, uint64_t val){
    if(ty == T_Unit){
        print_unit();
    }
    else if(ty == T_S64){
        print_int(val);
    }
    else if(ty == T_Bool){
         print_bool(val);
    }
    else if(ty == T_Vector){
        print_vector((uint64_t *)val);
    }
    else{
        fprintf(stderr, "invalid obj ty tag: %ld\n", val);
    }
}

void collect(uint64_t root_stack_top, uint64_t alloc_reg){
    fprintf(stderr, "cannot collect\n");
    return;
}