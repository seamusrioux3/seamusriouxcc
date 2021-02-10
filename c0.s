.global main


main:
pushq $33
popq %RAX
movq $8, %R8
addq %R8, %RAX
retq
