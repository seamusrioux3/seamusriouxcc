.global main


body:
callq read_int
movq %rax, 0(%rbp)
movq 0(%rbp), %rax
jmp end
main:
pushq %rbx
pushq %rbp
pushq %r12
pushq %r13
pushq %r14
pushq %r15
movq %rsp, %rbp
subq $8, %rsp
jmp body
end:
addq $8, %rsp
popq %rbx
popq %rbp
popq %r12
popq %r13
popq %r14
popq %r15
movq %rax, %rdi
callq print_int
retq
