.global main


main:
movq $10, %R8
movq $5, %R9
jmp l0
l0:
addq %R8, %R9
addq %R8, %R9
movq %R9, %RAX
retq
