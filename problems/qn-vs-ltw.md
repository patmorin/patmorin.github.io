---
layout: problem
title:  "Queue Number versus Layered Treewidth"
date:   2017-07-14
permalink: qn-vs-ltw.html
categories: openproblem solved
---
**Defunct:** This problem is more or less defunct at this point, because of this theorem:

<div class="theorem">
  If a graph $G$ has a layered $H$-partition with layered width $\ell$ where $\DeclareMathOperator{\qn}{qn}\qn(H)\le q$, then $\qn(G)\le 3q + 4$.
</div>

Every graph from an apex-minor-free family has such a layered $H$-partition (where $\ell$ and $q$ depend on the apex-minor) and so do $k$-planar graphs (where $\ell$ and $q$ depend on $k$.)  See [Dujmović et al.](https://arxiv.org/abs/1904.04791) and [Dujmović, Morin, and Wood](), respectively.

---
---

# The Original Problem

$\DeclareMathOperator{\depth}{depth}$[Bekos et al][bekos-ea] have recently shown that planar graphs of bounded maximum degree have bounded queue number.  Can we generlize this result to bounded layered treewidth graphs of bounded degree?

Here's what we have and what we need  (I think).

Here's what we have:

A graph $G_2$ that consists of
1. a max-degree $\Delta$ tree $T$ whose leaves all have the same depth, $h$, plus
2. a perfect matching $M$ on the leaves of $T$.

Furthermore, $G_2$ has layered treewidth at most $k$ using the layering $L_i = \lbrace v\in V(T) : \depth_T(v)=h-i\rbrace$.

Here's what I would like to have:

A partial order $\prec$ over $V(G_2)$ that has the following properties:

0. Two vertices of $G_2$ are comparable if and only if they belong to the same layer $L_i$.

1. $\prec$ defines a non-crossing drawing of $T$ where all nodes in $L_i$ are on the line $y=i$ in the order given by $\prec$.

2. $\prec$ defines an $O(1)$ page layout of $M$, i.e., for some $p\in O(1)$ there is no pencil of edges $x_1y_1,\ldots,x_py_p$ in $M$ where $x_1\prec x_2\prec\cdots\prec x_p \prec y_1 \prec\cdots y_p$.

# The Planar case

Bekos et al are given the partial order $\prec$ (it ultimately comes from a planar embedding of $G$ which translates into a planar embedding of $G_2$) and, in their case Requirement 3 is actually satisfied with $p=1$.  Still, I think it's instructive to see how to we could find $\prec$ if we weren't given this embedding.

Take any edge $x_0y_0$ of $M$ and consider the unique cycle $C=x_0,\ldots,(x_m=y_m),\ldots y_0$ in $G_2$ formed by $x_0y_0$ and the path, in $T$, from $x_0$ to $y_0$.  $G_2'=G_2-V(C)$ has connected components $A_1,\ldots,A_k$.  Each component $A_i$ is incident to one or more vertices of $C$.  We say that $A_i$ and $A_j$ are *incompatible* if there exists indices $a<b<c<d$ such that $A_i$ is adjacent to $v_a$ and $v_c$ and $A_j$ is adjacent to $v_b$ and $v_d$.  In other words, in a planar embedding of $G_2$ it is not possible to draw both $A_i$ and $A_j$ inside of $C$ nor is it possible to draw them both outside of $C$.  Now make a graph $H$ with vertex set $V(H)=\lbrace 1,\ldots,k\rbrace$ in which the edge $ij$ is present iff $A_i$ and $A_j$ are incompatible.  Note that, since $G_2$ is planar, $H$ has no odd cycles so it's bipartite.

Now this idea can be used in a recursive procedure to determine the order $\prec$.  Suppose someone has already told us that the $G_2$ has a planar embedding with outer face $F=v_0,\ldots,(v_h=w_h),w_{h-1},\ldots,w_0$ where each $v_i,w_i\in L_i$ and $v_0w_0$ is an edge of $M$.  Now we take any other edge $x_0y_0$ of $M$ and use the incompatibility graph $H$ described above which may have several components, each of which is bipartite.  Now one needs to make a quick argument that if $A_i$ and $A_j$ are in the same component of $H$ but on different sides of the bipartition, then at least one of $A_i$ or $A_j$ is not adjacent to any vertex in $V(F)\setminus V(C)$.  (Otherwise any planar drawing of $G_2$ would have $A_i$ and $A_j$ on opposite sides of $C$, but the vertices of $V(F)\setminus V(C)$ are all inside or all outside of $C$).  

Thus we can partition $V(G_2)\setminus V(F)\setminus V(C)$ into a set $A$ of vertices that should be drawn inside of $C$ and a set $B$ of vertices that should be drawn outside of $C$ (but inside of $F$).  

Now we can recurse on $G_2[V(C)\cup A]$ with $C$ as the outer face to order the vertices in $V(C)\cup A$.  Think of this as a drawing of $G[V(C)\cup A]$.  Note that before recursing, we had a choice about whether we should have $x_0\prec y_0$ or *vice-versa*.

Next consider the graph $G_2'$ obtained by contracting $(V(C)\cup A)\cap L_i$ for each $i\in\lbrace 1,\ldots,h\rbrace$.  In this graph $V(C)\cup A$ becomes a path $v_0,\ldots,v_m$ with $v_i\in L_i$.   The node $v_0$ has degree-1 and is unmatched in $M$, so we remove the maximal path $v_0,\ldots,v_k$ where each node in this path has degree at most 2.  Now we recurse on $G_2'$ to obtain an ordering on $V(F)\cup B\cup\lbrace v_0,\ldots,v_m\rbrace$.  Think of this also as a drawing of $G_2'$.


Now, we want to obtain a drawing of $G_2$ by replacing the path $v_0,\ldots,v_m$ with the drawing of $G_2[V(C)\cup A]$ obtained from the first recursive call.  Indeed this works, the only thing to look out for is that the drawing of $G_2[V(C)\cup A]$ may need to have its ordering reversed.  This happens because the path $v_1,\ldots,v_m$ in the drawing of $G_2'$ represents the outer face $x_0,\ldots,(x_m=y_m),y_{m-1},\ldots,y_0$ of the drawing of $G_2[V(C)\cup A]$. In $G_2$, some vertices of $G_2'$ are adjacent to $x_i$ or $y_i$ and but in $G_2'$ such vertices are all adjacent to $v_i$.  So after we draw $G_2'$ there is a distinction between vertices adjacent to $v_0,\ldots,v_m$ from the "$x$-side" and those adjacent to $v_0,\ldots,v_m$ from the "$y$-side".  Luckily (or by design) all the $x$-side vertices in $L_i$ precede $v_i$ and $v_i$ precedes all the $y$-side vertices, or vice-versa.  So we may have to reverse the left-to-right order of all the vertices in the drawing of $G_2[V(C)\cup A]$ to to make this consistent. (This corresponds to the note two paragraphs above about being able to choose whether $x_0\prec y_0$ or $y_0\prec x_0$ before recursing.)

So that's it. This method finds the planar drawing of $G_2$ required as input for the Bekos algorithm.

# Generalizing

Why do I think this has a hope of generalizing?  Well, the cycle $C$ is a separator of $G_2$ that has width 2 with respect to the layering $L_0,\ldots,L_h$.  (Note that we don't require this separator to be balanced, but we could.)  Almost by definition, bounded layered treewidth graphs always have such a separator, so we can assume we are give a separator $C'$ of small layered width.  $C'\cap L_0$ has constant size, so we can take $C$ to be $C'$ plus all vertices matched with $C'$ plus the set of all paths from $x\in C\cap L_0$ to the root of $T$.

No matter what order we pick for the vertices in $G_2[C]$ we can't create a large pencil, since $G_2[C]$ only has $O(1)$ edges in $L_0$.  So let's try an arbitrary drawing of $G_2[C]$ in which no pair of tree edges cross.  At this point we need to argue that the components of $G_2-C$ can somehow be organized into a way that fits neatly into this picture.  I'm not sure yet what this means or how to do it.  Maybe (as Vida has been telling me for several days now) we should consider the case where $G_2$ has bounded genus.  At least there we understand what the separator $C'$ looks like (see Section 3 of [Dujmovic, Morin, and Wood][dmw]).


[dmw]:https://arxiv.org/pdf/1306.1595.pdf
[ganley-heath]:https://www.sciencedirect.com/science/article/pii/S0166218X00001785
[bekos-ea]:https://arxiv.org/abs/1811.00816
