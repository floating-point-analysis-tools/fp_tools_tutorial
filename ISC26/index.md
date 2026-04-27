---
layout: default
comments: false
---


# Compiler-Assisted Floating-Point Error Analysis and Profiling with FPChecker

#### ISC High Performance 2026 (ISC26), Hamburg, Germany <br />
June 22, 2026 <br />

Time: 9:00am - 1pm Europe/Berlin (half-day tutorial) <br />
Location: CCH – Congress Center Hamburg, Room: Hall X12 - 1st Floor <br />

## Click [here](#) to fill out survey.

<p align="center">  <img src="./photos/SC24_tutorial_v4.jpg"> </p>

## Description

Floating-point arithmetic is essential in scientific computing, but it often 
introduces subtle errors and unexpected behavior in numerical software. 
As the demand grows to port code to lower floating-point precision 
for performance and energy benefits, developers need effective tools 
to analyze and understand floating-point error accumulation and propagation within their applications. 

This tutorial introduces compiler-assisted tools built on the FPChecker 
framework (https://fpchecker.org/), leveraging clang/LLVM to instrument
 C/C++ code and provide insights into floating-point behavior. 
 
 Participants will learn to assess the dynamic range and precision needs of 
 their applications, analyze and visualize how rounding errors and relative 
 errors propagate through different code regions, and detect issues such as 
 infinities or NaNs caused by numerical limitations. 
 
 The tutorial features hands-on demonstrations with accessible 
 examples—including simple linear solvers, finite difference methods, 
 and C/C++ numerical codes, designed to run on participants’ laptops. 
 In the advanced session (second part of the tutorial), attendees can 
 apply the tools to their own applications or to widely 
 used numerical libraries, gaining practical experience with 
 compiler-based floating-point analysis in real-world software. 
 
 All tools and examples will be distributed via Conda environments 
 for easy installation, and pre-configured Amazon AWS instances 
 will be available for participants unable to use Conda.


## Presenter

* [Ignacio Laguna](https://lagunaresearch.org/), Lawrence Livermore National Laboratory

## AWS Instances

TBD

## Presentation Slides

The tutorial slides are here:  [slides](slides/FPChecker_tutorial.pdf)

## Repositories:

* FPChecker: [https://github.com/LLNL/FPChecker](https://github.com/LLNL/FPChecker)
* [Documentation](https://fpchecker.org)
