---
layout: problem
title:  "Problems from the Palace"
date:   2017-07-14
permalink: ciazen.html
categories: openproblem
---

# 1 Stephan Felsner

You have a partial order $P$ of height 2.  The question "Is the dimension of $P$ at most 3?" is NP-complete.

Special cases to consider:

* $G_P$ is bipartite planar
* $G_P$ is 3-regular
* Containment of homothetic triangles(?)

($G_P$ is the cover graph.)

# 2 Penny Haxell

Theorem (Schnyder): Let $G$ be a planar triangulation.  Then there exists 3 linear orders $L_1$, $L_2$, and $L_3$ of $V(G)$ such that, for every edge $xy\in E(G)$ and every vertex $z\in V(G)$ there exists $i\in\lbrace 1,2,3\rbrace$ such that $z\ge_{L_i} x,y$.

Question: Is there a list version of this theorem where each edge is assigned a list?

# 3 Tom Trotter

David Kelly's construction gives planar posets of height 2 and large dimension.  Some questions should have been asked:

* Can the number of minimal elements in this construction be reduced? (no)
* Can the length of the longest chain be reduced?  (no)
* Can this be done with one long chain? (no)

Real questions:

* Do you need large standard examples for large dimension?  There are now examples where the dimension is twice as large as the standard example.
* Is the Boolean dimension of planar posets bounded?  (Uses arbitrary boolean formulas to determine if two elements are comparable.)

# 4 ???


# 5 Pat Morin: Non-Crossing Geodesic Obstacle Representations

This problem deals with showing the existence of a special type of F\'ary\ embedding of planar graphs.

For distinct points $p,q\in\R^2$, we say that $p$ $(i,k)$-dominates $q$ if we draw a regular $2k$-gon centered at $p$ and the ray originating at $p$ and containing $q$ itersects the $i$th edge of this $2k$-gon.  We write this as $q \prec_{i,k} p$. (There is a small ambiguity here when the ray passes through a vertex of the $2k$-gon, treat each edge of the $2k$-gon as contain its counterclockise endpoint but not its clockwise endpoint.)

We say that a non-crossing plane straight-line drawing of a graph $G$ is $k$-transitive if, for every $i\in\lbrace 1,\ldots,k\rbrace$ and every path $xyz$ in $G$ for which $x\prec_{i,k} y\prec_{i,k} z$, the edge $xz$ is also in $G$.  Intuitively, this captures the idea that if $xz$ is not in $G$ then the path $zyz$ should ``bend significantly'' at $y$.

Problem: Does there exist a constant $k$ such that every planar graph $G$ has a $k$-transitive non-crossing plane straight line drawing?


# 6 Daniel Goncalves

Same problem he posed in Barbados 2018.  (Cann every proper contact graphs of boxes in $\R^d$ be completed to a proper tiling of $\R^d$.)

# 7 Grzegorz Gulowski

Two planar graphs with the same vertex set.  

# 8 Gwenael Joret

Theorem (Pilipczuk, Siebertz): The vertex set of every planar graph can be partitioned into geodesic paths $P_1,\ldots,P_k$ in such a way that, if you contract each $P_i$ into a vertex, then the resulting minor has treewidth at most 8.

Meta-Problem: Can you use this result to solve problems on planar graphs?

Suppose $P$ has height $h$ with cover graph $G$ which is planar.  (May assume that radius of $G$ is at most $2h$.)

Known: $\dim(P)\le f(h)$

Known (but unpublished): $\dim(P)\le O(h^5)$.

Real problem: Use the Pilipczuk--Siebertz Theorem to improve this bound.

TODO: Read about this theorem and see if it includes a linear-time algorithm.

# 9 Vida Dujmovic

What is the size of the largest free-set in any $n$-vertex planar graph?

# 10 Jean Cardinal

Computational flip-distance questions.  

$\alpha$-orientations: $G$ has $n$ vertices and a vector $\alpha_1,\ldots,\alpha_n$ where we orient the edges of $G$ so that vertex $i$ has indegree $\alpha_i$.  A *flip* involves reversing the edges of a directed cycle.  What the computational complexity of computing the minimum number of flips required to convert one $\alpha$-orientation of $G$ into another?

This question is open even if $G$ is planar.

# 11 Kolja Knauer

Basil Coeteux: Two posets $P$ and $Q$.  Consider $P\cup Q$.  This is, in general not a poset.  What is the complexity of finding the largest poset contained in $P\cup Q$.
