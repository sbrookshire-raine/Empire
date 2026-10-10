---
name: rea_doctor
toolbelt: rea
one_line: Check REA reverse-engineering readiness (Node, engines, config)
---

# rea_doctor

Check whether [REA](https://github.com/morluto/rea) (Reverse Engineer Anything) is ready on this host.

## When to use

- Before native or JavaScript reverse-engineering tasks.
- When a `rea_*` call fails and you need remediation hints.

## Parameters

- None.

## Notes

Registered by the Toolbelt category `rea`. Enable **REA** on the Workbench Toolbelt (or `admit_for_goal("rea")`) first. Deep native analysis requires Hopper, Ghidra, or IDA configured on the machine; JavaScript/Electron static analysis needs only Node.
