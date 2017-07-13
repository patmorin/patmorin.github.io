---
layout: post
title:  "Obstacle Numbers of Planar Graphs"
date:   2017-07-13 09:32:53 -0400
permalink: obstacle-numbers.html
categories: openproblem
---
$\DeclareMathOperator{\obs}{obs}\newcommand{\R}{\mathbb{R}}\DeclareMathOperator{\cupdotop}{\dot{\cup}}$For a set $P\subset \R^2$ of points and a set $R$ of connected subsets of $\R^2$, the visibility graph of $P$ with respect to $R$ is the graph $G=(P,E)$ in which an edge $uw$ is in $E$ if and only the segment with endpoints $u$ and $w$ is disjoint from every element in $R$.  We say that $(P,R)$ is an *obstacle representation* of $G$.  The *obstacle number*, $\obs(G)$ of a graph $G$ is the minimum number of obstacles in any obstacle representation of a graph isomorphic to $G$.

It is known that there are $n$-vertex graphs with obstacle number $\Omega(n/(\log\log n)^2)$ (see [Dujmovic and Morin][dujmovic-morin]) and that every $n$-vertex graph has obstacle number $O(n\log n)$ (see [Balko, Cibulka, and Valtr][balko-cibulka-valtr]).

Less is known about obstacle numbers of planar graphs:

<div class="problem">
  What is the maximum obstacle number of an $n$-vertex planar graph?
</div>

A lower bound of 2 was recently shown by [Berman et al][berman-etal], who showed that the icosahedron has obstacle number 2 (and another graph with 10 vertices).  An upper bound of $O(n)$ comes from the fact that a planar drawing of an $n$-vertex planar graph has at most $2n-4$ faces and placing an obstacle inside each face gives an obstacle representation of this graph.  Actually, this bound has been reduced to $n-3$ by [Gimble etal][gimble-etal]. The same authors show that if $G$ is bipartite and planar, then $\obs(G)\le 1$.

Here's a lemma that might help, that follows the reasoning used in Lemma 4.1 of [Gimble etal][gimble-etal].  

<div class="lemma">
  If $G_1$ and $G_2$ each have outside obstacle number $k$, then their disjoint
  union, $G=G_1\cupdotop G_2$ has obstacle number $k$.
</div>

<div class="proof">
Observe that $\obs(G)\ge \obs(G_1)\ge k-1$.
Suppose this is not the case, and that $G$ has an obstacle representation with $k-1$ obstacles. Then, by definition, these must all be internal obstacles.
</div>



It is tempting to prove a lower bound greater than 2 by, for example, letting $G$ be $r$ disjoint copies of the icosahedron, $I$.  Since $\obs(I)=2$, every obstacle representation of $I$ has a bounded obstacle.  If $G$ has obstacle number of 2 then its obstacle representation contains $r$ representations of $I$ and these representations all share the same internal (and possibly external) obstacle.  If every obstacle representation of $I$ had at least one vertex not incident to an obstacle, then we would be done,


[dujmovic-morin]: http://www.combinatorics.org/ojs/index.php/eljc/article/view/v22i3p1
[balko-cibulka-valtr]: https://arxiv.org/abs/1610.04741
[berman-etal]: https://arxiv.org/abs/1606.03782
[gimble-etal]: https://arxiv.org/abs/1706.06992
