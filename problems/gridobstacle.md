---
layout: problem
title:  "Grid Obstacle Representations"
date:   2017-07-14
permalink: grid-obstacle.html
categories: openproblem
---
This is stuff I've been working on with Saeed Mehrabi following up [some work he did][biedl-mehrabi] with Therese Biedl.

Let $\Z^2$ denote the integer 2-dimensional integer grid, treated as a 4-regular graph or a point set depending on context. For two points in $p,q\in \Z^2$, let $\|pq\|_1$ denote their $L_1$ (Manhattan) distance.

A *non-blocking grid obstacle representation* $(\varphi, B)$ of a graph $G$ consists of a one-to-one mapping $\varphi:V(G)\to\Z^2$ and a set $B$ of connected subsets of $\Z^2$ such that $\cup B\cap \\{\varphi(v):v\in V(G)\\}=\emptyset$ and $uv\in E(G)$ if and only if there is a path from $\varphi(u)$ to $\varphi(v)$ in $\Z^2\setminus(\cup B)$ of length $\|uv\|_1$.

<div class="problem">
Does every planar graph have a non-blocking grid-obstacle representation?
</div>

We can show that every outerplanar graph has a non-blocking grid-obstacle representation.

The main difficulty comes from an implicit transitivity in these representations.  If, in the representation, there is a x-y-monotone path from $u$ to $v$ (so that $uv\in E(G)$) and there is an x-y-monotone path from $v$ to $w$ (so that $vw\in E(G)$) then there is also an x-y-monotone path from $u$ to $w$ (therefore $uw$ must be in $E(G)$).

This implies a necessary condition.  Let $\overrightarrow{E}(G)$ denote the directed edges of $G$ so that, if $uw\in E(G)$ then $uw$ and $wu$ are both in $\overrightarrow{E}(G)$.  Then it must be possible to find a coloring $c:\overrightarrow{E}(G)\to\\{-2,-1,1,2\\}$ such that

1. $c(uw) = -c(wu)$ for all $uw\in E(G)$;
2. If $c(uv) = c(vw)$, then $uw\in E(G)$; and
3. In an embedding of $G$, the colours around vertex every $v$ must occur in the order $-1^*-2^*1^*2^*$.

Is this possible to do for every planar graph $G$?

One observation is that, if $v$ is not part of a separating triangle, then the colours of its outgoing edges must be some rotation of $-1,1,2,2,2,\ldots,2$.  This feels a bit like Schnyder's tree decomposition might help.


[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
