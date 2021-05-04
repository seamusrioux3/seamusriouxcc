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
.quad 126
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
type1:
.quad 3
.quad 127
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
type2:
.quad 3
.quad 128
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.quad 1
.section	.text
.global main 

body:
movq $1016, 0(%rsp)
movq free_ptr(%rip), %rcx
addq 0(%rsp), %rcx
cmpq from_end(%rip), %rcx
jl label1
jmp label2
label1:
movq $1, %rcx
jmp label3
label2:
movq $1008, %rdi
movq %r12, %rsi
callq collect
movq $1, %rcx
jmp label3
label3:
movq free_ptr(%rip), %rax
movq %rax, 8(%rsp)
addq $1016, free_ptr(%rip)
movq 8(%rsp), %r11
leaq type0(%rip), %r10
movq %r10, 0(%r11)
movq $0, 16(%rsp)
movq 8(%rsp), %r11
movq 16(%rsp), %r10
movq %r10, 8(%r11)
movq $1, 32(%rsp)
movq 8(%rsp), %r11
movq 32(%rsp), %r10
movq %r10, 16(%r11)
movq $2, 48(%rsp)
movq 8(%rsp), %r11
movq 48(%rsp), %r10
movq %r10, 24(%r11)
movq $3, 64(%rsp)
movq 8(%rsp), %r11
movq 64(%rsp), %r10
movq %r10, 32(%r11)
movq $4, 80(%rsp)
movq 8(%rsp), %r11
movq 80(%rsp), %r10
movq %r10, 40(%r11)
movq $5, 96(%rsp)
movq 8(%rsp), %r11
movq 96(%rsp), %r10
movq %r10, 48(%r11)
movq $6, 112(%rsp)
movq 8(%rsp), %r11
movq 112(%rsp), %r10
movq %r10, 56(%r11)
movq $7, 128(%rsp)
movq 8(%rsp), %r11
movq 128(%rsp), %r10
movq %r10, 64(%r11)
movq $8, 144(%rsp)
movq 8(%rsp), %r11
movq 144(%rsp), %r10
movq %r10, 72(%r11)
movq $9, 160(%rsp)
movq 8(%rsp), %r11
movq 160(%rsp), %r10
movq %r10, 80(%r11)
movq $10, 176(%rsp)
movq 8(%rsp), %r11
movq 176(%rsp), %r10
movq %r10, 88(%r11)
movq $11, 192(%rsp)
movq 8(%rsp), %r11
movq 192(%rsp), %r10
movq %r10, 96(%r11)
movq $12, 208(%rsp)
movq 8(%rsp), %r11
movq 208(%rsp), %r10
movq %r10, 104(%r11)
movq $13, 224(%rsp)
movq 8(%rsp), %r11
movq 224(%rsp), %r10
movq %r10, 112(%r11)
movq $14, 240(%rsp)
movq 8(%rsp), %r11
movq 240(%rsp), %r10
movq %r10, 120(%r11)
movq $15, 256(%rsp)
movq 8(%rsp), %r11
movq 256(%rsp), %r10
movq %r10, 128(%r11)
movq $16, 272(%rsp)
movq 8(%rsp), %r11
movq 272(%rsp), %r10
movq %r10, 136(%r11)
movq $17, 288(%rsp)
movq 8(%rsp), %r11
movq 288(%rsp), %r10
movq %r10, 144(%r11)
movq $18, 304(%rsp)
movq 8(%rsp), %r11
movq 304(%rsp), %r10
movq %r10, 152(%r11)
movq $19, 320(%rsp)
movq 8(%rsp), %r11
movq 320(%rsp), %r10
movq %r10, 160(%r11)
movq $20, 336(%rsp)
movq 8(%rsp), %r11
movq 336(%rsp), %r10
movq %r10, 168(%r11)
movq $21, 352(%rsp)
movq 8(%rsp), %r11
movq 352(%rsp), %r10
movq %r10, 176(%r11)
movq $22, 368(%rsp)
movq 8(%rsp), %r11
movq 368(%rsp), %r10
movq %r10, 184(%r11)
movq $23, 384(%rsp)
movq 8(%rsp), %r11
movq 384(%rsp), %r10
movq %r10, 192(%r11)
movq $24, 400(%rsp)
movq 8(%rsp), %r11
movq 400(%rsp), %r10
movq %r10, 200(%r11)
movq $25, 416(%rsp)
movq 8(%rsp), %r11
movq 416(%rsp), %r10
movq %r10, 208(%r11)
movq $26, 432(%rsp)
movq 8(%rsp), %r11
movq 432(%rsp), %r10
movq %r10, 216(%r11)
movq $27, 448(%rsp)
movq 8(%rsp), %r11
movq 448(%rsp), %r10
movq %r10, 224(%r11)
movq $28, 464(%rsp)
movq 8(%rsp), %r11
movq 464(%rsp), %r10
movq %r10, 232(%r11)
movq $29, 480(%rsp)
movq 8(%rsp), %r11
movq 480(%rsp), %r10
movq %r10, 240(%r11)
movq $30, 496(%rsp)
movq 8(%rsp), %r11
movq 496(%rsp), %r10
movq %r10, 248(%r11)
movq $31, 512(%rsp)
movq 8(%rsp), %r11
movq 512(%rsp), %r10
movq %r10, 256(%r11)
movq $32, 528(%rsp)
movq 8(%rsp), %r11
movq 528(%rsp), %r10
movq %r10, 264(%r11)
movq $33, 544(%rsp)
movq 8(%rsp), %r11
movq 544(%rsp), %r10
movq %r10, 272(%r11)
movq $34, 560(%rsp)
movq 8(%rsp), %r11
movq 560(%rsp), %r10
movq %r10, 280(%r11)
movq $35, 576(%rsp)
movq 8(%rsp), %r11
movq 576(%rsp), %r10
movq %r10, 288(%r11)
movq $36, 592(%rsp)
movq 8(%rsp), %r11
movq 592(%rsp), %r10
movq %r10, 296(%r11)
movq $37, 608(%rsp)
movq 8(%rsp), %r11
movq 608(%rsp), %r10
movq %r10, 304(%r11)
movq $38, 624(%rsp)
movq 8(%rsp), %r11
movq 624(%rsp), %r10
movq %r10, 312(%r11)
movq $39, 640(%rsp)
movq 8(%rsp), %r11
movq 640(%rsp), %r10
movq %r10, 320(%r11)
movq $40, 656(%rsp)
movq 8(%rsp), %r11
movq 656(%rsp), %r10
movq %r10, 328(%r11)
movq $41, 672(%rsp)
movq 8(%rsp), %r11
movq 672(%rsp), %r10
movq %r10, 336(%r11)
movq $42, 688(%rsp)
movq 8(%rsp), %r11
movq 688(%rsp), %r10
movq %r10, 344(%r11)
movq $43, 704(%rsp)
movq 8(%rsp), %r11
movq 704(%rsp), %r10
movq %r10, 352(%r11)
movq $44, 720(%rsp)
movq 8(%rsp), %r11
movq 720(%rsp), %r10
movq %r10, 360(%r11)
movq $45, 736(%rsp)
movq 8(%rsp), %r11
movq 736(%rsp), %r10
movq %r10, 368(%r11)
movq $46, 752(%rsp)
movq 8(%rsp), %r11
movq 752(%rsp), %r10
movq %r10, 376(%r11)
movq $47, 768(%rsp)
movq 8(%rsp), %r11
movq 768(%rsp), %r10
movq %r10, 384(%r11)
movq $48, 784(%rsp)
movq 8(%rsp), %r11
movq 784(%rsp), %r10
movq %r10, 392(%r11)
movq $49, 800(%rsp)
movq 8(%rsp), %r11
movq 800(%rsp), %r10
movq %r10, 400(%r11)
movq $50, 816(%rsp)
movq 8(%rsp), %r11
movq 816(%rsp), %r10
movq %r10, 408(%r11)
movq $51, 832(%rsp)
movq 8(%rsp), %r11
movq 832(%rsp), %r10
movq %r10, 416(%r11)
movq $52, 848(%rsp)
movq 8(%rsp), %r11
movq 848(%rsp), %r10
movq %r10, 424(%r11)
movq $53, 864(%rsp)
movq 8(%rsp), %r11
movq 864(%rsp), %r10
movq %r10, 432(%r11)
movq $54, 880(%rsp)
movq 8(%rsp), %r11
movq 880(%rsp), %r10
movq %r10, 440(%r11)
movq $55, 896(%rsp)
movq 8(%rsp), %r11
movq 896(%rsp), %r10
movq %r10, 448(%r11)
movq $56, 912(%rsp)
movq 8(%rsp), %r11
movq 912(%rsp), %r10
movq %r10, 456(%r11)
movq $57, 928(%rsp)
movq 8(%rsp), %r11
movq 928(%rsp), %r10
movq %r10, 464(%r11)
movq $58, 944(%rsp)
movq 8(%rsp), %r11
movq 944(%rsp), %r10
movq %r10, 472(%r11)
movq $59, 960(%rsp)
movq 8(%rsp), %r11
movq 960(%rsp), %r10
movq %r10, 480(%r11)
movq $60, 976(%rsp)
movq 8(%rsp), %r11
movq 976(%rsp), %r10
movq %r10, 488(%r11)
movq $61, 992(%rsp)
movq 8(%rsp), %r11
movq 992(%rsp), %r10
movq %r10, 496(%r11)
movq $62, 1008(%rsp)
movq 8(%rsp), %r11
movq 1008(%rsp), %r10
movq %r10, 504(%r11)
movq $63, 1024(%rsp)
movq 8(%rsp), %r11
movq 1024(%rsp), %r10
movq %r10, 512(%r11)
movq $64, 1040(%rsp)
movq 8(%rsp), %r11
movq 1040(%rsp), %r10
movq %r10, 520(%r11)
movq $65, 1056(%rsp)
movq 8(%rsp), %r11
movq 1056(%rsp), %r10
movq %r10, 528(%r11)
movq $66, 1072(%rsp)
movq 8(%rsp), %r11
movq 1072(%rsp), %r10
movq %r10, 536(%r11)
movq $67, 1088(%rsp)
movq 8(%rsp), %r11
movq 1088(%rsp), %r10
movq %r10, 544(%r11)
movq $68, 1104(%rsp)
movq 8(%rsp), %r11
movq 1104(%rsp), %r10
movq %r10, 552(%r11)
movq $69, 1120(%rsp)
movq 8(%rsp), %r11
movq 1120(%rsp), %r10
movq %r10, 560(%r11)
movq $70, 1136(%rsp)
movq 8(%rsp), %r11
movq 1136(%rsp), %r10
movq %r10, 568(%r11)
movq $71, 1152(%rsp)
movq 8(%rsp), %r11
movq 1152(%rsp), %r10
movq %r10, 576(%r11)
movq $72, 1168(%rsp)
movq 8(%rsp), %r11
movq 1168(%rsp), %r10
movq %r10, 584(%r11)
movq $73, 1184(%rsp)
movq 8(%rsp), %r11
movq 1184(%rsp), %r10
movq %r10, 592(%r11)
movq $74, 1200(%rsp)
movq 8(%rsp), %r11
movq 1200(%rsp), %r10
movq %r10, 600(%r11)
movq $75, %r13
movq 8(%rsp), %r11
movq %r13, %r10
movq %r10, 608(%r11)
movq $76, 1224(%rsp)
movq 8(%rsp), %r11
movq 1224(%rsp), %r10
movq %r10, 616(%r11)
movq $77, 1240(%rsp)
movq 8(%rsp), %r11
movq 1240(%rsp), %r10
movq %r10, 624(%r11)
movq $78, 1256(%rsp)
movq 8(%rsp), %r11
movq 1256(%rsp), %r10
movq %r10, 632(%r11)
movq $79, 1272(%rsp)
movq 8(%rsp), %r11
movq 1272(%rsp), %r10
movq %r10, 640(%r11)
movq $80, 1288(%rsp)
movq 8(%rsp), %r11
movq 1288(%rsp), %r10
movq %r10, 648(%r11)
movq $81, 1304(%rsp)
movq 8(%rsp), %r11
movq 1304(%rsp), %r10
movq %r10, 656(%r11)
movq $82, 1320(%rsp)
movq 8(%rsp), %r11
movq 1320(%rsp), %r10
movq %r10, 664(%r11)
movq $83, 1336(%rsp)
movq 8(%rsp), %r11
movq 1336(%rsp), %r10
movq %r10, 672(%r11)
movq $84, 1352(%rsp)
movq 8(%rsp), %r11
movq 1352(%rsp), %r10
movq %r10, 680(%r11)
movq $85, 1368(%rsp)
movq 8(%rsp), %r11
movq 1368(%rsp), %r10
movq %r10, 688(%r11)
movq $86, 1384(%rsp)
movq 8(%rsp), %r11
movq 1384(%rsp), %r10
movq %r10, 696(%r11)
movq $87, 1400(%rsp)
movq 8(%rsp), %r11
movq 1400(%rsp), %r10
movq %r10, 704(%r11)
movq $88, 1416(%rsp)
movq 8(%rsp), %r11
movq 1416(%rsp), %r10
movq %r10, 712(%r11)
movq $89, 1432(%rsp)
movq 8(%rsp), %r11
movq 1432(%rsp), %r10
movq %r10, 720(%r11)
movq $90, 1448(%rsp)
movq 8(%rsp), %r11
movq 1448(%rsp), %r10
movq %r10, 728(%r11)
movq $91, %r9
movq 8(%rsp), %r11
movq %r9, %r10
movq %r10, 736(%r11)
movq $92, 1472(%rsp)
movq 8(%rsp), %r11
movq 1472(%rsp), %r10
movq %r10, 744(%r11)
movq $93, 1488(%rsp)
movq 8(%rsp), %r11
movq 1488(%rsp), %r10
movq %r10, 752(%r11)
movq $94, 1504(%rsp)
movq 8(%rsp), %r11
movq 1504(%rsp), %r10
movq %r10, 760(%r11)
movq $95, 1520(%rsp)
movq 8(%rsp), %r11
movq 1520(%rsp), %r10
movq %r10, 768(%r11)
movq $96, 1536(%rsp)
movq 8(%rsp), %r11
movq 1536(%rsp), %r10
movq %r10, 776(%r11)
movq $97, 1552(%rsp)
movq 8(%rsp), %r11
movq 1552(%rsp), %r10
movq %r10, 784(%r11)
movq $98, 1568(%rsp)
movq 8(%rsp), %r11
movq 1568(%rsp), %r10
movq %r10, 792(%r11)
movq $99, 1584(%rsp)
movq 8(%rsp), %r11
movq 1584(%rsp), %r10
movq %r10, 800(%r11)
movq $100, 1600(%rsp)
movq 8(%rsp), %r11
movq 1600(%rsp), %r10
movq %r10, 808(%r11)
movq $101, 1616(%rsp)
movq 8(%rsp), %r11
movq 1616(%rsp), %r10
movq %r10, 816(%r11)
movq $102, 1632(%rsp)
movq 8(%rsp), %r11
movq 1632(%rsp), %r10
movq %r10, 824(%r11)
movq $103, 1648(%rsp)
movq 8(%rsp), %r11
movq 1648(%rsp), %r10
movq %r10, 832(%r11)
movq $104, 1664(%rsp)
movq 8(%rsp), %r11
movq 1664(%rsp), %r10
movq %r10, 840(%r11)
movq $105, 1680(%rsp)
movq 8(%rsp), %r11
movq 1680(%rsp), %r10
movq %r10, 848(%r11)
movq $106, 1696(%rsp)
movq 8(%rsp), %r11
movq 1696(%rsp), %r10
movq %r10, 856(%r11)
movq $107, 1712(%rsp)
movq 8(%rsp), %r11
movq 1712(%rsp), %r10
movq %r10, 864(%r11)
movq $108, 1728(%rsp)
movq 8(%rsp), %r11
movq 1728(%rsp), %r10
movq %r10, 872(%r11)
movq $109, 1744(%rsp)
movq 8(%rsp), %r11
movq 1744(%rsp), %r10
movq %r10, 880(%r11)
movq $110, 1760(%rsp)
movq 8(%rsp), %r11
movq 1760(%rsp), %r10
movq %r10, 888(%r11)
movq $111, 1776(%rsp)
movq 8(%rsp), %r11
movq 1776(%rsp), %r10
movq %r10, 896(%r11)
movq $112, 1792(%rsp)
movq 8(%rsp), %r11
movq 1792(%rsp), %r10
movq %r10, 904(%r11)
movq $113, 1808(%rsp)
movq 8(%rsp), %r11
movq 1808(%rsp), %r10
movq %r10, 912(%r11)
movq $114, 1824(%rsp)
movq 8(%rsp), %r11
movq 1824(%rsp), %r10
movq %r10, 920(%r11)
movq $115, 1840(%rsp)
movq 8(%rsp), %r11
movq 1840(%rsp), %r10
movq %r10, 928(%r11)
movq $116, 1856(%rsp)
movq 8(%rsp), %r11
movq 1856(%rsp), %r10
movq %r10, 936(%r11)
movq $117, 1872(%rsp)
movq 8(%rsp), %r11
movq 1872(%rsp), %r10
movq %r10, 944(%r11)
movq $118, 1888(%rsp)
movq 8(%rsp), %r11
movq 1888(%rsp), %r10
movq %r10, 952(%r11)
movq $119, 1904(%rsp)
movq 8(%rsp), %r11
movq 1904(%rsp), %r10
movq %r10, 960(%r11)
movq $120, 1920(%rsp)
movq 8(%rsp), %r11
movq 1920(%rsp), %r10
movq %r10, 968(%r11)
movq $121, 1936(%rsp)
movq 8(%rsp), %r11
movq 1936(%rsp), %r10
movq %r10, 976(%r11)
movq $122, 1952(%rsp)
movq 8(%rsp), %r11
movq 1952(%rsp), %r10
movq %r10, 984(%r11)
movq $123, 1968(%rsp)
movq 8(%rsp), %r11
movq 1968(%rsp), %r10
movq %r10, 992(%r11)
movq $124, 1984(%rsp)
movq 8(%rsp), %r11
movq 1984(%rsp), %r10
movq %r10, 1000(%r11)
movq $125, 2000(%rsp)
movq 8(%rsp), %r11
movq 2000(%rsp), %r10
movq %r10, 1008(%r11)
movq $1024, 2016(%rsp)
movq free_ptr(%rip), %rax
movq %rax, 2024(%rsp)
movq 2016(%rsp), %rax
addq %rax, 2024(%rsp)
movq 2024(%rsp), %rax
cmpq from_end(%rip), %rax
jl label4
jmp label5
label4:
movq $1, %rcx
jmp label6
label5:
movq $1016, %rdi
movq %r12, %rsi
callq collect
movq $1, %rcx
jmp label6
label6:
movq free_ptr(%rip), %rax
movq %rax, 2032(%rsp)
addq $1024, free_ptr(%rip)
movq 2032(%rsp), %r11
leaq type1(%rip), %r10
movq %r10, 0(%r11)
movq $0, 2040(%rsp)
movq 2032(%rsp), %r11
movq 2040(%rsp), %r10
movq %r10, 8(%r11)
movq $1, 2056(%rsp)
movq 2032(%rsp), %r11
movq 2056(%rsp), %r10
movq %r10, 16(%r11)
movq $2, 2072(%rsp)
movq 2032(%rsp), %r11
movq 2072(%rsp), %r10
movq %r10, 24(%r11)
movq $3, 2088(%rsp)
movq 2032(%rsp), %r11
movq 2088(%rsp), %r10
movq %r10, 32(%r11)
movq $4, 2104(%rsp)
movq 2032(%rsp), %r11
movq 2104(%rsp), %r10
movq %r10, 40(%r11)
movq $5, 2120(%rsp)
movq 2032(%rsp), %r11
movq 2120(%rsp), %r10
movq %r10, 48(%r11)
movq $6, 2136(%rsp)
movq 2032(%rsp), %r11
movq 2136(%rsp), %r10
movq %r10, 56(%r11)
movq $7, 2152(%rsp)
movq 2032(%rsp), %r11
movq 2152(%rsp), %r10
movq %r10, 64(%r11)
movq $8, 2168(%rsp)
movq 2032(%rsp), %r11
movq 2168(%rsp), %r10
movq %r10, 72(%r11)
movq $9, 2184(%rsp)
movq 2032(%rsp), %r11
movq 2184(%rsp), %r10
movq %r10, 80(%r11)
movq $10, 2200(%rsp)
movq 2032(%rsp), %r11
movq 2200(%rsp), %r10
movq %r10, 88(%r11)
movq $11, 2216(%rsp)
movq 2032(%rsp), %r11
movq 2216(%rsp), %r10
movq %r10, 96(%r11)
movq $12, 2232(%rsp)
movq 2032(%rsp), %r11
movq 2232(%rsp), %r10
movq %r10, 104(%r11)
movq $13, 2248(%rsp)
movq 2032(%rsp), %r11
movq 2248(%rsp), %r10
movq %r10, 112(%r11)
movq $14, 2264(%rsp)
movq 2032(%rsp), %r11
movq 2264(%rsp), %r10
movq %r10, 120(%r11)
movq $15, 2280(%rsp)
movq 2032(%rsp), %r11
movq 2280(%rsp), %r10
movq %r10, 128(%r11)
movq $16, 2296(%rsp)
movq 2032(%rsp), %r11
movq 2296(%rsp), %r10
movq %r10, 136(%r11)
movq $17, 2312(%rsp)
movq 2032(%rsp), %r11
movq 2312(%rsp), %r10
movq %r10, 144(%r11)
movq $18, 2328(%rsp)
movq 2032(%rsp), %r11
movq 2328(%rsp), %r10
movq %r10, 152(%r11)
movq $19, 2344(%rsp)
movq 2032(%rsp), %r11
movq 2344(%rsp), %r10
movq %r10, 160(%r11)
movq $20, 2360(%rsp)
movq 2032(%rsp), %r11
movq 2360(%rsp), %r10
movq %r10, 168(%r11)
movq $21, 2376(%rsp)
movq 2032(%rsp), %r11
movq 2376(%rsp), %r10
movq %r10, 176(%r11)
movq $22, 2392(%rsp)
movq 2032(%rsp), %r11
movq 2392(%rsp), %r10
movq %r10, 184(%r11)
movq $23, 2408(%rsp)
movq 2032(%rsp), %r11
movq 2408(%rsp), %r10
movq %r10, 192(%r11)
movq $24, 2424(%rsp)
movq 2032(%rsp), %r11
movq 2424(%rsp), %r10
movq %r10, 200(%r11)
movq $25, 2440(%rsp)
movq 2032(%rsp), %r11
movq 2440(%rsp), %r10
movq %r10, 208(%r11)
movq $26, 2456(%rsp)
movq 2032(%rsp), %r11
movq 2456(%rsp), %r10
movq %r10, 216(%r11)
movq $27, 2472(%rsp)
movq 2032(%rsp), %r11
movq 2472(%rsp), %r10
movq %r10, 224(%r11)
movq $28, 2488(%rsp)
movq 2032(%rsp), %r11
movq 2488(%rsp), %r10
movq %r10, 232(%r11)
movq $29, 2504(%rsp)
movq 2032(%rsp), %r11
movq 2504(%rsp), %r10
movq %r10, 240(%r11)
movq $30, 2520(%rsp)
movq 2032(%rsp), %r11
movq 2520(%rsp), %r10
movq %r10, 248(%r11)
movq $31, 2536(%rsp)
movq 2032(%rsp), %r11
movq 2536(%rsp), %r10
movq %r10, 256(%r11)
movq $32, 2552(%rsp)
movq 2032(%rsp), %r11
movq 2552(%rsp), %r10
movq %r10, 264(%r11)
movq $33, 2568(%rsp)
movq 2032(%rsp), %r11
movq 2568(%rsp), %r10
movq %r10, 272(%r11)
movq $34, 2584(%rsp)
movq 2032(%rsp), %r11
movq 2584(%rsp), %r10
movq %r10, 280(%r11)
movq $35, 2600(%rsp)
movq 2032(%rsp), %r11
movq 2600(%rsp), %r10
movq %r10, 288(%r11)
movq $36, 2616(%rsp)
movq 2032(%rsp), %r11
movq 2616(%rsp), %r10
movq %r10, 296(%r11)
movq $37, 2632(%rsp)
movq 2032(%rsp), %r11
movq 2632(%rsp), %r10
movq %r10, 304(%r11)
movq $38, 2648(%rsp)
movq 2032(%rsp), %r11
movq 2648(%rsp), %r10
movq %r10, 312(%r11)
movq $39, 2664(%rsp)
movq 2032(%rsp), %r11
movq 2664(%rsp), %r10
movq %r10, 320(%r11)
movq $40, 2680(%rsp)
movq 2032(%rsp), %r11
movq 2680(%rsp), %r10
movq %r10, 328(%r11)
movq $41, 2696(%rsp)
movq 2032(%rsp), %r11
movq 2696(%rsp), %r10
movq %r10, 336(%r11)
movq $42, 2712(%rsp)
movq 2032(%rsp), %r11
movq 2712(%rsp), %r10
movq %r10, 344(%r11)
movq $43, 2728(%rsp)
movq 2032(%rsp), %r11
movq 2728(%rsp), %r10
movq %r10, 352(%r11)
movq $44, 2744(%rsp)
movq 2032(%rsp), %r11
movq 2744(%rsp), %r10
movq %r10, 360(%r11)
movq $45, 2760(%rsp)
movq 2032(%rsp), %r11
movq 2760(%rsp), %r10
movq %r10, 368(%r11)
movq $46, 2776(%rsp)
movq 2032(%rsp), %r11
movq 2776(%rsp), %r10
movq %r10, 376(%r11)
movq $47, 2792(%rsp)
movq 2032(%rsp), %r11
movq 2792(%rsp), %r10
movq %r10, 384(%r11)
movq $48, 2808(%rsp)
movq 2032(%rsp), %r11
movq 2808(%rsp), %r10
movq %r10, 392(%r11)
movq $49, 2824(%rsp)
movq 2032(%rsp), %r11
movq 2824(%rsp), %r10
movq %r10, 400(%r11)
movq $50, 2840(%rsp)
movq 2032(%rsp), %r11
movq 2840(%rsp), %r10
movq %r10, 408(%r11)
movq $51, 2856(%rsp)
movq 2032(%rsp), %r11
movq 2856(%rsp), %r10
movq %r10, 416(%r11)
movq $52, 2872(%rsp)
movq 2032(%rsp), %r11
movq 2872(%rsp), %r10
movq %r10, 424(%r11)
movq $53, 2888(%rsp)
movq 2032(%rsp), %r11
movq 2888(%rsp), %r10
movq %r10, 432(%r11)
movq $54, 2904(%rsp)
movq 2032(%rsp), %r11
movq 2904(%rsp), %r10
movq %r10, 440(%r11)
movq $55, 2920(%rsp)
movq 2032(%rsp), %r11
movq 2920(%rsp), %r10
movq %r10, 448(%r11)
movq $56, 2936(%rsp)
movq 2032(%rsp), %r11
movq 2936(%rsp), %r10
movq %r10, 456(%r11)
movq $57, 2952(%rsp)
movq 2032(%rsp), %r11
movq 2952(%rsp), %r10
movq %r10, 464(%r11)
movq $58, 2968(%rsp)
movq 2032(%rsp), %r11
movq 2968(%rsp), %r10
movq %r10, 472(%r11)
movq $59, 2984(%rsp)
movq 2032(%rsp), %r11
movq 2984(%rsp), %r10
movq %r10, 480(%r11)
movq $60, 3000(%rsp)
movq 2032(%rsp), %r11
movq 3000(%rsp), %r10
movq %r10, 488(%r11)
movq $61, 3016(%rsp)
movq 2032(%rsp), %r11
movq 3016(%rsp), %r10
movq %r10, 496(%r11)
movq $62, 3032(%rsp)
movq 2032(%rsp), %r11
movq 3032(%rsp), %r10
movq %r10, 504(%r11)
movq $63, 3048(%rsp)
movq 2032(%rsp), %r11
movq 3048(%rsp), %r10
movq %r10, 512(%r11)
movq $64, 3064(%rsp)
movq 2032(%rsp), %r11
movq 3064(%rsp), %r10
movq %r10, 520(%r11)
movq $65, 3080(%rsp)
movq 2032(%rsp), %r11
movq 3080(%rsp), %r10
movq %r10, 528(%r11)
movq $66, 3096(%rsp)
movq 2032(%rsp), %r11
movq 3096(%rsp), %r10
movq %r10, 536(%r11)
movq $67, 3112(%rsp)
movq 2032(%rsp), %r11
movq 3112(%rsp), %r10
movq %r10, 544(%r11)
movq $68, 3128(%rsp)
movq 2032(%rsp), %r11
movq 3128(%rsp), %r10
movq %r10, 552(%r11)
movq $69, 3144(%rsp)
movq 2032(%rsp), %r11
movq 3144(%rsp), %r10
movq %r10, 560(%r11)
movq $70, 3160(%rsp)
movq 2032(%rsp), %r11
movq 3160(%rsp), %r10
movq %r10, 568(%r11)
movq $71, 3176(%rsp)
movq 2032(%rsp), %r11
movq 3176(%rsp), %r10
movq %r10, 576(%r11)
movq $72, 3192(%rsp)
movq 2032(%rsp), %r11
movq 3192(%rsp), %r10
movq %r10, 584(%r11)
movq $73, 3208(%rsp)
movq 2032(%rsp), %r11
movq 3208(%rsp), %r10
movq %r10, 592(%r11)
movq $74, 3224(%rsp)
movq 2032(%rsp), %r11
movq 3224(%rsp), %r10
movq %r10, 600(%r11)
movq $75, 3240(%rsp)
movq 2032(%rsp), %r11
movq 3240(%rsp), %r10
movq %r10, 608(%r11)
movq $76, 3256(%rsp)
movq 2032(%rsp), %r11
movq 3256(%rsp), %r10
movq %r10, 616(%r11)
movq $77, 3272(%rsp)
movq 2032(%rsp), %r11
movq 3272(%rsp), %r10
movq %r10, 624(%r11)
movq $78, 3288(%rsp)
movq 2032(%rsp), %r11
movq 3288(%rsp), %r10
movq %r10, 632(%r11)
movq $79, 3304(%rsp)
movq 2032(%rsp), %r11
movq 3304(%rsp), %r10
movq %r10, 640(%r11)
movq $80, 3320(%rsp)
movq 2032(%rsp), %r11
movq 3320(%rsp), %r10
movq %r10, 648(%r11)
movq $81, 3336(%rsp)
movq 2032(%rsp), %r11
movq 3336(%rsp), %r10
movq %r10, 656(%r11)
movq $82, 3352(%rsp)
movq 2032(%rsp), %r11
movq 3352(%rsp), %r10
movq %r10, 664(%r11)
movq $83, 3368(%rsp)
movq 2032(%rsp), %r11
movq 3368(%rsp), %r10
movq %r10, 672(%r11)
movq $84, 3384(%rsp)
movq 2032(%rsp), %r11
movq 3384(%rsp), %r10
movq %r10, 680(%r11)
movq $85, 3400(%rsp)
movq 2032(%rsp), %r11
movq 3400(%rsp), %r10
movq %r10, 688(%r11)
movq $86, 3416(%rsp)
movq 2032(%rsp), %r11
movq 3416(%rsp), %r10
movq %r10, 696(%r11)
movq $87, 3432(%rsp)
movq 2032(%rsp), %r11
movq 3432(%rsp), %r10
movq %r10, 704(%r11)
movq $88, 3448(%rsp)
movq 2032(%rsp), %r11
movq 3448(%rsp), %r10
movq %r10, 712(%r11)
movq $89, 3464(%rsp)
movq 2032(%rsp), %r11
movq 3464(%rsp), %r10
movq %r10, 720(%r11)
movq $90, 3480(%rsp)
movq 2032(%rsp), %r11
movq 3480(%rsp), %r10
movq %r10, 728(%r11)
movq $91, 3496(%rsp)
movq 2032(%rsp), %r11
movq 3496(%rsp), %r10
movq %r10, 736(%r11)
movq $92, 3512(%rsp)
movq 2032(%rsp), %r11
movq 3512(%rsp), %r10
movq %r10, 744(%r11)
movq $93, 3528(%rsp)
movq 2032(%rsp), %r11
movq 3528(%rsp), %r10
movq %r10, 752(%r11)
movq $94, 3544(%rsp)
movq 2032(%rsp), %r11
movq 3544(%rsp), %r10
movq %r10, 760(%r11)
movq $95, 3560(%rsp)
movq 2032(%rsp), %r11
movq 3560(%rsp), %r10
movq %r10, 768(%r11)
movq $96, 3576(%rsp)
movq 2032(%rsp), %r11
movq 3576(%rsp), %r10
movq %r10, 776(%r11)
movq $97, 3592(%rsp)
movq 2032(%rsp), %r11
movq 3592(%rsp), %r10
movq %r10, 784(%r11)
movq $98, 3608(%rsp)
movq 2032(%rsp), %r11
movq 3608(%rsp), %r10
movq %r10, 792(%r11)
movq $99, 3624(%rsp)
movq 2032(%rsp), %r11
movq 3624(%rsp), %r10
movq %r10, 800(%r11)
movq $100, 3640(%rsp)
movq 2032(%rsp), %r11
movq 3640(%rsp), %r10
movq %r10, 808(%r11)
movq $101, 3656(%rsp)
movq 2032(%rsp), %r11
movq 3656(%rsp), %r10
movq %r10, 816(%r11)
movq $102, %r8
movq 2032(%rsp), %r11
movq %r8, %r10
movq %r10, 824(%r11)
movq $103, 3680(%rsp)
movq 2032(%rsp), %r11
movq 3680(%rsp), %r10
movq %r10, 832(%r11)
movq $104, 3696(%rsp)
movq 2032(%rsp), %r11
movq 3696(%rsp), %r10
movq %r10, 840(%r11)
movq $105, 3712(%rsp)
movq 2032(%rsp), %r11
movq 3712(%rsp), %r10
movq %r10, 848(%r11)
movq $106, 3728(%rsp)
movq 2032(%rsp), %r11
movq 3728(%rsp), %r10
movq %r10, 856(%r11)
movq $107, 3744(%rsp)
movq 2032(%rsp), %r11
movq 3744(%rsp), %r10
movq %r10, 864(%r11)
movq $108, 3760(%rsp)
movq 2032(%rsp), %r11
movq 3760(%rsp), %r10
movq %r10, 872(%r11)
movq $109, 3776(%rsp)
movq 2032(%rsp), %r11
movq 3776(%rsp), %r10
movq %r10, 880(%r11)
movq $110, 3792(%rsp)
movq 2032(%rsp), %r11
movq 3792(%rsp), %r10
movq %r10, 888(%r11)
movq $111, 3808(%rsp)
movq 2032(%rsp), %r11
movq 3808(%rsp), %r10
movq %r10, 896(%r11)
movq $112, 3824(%rsp)
movq 2032(%rsp), %r11
movq 3824(%rsp), %r10
movq %r10, 904(%r11)
movq $113, 3840(%rsp)
movq 2032(%rsp), %r11
movq 3840(%rsp), %r10
movq %r10, 912(%r11)
movq $114, 3856(%rsp)
movq 2032(%rsp), %r11
movq 3856(%rsp), %r10
movq %r10, 920(%r11)
movq $115, 3872(%rsp)
movq 2032(%rsp), %r11
movq 3872(%rsp), %r10
movq %r10, 928(%r11)
movq $116, 3888(%rsp)
movq 2032(%rsp), %r11
movq 3888(%rsp), %r10
movq %r10, 936(%r11)
movq $117, 3904(%rsp)
movq 2032(%rsp), %r11
movq 3904(%rsp), %r10
movq %r10, 944(%r11)
movq $118, 3920(%rsp)
movq 2032(%rsp), %r11
movq 3920(%rsp), %r10
movq %r10, 952(%r11)
movq $119, 3936(%rsp)
movq 2032(%rsp), %r11
movq 3936(%rsp), %r10
movq %r10, 960(%r11)
movq $120, 3952(%rsp)
movq 2032(%rsp), %r11
movq 3952(%rsp), %r10
movq %r10, 968(%r11)
movq $121, 3968(%rsp)
movq 2032(%rsp), %r11
movq 3968(%rsp), %r10
movq %r10, 976(%r11)
movq $122, 3984(%rsp)
movq 2032(%rsp), %r11
movq 3984(%rsp), %r10
movq %r10, 984(%r11)
movq $123, 4000(%rsp)
movq 2032(%rsp), %r11
movq 4000(%rsp), %r10
movq %r10, 992(%r11)
movq $124, 4016(%rsp)
movq 2032(%rsp), %r11
movq 4016(%rsp), %r10
movq %r10, 1000(%r11)
movq $125, 4032(%rsp)
movq 2032(%rsp), %r11
movq 4032(%rsp), %r10
movq %r10, 1008(%r11)
movq $126, 4048(%rsp)
movq 2032(%rsp), %r11
movq 4048(%rsp), %r10
movq %r10, 1016(%r11)
movq $1032, 4064(%rsp)
movq free_ptr(%rip), %rax
movq %rax, 4072(%rsp)
movq 4064(%rsp), %rax
addq %rax, 4072(%rsp)
movq 4072(%rsp), %rax
cmpq from_end(%rip), %rax
jl label7
jmp label8
label7:
movq $1, %rcx
jmp label9
label8:
movq $1024, %rdi
movq %r12, %rsi
callq collect
movq $1, %rcx
jmp label9
label9:
movq free_ptr(%rip), %rax
movq %rax, 4080(%rsp)
addq $1032, free_ptr(%rip)
movq 4080(%rsp), %r11
leaq type2(%rip), %r10
movq %r10, 0(%r11)
movq $0, 4088(%rsp)
movq 4080(%rsp), %r11
movq 4088(%rsp), %r10
movq %r10, 8(%r11)
movq $1, 4104(%rsp)
movq 4080(%rsp), %r11
movq 4104(%rsp), %r10
movq %r10, 16(%r11)
movq $2, 4120(%rsp)
movq 4080(%rsp), %r11
movq 4120(%rsp), %r10
movq %r10, 24(%r11)
movq $3, 4136(%rsp)
movq 4080(%rsp), %r11
movq 4136(%rsp), %r10
movq %r10, 32(%r11)
movq $4, 4152(%rsp)
movq 4080(%rsp), %r11
movq 4152(%rsp), %r10
movq %r10, 40(%r11)
movq $5, 4168(%rsp)
movq 4080(%rsp), %r11
movq 4168(%rsp), %r10
movq %r10, 48(%r11)
movq $6, 4184(%rsp)
movq 4080(%rsp), %r11
movq 4184(%rsp), %r10
movq %r10, 56(%r11)
movq $7, 4200(%rsp)
movq 4080(%rsp), %r11
movq 4200(%rsp), %r10
movq %r10, 64(%r11)
movq $8, 4216(%rsp)
movq 4080(%rsp), %r11
movq 4216(%rsp), %r10
movq %r10, 72(%r11)
movq $9, 4232(%rsp)
movq 4080(%rsp), %r11
movq 4232(%rsp), %r10
movq %r10, 80(%r11)
movq $10, %r15
movq 4080(%rsp), %r11
movq %r15, %r10
movq %r10, 88(%r11)
movq $11, 4256(%rsp)
movq 4080(%rsp), %r11
movq 4256(%rsp), %r10
movq %r10, 96(%r11)
movq $12, 4272(%rsp)
movq 4080(%rsp), %r11
movq 4272(%rsp), %r10
movq %r10, 104(%r11)
movq $13, 4288(%rsp)
movq 4080(%rsp), %r11
movq 4288(%rsp), %r10
movq %r10, 112(%r11)
movq $14, 4304(%rsp)
movq 4080(%rsp), %r11
movq 4304(%rsp), %r10
movq %r10, 120(%r11)
movq $15, 4320(%rsp)
movq 4080(%rsp), %r11
movq 4320(%rsp), %r10
movq %r10, 128(%r11)
movq $16, 4336(%rsp)
movq 4080(%rsp), %r11
movq 4336(%rsp), %r10
movq %r10, 136(%r11)
movq $17, 4352(%rsp)
movq 4080(%rsp), %r11
movq 4352(%rsp), %r10
movq %r10, 144(%r11)
movq $18, 4368(%rsp)
movq 4080(%rsp), %r11
movq 4368(%rsp), %r10
movq %r10, 152(%r11)
movq $19, 4384(%rsp)
movq 4080(%rsp), %r11
movq 4384(%rsp), %r10
movq %r10, 160(%r11)
movq $20, 4400(%rsp)
movq 4080(%rsp), %r11
movq 4400(%rsp), %r10
movq %r10, 168(%r11)
movq $21, 4416(%rsp)
movq 4080(%rsp), %r11
movq 4416(%rsp), %r10
movq %r10, 176(%r11)
movq $22, 4432(%rsp)
movq 4080(%rsp), %r11
movq 4432(%rsp), %r10
movq %r10, 184(%r11)
movq $23, 4448(%rsp)
movq 4080(%rsp), %r11
movq 4448(%rsp), %r10
movq %r10, 192(%r11)
movq $24, 4464(%rsp)
movq 4080(%rsp), %r11
movq 4464(%rsp), %r10
movq %r10, 200(%r11)
movq $25, 4480(%rsp)
movq 4080(%rsp), %r11
movq 4480(%rsp), %r10
movq %r10, 208(%r11)
movq $26, 4496(%rsp)
movq 4080(%rsp), %r11
movq 4496(%rsp), %r10
movq %r10, 216(%r11)
movq $27, 4512(%rsp)
movq 4080(%rsp), %r11
movq 4512(%rsp), %r10
movq %r10, 224(%r11)
movq $28, 4528(%rsp)
movq 4080(%rsp), %r11
movq 4528(%rsp), %r10
movq %r10, 232(%r11)
movq $29, 4544(%rsp)
movq 4080(%rsp), %r11
movq 4544(%rsp), %r10
movq %r10, 240(%r11)
movq $30, 4560(%rsp)
movq 4080(%rsp), %r11
movq 4560(%rsp), %r10
movq %r10, 248(%r11)
movq $31, 4576(%rsp)
movq 4080(%rsp), %r11
movq 4576(%rsp), %r10
movq %r10, 256(%r11)
movq $32, 4592(%rsp)
movq 4080(%rsp), %r11
movq 4592(%rsp), %r10
movq %r10, 264(%r11)
movq $33, 4608(%rsp)
movq 4080(%rsp), %r11
movq 4608(%rsp), %r10
movq %r10, 272(%r11)
movq $34, 4624(%rsp)
movq 4080(%rsp), %r11
movq 4624(%rsp), %r10
movq %r10, 280(%r11)
movq $35, 4640(%rsp)
movq 4080(%rsp), %r11
movq 4640(%rsp), %r10
movq %r10, 288(%r11)
movq $36, 4656(%rsp)
movq 4080(%rsp), %r11
movq 4656(%rsp), %r10
movq %r10, 296(%r11)
movq $37, 4672(%rsp)
movq 4080(%rsp), %r11
movq 4672(%rsp), %r10
movq %r10, 304(%r11)
movq $38, 4688(%rsp)
movq 4080(%rsp), %r11
movq 4688(%rsp), %r10
movq %r10, 312(%r11)
movq $39, 4704(%rsp)
movq 4080(%rsp), %r11
movq 4704(%rsp), %r10
movq %r10, 320(%r11)
movq $40, 4720(%rsp)
movq 4080(%rsp), %r11
movq 4720(%rsp), %r10
movq %r10, 328(%r11)
movq $41, 4736(%rsp)
movq 4080(%rsp), %r11
movq 4736(%rsp), %r10
movq %r10, 336(%r11)
movq $42, 4752(%rsp)
movq 4080(%rsp), %r11
movq 4752(%rsp), %r10
movq %r10, 344(%r11)
movq $43, 4768(%rsp)
movq 4080(%rsp), %r11
movq 4768(%rsp), %r10
movq %r10, 352(%r11)
movq $44, 4784(%rsp)
movq 4080(%rsp), %r11
movq 4784(%rsp), %r10
movq %r10, 360(%r11)
movq $45, 4800(%rsp)
movq 4080(%rsp), %r11
movq 4800(%rsp), %r10
movq %r10, 368(%r11)
movq $46, 4816(%rsp)
movq 4080(%rsp), %r11
movq 4816(%rsp), %r10
movq %r10, 376(%r11)
movq $47, 4832(%rsp)
movq 4080(%rsp), %r11
movq 4832(%rsp), %r10
movq %r10, 384(%r11)
movq $48, 4848(%rsp)
movq 4080(%rsp), %r11
movq 4848(%rsp), %r10
movq %r10, 392(%r11)
movq $49, 4864(%rsp)
movq 4080(%rsp), %r11
movq 4864(%rsp), %r10
movq %r10, 400(%r11)
movq $50, 4880(%rsp)
movq 4080(%rsp), %r11
movq 4880(%rsp), %r10
movq %r10, 408(%r11)
movq $51, 4896(%rsp)
movq 4080(%rsp), %r11
movq 4896(%rsp), %r10
movq %r10, 416(%r11)
movq $52, 4912(%rsp)
movq 4080(%rsp), %r11
movq 4912(%rsp), %r10
movq %r10, 424(%r11)
movq $53, 4928(%rsp)
movq 4080(%rsp), %r11
movq 4928(%rsp), %r10
movq %r10, 432(%r11)
movq $54, 4944(%rsp)
movq 4080(%rsp), %r11
movq 4944(%rsp), %r10
movq %r10, 440(%r11)
movq $55, 4960(%rsp)
movq 4080(%rsp), %r11
movq 4960(%rsp), %r10
movq %r10, 448(%r11)
movq $56, 4976(%rsp)
movq 4080(%rsp), %r11
movq 4976(%rsp), %r10
movq %r10, 456(%r11)
movq $57, 4992(%rsp)
movq 4080(%rsp), %r11
movq 4992(%rsp), %r10
movq %r10, 464(%r11)
movq $58, 5008(%rsp)
movq 4080(%rsp), %r11
movq 5008(%rsp), %r10
movq %r10, 472(%r11)
movq $59, 5024(%rsp)
movq 4080(%rsp), %r11
movq 5024(%rsp), %r10
movq %r10, 480(%r11)
movq $60, 5040(%rsp)
movq 4080(%rsp), %r11
movq 5040(%rsp), %r10
movq %r10, 488(%r11)
movq $61, 5056(%rsp)
movq 4080(%rsp), %r11
movq 5056(%rsp), %r10
movq %r10, 496(%r11)
movq $62, 5072(%rsp)
movq 4080(%rsp), %r11
movq 5072(%rsp), %r10
movq %r10, 504(%r11)
movq $63, 5088(%rsp)
movq 4080(%rsp), %r11
movq 5088(%rsp), %r10
movq %r10, 512(%r11)
movq $64, 5104(%rsp)
movq 4080(%rsp), %r11
movq 5104(%rsp), %r10
movq %r10, 520(%r11)
movq $65, 5120(%rsp)
movq 4080(%rsp), %r11
movq 5120(%rsp), %r10
movq %r10, 528(%r11)
movq $66, 5136(%rsp)
movq 4080(%rsp), %r11
movq 5136(%rsp), %r10
movq %r10, 536(%r11)
movq $67, 5152(%rsp)
movq 4080(%rsp), %r11
movq 5152(%rsp), %r10
movq %r10, 544(%r11)
movq $68, 5168(%rsp)
movq 4080(%rsp), %r11
movq 5168(%rsp), %r10
movq %r10, 552(%r11)
movq $69, 5184(%rsp)
movq 4080(%rsp), %r11
movq 5184(%rsp), %r10
movq %r10, 560(%r11)
movq $70, 5200(%rsp)
movq 4080(%rsp), %r11
movq 5200(%rsp), %r10
movq %r10, 568(%r11)
movq $71, 5216(%rsp)
movq 4080(%rsp), %r11
movq 5216(%rsp), %r10
movq %r10, 576(%r11)
movq $72, 5232(%rsp)
movq 4080(%rsp), %r11
movq 5232(%rsp), %r10
movq %r10, 584(%r11)
movq $73, 5248(%rsp)
movq 4080(%rsp), %r11
movq 5248(%rsp), %r10
movq %r10, 592(%r11)
movq $74, 5264(%rsp)
movq 4080(%rsp), %r11
movq 5264(%rsp), %r10
movq %r10, 600(%r11)
movq $75, 5280(%rsp)
movq 4080(%rsp), %r11
movq 5280(%rsp), %r10
movq %r10, 608(%r11)
movq $76, 5296(%rsp)
movq 4080(%rsp), %r11
movq 5296(%rsp), %r10
movq %r10, 616(%r11)
movq $77, 5312(%rsp)
movq 4080(%rsp), %r11
movq 5312(%rsp), %r10
movq %r10, 624(%r11)
movq $78, 5328(%rsp)
movq 4080(%rsp), %r11
movq 5328(%rsp), %r10
movq %r10, 632(%r11)
movq $79, 5344(%rsp)
movq 4080(%rsp), %r11
movq 5344(%rsp), %r10
movq %r10, 640(%r11)
movq $80, 5360(%rsp)
movq 4080(%rsp), %r11
movq 5360(%rsp), %r10
movq %r10, 648(%r11)
movq $81, 5376(%rsp)
movq 4080(%rsp), %r11
movq 5376(%rsp), %r10
movq %r10, 656(%r11)
movq $82, 5392(%rsp)
movq 4080(%rsp), %r11
movq 5392(%rsp), %r10
movq %r10, 664(%r11)
movq $83, 5408(%rsp)
movq 4080(%rsp), %r11
movq 5408(%rsp), %r10
movq %r10, 672(%r11)
movq $84, 5424(%rsp)
movq 4080(%rsp), %r11
movq 5424(%rsp), %r10
movq %r10, 680(%r11)
movq $85, 5440(%rsp)
movq 4080(%rsp), %r11
movq 5440(%rsp), %r10
movq %r10, 688(%r11)
movq $86, 5456(%rsp)
movq 4080(%rsp), %r11
movq 5456(%rsp), %r10
movq %r10, 696(%r11)
movq $87, 5472(%rsp)
movq 4080(%rsp), %r11
movq 5472(%rsp), %r10
movq %r10, 704(%r11)
movq $88, 5488(%rsp)
movq 4080(%rsp), %r11
movq 5488(%rsp), %r10
movq %r10, 712(%r11)
movq $89, 5504(%rsp)
movq 4080(%rsp), %r11
movq 5504(%rsp), %r10
movq %r10, 720(%r11)
movq $90, 5520(%rsp)
movq 4080(%rsp), %r11
movq 5520(%rsp), %r10
movq %r10, 728(%r11)
movq $91, 5536(%rsp)
movq 4080(%rsp), %r11
movq 5536(%rsp), %r10
movq %r10, 736(%r11)
movq $92, 5552(%rsp)
movq 4080(%rsp), %r11
movq 5552(%rsp), %r10
movq %r10, 744(%r11)
movq $93, 5568(%rsp)
movq 4080(%rsp), %r11
movq 5568(%rsp), %r10
movq %r10, 752(%r11)
movq $94, 5584(%rsp)
movq 4080(%rsp), %r11
movq 5584(%rsp), %r10
movq %r10, 760(%r11)
movq $95, 5600(%rsp)
movq 4080(%rsp), %r11
movq 5600(%rsp), %r10
movq %r10, 768(%r11)
movq $96, 5616(%rsp)
movq 4080(%rsp), %r11
movq 5616(%rsp), %r10
movq %r10, 776(%r11)
movq $97, 5632(%rsp)
movq 4080(%rsp), %r11
movq 5632(%rsp), %r10
movq %r10, 784(%r11)
movq $98, 5648(%rsp)
movq 4080(%rsp), %r11
movq 5648(%rsp), %r10
movq %r10, 792(%r11)
movq $99, 5664(%rsp)
movq 4080(%rsp), %r11
movq 5664(%rsp), %r10
movq %r10, 800(%r11)
movq $100, 5680(%rsp)
movq 4080(%rsp), %r11
movq 5680(%rsp), %r10
movq %r10, 808(%r11)
movq $101, 5696(%rsp)
movq 4080(%rsp), %r11
movq 5696(%rsp), %r10
movq %r10, 816(%r11)
movq $102, 5712(%rsp)
movq 4080(%rsp), %r11
movq 5712(%rsp), %r10
movq %r10, 824(%r11)
movq $103, 5728(%rsp)
movq 4080(%rsp), %r11
movq 5728(%rsp), %r10
movq %r10, 832(%r11)
movq $104, 5744(%rsp)
movq 4080(%rsp), %r11
movq 5744(%rsp), %r10
movq %r10, 840(%r11)
movq $105, 5760(%rsp)
movq 4080(%rsp), %r11
movq 5760(%rsp), %r10
movq %r10, 848(%r11)
movq $106, 5776(%rsp)
movq 4080(%rsp), %r11
movq 5776(%rsp), %r10
movq %r10, 856(%r11)
movq $107, 5792(%rsp)
movq 4080(%rsp), %r11
movq 5792(%rsp), %r10
movq %r10, 864(%r11)
movq $108, 5808(%rsp)
movq 4080(%rsp), %r11
movq 5808(%rsp), %r10
movq %r10, 872(%r11)
movq $109, %rdx
movq 4080(%rsp), %r11
movq %rdx, %r10
movq %r10, 880(%r11)
movq $110, 5832(%rsp)
movq 4080(%rsp), %r11
movq 5832(%rsp), %r10
movq %r10, 888(%r11)
movq $111, 5848(%rsp)
movq 4080(%rsp), %r11
movq 5848(%rsp), %r10
movq %r10, 896(%r11)
movq $112, 5864(%rsp)
movq 4080(%rsp), %r11
movq 5864(%rsp), %r10
movq %r10, 904(%r11)
movq $113, %rsi
movq 4080(%rsp), %r11
movq %rsi, %r10
movq %r10, 912(%r11)
movq $114, 5888(%rsp)
movq 4080(%rsp), %r11
movq 5888(%rsp), %r10
movq %r10, 920(%r11)
movq $115, 5904(%rsp)
movq 4080(%rsp), %r11
movq 5904(%rsp), %r10
movq %r10, 928(%r11)
movq $116, 5920(%rsp)
movq 4080(%rsp), %r11
movq 5920(%rsp), %r10
movq %r10, 936(%r11)
movq $117, 5936(%rsp)
movq 4080(%rsp), %r11
movq 5936(%rsp), %r10
movq %r10, 944(%r11)
movq $118, 5952(%rsp)
movq 4080(%rsp), %r11
movq 5952(%rsp), %r10
movq %r10, 952(%r11)
movq $119, 5968(%rsp)
movq 4080(%rsp), %r11
movq 5968(%rsp), %r10
movq %r10, 960(%r11)
movq $120, 5984(%rsp)
movq 4080(%rsp), %r11
movq 5984(%rsp), %r10
movq %r10, 968(%r11)
movq $121, 6000(%rsp)
movq 4080(%rsp), %r11
movq 6000(%rsp), %r10
movq %r10, 976(%r11)
movq $122, 6016(%rsp)
movq 4080(%rsp), %r11
movq 6016(%rsp), %r10
movq %r10, 984(%r11)
movq $123, 6032(%rsp)
movq 4080(%rsp), %r11
movq 6032(%rsp), %r10
movq %r10, 992(%r11)
movq $124, 6048(%rsp)
movq 4080(%rsp), %r11
movq 6048(%rsp), %r10
movq %r10, 1000(%r11)
movq $125, 6064(%rsp)
movq 4080(%rsp), %r11
movq 6064(%rsp), %r10
movq %r10, 1008(%r11)
movq $126, 6080(%rsp)
movq 4080(%rsp), %r11
movq 6080(%rsp), %r10
movq %r10, 1016(%r11)
movq $127, 6096(%rsp)
movq 4080(%rsp), %r11
movq 6096(%rsp), %r10
movq %r10, 1024(%r11)
movq 4080(%rsp), %rax
jmp end
main:
pushq %rbx
pushq %rbp
pushq %r12
movq %rsp, %rbp
subq $6112, %rsp
callq init_mem
movq rootstack_start(%rip), %r12
jmp body
end:
movq T_Vector(%rip), %rdi
movq %rax, %rsi
callq print_value
addq $6112, %rsp
popq %r12
popq %rbp
popq %rbx
retq



