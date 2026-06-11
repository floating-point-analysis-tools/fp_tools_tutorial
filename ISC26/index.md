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

Floating-point arithmetic is central to scientific computing, but small rounding
effects can accumulate into significant numerical errors, especially when
applications are ported to lower precision for performance and energy savings.
This tutorial introduces compiler-assisted analysis tools built on the
FPChecker framework (https://fpchecker.org/) and clang/LLVM to instrument C/C++
code and expose floating-point behavior.

Participants will learn how to evaluate dynamic range and precision
requirements, track rounding and relative error propagation across code
regions, and detect infinities and NaNs caused by numerical limits. Hands-on
examples, including linear solvers, finite-difference methods, and other C/C++
codes, will run on participants' laptops. In the advanced session, attendees
can apply the tools to applications or widely used numerical
libraries. All tools and examples will be distributed through Conda, with
pre-configured AWS instances available for participants who cannot use it.

## Presenter

* [Ignacio Laguna](https://lagunaresearch.org/), Lawrence Livermore National Laboratory

## AWS Instances

[https://fpchecker.org/usernames](https://fpchecker.org/usernames)

## Presentation Slides

The tutorial slides are here:  [slides](slides/ISC26-fpchecker_tutorial.pdf)

## Repositories:

* FPChecker: [https://github.com/LLNL/FPChecker](https://github.com/LLNL/FPChecker)
* [Documentation](https://fpchecker.org)
