.global main


body:
movq $1, %rcx
movq $2, %rcx
callq read_int
callq read_int
movq $13, %rcx
movq $11, %r8
movq $4, %r10
movq $7, %r9
callq read_int
movq %rax, %rcx
cmpq %rcx, %r9
movq %r10, %rcx
cmovq l %r8, %rcx
callq read_int
movq %rax, %rdx
movq %rdx, %rbx
negq %rbx
cmpq %rbx, %rcx
jl label1
jmp end
label1:
movq %rcx, %rax
jmp end
label3:
movq %rcx, %rax
jmp end
label4:
jmp end
label2:
cmpq %rcx, %rax
je label3
jmp label4
main:
pushq %r12
pushq %r13
pushq %r14
pushq %r15
jmp body
end:
popq %r12
popq %r13
popq %r14
popq %r15
movq %rax, %rdi
callq print_int
retq
