section .text         ;declare this section to include executable instructions

global _my_memset      ;export the 'my_memset' symbol to be accessible outside of file
_my_memset:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


	      mov rcx, 0
        mov rax, rsi
_loop:
      	cmp rcx, rdx
      	je _end
      	mov [rdi], al
      	add rcx, 1
      	add rdi, 1
      	jmp _loop
_end:	

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global _my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
_my_strncpy:
        push rbp      ;saves the base pointer for the previous functions stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, 0
_loop2:
        cmp rcx, rdx
        je _end2
        mov al, [rsi]
        mov [rdi], al
        add rcx, 1
        add rdi, 1
        add rsi, 1
        jmp _loop2
_end2: 


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!