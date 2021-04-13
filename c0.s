.global main


body:
callq read_int
movq %rax, %rdx
movq $6, %rsi
callq read_int
movq %rax, %r8
movq $0, %rdi
callq read_int
movq %rax, %rcx
cmpq %rcx, %rdi
movq %r8, %rcx
cmove %rsi, %rcx
movq %rdx, %rbx
addq %rcx, %rbx
movq %rbx, %rax
jmp end
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
