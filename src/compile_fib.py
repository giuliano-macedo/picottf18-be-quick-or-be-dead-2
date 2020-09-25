from os import system
from pwn import ELF
print("compiling")
#O2,O1 or the assert will trigger
system("gcc -O2 fib_iterative.c -o ./fib_iterative")

print("extracting fib")
binary=ELF("./be-quick-or-be-dead-2")
fib_binary=ELF("./fib_iterative")
fib=fib_binary.functions["fib"]
assert fib.size<binary.functions["fib"].size, "instructions variable must have less machine code than the current fib implementation"

print("fib size:",fib.size)
with open("fib_iterative.txt","w") as f:
	print(fib_binary.disasm(fib.address,fib.size),file=f)
