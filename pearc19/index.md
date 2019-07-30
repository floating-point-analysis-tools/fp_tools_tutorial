---
layout: default
comments: false
---


# Tutorial on Floating-Point Analysis Tools
#### PEARC19, Chicago, Illinois, USA <br />
Jul 30th, 2019 <br />
Time: 1:30pm-5:00pm (Tutorial Half-day)

<span style="color:red">Your feedback is sincerely appreciated:</span> [Take survey](https://docs.google.com/forms/d/e/1FAIpQLSf_g7sBKNg76Z_Bn5vLPSTSUv-o8p30nFFJI16GDKJXqrFl-Q/viewform)

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
| 4:50pm - 5:00pm     |  Questions & Answers       |           |        |


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

### AWS IP Addresses

#### GPU modules (FPChecker)
- 18.217.160.109
- 13.59.35.192
- 18.222.18.201
- 18.220.28.170
- 3.17.182.165
- 52.15.126.212
- 18.224.21.81
- 18.217.90.15

#### CPU modules (FLiT, Precimonious, ADAPT)
- 18.218.102.119
- 18.188.227.133
- 3.17.12.64
- 3.17.14.56
- 13.58.5.162
- 18.191.167.213
- 18.191.201.118
- 3.16.169.225

Users and passwords will be provided during the tutorial.






