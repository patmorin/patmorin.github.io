---
layout: problem
title:  "Grid Obstacle Representations"
date:   2017-07-14
permalink: grid-obstacle.html
categories: openproblem
---
This is stuff I've been working on with Saeed Mehrabi and Paz Carmi following up [some work he did][biedl-mehrabi] with Therese Biedl.

A *non-blocking grid obstacle representation* of a planar graph $G$ is (equivalent to) a planar drawing of $G$ in which, for every pair $u,w\in V(G)$, the drawing contains an x-y-monotone path from $u$ to $w$ if and only if $uw\in E(G)$.

<div class="problem">
Does every planar graph have a non-blocking grid-obstacle representation?
</div>

We can show that every maximal outerplanar graph has a non-blocking grid-obstacle representation.  (This is done with a depth-first layering of the graph.)

<div class="problem">
   Does every outerplanar graph have a non-blocking grid obstacle representation?
</div>

The main difficulty comes from an implicit transitivity in these representations.  If, in the representation, there is a x-y-monotone path from $u$ to $v$ (so that $uv\in E(G)$) and there is an x-y-monotone path from $v$ to $w$ (so that $vw\in E(G)$) then there is also an x-y-monotone path from $u$ to $w$ (therefore $uw$ must be in $E(G)$).

At first we thought the triangular grid was a counterexample, but then we discovered this drawing of the triangular grid:

![triangular grid](images/triangular-grid.svg)

# Triangulations Suffice.

Here is an observation of Paz:

<div class="lemma">
  If every triangulation has a non-blocking grid obstacle representation then every planar graph has a non-blocking grid obstacle representation.
</div>

<div class="proof" markdown="1">
  Give a planar graph $G$, place Steiner vertices into each of its non-triangular faces and triangulate so that every newly introduced edge is incident to at least one Steiner vertex.  If we can find a non-blocking grid obstacle representation of this triangulation, then removing the Steiner vertices gives a non-blocking grid obstacle representation of $G$.
</div>


# A Combinatorial View

So now we assume $G$ is a triangulation.
Let $\overrightarrow{E}(G)$ denote the directed edges of $G$ so that, if $uw\in E(G)$ then $uw$ and $wu$ are both in $\overrightarrow{E}(G)$.  
It must be possible to find a coloring $c:\overrightarrow{E}(G)\to\\{0,1,2,3\\}$ such that



1. $c(uw) = (c(wu)+2)\bmod 4$ for all $uw\in E(G)$;
2. if $c(uv) = c(vw)$, then $uw\in E(G)$ and c(uw)=c(uv); and
3. for every vertex $u$ whose neighbours in clockwise order are $v_1,\ldots,v_k$, the sequence of colours $c(v_1),\ldots,c(v_k)$ is non-decreasing (with the appropriate choice of starting vertex $v_1$).
4. For every vertex $u$ not on the outer face of $G$, $u$ has two neighbours $x$ and $y$ such that $c(ux)\equiv c(uy)+2\pmod 4$

<div class="lemma">
  If $v$ is not part of a separating triangle, then its neighbours are coloured $i,i+2,i+3,i+3,i+3 \pmod 4$ for some $i\in\{0,1,2,3\}$.
</div>

<div class="proof">
  By the fourth rule, we can assume that $u$ has two consecutive neighbours $v_1$ and $v_2$ with $c(v_1)=0$ and $c(v_2)=2$. Since $u$ is not incident to any separating tri
</div>



[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
