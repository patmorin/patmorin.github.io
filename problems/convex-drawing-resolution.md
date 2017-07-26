---
layout: problem
title:  "Resolution of Convex Drawings"
date:   2017-07-13 09:32:53 -0400
permalink: convex-drawing-resolution.html
categories: openproblem
---
$\DeclareMathOperator{\deg}{deg}$Tutte's Theorem states that every internally 3-connected planar graph has a convex drawing and that we can even pick the outer face and the convex polygon that it maps to.

<div class="problem">
  What is the smallest value of $N$ such that every $n$-vertex internally 3-connected planar graph has a convex drawing with its vertices on the $N\times N$ grid?
</div>

Let $G$ be an $n$-vertex internally 3-connected planar graph and let $C$ be the outer face of $G$. Tutte's proof shows that the system of linear equations
\\[
    \left\\{ (x_u,y_u) = (1/\deg(u))\sum_{(u,w)\in E(G)}(x_w,y_w) : v\in V(G)\setminus V(C) \right\\}
\\]
has a unique solution, after fixing the coordinates of $C$ to be the vertices of a convex polygon.  If we take coordinates of $C$ to be positive integers in $O(n)$, then [Bareiss' Algorithm][bareiss-algorithm] implies that the each of the coordinates obtained by the solution to this system of equations is rational and can be represented using $O(n\log n)$ bits.  Multiplying through by the product of the denominators therefore implies that $N\le n^{O(n^2)}$.

<div class="problem">
  Can we improve the preceding argument to show $N\le n^{O(n)}$
</div>

The difficulty in this problem comes from graphs that are internally 3-connected, but not 3-connected:
It is known that, if the triconnected component decomposition tree of $G$ has at $\ell\le 4$ leaves, then $G$ has a convex drawing on an $O(n)\times O(n)$ grid.  See [Chrobak][chrobak] (for the three connected case), [Kamada, Miura, and Nishizeki][kamada-miura-nishizeki] (for $\ell\in\\{1,2,3\\}$), and [Zhou and Nishizeki][zhou-nishizeki] (for $\ell = 4$).
The problem seems to be completely open for $\ell \ge 5$.  It's not even known if this can be done on a polynomial grid.

## Fixing y-coordinates

An extension of Tutte's Theorem implies that, not only can the outer face of $G$ be specified, but one can also fix the $y$-coordinates of $G$'s vertices provided that every vertex has at least one neighbour above it and at least one neighbor below it. This follows from an extension of Tutte's proof to the case where every vertex is assigned a weighted average of its neighbours. See [Floater][floater] or [Gortler, Gotsmand, and Thurston][gortler-gotsman-thurston]. This result also seems to appear
in a paper by [Hong and Nagamochi][hong-nagamochi].

The same argument of Bareiss' algorithm implies that the resulting drawing can be achieved with integer $x$-coordinates no larger than $n^{O(n^2)}$.  A lower bound construction, due to [Lin and Eades][lin-eades], shows that $x$-coordinates of size $n^{\Omega(n)}$ may be necessary.  A resolution to the second problem above would get matching upper and lower bounds.

[chrobak]: https://doi.org/10.1142/S0218195997000144
[bareiss-algorithm]: https://en.wikipedia.org/wiki/Bareiss_algorithm
[zhou-nishizeki]: https://doi.org/10.1142/S179383091000070X
[kamada-miura-nishizeki]: http://dx.doi.org/10.1007/11940128_15
[floater]: https://doi.org/10.1142/S021865439800012X
[gortler-gotsman-thurston]: https://doi.org/10.1016/j.cagd.2005.05.002
[hong-nagamochi]: https://doi.org/10.1016/j.jda.2009.05.003
[lin-eades]: https://core.ac.uk/download/pdf/82361347.pdf
