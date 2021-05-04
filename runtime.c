#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define DEBUG  1

//types
extern uint64_t T_Unit;
extern uint64_t  T_S64;
extern uint64_t  T_Bool; 
extern uint64_t T_Vector;

//memory
uint8_t* free_ptr;
intptr_t from_end;

static uint8_t * to_start;
intptr_t * rootstack_start;
static intptr_t * rootstack_end;
static int heap_size = (1<<12);

//functions
void init_mem();
int64_t read_int(void);
void initialize();
void scan(intptr_t ** qhead);

//print functions
void print_value(uint64_t val, uint64_t ty);
void print_vector(uint64_t *val);


void init_heap(){
    to_start = (uint8_t*)malloc(heap_size);
    if(!to_start){
        fprintf(stderr, "cannot alloc free space in init_heap\n");
        exit(1);
    }
    from_end = (intptr_t)to_start + heap_size;
    free_ptr = to_start;
    return;
}

void init_mem(){
    rootstack_end = (intptr_t*)malloc(heap_size);
    if(!rootstack_end){
        fprintf(stderr, "cannot init_mem\n");
        exit(1);
    }
    rootstack_start = rootstack_end + heap_size;
    return;
}   

void enqueue(intptr_t *objp){
    intptr_t * new_loc = (intptr_t *)free_ptr;
    intptr_t *obj = (intptr_t *)*objp;
    intptr_t *ty = (intptr_t *)obj[0];
    size_t size =0;
    fprintf(stderr,"enqueue %p %p %p\n", objp, obj, ty);
    //its a forwarding pointer
    if(to_start <= (uint8_t *)ty && (intptr_t)ty < from_end){
        size = 0;
        new_loc = ty;
        fprintf(stderr,"enque fwd\n");
    }else{
        fprintf(stderr,"enque copy\n");
        size = ty[1]+1;
        for(size_t i =0; i<size; i++){
            new_loc[i] = obj[i];
        }
    }
    fprintf(stderr,"enqueue size(%ld) newloc(%p) \n", size, new_loc);
    free_ptr+= size * sizeof(intptr_t);
    *objp = (intptr_t)new_loc;
    *obj = (intptr_t)new_loc;
}


void scan(intptr_t ** qhead){
    uint64_t * obj = *qhead;
    uint64_t * ty = (intptr_t *)obj[0];;
    fprintf(stderr,"scan %p %p %p", qhead, ty, obj);
    for(size_t i=0; i< ty[1]; i++){
        intptr_t elem_ty = ty[2+i];
        if(elem_ty == T_Vector){
            enqueue(obj+1+i);
        }
    }
    *qhead += ty[1] +1;
}

void collect(uint64_t size, intptr_t * rootstack);
void collect(uint64_t size, intptr_t * rootstack){
    size_t howManyRoots = rootstack_start - rootstack;
    fprintf(stderr, "collect: %d %ld %p %p (%ld)\n", heap_size, size, rootstack, rootstack_start, howManyRoots);

    //create new heap
    uint8_t * from_start = to_start;
    intptr_t from_end = from_end; 
    init_heap();

    //Enqueue root set
    for(intptr_t* rootp = rootstack; rootp < rootstack_start; rootp += 1){
        enqueue(rootp);
    }

    uint8_t * qhead = to_start;

    //Scan the queue
    while(qhead < free_ptr){
        scan((intptr_t **)&qhead);
    }

    free(from_start);

    //See if enough space
    if(free_ptr + size < (uint8_t*)from_end){
        return;
    }
    heap_size = heap_size <<1;
    collect(size, rootstack);
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

