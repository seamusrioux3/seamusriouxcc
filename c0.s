.global main


main:

movq $10, !i
movq $5, !j
movq !i, !k
addq !j, !k
movq !i, !l
addq !k, !l
movq !l, %RAX
retq
