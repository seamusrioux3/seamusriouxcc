.section	.data
.global T_Unit
T_Unit:	.quad	0
.global T_S64
T_S64:	.quad	1
.global T_Bool
T_Bool:	.quad	2
.global T_Vector
T_Vector:	.quad	3
type0:
.quad 3
.quad 5
.quad 2
.quad 2
.quad 2
.quad 1
.quad 1
.section	.text
.global main 

body:
movq $48, 0(%rsp)
movq free_ptr(%rip), %rdx
addq 0(%rsp), %rdx
cmpq from_end(%rip), %rdx
jg label1
jmp label2
label1:
movq $40, %rdi
callq collect
movq $1, %rdx
jmp label3
label2:
movq $1, %rdx
jmp label3
label3:
movq free_ptr(%rip), %rax
movq %rax, 8(%rsp)
addq $48, free_ptr(%rip)
movq 8(%rsp), %r11
leaq type0(%rip), %r10
movq %r10, 0(%r11)
movq $1, %r13
movq 8(%rsp), %r11
movq %r13, %r10
movq %r10, 8(%r11)
movq $0, %r9
movq 8(%rsp), %r11
movq %r9, %r10
movq %r10, 16(%r11)
movq $0, %r15
movq 8(%rsp), %r11
movq %r15, %r10
movq %r10, 24(%r11)
movq $2, %r14
movq 8(%rsp), %r11
movq %r14, %r10
movq %r10, 32(%r11)
movq $5, %r8
movq 8(%rsp), %r11
movq %r8, %r10
movq %r10, 40(%r11)
movq 8(%rsp), %rax
jmp end
main:
pushq %rbx
pushq %rbp
movq %rsp, %rbp
subq $56, %rsp
callq init_mem
jmp body
end:
movq T_Vector(%rip), %rdi
movq %rax, %rsi
callq print_value
addq $56, %rsp
popq %rbp
popq %rbx
retq



