.global main


main:
callq begin
movq %RAX, %RDI
callq print_int
retq
begin:
pushq %RBP
movq %RSP, %RBP
subq $64, %RSP
jmp body
body:
callq read_int
movq %RAX, 0(%RBP)
callq read_int
movq %RAX, -8(%RBP)
movq $42, -16(%RBP)
callq read_int
movq %RAX, -24(%RBP)
callq read_int
movq %RAX, -32(%RBP)
movq -24(%RBP), %RAX
movq %RAX, -40(%RBP)
movq -32(%RBP), %RAX
addq %RAX, -40(%RBP)
movq -16(%RBP), %RAX
movq %RAX, -48(%RBP)
movq -40(%RBP), %RAX
addq %RAX, -48(%RBP)
movq -48(%RBP), %RAX
jmp end
end:
addq $64, %RSP
popq %RBP
retq
