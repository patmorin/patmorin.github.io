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
  Given a planar graph $G$, place Steiner vertices into each of its non-triangular faces and triangulate so that every newly introduced edge is incident to at least one Steiner vertex.  If we can find a non-blocking grid obstacle representation of this triangulation, then removing the Steiner vertices gives a non-blocking grid obstacle representation of $G$.
</div>

# 2-Trees

Vida and David have a lemma that says every 2-tree $T$ has a non-empty independent set $S$ such that (i) $T\setminus S$ is a triangle or (ii) $T\setminus S$ has a degree-2 vertex $v$ with neighbours $x$ and $y$ such that every element of $S$ is adjacent to $vx$ or to $vy$.  Using lemma we can prove:

<div class="theorem">
   Every 2-tree has a non-blocking grid-obstacle representation.
</div>

<div class="proof" markdown="1">
{:.center}
![2-tree proof](images/2-trees.jpg)
</div>

Can we extend this to partial 2-trees?  Paz and Saeed claim to have a proof of the following:

<div class="theorem">
   Every outerplanar graph has a non-blocking grid-obstacle representation.
</div>


# Negative Result for Triangulations

## 3-Connected Triangulations

There's an easy argument that shows that not all triangulations have non-blocking grid obstacle representations.

<div class="lemma">
  Let $G$ be the subgraph of the (infinite) triangular grid obtained by taking the graph induced by all vertices within distance 5 of a particular vertex $v$.  Then any x-y-monotone embedding of $G$ contains some monotone triangle, i.e., a cycle $x,y,z$ such that the slopes of $xy$, $yz$, and $xz$ all have the same sign.
</div>

## 4-Connected Triangulations

Let $G$ be a grid-obstacle representation of a 4-connected triangulation.  Thus $G$ is a planar drawing whose vertices are identified with points in $\R^2$ and whose edges are x-y-monotone curves.  For a vertex $u$ of $G$, let $Q_i(u)$ denote the $i$th quadrant centered at $u$, where quadrants are labelled $0,\ldots,3$ in clockwise order.  Here and throughout the subscript $i$ in $Q_i(u)$ is implicitly taken modulo 4.

<div class="lemma">
  For every internal vertex $u$ of $G$, there is an $i\in\{0,\ldots,3\}$ such that $u$ has exactly one neighbour in $Q_{i-1}(u)$, exactly one neighbour in $Q_{i+1}(u)$, and all remaining neighbours in $Q_i(u)$.
</div>

<div class="proof">
  If this were not the case then, since $G$ is 4-connected, $u$ would have two non-adjacent neighbours $x$ and $y$ with $x\in Q_j(u)$ and $y\in Q_{j+2}(u)$.  But this is a contradiction, since then the path $xuy$ is x-y-monotone but $x$ and $y$ are not adjacent.
</div>

The preceding lemma classifies the internal vertices of $u$ into four types $0$, $1$, $2$, and $3$.  We therefore, define $c(u)$ as the type of the vertex $u$.  For an internal vertex $u$ with $c(u)=i$, it is helpful to think of $u$ has having most of its neighbours in $Q_i(u)$ and as having none of its neighbours in $Q_{i+2}(u)$.


<div class="lemma">
  For an internal vertex $u$ of $G$ with $c(u)=i$, the neighbour $x$ of $u$ in $Q_{i-1}(u)$ is either an outer vertex or $c(x) = i+1$.  Similarly, the neighbour $y$ of $u$ in $Q_{i+i}(u)$ has $c(y)=i-1$.
</div>

<div class="proof">
  The vertex $x$ has two neighbours, namely $y$ and $u$ in $Q_{i+1}(z)$ so $c(z)=i+1$. The same argument applies to $y$.
</div>

<div class="lemma">
  The partial function $c\colon V\to\{0,1,2,3\}$ is a proper colouring of the internal vertices of $G$.
</div>

<div class="proof">
  Let $u$ be an internal vertex of $G$ with $c(u)=i$.  Then $u$'s neighbours $x$ and $y$ in $Q_{i-1}(u)$ and $Q_{i+1}(u)$ are each either outer vertices or have $c(x)=i+1$ and $c(y)=i-1$. Similarly, $u$'s neighbor $y$ in $Q_{i+1}(u)$ is either an outer vertex or $c(y)=i-1$.  Any vertex $z\in Q_i(u)$ has at least one neighbour (namely $u$) in $Q_{i+2}(z)$ so $z$ is either an outer vertex or $c(z)\neq i$.
</div>

Now consider the graph $H$ shown here, and let the letters attached to vertices denote the colour of these vertices:

{:.center}
![2-tree proof](images/h.svg)

<div class="lemma">
   If $G$ is a non-blocking grid obstacle representation and $G$ contains $H$ and all its vertices are interior, then $\{c(e),c(f),c(g),c(g)\} = \{0,1,2,3\}$.
</div>

<div class="proof">
   The proof is a lengthy, but not difficult case analysis starting with the assumptions that $a=0$ and $c=2$ or that $a=0$ and $c=1$ and using the last two lemmas above.
</div>

<div class="theorem">
   There exists a triangulation $G$ that does not have a non-blocking grid obstacle representation.
</div>

<div class="proof">
  Create a triangulation $G$ that contains two copies of $H$ in which each of the vertices labelled $e$, $f$, $g$, and $h$ is adjacent to a common vertex $z_1$ and $z_2$ and such no vertex of the first copy is on the same face as any vertex of the second copy.  Then in any planar drawing of $G$, one of these copies of $H$ along with its corresponding vertex $z_i$ has only interior vertices.  By the previous lemma means that $z_i$ has neighbours of colours $0$, $1$, $2$, and $3$.  Therefore, $z_i$ has the same colour as one of its neighbours, contradicting the proper colouring lemma above.
</div>









{::comment}
Stop reading here.

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
{:/comment}


[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
