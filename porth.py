#!/usr/bin/env python3
# pylint: disable=missing-module-docstring, invalid-name, missing-function-docstring, global-statement

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
OP_DUMP = iota()
OP_DUMP = iota()
COUNT_OPS = iota()


def push(x):
    return (OP_PUSH, x)


def plus():
    return (OP_PLUS, )


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
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "unreachable"


def compile_program(program):
    assert False, "Not Implemented"


program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(420),
    dump(),
]
simulate_program(program)
