---
layout: problem
title:  "Pizza Cutting"
date:   2017-07-14
permalink: pizza-cutting.html
categories: openproblem
---
<div class="problem" markdown="1">
Prove or disprove the following pizza-cutting conjecture:
For any set of $kd$ measures $M_1,\ldots,M_{kd}$, in $\R^d$, there is a set of $k$ hyperplanes forming an arrangement $A$ whose cells can be 2-colored so that each of the measures is bisected by each of the colour classes.
</div>

[Barba and Schnider][barba-schnider] (page 174) have proven this in $\R^2$ for $k=2$ using a clever application of the Stone-Tukey Theorem along with the fact that a pair of lines can be viewed as a degenerate conic section.

There is also the algorithmic question:

<div class="problem" markdown="1">
Give a fast algorithm for the case $k=d=2$ and each of the four measures is a set of $n$ points.
</div>

An $O(n^4)$ time algorithm is fairly easy.  Do better.


[barba-schnider]: http://2017.cccg.ca/proceedings/CCCG2017.pdf
