---
layout: project
title:  "$k$-Holes in Random Point Sets"
categories:
---
A *$k$-hole* in a point set $S$ is a simple $k$-gon $K$ whose vertices are in $S$ and such that no point of $S$ is in the interior of $K$.  A $k$-hole is *convex* if the polygon $K$ is convex.

At the 2018 Workshop on Probability and Combinatorics Vida asked about how many $k$-holes there are in a random $n$-point set.  This was motivated by recent work by Aicholzer et al ([A](https://www.sciencedirect.com/science/article/pii/S0925772113001727), [B](https://www.sciencedirect.com/science/article/pii/S0925772114001321)) on $k$-gons and $k$-holes in point sets.

We decided that, by the standard stencilling argument, there must exist convex $k$-holes of size $\Omega(\log n/\log\log n)$, though now it seems that this was already a result of [Balogh et al (2013)](https://www.sciencedirect.com/science/article/pii/S0925772112001599).

For the case $k=4$, [Fabila-Monroy et al (2014)](https://www.sciencedirect.com/science/article/pii/S1571065314000237) showed that the expected number of $k$-holes in a random $n$-point set is $\Theta(n^2\log n)$ and that the expected number of convex $k$-holes is $\Theta(n^2)$.

The remainder of this text is mostly copied from [the workshop coauthor site](https://coauthor.csail.mit.edu/ProbComb2018/m/YFqQAASL34gxNnryz).


# Larger values of $k$

## Lower bound

Luc had an argument for showing that the expected number of convex $k$-holes (for any constant $k\ge 5$ is $\Omega(n^2)$. The rough sketch of the argument (for 5-holes) is as follows:

Consider the $\Omega(n^2)$ pairs of points whose interpoint distance is in the interval, say $[1/8,1/4]$ and such that neither point is closer than $1/4$ to the boundary of the unit square.
For each such pair $ab$, consider one of the two rectangles, $R$ that has one side $ab$ and the other sides of length $1/4$.
With constant probability, the closest point $p$ in $R$ to $ab$ has distance $\Theta(1/n)$ from the segment $ab$ and it’s projection onto $ab$ lies in the middle third of $ab$.
Conditioned on the previous statement, with constant probability, the are two points $q$ and $r$ in $R$ such that $abrpq$ is a 5-hole.

Thus, the expected number of 5-holes is $\Omega(n^2)$.  (Note, this may overcount by a factor of at most 5.)

Is this result tight?  

## Upper bound

Luc also has an upper bound of $O(n^2)$ on the number of 5 holes.  The idea is as follows: Partition the pairs of points into classes where the $i$th class consists of points whose distance is between $2^{i}$ and $2^{-(i+1)}$.  The sizes of these classes decrease exponentially in $i$ so only the first few classes matter.
Consider a pair $a,b$ in class $i$ and partition the unit square into bands $B_0,B_1,B_2,\ldots,B_r$ where $B_j$ contains all points $p\in B$ such that the triangle $abp$ has area in the interval $[j/n,(j+1)/n)$. Say that a point $p\in B$ is good if the triangle $abp$ is empty of other points.  
The number of points in $B_j$ is a binomial$(n,1/n)$ random variable and the probability that a triangle $abp$ with $p\in B_j$ is good is at most $(1-j/n)^{n-3}\approx e^{-j}$.  Now, if we let $X$ denote the number of good points in $B$, then the number of 5-gons that include $ab$ as an edge is not more than $\binom{X}{3}$.  We understand $X$ well enough to show that it is subexponential with mean $O(1)$.
This approach seems to prove an upper bound on the expected number of $k$-holes for any constant value of $k$.

Omer says that the same argument is useful in $\R^3$, with a bound of $\Theta(n^3)$.
Separate convex polytopes according to the triangle with largest area among their vertices.
There are $\binom{n}{3}$ triangles, and each has 3 points at uniform locations in the box.
Given one such triangle, the other vertices must be in the orthogonal prism with that triangle as cross section, otherwise there would be a triangle with larger area. (We can truncate the prism, since far enough vertices would give a larger area triangle, but that’s not needed.)
The number of vertices within this prism such that the simplex they form with the base triangle is empty, denoted $X$, has moments uniformly bounded, independently of the area of the triangle.
With applause for Luc for resisting coauthor.
