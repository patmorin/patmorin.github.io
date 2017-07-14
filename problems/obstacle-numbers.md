---
layout: post
title:  "Obstacle Numbers"
date:   2017-07-13 09:32:53 -0400
permalink: obstacle-numbers.html
categories: openproblem
---
$\DeclareMathOperator{\obs}{obs}\newcommand{\R}{\mathbb{R}}\DeclareMathOperator{\cupdotop}{\dot{\cup}}$For a set $P\subset \R^2$ of points and a set $R$ of connected subsets of $\R^2$, the visibility graph $V_R(P)$ of $P$ with respect to $R$ is the graph $G=(P,E)$ in which an edge $uw$ is in $E$ if and only the segment with endpoints $u$ and $w$ is disjoint from every element in $R$.  We say that $(P,R)$ is an *obstacle representation* of $G$.  The *obstacle number*, $\obs(G)$ of a graph $G$ is the minimum number of obstacles in any obstacle representation of a graph isomorphic to $G$.

<div class="problem">
  What is the maximum obstacle number of an $n$-vertex graph?
</div>

It is known that there are $n$-vertex graphs with obstacle number $\Omega(n/(\log\log n)^2)$ (see [Dujmović and Morin][dujmovic-morin]) and that every $n$-vertex graph has obstacle number $O(n\log n)$ (see [Balko, Cibulka, and Valtr][balko-cibulka-valtr]).
The lower bound is non-constructive; it shows that a random graph has high obstacle number with high probability.

<div class="problem">
  Give an explicit construction of a graph with large obstacle number.
</div>

## Obstacle Numbers of Product Graphs

<div class="problem">
  If $G_1$ has obstacle number $k$ and $G_2$ has obstacle number $k$, then what can we say about $\obs(G_1\times G_2)$?
</div>

## Planar Graphs
Less is known about obstacle numbers of planar graphs:

<div class="problem">
  What is the maximum obstacle number of an $n$-vertex planar graph?
</div>

A lower bound of 2 was recently shown by [Berman et al][berman-etal], who showed that the icosahedron (as well as another planar graph with 10 vertices) has obstacle number 2.  An upper bound of $O(n)$ comes from the fact that a planar drawing of an $n$-vertex planar graph has at most $2n-4$ faces and placing an obstacle inside each face gives an obstacle representation of this graph.  Actually, this bound has been reduced to $n-3$ by [Gimble etal][gimble-etal].  The bound of $n-3$ is tight for planar representations of planar graphs.

[Gimble etal][gimble-etal] also show that if $G$ is bipartite and planar, then $\obs(G)\le 1$.  This makes it plausible that all bipartite

## Sparse graphs

The known graphs with large obstacle number (namely $G_{n,1/2}$) are dense. If we can't find planar graphs with large obstacle number, then maybe we can find other sparse graphs with large obstacle number:

<div class="problem">
  Is there a constant $d$ such that $d$-degenerate graphs have arbitrarily large obstacle number?
</div>


## A Lemma
An *outside obstacle* in an obstacle representation $(P,R)$ is an obstacle that is not bounded by visibility edges, i.e, there is a path from the obstacle to infinity that does not intersect any edge of $V_R(P)$. An *outside obstacle representation* of $G$ is an obstacle representation of $G$ that has an outside obstacle.  The *outside obstacle number* of $G$ is the minimum number of obstacles in any outside obstacle representation of $G$.

Here's a lemma that might help that might be helpful for solving these kinds of problems. (It's an easy generalization of Lemma 4.1
in [Berman etal's paper][berman-etal]).

<div class="lemma">
  If $G_1$ and $G_2$ each have outside obstacle number $k$, then their disjoint
  union, $G=G_1\cupdotop G_2$ has obstacle number $k$.
</div>

<div class="proof" markdown="1">
Observe that $\obs(G_1)\ge k-1$ since, otherwise, we could add a useless outside obstacle to an obstacle representation of $G_1$ with less than $k-1$ obstacles to show that the outside obstacle number of $G_1$ is less than $k$. Also $\obs(G) > \obs(G_1)$ since any obstacle representation of $G$ gives an obstacle representation of $G_1$ just by deleting vertices of $G_2$.

Therefore, the only concern is that $G$ has an obstacle representation with $k-1$ obstacles and that these are all inner obstacles. Take any line, $\ell$ tangent to the convex hull, $C$, of these obstacles.  Then the same argument used in Lemma 4.1 of [Berman et al's paper][berman-etal] shows that $G_1$ and $G_2$ each contain vertices on both sides of $\ell$.  But this is contradiction, since there is some pair of vertices $u\in V(G_1)$ and $w\in V(G_2)$ that are on the side $\ell$ that does not contain $C$.  These vertices are not blocked by any obstacle but they are not adjacent in $G$, so this is not an obstacle representation of $G$.
</div>

Since the disjoint union of planar graphs is also planar, the preceding lemma reduces the problem of finding graphs with obstacle number $k$ to the problem of finding graphs with outside obstacle number $k$.

[dujmovic-morin]: http://www.combinatorics.org/ojs/index.php/eljc/article/view/v22i3p1
[balko-cibulka-valtr]: https://arxiv.org/abs/1610.04741
[berman-etal]: https://arxiv.org/abs/1606.03782
[gimble-etal]: https://arxiv.org/abs/1706.06992
