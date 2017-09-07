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


Let $G$ be an embedded triangulation without separating triangles.
Let $\overrightarrow{E}(G)$ denote the directed edges of $G$ so that, if $uw\in E(G)$ then $uw$ and $wu$ are both in $\overrightarrow{E}(G)$.  A *good colouring* of $\overrightarrow{E}(G)$ is a map $c:\overrightarrow{E}(G)\to\\{0,1,2,3\\}$ such that

1. $c(uw) = (c(wu)+2)\bmod 4$ for all $uw\in E(G)$;
2. if $c(uv) = c(vw)$, then $uw\in E(G)$ and c(uw)=c(uv);
3. for every vertex $u$ whose neighbours in clockwise order are $v_1,\ldots,v_k$, the sequence of colours $c(v_1),\ldots,c(v_k)$ is non-decreasing (with the appropriate choice of starting vertex $v_1$); and
4. For every vertex $u$ not on the outer face of $G$, $u$ has two neighbours $x$ and $y$ such that $c(ux)\equiv c(uy)+2\pmod 4$ (equivalently $c(ux)=c(yu)$).

<div class="lemma">
  Let $u$ be some vertex not on the outer face and not part of a separating triangle and let $v_1,\ldots,v_k$ be the neighbours of $u$, in clockwise order.  Then (after a rotation of indices) $c(uv_1)\equiv i\pmod 4$, $c(uv_2)\equiv i+2\pmod 4$, and for each $j\in\{3,\ldots,k\}$, $c(uv_j)\equiv i+2\pmod 4$, for some $i\in\{0,1,2,3\}$.
</div>

<div class="proof">
  Omitted.
</div>

The preceding lemma naturally partitions the set of internal vertices into four types, one for each value of $i$.  For a vertex $v$, let $t(v)$ denote the type of $v$.  If $t_c(v)=i$, we call $v$ a type-$i$ vertex.  It's helpful to think of a type-$i$ vertex as having most of its neighbours in quadrant $i$ and none of its neighbours in quadrant $(i+2)\bmod 4$.

<div class="lemma">
  The partial function $t_c:V\to\{0,\ldots,3\}$ is a proper four coloring of the internal vertices of $G$.
</div>

<div class="proof">
  Omitted.
</div>

With a little bit of padding we can prove the following, which shows that proving that every triangulation has a non-blocking grid-obstacle representation is at least as hard as proving the four-colour theorem:

<div class="lemma">
   If $G$ is a triangulation that is not four-colourable, then there exists a planar triangulation $G'$ that does not have a non-blocking grid obstacle representation.
</div>

We can maybe more constructive, though.  Let $c$ be a good colouring of $G$ and define the relations $<\_x$ and $<\_y$ where $u <\_x w$ if $c(uw)\in\\{0,1\\}$ and that $u<\_y w$ if $c(uw)\in \\{0,3\\}$.

<div class="lemma">
   The relations $\lt_x$ and $\lt_y$ are partial orders.
</div>

<div class="proof">
   Assume that $\lt_x$ contains a cycle and consider the shortest such cycle
   $u_1\lt_x u_2\lt_x\cdots\lt_x u_r\lt_x u_1$.  Then by minimality, the sequence $\langle c(u_iu_{i+1}):i=1,\ldots,r,1\rangle$ alternating.

   Now consider the types of $u_1,\ldots,u_r$ and show that closing the cycle
   messes up the ordering somehow.
</div>

<div class="lemma">
   A triangulation $G$ without separating triangles has a grid obstacle representation if and only $\overrightarrow{E}(G)$ has a good colouring.
</div>

Finally, we note that we can recover the edge-colouring $c$ from the vertex coloring $t$.

<div class="lemma">
   If $c$ is a good colouring, then it is the unique good colouring that
   produces the type function $t_c$.
</div>

So this means that what we're really trying to prove is a strengthening of the Four-Colour Theorem that not only gives a proper four-colouring of $V(G)$, but gives one that is defined by some good colouring of $\overrightarrow{E}(G)$



[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
