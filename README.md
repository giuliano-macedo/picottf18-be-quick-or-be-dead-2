# PicoCTF 2018 solution for the problem 'Be quick or be dead 2' using the iterative Fibonacci function

## disclaimer
i got the binary from [here](https://github.com/PlatyPew/picoctf-2018-writeup/blob/master/Reversing/be-quick-or-be-dead-2/files/be-quick-or-be-dead-2)
**this solution is very overkill**

# pre-requisites
* python >=3.6
* pip
* gcc

# installation
just pip it after `venv`
```bash
pip install -r requirements.txt
```

# write up

the binary contains a recursive implementation of nth Fibonacci number function,
called 'fib', that is calculation for the 1083th Fibonacci number that is used to print the flag,
since the recursive function is very slow, and that this number causes 64bit integer overflow the function 
may run forever. 

the correct answer for the problem would be:
```
9641162182178966878126331027202834784434723577592322830700454745652427494401346945631082965963962317692358822696127040961581675695438118874508418491101822679355067810556808551572644321954159676320600161466564032755133080685122
```

however, since overflow, the program would accept the following integer from the fib function: `-1066907070`

the program then waits for the computation for 3 seconds, if the fib function is still running until there 
it will fail and not print the flag, otherwise it will print the flag.


this solution therefore compiles an iterative version of the nth Fibonacci number computation in another binary
extracts it and patch onto the original binary,
since this solution is *O(1)* it will run basically instantly in any machine and print the flag.


# Usage

run the `compile_fib.py` to generate `fib_iterative.txt` that have the assembly code for 
the iterative version of the Fibonacci, edit the labels from the jump-based instructions 
and insert into `patch_it` and the binary `be-quick-or-be-dead-2_patched` will be created 
and will print the flag.
