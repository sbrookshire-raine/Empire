"""Linux x86_64 test-only seccomp launcher; blocks socket syscalls across exec."""
import ctypes
import errno
import os
import platform
import sys


def isolate():
    if sys.platform != 'linux' or platform.machine() != 'x86_64':
        raise RuntimeError('offline test isolation requires Linux x86_64')
    class Filter(ctypes.Structure):
        _fields_ = [('code', ctypes.c_ushort), ('jt', ctypes.c_ubyte), ('jf', ctypes.c_ubyte), ('k', ctypes.c_uint)]
    class Program(ctypes.Structure):
        _fields_ = [('length', ctypes.c_ushort), ('filter', ctypes.POINTER(Filter))]
    # Enforce x86_64, kill incompatible architecture; reject x32 syscall ABI.
    rows = [(0x20, 0, 0, 4), (0x15, 1, 0, 0xC000003E), (0x06, 0, 0, 0x80000000),
            (0x20, 0, 0, 0), (0x45, 0, 1, 0x40000000), (0x06, 0, 0, 0x80000000)]
    for nr in (41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,288,299,307):
        rows += [(0x15, 0, 1, nr), (0x06, 0, 0, 0x00050000 | errno.EPERM)]
    rows += [(0x06, 0, 0, 0x7fff0000)]
    array=(Filter * len(rows))(*(Filter(*r) for r in rows))
    program=Program(len(rows),array)
    libc=ctypes.CDLL(None, use_errno=True)
    if libc.prctl(38,1,0,0,0) or libc.prctl(22,2,ctypes.byref(program),0,0):
        raise OSError(ctypes.get_errno(), 'seccomp installation failed')

if __name__ == '__main__':
    isolate()
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python offline_exec.py COMMAND [ARGS...]')
    os.execvp(sys.argv[1],sys.argv[1:])
