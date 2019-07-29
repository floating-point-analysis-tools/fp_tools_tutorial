---
layout: default
comments: false
---


# Tutorial on Floating-Point Analysis Tools
#### PEARC19, Chicago, Illinois, USA <br />
Jul 30th, 2019 <br />
Time: 1:30pm-5:00pm (Tutorial Half-day)

## Presenters

* [Ignacio Laguna](http://lagunaresearch.org/) (organizer), Lawrence Livermore National Lab
* Michael Bentley, University of Utah
* Ian Briggs, University of Utah
* [Ganesh Gopalakrishnan](https://www.cs.utah.edu/~ganesh/), University of Utah
* [Harshitha Menon](http://harshithamenon.com/), Lawrence Livermore National Lab
* [Cindy Rubio González](https://web.cs.ucdavis.edu/~rubio/), University of California, Davis
* Tristan Lucas Vanderbruggen, Lawrence Livermore National Lab

### Schedule

| Time | Module | Presenter | Slides |
|------|--------|-----------|--------|
| 1:30pm - 1:40pm | Introduction |  Ganesh, Ignacio | [slides](./slides/intro-slides.pdf) |
| 1:40pm - 2:20pm |  **FPChecker**  | Ignacio          | [slides](./slides/Module-FPChecker.pdf), [source](./source/Module-FPChecker.zip)|
|      |  Key Topics:       |           |        |
|      |  - Floating-point exceptions, GPUs, CUDA       |           |        |
| 2:20pm - 3:00pm |  **FLiT**  | Ganesh, Mike, Ian          | [slides](./slides/Module-FLiT.pdf), [source](./source/Module-FLiT.zip)|
|      |  Key Topics:       |           |        |
|      |  - Compiler optimizations, floating-point variability       |           |        |
|      |  -        |           |        |
| 3:00pm - 3:30pm     |  **Break**       |           |        |
| 3:30pm - 4:10pm |  **Precimonious**  | Cindy          | [slides](./slides/Module-Precimonious.pdf), [source](./source/Module-Precimonious.zip)|
|      |  Key Topics:       |           |        |
|      |  - Floating-point mixed-precision, tuning       |           |        |
| 4:10pm - 4:50pm |  **ADAPT**  | Tristan, Harshitha          | [slides](./slides/Module-ADAPT.pdf), [source](./source/Module-ADAPT.zip)|
|      |  Key Topics:       |           |        |
|      |  - Algorithmic differentiation, input sensitivity       |           |        |

### Access to AWS Instances

We provide exercises for each module in AWS instances. You will be given a username and password,
along with the IP address of the instance. You can access the instance via ssh as follows:

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



