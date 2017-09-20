---
layout: problem
title:  "Grid Obstacle Representations"
date:   2017-07-14
permalink: grid-obstacle.html
categories: openproblem
---
This is stuff I've been working on with other CG Lab Members following up on [some work of Saeed Mehrabi and Therese Biedl][biedl-mehrabi].

## A Very General definition

For two graphs $H$ and $G$, a *non-blocking $H$-obstacle representation* of $G$ is a pair $(\varphi:V(G)\to V(H), S\subseteq H)$, with the following properties:

1. $\varphi$ is one-to-one, i.e., $\varphi(u)\neq\varphi(w)$ if and only if $u\neq w$;
2. for every $u\in V(G)$, $\varphi(u)\not\in S$; and
3. for every $u,w\in V(G)$, $d_{H\setminus S}(\varphi(u),\varphi(w)=d_{H}(\varphi(u),\varphi(w)$ if and only if $uw\in E(G)$.

In the "plane case" there is also a mapping $\tau$ from edges of $G$ onto shortest paths in in $H\setminus S$ such that
1. for any $uw\in E(G)$, $\tau(uw)$ is a shortest path in $H\setminus S$ from $u$ to $w$; and
2. for any $e_1\neq e_2$, $\tau(e_1)$ and $\tau(e_2)$ have no vertices in common except, possibly, their endpoints.

In this case, we call $(\varphi,S,\tau)$ a plane non-blocking $H$-obstacle representation of $G$.

Note that for a fixed $H$, the property "$G$ has a (plane) non-blocking $H$ representation" is not monotone in $E(G)$.  It is, however, monotone in $V(G)$:

<div class="observation">
  If $G$ has an a (plane) non-blocking $H$-obstacle representation, then so does every induced subgraph of $G$.
</div>

Most previous work has taken $H$ to be the square grid, in which case this representation is called a (plane) non-blocking grid obstacle representation.


## The Square Grid

By using a fine enough grid, it is not hard to see that a planar graph $G$ has a plane non-blocking grid-obstacle representation if and only if there is plane drawing of $G$ in which, for every pair $u,w\in V(G)$, the drawing contains an x-y-monotone path from $u$ to $w$ if and only if $uw\in E(G)$.  Here are some things we have been able to show:

* Every partial 2-tree has a plane non-blocking grid obstacle representation
* Not every planar graph has a plane non-blocking grid obstacle representation
  * A fairly simple argument shows that the complete 3-ary 3-tree of height 4 does not have a non-blocking grid obstacle representation
  * A more detailed argument shows that a particular 4-connected planar graph
      has no non-blocking grid obstacle representation.
* The infinite triangular grid has a non-blocking grid obstacle representation.


# Notations

For a point/vertex $u$ and an integer $i\in\\{0,\ldots,3\\}$, let $Q_i(u)$ denote the $i$th open quadrant with corner at $u$.  More precisely,
\begin{align}
   Q_i(u) = \left\\{ u+\begin{cases}
      (x,y): x,y> 0 & \text{when $i=0$} \newline
      (x,y): x,-y> 0 & \text{when $i=1$} \newline
      (x,y): -x,-y> 0 & \text{when $i=2$} \newline
      (x,y): -x,y> 0 & \text{when $i=3$}
  \end{cases} \right\\}
\end{align}

A *chord* in an outerplanar graph is an edge with bounded faces on each side of it.


{::comment}

# Outerplanar Graphs

## 2-Connected Outerplanar Graphs

<div class="thm">
  Every 2-connected outerplanar graph has a straight-line non-blocking grid obstacle representation in which all vertices appear on the outer face.
</div>

<div class="proof" markdown="1">
  Let $G$ be a 2-connected outerplanar graph.   The proof is by induction on the number of chords of $G$.  If $G$ has no chords, then it is a cycle and we can easily find a grid obstacle representation that looks like a lightning-bolt (if the number of vertices is even) or like a lightning bolt with a blunt end (if the number of vertices is odd).

  Assume that $G$ therefore has at least one chord. Then $G$ has a chord $xy$ such that $G\setminus\\{x,y\\}$ has one component that is a path.  Therefore, there is a path $x=v_0,\ldots,v_k=y$ on the outer face of $G$ where $v_i$ has degree 2 for all $i\in\\{1,\ldots,k-1\\}$.  Now, apply the inductive hypothesis to obtain a non-blocking grid-representation of $G\setminus\\{v_1,\ldots,v_{k-1}\\}$.  Suppose, without loss of generality that, in this representation, $y\in Q_0(x)$, so $y$ is above and to the right of $x$, and that the face to the left of $xy$ is an interior face.

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

<div class="lemma" markdown="1">
  Let $G$ be a chord-free outerplanar graph with two adjacent vertices $x$ and $y$, such that there is a unique cycle containing $xy$.  Then, for any two points $x'$ and $y'$ with $y'\in Q_0(x')$, any point $m$ on the open segment $x'y'$, and any $\epsilon>0$, there is a straight-line non-blocking grid representation of $G$ in which

  1. all vertices of $G$ appear on the outer face;
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

  Otherwise, $G$ has some chord $xy$ such that removing $xy$ from $G$ partitions $G$ into several connected subgraphs $G_1,\ldots,G_{k}$ and at least one of these subgraphs, say $G_1$ is such that $G[V(G_1)\cup\{x,y\}]$ has the structure needed to apply the preceding lemma.  In this case, apply induction on $G'=G[V(G_2)\cup\cdots\cup V(G_k)\cup\\{x,y\\}]$.  Like the proof for 2-connected planar graphs, this produces an embedding of $G'$. In particular, it fixes the locations of $x$ and $y$ and the edge $xy$ has a bounded face on one side of it.  Now, following the same 3-case argument as in the proof for 2-connected planar graphs, and using the preceding lemma, we add $G_1$ to this embedding.
</div>

{:/comment}

# Partial 2-Trees

We make use of the following Lemma of Dujmovic and Wood:

<div class="lemma">
  Every 2-tree $T$ is either a 3-cycle or it contains a non-empty independent set $S$ such that $T\setminus S$ is a 2-tree that has a degree-2 vertex $u$ with neighbours $x$ and $y$ such that every element of $S$ is adjacent to $ux$ or to $uy$.
</div>

<div class="theorem">
   Every partial 2-tree has a straight-line non-blocking grid obstacle representation.
</div>

<div class="proof" markdown="1">
  Let $G$ be a partial 2-tree. We can, without loss of generality, assume that $G$
  is connected.  If $|V(G)|< 4$, then the result is trivial, so we can assume $|V(G)|\ge 4$.  We now proceed by induction on $|V(G)|$.

  Let $T=T(G)$ be a 2-tree with vertex set $V(G)$ and that contains $G$.  Apply the preceding lemma to $T$ to find the vertex set $S$ and the vertices $u$, $x$, and $y$ described in the lemma.  Now apply induction to find a non-blocking grid representation of the graph $G'$ whose vertex set is $V(G')=V(G)\setminus S$ and whose edge set is $E(G')=E(G\setminus S)\cup\\{ux,uy\\}$.

  Now observe that, since $u$ has degree 2 in $G'$ and the edges $ux$ and $uy$ are in $G'$, this embedding does not contain any monotone path of the form $uxw$ or $uyw$ for any $w\in V(G)\setminus\\{u,x,y\\}$.  Therefore, if we place the vertices in $S$ sufficiently close to $u$, we will not create any monotone path of the form $ayw$ or $axw$ for any $a\in S$ and any $w\in V(G)\setminus \\{u,x,y\\}$.  What remains is to show how to place the elements of $S$ in order to avoid unwanted monotone paths of the form $uay$, $uax$, or $aub$ for any $a,b\in S$.

  There are three cases to consider:

  - $x\in Q_i(u)$ and $y\in Q_{i+2}(u)$ for some $i\in\\{0,\ldots,3\\}$. Without loss of generality, assume that $Q_{i+3}(u)$ does not intersect the segment $xy$. Then we can embed the elements of $S$ in $Q_{i+3}$ without creating any new monotone paths.

  {:.center}
  ![2-tree case 1](images/2tree-1.svg)

  - $x,y\in Q_i(u)$ for some $i\in\\{0,\ldots,3\\}$. There are two subcases:
    - At least one of $ux$ or $uy$ is in $E(G)$. Suppose $ux\in E(G)$.  Then we embed $S_x$ in $Q_i(u)$ and embed $S_y$ in $Q_{i+1}(u)$.  The only monotone paths this creates are of the form $uax$ with $a\in S_x$, which is acceptable since $ux\in E(G)$.
    - Neither $ux$ nor $uy$ is in $E(G)$. In this case, we embed all of $S$ in $Q_{i+2}(u)$.  This does not create any new monotone paths.

    {:.center}
    ![2-tree case 2.1](images/2tree-2.svg)
    ![2-tree case 2.1](images/2tree-3.svg)

  - $x\in Q_i(u)$ and $y\in Q_{i+1}(u)$ for some $i\in\\{0,\ldots,3\\}$.  We have two subcases to consider:
    - $\|\{ux,uy\}\cap E(G)\|=1$.  In this case, assume $ux\in E(G)$. Then we embed the vertices of $S_x$ in $Q_i(u)$ and we embed the vertices of $S_y$ in $Q_{i+3}(u)$.  The only monotone paths this creates are of the form $uax$ with $a\in S_x$, which is acceptable since $ux\in E(G)$.
    - $\|\\{ux,uy\\}\cap E(G)\|=2$.  In this case we embed the vertices of $S_x$ in $Q_i(u)$ and we embed the vertices of $S_y$ in $Q_{i+1}(u)$.  The only monotone paths this creates are of the form $uax$ with $a\in S_x$ and $uby$ with $b\in S_y$, which is acceptable since $ux,uy\in E(G)$.
    - $\|\\{ux,uy\\}\cap E(G)\|=0$.  In this case, we embed all of $S$ into $Q_{i+2}\cup Q_{i+3}$.  This does not create any new monotone paths.

    {:.center}
    ![2-tree case 2.1](images/2tree-4.svg)
    ![2-tree case 2.1](images/2tree-5.svg)
    ![2-tree case 2.1](images/2tree-6.svg)

This completes the proof.
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

<div class="problem">
   Is there a 4-connected triangulation of maximum degree 6 that does not have a non-blocking grid obstacle representation?
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


# Extensions and Generalizations

Here we present a couple of directions for future research.

## Triangular Grid

If we go back to the general definition of non-blocking $H$ representation and take $H$ to be the infinite triangular grid, then we come up with an interesting variant.

For any $d\in\N$, and any $u\in\R^2$, define the $i$th $d$-sector of $u$ as
\\[
Q^{d}_i(u) = \\{ u+r: r\in\R^2,\,\lfloor d\angle(u+(1,0),u,r)/(2\pi)\rfloor=i \\}
\\]
Where $\angle (a,b,c)\in[0,2\pi)$ denotes the counterclockwise angle between the segments $ab$ and $cb$.

A curve $f:[0,1]\to\R^2$ is $d$-monotone in direction $i$ if $f(b)\in Q^d_i(f(a))$ for all $0 \le a < b \le 1$.  We say that $f$ is $d$-monotone if there exists some $i\in\\{0,\ldots,d-1\\}$ such that $f$ is $d$-monotone in direction $i$.

A plane graph $G$ has a plane non-blocking 6-grid obstacle representation if and only if it has a a drawing such that, for every $u,v\in V(G)$, $G$ contains a $d$-monotone path from from $u$ to $v$ if and only if $uv\in E(G)$. Note that in the case $d=4$, a curve is 4-monotone if and only if it is x-y-monotone, so non-blocking 4-grid obstacle representations are the non-blocking grid obstacle representations described above.

<div class="theorem">
  Every planar 3-tree has a straight-line non-blocking 6-grid obstacle representation.
</div>

<div class="proof" markdown="1">
The proof is by induction on the size of the 3-tree $G$.  The smallest planar 3-tree is the clique $K_4$ on four vertices, for which any planar drawing gives a non-blocking 6-monotone representation.

That result of Dujmovic and Wood, when specialized to planar 3-trees says that every planar 3-tree is either $K_4$ or has a vertex $u$ and an independent set $S$ ($\|S\|\le 3$) such that $G\setminus S$ is a 3-tree, $u$ has degree 3 in $G\setminus S$, with neighbours $x$, $y$, and $z$, and every vertex $r$ in $S$ forms a clique with exactly one of $uxy$, $uyz$, or $uzx$.

In the case $\|V(G)\|>4$, we applying the preding result and recurse on $G\setminus S$.  This gives us back a non-blocking 6-grid obstacle representation of $G\setminus S$.  There are two cases to consider, depending on the locations $x$, $y$, and $z$, with respect to $u$.  In both cases, the elements of $S$ are placed very close to $u$, so we do not create any new monotone paths involving vertices other than those in $\\{u,x,y,z\\}\cup S$.  Furthermore, since $\\{u,x,y,z\\}$ form a complete graph, we only need to worry about possibly creating a new monotone path involving at least one vertex of $S$.

1. No two neighbours of $u$ are in consecutive 6-sectors, e.g., $x\in Q^6_1(u)$, $y\in Q^6_3(u)$ and $z\in Q^6_5(u)$.  In this case, we add the elements of $S$ as in the following figure:

{:.center}
![3-tree proof case 1](images/3tree-1.svg)

2. Two neighbours of $u$ are in consecutive 6-sectors, e.g., $x\in Q^6_1(u)$, $y\in Q^6_2(u)$, and $z\in Q^6_5(u)$.  In this case we add the elements of $S$ as in the following figure:

{:.center}
![3-tree proof case 2](images/3tree-2.svg)

</div>



Here's a stronger version of the preceding theorem:

<div class="theorem">
  Every partial planar 3-tree has a non-blocking 6-grid obstacle representation.
</div>

<div class="proof" markdown="1">
  The proof follows the same lines the preceding proof except that we apply induction on the graph $G'$ whose vertices are $V(G)\setminus S$ and whose edge set is $E(G\setminus S)\cup\\{ux,uy,uz\\}$.  Then we have lots of cases to consider depending on the positions of $x$, $y$, and $z$ with respect to $u$ as well as whether the edges $ux$, $uy$, and $uz$ are present in $G$. Here what the cases look like:

  {:.center}
  ![partial-3-tree proof case](images/partial-3tree-1.svg)
  ![partial-3-tree proof case](images/partial-3tree-2.svg)
  ![partial-3-tree proof case](images/partial-3tree-3.svg)
  ![partial-3-tree proof case](images/partial-3tree-4.svg)
  ![partial-3-tree proof case](images/partial-3tree-5.svg)
  ![partial-3-tree proof case](images/partial-3tree-6.svg)
  ![partial-3-tree proof case](images/partial-3tree-7.svg)
  ![partial-3-tree proof case](images/partial-3tree-8.svg)
  ![partial-3-tree proof case](images/partial-3tree-9.svg)
  ![partial-3-tree proof case](images/partial-3tree-10.svg)
  ![partial-3-tree proof case](images/partial-3tree-11.svg)
  ![partial-3-tree proof case](images/partial-3tree-12.svg)
  ![partial-3-tree proof case](images/partial-3tree-13.svg)
  ![partial-3-tree proof case](images/partial-3tree-14.svg)

</div>

The fact that every 3-tree (and even partial 3-tree) has a non-blocking 6-grid obstacle representation but not a non-blocking 4-grid obstacle representation raises the following open problem:

<div class="problem">
  Does every planar graph graph have a non-blocking 6-grid obstacle representation?
</div>

For any planar graph $G$, we can always add Steiner vertices and edges to obtain a triangulation that contains $G$ as an induced subgraph. Therefore, it suffices to study the preceding problem for triangulations.

## Non-Planar Graphs

This problem can have two possible extension to non-planar graphs:

**Version 1:** A *x-y-transitive embedding* of a graph $G$ is a drawing of $G$ in which, for every pair $u,w\in V(G)$, the embedding contains an x-y-monotone path from $u$ to $w$ if and only if $uw\in E(G)$.  

**Version 2:** A *x-y-transitive drawing* of a graph $G$ is a drawing of $G$ in which, for every pair $u,w\in V(G)$, the drawing, treated as the union of all its edges and vertices contains an x-y-monotone path from $u$ to $w$ if and only if $uw\in E(G)$.  

The key difference between these two versions is what happens when two edges $uw$ and $xy$ cross. In the first version, this has no effect on the definition.  In the second version, if $uw$ and $xy$ both have positive slope, then the edges $ux$ and $wy$ must be present and have positive slope.  The second version is closer in spirit to the original non-blocking grid-obstacle question.

Here's an easy result:

<div class="theorem">
   There exist graphs that do not have an x-y-transitive embedding or drawing.
</div>

<div class="proof">
  Consider some x-y-transitive embedding of any $n$-vertex graph $G$.  Then, by Dilwerth's Theorem, there is a set $S$ of $\sqrt{n}$ vertices that form an xy-monotone sequence.  The set $S$ must induce a collection of disjoint cliques in $G$.  One or these cliques must have at least $n^{1/4}$ vertices or there must be at least $n^{1/4}$ cliques. In the latter case, selecting one vertex from each clique produces an independent set of size at least $n^{1/4}$.

  The result now follows from the existence of graphs (established by Erdos and Renyi) having no indpendent set or clique of size $\log n$.
</div>


Here's another easy result:

<div class="theorem">
   Every 4-colourable graph, and hence every planar graph has an x-y-transitive embedding.
</div>

<div class="proof">
  Embed the graph on the four sides of the unit square, so that each side gets a colour class.  Then any path of length 2 has a middle vertex that is extreme in either the x or y direction, so it is not monotone.
</div>

It seems much more difficult to find an x-y-transitive drawing.


[biedl-mehrabi]: https://arxiv.org/abs/1708.01903
