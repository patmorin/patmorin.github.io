---
layout: post
title:  "Blockers and Midpoints"
date:   2017-07-14
permalink: blockers-and-midpoints.html
categories: openproblem
---
A point $x$ *blocks* two points $p$ and $q$ if $x$ is in the interior of the open segment $pq$. A point set $B$ *blocks* a point set $S$ if, for every $p,q\in \binom{S}{2}$, the is an $x\in S$ that blocks $p$ and $q$.  We call $b$ a blocking set.  For $S\subset\R^2$, define
\\[
   b(S) = \min\\{|B|: \text{$B$ blocks $S$}\\}
\\]
and for $n\in\N$, define
\\[
  b(n) = \min\left\\{b(S): S\in \binom{\R^2}{n},\, \text{$S$ in general position}\right\\}
\\]
<div class="problem">
  Determine the growth of $b(n)$.
</div>
There is a linear lower bound: $b(n) \ge 2n-3$ because every edge of a triangulation of $S$ needs its own blocker.  The constant $2$ can be improved [1][dumitrescu-pach-toth], but no superlinear lower bound is known.  The best upper-bound is due to [Pach][pach], who gives examples of $n$-point sets in general position that have only $n2^{O(\sqrt{\log n})}$ midpoints.

The survey by [Pór and Wood][por-wood] covers this and many related problems, including the next one.

## Midpoints


The *midpoint* of two points $p$ and $q$ is the point $(p+q)/2$. Let $\mu(n)$ denote the smallest number of distinct midpoints determined by (the $\binom{n}{2})$ pairs of points in) an $n$ point set in general position, i.e.,
\[
    \mu(n) = \min\\{(p+q)/2 : p,q\in\binom{S}{2}, |S|=n,\, \text{$S$} in general position}\\}
\]


<div class="problem">
  Determine the growth of $\mu(n)$.
</div>
As mentioned above, Pach shows that $\mu(n)\le n2^{O(\sqrt{\log n})}$ and also that $\lim_{n\rightarrow\infty} \mu(n)/n = \infty$. This proof is repeated by [Matousek][matousek].  [Stanchescu][stanchescu] gives a more concrete lower bound $\mu(n)\in\Omega(n(\log n)^{\delta})$ for any $\delta < 1/8$.

# $\epsilon$-Disk Version

A recent construction of Balko, Cibulka, and Valtr (see my page [Problems on Obstacle Numbers](obstacle-numbers.md)) motivates the following question:

<div class="problem">
  Let $S:(0,1]\to(\R^2)^n$ define a continuous family of $n$ point sets with the property that, for all $\epsilon\in(0,1]$, $S(\epsilon)$ is in general position and can be blocked by a set of $b'(n)$ $\epsilon$-disks, each disjoint from $S(\epsilon)$.  What is the minimum value of $b'(n)$?.
</div>

Note that $f(n)$ is different from $b(n)$ because at the limit $\epsilon=0$, the point set $S(0)$ may not be in general position. Indeed, the construction of Balko, Cibulka, and Valtr shows that $f(n)\in O(n\log n)$.  Actually, in their construction the blocking disks are placed at the midpoints of the segments they block, so we can also as a midpoint version of this problem:

<div class="problem">
  Let $S:(0,1]\to(\R^2)^n$ define a continuous family of $n$ point sets with the property that, for all $\epsilon\in(0,1]$, $S(\epsilon)$ is in general position and the midpoints of $S(\epsilon)$ are contained in a set of $\mu'(n)$ $\epsilon$-disks, each disjoint from $S(\epsilon)$.  What is the minimum value of $\mu'(n)$?.
</div>


Of course, we can ask the same question about


[por-wood]: http://dx.doi.org/10.20382/jocg.v1i1a3
[pach]: https://www.math.nyu.edu/~pach/publications/midpoint.ps
[dumitrescu-pach-toth]: http://www.cs.uwm.edu/faculty/ad/blocking.pdf
[stanchescu]: https://doi.org/10.1016/S0012-365X(01)00441-1
[matousek]: https://doi.org/10.1007/s00454-009-9185-z
