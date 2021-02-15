.global main


main:
callq begin
movq %RAX, %RDI
callq print_int
retq
begin:
pushq %RBP
movq %RSP, %RBP
subq $464, %RSP
jmp body
body:
movq $4, 0(%RBP)
callq read_int
movq %RAX, -8(%RBP)
movq 0(%RBP), %RAX
movq %RAX, -16(%RBP)
movq -8(%RBP), %RAX
addq %RAX, -16(%RBP)
movq $-5, -24(%RBP)
movq -16(%RBP), %RAX
movq %RAX, -32(%RBP)
movq -24(%RBP), %RAX
addq %RAX, -32(%RBP)
movq $4, -40(%RBP)
callq read_int
movq %RAX, -48(%RBP)
movq -40(%RBP), %RAX
movq %RAX, -56(%RBP)
movq -48(%RBP), %RAX
addq %RAX, -56(%RBP)
movq $-5, -64(%RBP)
movq -56(%RBP), %RAX
movq %RAX, -72(%RBP)
movq -64(%RBP), %RAX
addq %RAX, -72(%RBP)
callq read_int
movq %RAX, -80(%RBP)
movq -72(%RBP), %RAX
movq %RAX, -88(%RBP)
movq -80(%RBP), %RAX
addq %RAX, -88(%RBP)
movq $4, -96(%RBP)
callq read_int
movq %RAX, -104(%RBP)
movq -96(%RBP), %RAX
movq %RAX, -112(%RBP)
movq -104(%RBP), %RAX
addq %RAX, -112(%RBP)
movq $-5, -120(%RBP)
movq -112(%RBP), %RAX
movq %RAX, -128(%RBP)
movq -120(%RBP), %RAX
addq %RAX, -128(%RBP)
movq -128(%RBP), %RAX
movq %RAX, -136(%RBP)
negq -136(%RBP)
movq -88(%RBP), %RAX
movq %RAX, -144(%RBP)
movq -136(%RBP), %RAX
addq %RAX, -144(%RBP)
movq $13, -152(%RBP)
movq $13, -160(%RBP)
movq -152(%RBP), %RAX
movq %RAX, -168(%RBP)
movq -160(%RBP), %RAX
addq %RAX, -168(%RBP)
callq read_int
movq %RAX, -176(%RBP)
movq $12, -184(%RBP)
movq $15, -192(%RBP)
callq read_int
movq %RAX, -200(%RBP)
movq $12, -208(%RBP)
movq -192(%RBP), %RAX
movq %RAX, -216(%RBP)
movq -208(%RBP), %RAX
addq %RAX, -216(%RBP)
movq $-1, -224(%RBP)
movq $7, -232(%RBP)
callq read_int
movq %RAX, -240(%RBP)
movq -232(%RBP), %RAX
movq %RAX, -248(%RBP)
movq -240(%RBP), %RAX
addq %RAX, -248(%RBP)
movq $-11, -256(%RBP)
movq -248(%RBP), %RAX
movq %RAX, -264(%RBP)
movq -256(%RBP), %RAX
addq %RAX, -264(%RBP)
movq -224(%RBP), %RAX
movq %RAX, -272(%RBP)
movq -264(%RBP), %RAX
addq %RAX, -272(%RBP)
movq -168(%RBP), %RAX
movq %RAX, -280(%RBP)
movq -272(%RBP), %RAX
addq %RAX, -280(%RBP)
callq read_int
movq %RAX, -288(%RBP)
movq -288(%RBP), %RAX
movq %RAX, -296(%RBP)
negq -296(%RBP)
movq $-2, -304(%RBP)
movq -296(%RBP), %RAX
movq %RAX, -312(%RBP)
movq -304(%RBP), %RAX
addq %RAX, -312(%RBP)
movq -312(%RBP), %RAX
movq %RAX, -320(%RBP)
negq -320(%RBP)
callq read_int
movq %RAX, -328(%RBP)
callq read_int
movq %RAX, -336(%RBP)
movq $-8, -344(%RBP)
callq read_int
movq %RAX, -352(%RBP)
callq read_int
movq %RAX, -360(%RBP)
movq -360(%RBP), %RAX
movq %RAX, -368(%RBP)
negq -368(%RBP)
movq -320(%RBP), %RAX
movq %RAX, -376(%RBP)
movq -368(%RBP), %RAX
addq %RAX, -376(%RBP)
callq read_int
movq %RAX, -384(%RBP)
movq $16, -392(%RBP)
callq read_int
movq %RAX, -400(%RBP)
callq read_int
movq %RAX, -408(%RBP)
movq -400(%RBP), %RAX
movq %RAX, -416(%RBP)
movq -408(%RBP), %RAX
addq %RAX, -416(%RBP)
movq -392(%RBP), %RAX
movq %RAX, -424(%RBP)
movq -416(%RBP), %RAX
addq %RAX, -424(%RBP)
movq $3, -432(%RBP)
movq -432(%RBP), %RAX
movq %RAX, -440(%RBP)
negq -440(%RBP)
movq -376(%RBP), %RAX
movq %RAX, -448(%RBP)
movq -440(%RBP), %RAX
addq %RAX, -448(%RBP)
movq -280(%RBP), %RAX
movq %RAX, -456(%RBP)
movq -448(%RBP), %RAX
addq %RAX, -456(%RBP)
movq -456(%RBP), %RAX
jmp end
end:
addq $464, %RSP
popq %RBP
retq
