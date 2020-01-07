---
layout: page
comments: false
---

<img src="img/tutorial-banner-5.png" alt="banner" style="width:1200px;" />

## Tutorial Material

- [LANL](/LANL), January, 2020
- [SC19](/sc19), Denver, Colorado, USA, Nov 17th, 2019
- [PEARC19](/pearc19), Chicago, Illinois, USA, Jul 30th, 2019


## Background

<!--
<p class="message">
</p>
-->

<p class="message">
Dealing with floating-point arithmetic to perform numerical computations is challenging. Not only do round-off errors occur and accumulate at all levels of computation, but also
compiler optimizations and low precision arithmetic can significantly affect the final computational results. With accelerators dominating HPC systems, computational scientists are faced with even bigger challenges to program reliable and reproducible floating-point programs. <br />

This tutorial demonstrates tools that are available today to analyze floating-point scientific software.
</p>

## Tools

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

### HiFPTuner

HiFPTuner is a dynamic precision tuner. Different from other tuners, it explores the community structure of the floating-point variables and uses the community structure to guide precision tuning to find better precision configurations in less time.

[https://github.com/ucd-plse/HiFPTuner](https://github.com/ucd-plse/HiFPTuner) 

### FloatSmith

FloatSmith provides automated source-to-source tuning and transformation of floating-point code for mixed precision using three existing tools: 1) CRAFT, 2) ADAPT, and 3) TypeForge. The primary search loop is guided by CRAFT and uses TypeForge to prototype mixed-precision versions of an application. ADAPT results can optionally be used to help narrow the search space, and there are a variety of options to customize the search.

[https://github.com/crafthpc/floatsmith](https://github.com/crafthpc/floatsmith)

### FPBench

FPBench provides benchmarks, compilers, and standards for the floating-point research community.

[https://github.com/FPBench/FPBench](https://github.com/FPBench/FPBench)

### ReMPI

ReMPI is a record-and-replay tool for MPI+OpenMP applications. It helps in debugging floating-point program
executions that produce different floating-point results due to MPI non-determinism.

[https://github.com/PRUNERS/ReMPI](https://github.com/PRUNERS/ReMPI)

### ARCHER

Archer is a data race detector for OpenMP programs.
Archer combines static and dynamic techniques to identify 
data races in large OpenMP applications, leading to low runtime 
and memory overheads, while still offering high accuracy and precision. 

[https://github.com/PRUNERS/archer](https://github.com/PRUNERS/archer)

## Presentations

01/07/2020:  [__Tools and Techniques for Floating-Point Analysis__](/slides/webinar-IDEAS-ilaguna.pdf), Ignacio Laguna, LLNL.

