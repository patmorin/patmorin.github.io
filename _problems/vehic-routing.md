---
layout: problem
title:  "Geometric Vehicle Routing/Scheduling Problems"
date:   2017-07-14
permalink: vehicle-routing.html
categories: openproblem
---
$\DeclareMathOperator{\dist}{dist}$Sasanka Roy gave [a talk](http://cglab.ca/seminar/2019/sasankaRouting.html) about vehicle routing problems that have the following kind of flavour:

We are given a set $S=\lbrace f_1,\ldots,f_n\rbrace$ of curves and we want to find a maximum subset $S'\subseteq S$ such that, for any two $f_i,f_j\in S'$ there is no time $0\le t\le 1$ such that $f_i(t)=f_j(t)$.  (Think of these curves as planned vehicle trajectories and $f_i(t)=f_j(t)$ represents a collision that occurs if we let vehicle $i$ and vehicle $j$ proceed with their planned trajectories.)

Sasanka showed us that most versions of these problems are NP-hard, at least.  This is true even when the curves are L-shapes, all of the same size, and trajectories have constant speed.  There are constant factor approximations for some of these cases.

Maybe a more interesting question is about variations on this problem that Sasanka suggested:  The input is $S=\lbrace f_1,\ldots,f_n \rbrace$ where $f_i:\mathbb{R}\to\mathbb{R}^2$ is a continuous function.  We then want to  assign each vehicle a *delay* $t_i\ge 0$ so that, for any $f_i,f_j\in S$ there is no time $t\in\mathbb{R}$ such that $\dist(f_i(t-t_i), f_j(t-t_j)) \le 1$.
We want to do this so that the maximum delay is minimized (or maybe the maximum completion time; think more about definitions here).

These are surely hard problems in full generality, but there are natural lower bounds you can get by lifting each curve into 3-D and fattening it into a unit tube:  Then, if there exists a vertical that whose total intersection with these tubes has length $\ell$, then $\ell$ represents the minimum make-span.  Can we find schedules that approximate this?
