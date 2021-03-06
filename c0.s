.global main


body:
callq read_int
callq read_int
movq %rax, 101(%rbp)
negq 101(%rbp)
callq read_int
movq $16, 101(%rbp)
movq $10, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
movq $14, %rdx
movq $16, %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
callq read_int
movq %rax, %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
negq 101(%rbp)
negq 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
callq read_int
movq %rax, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
negq 101(%rbp)
movq $2, 101(%rbp)
negq 101(%rbp)
negq 101(%rbp)
negq 101(%rbp)
movq $16, 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq $8, 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq $2, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
movq 101(%rbp), %rdx
negq %rdx
addq %rdx, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq 101(%rbp), %rdx
negq %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
callq read_int
movq %rax, %rdx
callq read_int
movq %rax, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
callq read_int
movq %rax, %rdx
addq %rdx, 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq $12, 101(%rbp)
movq $5, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
movq $16, %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
movq $1, 101(%rbp)
callq read_int
movq %rax, %rdx
addq %rdx, 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
movq $10, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rax
addq %rax, 101(%rbp)
movq $15, 101(%rbp)
callq read_int
movq %rax, 101(%rbp)
movq 101(%rbp), %rdx
negq %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
callq read_int
movq %rax, %rdx
movq $7, %rdx
movq $2, %rdx
movq %rdx, 101(%rbp)
negq 101(%rbp)
movq 101(%rbp), %rdx
addq 101(%rbp), %rdx
movq %rdx, %r15
negq %r15
movq 101(%rbp), %r14
addq %r15, %r14
movq $9, %r14
movq %r14, %r13
negq %r13
movq $1, %r15
movq $13, %r14
movq %r15, %r12
addq %r14, %r12
movq %r13, %rdx
addq %r12, %rdx
callq read_int
movq %rax, %r12
callq read_int
movq %rax, %rdx
movq %r12, %r11
addq %rdx, %r11
callq read_int
movq %rax, %r12
callq read_int
movq %rax, %rdx
movq %r12, %r10
addq %rdx, %r10
movq %r11, %r8
addq %r10, %r8
movq $11, %r8
callq read_int
movq %rax, %r8
negq %r8
movq $15, %r10
movq %r10, %r9
negq %r9
movq %r9, %rdi
negq %rdi
movq %r8, %rsi
addq %rdi, %rsi
movq %rsi, %rdx
negq %rdx
callq read_int
movq $3, %rax
negq %rax
negq %rax
negq %rax
negq %rax
negq %rax
jmp end
main:
pushq %rbp
movq %rsp, %rbp
pushq %rbx
pushq %r12
pushq %r13
pushq %r14
pushq %r15
subq $110, %rsp
jmp body
end:
addq $110, %rsp
popq %rbx
popq %rbp
popq %r12
popq %r13
popq %r14
popq %r15
movq %rax, %rdi
callq print_int
retq
