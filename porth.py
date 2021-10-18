#!/usr/bin/env python3
# pylint: disable=missing-module-docstring, invalid-name, missing-function-docstring, global-statement

import sys
import subprocess

iota_counter = 0


def iota(reset=False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result


OP_PUSH = iota(True)
OP_PLUS = iota()
OP_MINUS = iota()
OP_DUMP = iota()
COUNT_OPS = iota()


def push(x):
    return (OP_PUSH, x)


def plus():
    return (OP_PLUS, )


def minus():
    return (OP_MINUS, )


def dump():
    return (OP_DUMP, )


def simulate_program(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 4, "Exhaustive handling of operations in simulation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "unreachable"


def compile_program(program, out_file_path):
    with open(out_file_path, "w") as out:
        out.write("segment .text\n")
        out.write("global _start\n")
        out.write("_start:\n")
        out.write("    mov rax, 60\n")
        out.write("    mov rdi, 0\n")
        out.write("    syscall\n")


# TODO: unhardcode program
program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(500),
    push(80),
    minus(),
    dump(),
]


def usage():
    print("Usage: porth <SUBCOMMAND> [ARGS]")
    print("SUBCOMMANDS:")
    print("     help    Print this help menu")
    print("     sim     Simulate the program")
    print("     com     Compile the program")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        print("Error: no subcommand provided")
        sys.exit(1)

    subcommand = sys.argv[1]

    if subcommand == "help":
        usage()
        sys.exit()
    elif subcommand == "sim":
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program, "output.asm")
        subprocess.call(["nasm", "-felf64", "output.asm"])
        subprocess.call(["ld", "-o", "output", "output.o"])
    else:
        print("Error: unknown subcommand")
