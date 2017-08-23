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

This implies a necessary condition.  Let $\overrightarrow{E}(G)$ denote the directed edges of $G$ so that, if $uw\in E(G)$ then $uw$ and $wu$ are both in $\overrightarrow{E}(G)$.  Then it must be possible to find a coloring $c:\overrightarrow{E}(G)\to\\{-2,-1,1,2\\}$ such that

1. $c(uw) = -c(wu)$ for all $uw\in E(G)$;
2. If $c(uv) = c(vw)$, then $uw\in E(G)$; and
3. In an embedding of $G$, the colours around vertex every $v$ must occur in the order $-1^*-2^*1^*2^*$.

Is this possible to do for every planar graph $G$?  We suspect the answer is no. At first we thought the triangular grid was a counterexample, but then we discovered this drawing of the triangular grid:

![triangular grid](images/triangular-grid.svg)

<div class="conjecture">
  Every triangulation has a non-blocking grid obstacle representation, but not every planar graph does.
</div>


One observation is that, if $v$ is not part of a separating triangle, then the colours of its outgoing edges must be some rotation of $-1,1,2,2,2,\ldots,2$.  This feels a bit like Schnyder's 3-tree partition  might help.


[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
