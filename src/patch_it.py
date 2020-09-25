from pwn import ELF,context
context.arch = 'amd64'

binary=ELF("./be-quick-or-be-dead-2")

#written based on fib_iterative.txt
instructions="""
         test   edi, edi
         jle    l1
         xor    edx, edx
         mov    esi, 0x1
         xor    ecx, ecx
         jmp    l2
         nop
l3:      mov    ecx, eax
l2:      add    edx, 0x1
         lea    eax, [rcx+rsi*1]
         mov    esi, ecx
         cmp    edi, edx
         jne    l3
         ret    
         nop
l1:      xor    eax, eax
         ret
"""

binary.asm(binary.functions["fib"].address,instructions)
fname="be-quick-or-be-dead-2_patched"
binary.save(fname)

print(f"saved '{fname}'")
