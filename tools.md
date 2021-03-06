---
layout: page
title: Tools
---

### FPChecker

FPChecker is tool to detect floating-point exceptions (e.g.,
NaNs, division by zero) on NVIDIA GPUs. It uses clang/LLVM to compile and
instrument CUDA kernels. The tool informs to users the location where 
exceptions occurred (file and line number).

[https://github.com/LLNL/FPChecker](https://github.com/LLNL/FPChecker)

### FLiT

FLiT (Floating-point Litmus Tests) is a C++ test 
infrastructure for detecting variability in 
floating-point code caused by variations in 
compiler code generation, hardware and execution environments.

[https://github.com/PRUNERS/FLiT](https://github.com/PRUNERS/FLiT)

### ARCHER

Archer is a data race detector for OpenMP programs.
Archer combines static and dynamic techniques to identify 
data races in large OpenMP applications, leading to low runtime 
and memory overheads, while still offering high accuracy and precision. 

[https://github.com/PRUNERS/archer](https://github.com/PRUNERS/archer)

### ADAPT

ADAPT is a tool for mixed precision analysis. The tool uses 
algorithmic differentiation to estimate the output error due to 
lowering the precision of variables. ADAPT also provides a floating-point 
rounding error sensitivity profile of the code. 

[https://github.com/LLNL/adapt-fp](https://github.com/LLNL/adapt-fp)

### Precimonious

Precimonious is a framework to automatically tune
the precision of floating-point variables. The tool allows users to specify
a target error and performance threshold, and uses the clang/LLVM compiler
a main compiler infrastructure.

[https://github.com/corvette-berkeley/precimonious](https://github.com/corvette-berkeley/precimonious)
