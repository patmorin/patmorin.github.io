---
layout: problem
title:  "Grid Obstacle Representations"
date:   2017-07-14
permalink: grid-obstacle.html
categories: openproblem
---
This is stuff I've been working on with Saeed Mehrabi and Paz Carmi following up on [some work he did][biedl-mehrabi] with Therese Biedl.

A *non-blocking grid obstacle representation* of a planar graph $G$ is (equivalent to) a planar drawing of $G$ in which, for every pair $u,w\in V(G)$, the drawing contains an x-y-monotone path from $u$ to $w$ if and only if $uw\in E(G)$.  Here are some things we have been able to show:

* Every outerplanar graph has a non-blocking grid obstacle representation.
* Every 2-tree has a non-blocking grid obstacle representation
* Not every planar graph has a non-blocking grid obstacle representation
  * A fairly simple argument shows that the complete 3-ary 3-tree of height 4 does not have a non-blocking grid obstacle representation
  * A more detailed argument shows that a particular 4-connected planar graph
      has no non-blocking grid obstacle representation.
* The infinite triangular grid has a non-blocking grid obstacle representation.

This leaves the following question:
<div class="problem">
  Does every partial 2-tree have a non-blocking grid obstacle representation?
</div>

# Notations

For a point/vertex $u$ and an integer $i\in\\{0,\ldots,3\\}$, let $Q_i(u)$ denote the open $i$the quadrant with corner at $u$.  More precisely,
\begin{align}
   Q_i(u) = \left\\{ u+\begin{cases}
      (x,y): x,y> 0 & \text{when $i=0$} \newline
      (x,y): x,-y> 0 & \text{when $i=1$} \newline
      (x,y): -x,-y> 0 & \text{when $i=2$} \newline
      (x,y): -x,y> 0 & \text{when $i=3$}
  \end{cases} \right\\}
\end{align}

A *chord* in an outerplanar graph is an edge with bounded faces on each side of it.

# Outerplanar Graphs

## 2-Connected Outerplanar Graphs

<div class="thm">
  Every 2-connected outerplanar graph has a straight-line non-blocking grid obstacle representation in which all vertices appear on the outer face.
</div>

<div class="proof" markdown="1">
  Let $G$ be a 2-connected outerplanar graph.   The proof is by induction on the number of chords of $G$.  If $G$ has no chords, then it is a cycle and we can easily find a grid obstacle representation that looks like a lightning-bolt (if the number of vertices is even) or like a lightning bolt with a blunt end of the number of vertices is odd.

  Assume that $G$ therefore has at least one chord. Then $G$ has a chord $xy$ such that $G\setminus\\{x,y\\}$ has one component that is a path.  Therefore, there is a path $x=v_0,\ldots,v_k=y$ on the outer face of $G$ and $v_i$ has degree 2 for all $i\in\\{1,\ldots,k-1\\}$.  Now, apply the inductive hypothesis to obtain a non-blocking grid-representation of $G\setminus\\{v_1,\ldots,v_{k-1}\\}$.  Suppose, without loss of generality that, in this representation, $y\in Q_0(x)$, so $y$ is above and to the right of $x$, and that the face to the left of $xy$ is an interior face.

  * Case 1: $y$ has a neighbour $z$ in $Q_0(y)$. In this case, we claim that $x$ has no neighbour in $Q_2(x)$, for if it had a neighbour $w$ in $Q_2(x)$, then $wxyz$ would be a monotone path, and would therefore induce a $K_4$ in $G$, contradicting the assumption that $G$ is outerplanar.  Therefore, there is a sufficiently small neighbourhood near $y$ in $Q_1(y)\cap Q_0(x)$ in which we can embed that path $v_1,\ldots,v_{k-1}$ as an x-monotone zig-zag.

  {:.center}
  ![xy-a](images/xy-a.svg)


  * Case 2: $x$ has a neighbour $w$ in $Q_2(x)$.  This case is symmetric to Case 1 above.

  * Case 3: $x$ has no neighbour in $Q_2(x)$ and $y$ has no neighbour in $Q_0(y)$.  In this case, we can embed $v_1,\ldots,v_{k-1}$ as an x-monotone zig-zag path in some sufficiently small neighbourhood near (say) the midpoint of $xy$.

  {:.center}  
  ![xy-a](images/xy-b.svg)

</div>

## General Outerplanar Graphs

For general outerplanar graphs, we rely on the following technical lemma:

<div class="lemma">
  Let $G$ be a chord-free outerplanar graph with two vertices adjacent $x$ and $y$, each of degree-1 such that there is a unique cycle containing $xy$ from $x$ to $y$.  Then, for any two points $x'$ and $y'$ with $y'\in Q_0(x')$, any point $m$ on the open segment $x'y'$, and any $\epsilon>0$, there is a straight-line non-blocking grid representation of $G$ in which
  1. All vertices of $G$ appear on the outer face;
  2. $x$ and $y$ are drawn at positions $x'$ and $y'$, respectively;
  3. the vertices $V(G)\setminus\\{x,y\\}$ all appear in a ball of radius $\epsilon$ centered at $m$; and
  4. the vertices $V(G)\setminus\\{x,y\\}$ are all to the right of the supporting line of $x'y'$.
</div>

<div class="proof">
  Sketch: Do induction on the number of vertices, either by removing a degree 1 vertex or by removing an entire cycle that is only connected to the rest of the graph by a single vertex. (Maintain the invariant that any vertex only has neighbours in at most 2 consecutive quadrants.)
</div>

<div class="theorem">
  Every outerplanar graph $G$ has a straight-line non-blocking grid obstacle representation in which all vertices appear on the outer face.  
</div>

<div class="proof">
  Without loss of generality, we can assume that $G$ is connected.
  The proof is, again, by induction on the number of chords in $G$. If $G$ has no chords, then we can apply the preceding lemma with dummy values of $x$ and $y$.  

  Otherwise, $G$ has some chord $xy$ such that removing $xy$ from $G$ partitions $G$ is into several connected subgraphs $G_1,\ldots,G_{k}$ and at least one of these subgraphs, say $G_1$ is such that $G[V(G_1)\cup\\{x,y\\}]$ has the structure needed to apply the preceding lemma.  In this case, apply induction on $G'=G[V(G_2)\cup\cdots\cup V(G_k)\cup\\{x,y\\}]$.  Like the proof for 2-connected planar graphs, this produces an embedding of $G'$. In particular, it fixes the locations of $x$ and $y$ and the edge $xy$ has a bounded face on one side of it.  Now, following the same 3-case argument as in the proof for 2-connected planar graphs, and using the preceding lemma, we add G_1$ to this embedding.
</div>

# 2-Trees

Vida and David have a lemma that says every 2-tree $T$ has a non-empty independent set $S$ such that (i) $T\setminus S$ is a triangle or (ii) $T\setminus S$ has a degree-2 vertex $v$ with neighbours $x$ and $y$ such that every element of $S$ is adjacent to $vx$ or to $vy$.  Using lemma we can prove:

<div class="theorem">
   Every 2-tree has a non-blocking grid obstacle representation.
</div>

<div class="proof" markdown="1">
{:.center}
![2-tree proof](images/2-trees.jpg)
</div>


# Triangulations

Initially, we thought that there might be no non-blocking grid obstacle representation of the triangular grid, but then we found one:

<div class="theorem">
   The infinite triangular grid has a non-blocking grid obstacle representation.
</div>

![triangular grid](images/triangular-grid.svg)

## 3-Connected Triangulations

There's an easy argument that shows that not all triangulations have non-blocking grid obstacle representations.  It starts with the following geometric lemma:

<div class="lemma">
  Any triangle $xyz$ can be labelled so that $y,z\in Q_i(x)$ for some $i\in\{0,\ldots,3\}$.
</div>

<div class="proof">
  A short case analysis.
</div>

A *subdivision* of a triangle $xyz$ is obtained by adding a vertex $w$ in the interior of $xyz$ and adding the edges $wx$, $wy$, $wz$.  A $d$-level subdivision of $xyz$ is obtained by repeating this process recursively to a depth of $d$.

<div class="lemma">
   Let $G$ be a non-blocking grid obstacle representation of some graph, and let $xyz$ be a three-cycle in $G$ whose three edges all have positive slope.  Then $xyz$ does not contains a 2-level subdivision in its interior.
</div>

<div class="proof">
   A short case analysis on the position of the first-level subdivision vertex.
</div>

<div class="lemma">
   Let $G$ be a non-blocking grid obstacle representation of some graph, and let $xyz$ be a three-cycle in $G$ with $yz\in Q_i(x)$ for some $i$.  Then $xyz$ does not contains a 3-level subdivision in its interior.
</div>

<div class="proof">
   A short case analysis shows that the first-level subdivision vertex must create a triangle whose edges all have the same slope, then we apply the previous lemma.
</div>

<div class="theorem">
   The graph $G$ that is a 4-level subdivision of a triangle does not have a non-blocking grid obstacle representation.
</div>

<div class="proof">
   This follows from the previous three proofs, by taking the outer face as $xyz$ and observing that this face contains a 3-level subdivision.
</div>

## 4-Connected Triangulations

Let $G$ be a grid obstacle representation of a 4-connected triangulation.  Thus $G$ is a planar drawing whose vertices are identified with points in $\R^2$ and whose edges are x-y-monotone curves.  For a vertex $u$ of $G$, let $Q_i(u)$ denote the $i$th quadrant centered at $u$, where quadrants are labelled $0,\ldots,3$ in clockwise order.  Here and throughout the subscript $i$ in $Q_i(u)$ is implicitly taken modulo 4.

<div class="lemma">
  For every internal vertex $u$ of $G$, there is an $i\in\{0,\ldots,3\}$ such that $u$ has exactly one neighbour in $Q_{i-1}(u)$, exactly one neighbour in $Q_{i+1}(u)$, and all remaining neighbours in $Q_i(u)$.
</div>

<div class="proof">
  If this were not the case then, since $G$ is 4-connected, $u$ would have two non-adjacent neighbours $x$ and $y$ with $x\in Q_j(u)$ and $y\in Q_{j+2}(u)$.  But this is a contradiction, since then the path $xuy$ is x-y-monotone but $x$ and $y$ are not adjacent.
</div>

The preceding lemma classifies the internal vertices of $u$ into four types $0$, $1$, $2$, and $3$.  We therefore define $c(u)$ as the *type* of the vertex $u$.  For an internal vertex $u$ with $c(u)=i$, it is helpful to think of $u$ has having most of its neighbours in $Q_i(u)$ and as having none of its neighbours in $Q_{i+2}(u)$.


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
  Let $u$ be an internal vertex of $G$ with $c(u)=i$.  Then $u$'s neighbours $x$ and $y$ in $Q_{i-1}(u)$ and $Q_{i+1}(u)$ are each either outer vertices or have $c(x)=i+1$ and $c(y)=i-1$. Similarly, $u$'s neighbour $y$ in $Q_{i+1}(u)$ is either an outer vertex or $c(y)=i-1$.  Any vertex $z\in Q_i(u)$ has at least one neighbour (namely $u$) in $Q_{i+2}(z)$ so $z$ is either an outer vertex or $c(z)\neq i$.
</div>

Now consider the graph $H$ shown here, and let the letters attached to vertices denote the colour of these vertices:

{:.center}
![2-tree proof](images/h.svg)

<div class="lemma">
   If $G$ is a non-blocking grid obstacle representation and $G$ contains $H$ and all its vertices are interior, then $c(e)=i$, $c(f)=i+1$, $c(g)=i+2$ and $c(h)=i+3$.
</div>

<div class="proof">
   The proof is a lengthy, but not difficult case analysis starting with the assumptions that $a=0$ and $c=2$ or that $a=0$ and $c=1$ and using the last two lemmas above.
</div>

<div class="theorem">
   There exists a 4-connected triangulation $G$ with maximum degree 7 that does not have a non-blocking grid obstacle representation.
</div>

<div class="proof" markdown="1">
  {:.center}
  ![g](images/g.svg)
</div>









{::comment}
Stop reading here.

# Triangulations Suffice.

Here is an observation of Paz:

<div class="lemma">
  If every triangulation has a non-blocking grid obstacle representation then every planar graph has a non-blocking grid obstacle representation.
</div>

<div class="proof" markdown="1">
  Given a planar graph $G$, place Steiner vertices into each of its non-triangular faces and triangulate so that every newly introduced edge is incident to at least one Steiner vertex.  If we can find a non-blocking grid obstacle representation of this triangulation, then removing the Steiner vertices gives a non-blocking grid obstacle representation of $G$.
</div>

# 2-Trees


Can we extend this to partial 2-trees?  Paz and Saeed claim to have a proof of the following:

<div class="theorem">
   Every outerplanar graph has a non-blocking grid obstacle representation.
</div>


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

With a little bit of padding we can prove the following, which shows that proving that every triangulation has a non-blocking grid obstacle representation is at least as hard as proving the four-colour theorem:

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
