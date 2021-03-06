---
layout: default
comments: false
---


# Tutorial on Floating-Point Analysis and Reproducibility Tools for Scientific Software
#### SC19, Denver, Colorado, USA <br />
Nov 17th, 2019 <br />
Time: 8:30am - 5pm (full day tutorial) <br />
Room: 405

<p align="center">   
<a href="https://integrus.cs.utah.edu/">Get AWS Credentials Here</a>
</p>

<p align="center">  <img src="./photos/SC19-color-hor-small.jpg"> </p>

<p align="center">  <img src="./photos/IMG-2828.JPG"> </p>

## Presenters

* [Ignacio Laguna](http://lagunaresearch.org/) (organizer), Lawrence Livermore National Laboratory
* Michael Bentley, University of Utah
* Ian Briggs, University of Utah
* [Ganesh Gopalakrishnan](https://www.cs.utah.edu/~ganesh/), University of Utah
* [Hui Guo](https://hguo15.github.io/huiguo.github.io/), University of California, Davis
* [Michael O. Lam](https://w3.cs.jmu.edu/lam2mo/), James Madison University
* [Harshitha Menon](http://harshithamenon.com/), Lawrence Livermore National Laboratory
* [Pavel Panchekha](https://pavpanchekha.com/), University of Utah
* [Cindy Rubio González](https://web.cs.ucdavis.edu/~rubio/), University of California, Davis


### Schedule

#### Morning Schedule

| Time | Module | Presenter | Slides |
|------|--------|-----------|--------|
| 8:30 - 8:40am | Introduction (housekeeping) |  Ignacio | [slides](./slides/intro-Ignacio.pdf) |
| 8:40 - 8:55am | Floating-point background |  Ganesh | [slides](./slides/Ganesh_introduction.pdf) |
| 8:55 - 9:35am |  **FPChecker**:  floating-point exceptions, GPUs, CUDA | Ignacio          | [slides](./slides/Module-FPChecker.pdf), [source](./source/Module-FPChecker.zip)|
| 9:35 - 10:00am |  **ARCHER**:  data races, OpenMP  | Ian, Mike          | [slides](./slides/Module-ARCHER.pdf), [source](./source/Module-Archer.zip)|
| 10:00 - 10:30am     |  **Break**       |           |        |
| 10:30 - 11:30am |  **FLiT**: floating-point variability, compiler optimizations  | Ian, Mike          | [slides](./slides/Module-FLiT.pdf), [source](./source/Module-FLiT.zip)|
| 11:30 - 12:00pm |  **ReMPI**: MPI, floating-point variability  | Ian, Mike          | [slides](./slides/Module-ReMPI.pdf), [source](./source/Module-ReMPI.zip)|

| 12:00 - 1:30pm |  **Lunch Break**       |  (pay on your own)         |        |

#### Afternoon Schedule

| Time | Module | Presenter | Slides |
|------|--------|-----------|--------|
| 1:30 - 1:35pm | Afternoon overview |  Ignacio | [slides](./slides/intro-Ignacio.pdf) |
| 1:35 - 2:45pm |  **Precimonious & HiFPTuner**: mixed-precision tuning  | Cindy          | [slides](./slides/Module-Preci_HiFPTuner.pdf), [source](./source/Module-Precimonious_HiFPTuner.zip)|
| 2:45 - 3:00pm |  **FPBench**:  floating-point benchmarks | Pavel          | [slides](./slides/Module-FPBench.pdf), [source](#)|
| 3:00 - 3:30pm     |  **Break**       |           |        |
| 3:30 - 4:50pm |  **ADAPT, FloatSmith**: algorithmic differentiation, tuning  | Mike          | [slides](./slides/Module-ADAPT_FloatSmith.pdf), [source](./source/Module-ADAPT_FloatSmith.zip)|
| 4:50 - 5:00pm     |  Questions & Answers       |           |        |


### Access to AWS Instances

We provide exercises for each module in AWS instances. You can get a username, password,
along with the IP address of an instance [here](https://integrus.cs.utah.edu/). 
You can access the instance via ssh as follows:

```
ssh [USERNAME]@[IP ADDRESS]
```

### Directory Structure

The directory structure in your home directory will look like this:

```
/home/user1/
   |---Module-TOOL1
      |---exercise-1
      |---exercise-2
      |---exercise-3
   |---Module-TOOL2
      |---exercise-1
      |---exercise-2
      |---exercise-3
   ...
```

Each module directory contains directories for each exercise. Please run the exercises in each of them as indicated
by the speaker.







