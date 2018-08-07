   .syntax unified
   .arch armv6
   .fpu vfp
   @roee landesman
   .global main

main:
   push {r6, r7, lr}

loop:
   ldr r0, =prompt1     @ number 1 print message
   bl printf

   ldr r0, =scannumber  @ scan the number
   mov r1, sp
   bl scanf
   ldr r6, [sp]         @ store number 1 in register r6

   ldr r0, =prompt2     @ number 2 print message
   bl printf

   ldr r0, =scannumber
   mov r1, sp
   bl scanf
   ldr r7, [sp]         @ store number 2 in register r7

   ldr r0, =operation   @ ask for operation from user
   bl printf

   ldr r0, =scanchar    @ scan for operation
   mov r1, sp
   bl scanf

   ldr r0, =addSign @ Load the address for addition sign
   ldrb r0, [r0]    @ Load the actual value for '+'
   ldrb r1, [sp]    @ Save the value from the last scan (operation-scan)
   cmp r1, r0       @ Compare the two!
   beq addbranch    @ Branch if equal

   ldr r0, =subSign @ Same as above, but with subtraction
   ldrb r0, [r0]
   ldrb r1, [sp]
   cmp r1, r0
   beq subbranch


   ldr r0, =multSign  @ Same as above, but with multiplication
   ldrb r0, [r0]
   ldrb r1, [sp]
   cmp r1, r0
   beq multbranch

   ldr r0, =invalid   @ Invalid message/print
   bl printf
   b loop

addbranch:
   mov r0, r6
   mov r1, r7
   bl intadd

   mov r1, r0
   ldr r0, =result
   bl printf

   b finalQ
subbranch:
   mov r0, r6
   mov r1, r7
   bl intsub

   mov r1, r0
   ldr r0, =result
   bl printf

   b finalQ
multbranch:
   mov r0, r6
   mov r1, r7
   bl intmul

   mov r1, r0
   ldr r0, =result
   bl printf

   b finalQ

finalQ:
  ldr r0, =repeat
  bl printf

  ldr r0, =scanchar
  mov r1, sp
  bl scanf

  ldr r0, =yes
  ldrb r0, [r0]
  ldrb r1, [sp]
  cmp r1, r0
  beq loop
  pop {r6, r7, lr}




scanchar:
    .asciz  " %c"
scannumber:
    .asciz  " %d"
printnum:
   .asciz "\n%d"
prompt1:
  .asciz "Enter number 1 please: "
prompt2:
  .asciz "Enter number 2 please: "
operation:
  .asciz "Enter operation please: "
invalid:
  .asciz "Invalid input, please try again! \n"
result:
   .asciz "Result: %d \n"
repeat:
   .asciz "Would you like to continue? If so, enter char "y": "
test:
   .asciz "%c"
test2:      @ Ignore this, just for testing purposes
   .asciz "%c ahhh"

multSign:
    .byte   '*'
addSign:
    .byte   '+'
subSign:
    .byte   '-'
yes:
    .byte   'y'
