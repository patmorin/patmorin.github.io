---
layout: problem
title:  "Plane Graphs on a Constant Number of Tracks"
date:   2017-07-14
permalink: track-number.html
categories: openproblem, synthesis
---
$\newcommand{\Q}{\mathcal{Q}}\newcommand{\X}{\mathcal{X}}\newcommand{\D}{\mathcal{D}}$This is a summary of Jiun-Jie Wang's new paper: [Layouts for Plane Graphs on Constant Number of Tracks][wang].  These notes are mainly to help me understand the paper.

# The Big Picture

$\DeclareMathOperator{\tn}{tn}$A *track assignment* of a graph $G$ is a proper $t$-colouring $c:V(G)\to\\{1,\ldots,t\\}$ of $G$'s vertices, along with a total ordering $<_i$ of the vertices in each colour class $i\in\\{1,\ldots,t\\}$.  An *X-crossing* in a track assignment is a pair of edges $vw$ and $xy$ with $c(v)=c(x)=i$, $c(w)=c(y)=j$, $v<_i x$, and $w<_j y$.  The *span* of a track assignment $c$ is the maximum value $\|c(u)-c(w)\|$ where $uw$ is an edge of $G$.

A $(k,t)$-track layout of $G$ is a $t$-track assignment along with a $k$-colouring $s:E(G)\to\\{1,\ldots,k\\}$ of $G$'s edges in which the edges of each X-crossing are assigned two different colours.  A $(1,t)$-track layout is called a $t$-track layout.  The minimum $t$ for which $G$ has a $t$-track layout is called the *track number* of $G$, and is denoted by $\tn(G)$

It follows from gluing together results by [Dujmovic and Wood][dw-dmtcs] and [Dujmovic, Por, and Wood][dpw-dmtcs] that if $G$ has a track assignment $c$ for which

1. the queue number of the subgraph induced by each colour class of $c$ is at most $\Q$;
2. the largest set of pairwise X-crossing edges is at most $\X$; and
3. the span of $c$ is at most $\D$,

then $\tn(G) \le f(\Q,\X,\D)$ for some function $f:\N^3\to \N$.  

Therefore, it suffices to find a track assignment for which $\Q,\X,\D\in O(1)$.  From now on, we'll call this a $(\Q,\X,\D)$-layout. (Wang calls it a $(\Q,\X,\D)$-well-placed layout in a ladder $\mathcal{H}$.)

* Input: Plane graph $G$
* Let $G^1$ be a 1-subdivision of $G$.
* Get a composite-layerlike embedding, $E$, of $G^1$ (Theorem 4 in Section 4)
* Convert $E$ into a $(\Q,\X,\D)$-layout $c$ of $G^1$ (Theorem 10, last page)
* By the results discussed above, $\tn(G^1) \in O(1)$ and, therefore, by a result of Dujmovic and Wood \[[1, Lemma 7][dw-dmtcs]\] $\tn(G)\in O(1)$.

# Key Definitions

These are my interpretations of some key definitions:

* A *layer* is a horizontal line.  Layers proceed downward, with higher numbered layers below lower numbered layers.
* A *layerlike graph* is a plane graph where the vertices are assigned to layers $1,\ldots,k$, and there is an ordering of the vertices on each layer with the restriction that edges always join two vertices on the same layer or on consecutive layers.

> A layerlike graph Π is a graph whose vertices are partitioned and placed on contiguous layers such that no edge is placed between any two non-contiguous layers and no edges are crossing.

* A *downpointing triangle* in a layerlike graph is a cycle with all but one vertex on layer $i$ and the remaining vertex on layer $i+1$.

> Given a layerlike graph Π, a down-pointing triangle ▽ is a a cycle (l, · · · , r, m) that vertices on the cycle (l, · · · , r, m) are on the two contiguous layers where the path from l to r are on the upper layer and the vertex m is on the lower layer

* A *bowl* in a layerlike graph is a cycle with all vertices on the same layer.

> A bowl ♥ is a cycle (l, · · · , r) that the cycle are on the same layer where each vertex of the cycle is on the same layer.

* A *composite-layerlike graph* is a plane graph that has a *backbone* $K$ that is a layerlike graph.  Each bowl $\heartsuit$ of $K$ can contain a composite-layerlike graph whose first layer is $\heartsuit$.  Each downpointing triangle $\triangledown$ of $K$ can contain a composite-layerlike graph whose first layer is the top layer of $\triangledown$.

> A composite-layerlike graph G can be recursively defined as follows: G consists of a layerlike graph Π such that each bowl ♥ of G has a smaller composite-layerlike graph G1 where G1’s first layer is the bowl ♥, and each down-pointing triangle ▽ has a composite-layerlike graph G2 where the first layer of G2 is the upper layer of ▽.

This object should really be called a composite-layerlike embedding of a plane graph.

# Theorem 2

This theorem says that, if $G$ is a $(\Q,\X,\D)$-layout, then $G$ can also be drawn as a $(\Q,\X,O(\D))$-well-placed graph with only $O(\D)$ layers.

The proof of this is to wrap the graph onto $O(\D)$ layers.  The fact that the edge span is $\D$ ensures that this wrapping doesn't increase $\Q$ or $\X$. This is basically the original wrapping argument from \[[1][dmw-sicomp]\]. But actually, I don't think this is needed since it we can use one of the results in one the \{Dujmovic, Por, Morin, Wood\} papers.

# Section 3

This section discusses how to take a composite-layerlike (embedding of a planar) graph $G$ and turn it into a $(\Q,\X,\D)$-layout with $\Q,\X,\D\in O(1)$.  Part of this Section includes Conjecture 1, which is later proved in Section 7.

# Section 4

This section shows how to find a composite-layerlike embedding of a plane graph.  More specificially, it shows (in Theorem 4) that a 1-subdivision of any planar graph $G$ has a composite-layerlike embedding.

I found this proof (which is supposedly the easy part of the paper) almost impossible to follow.  I think we can do this more easily.

A *near-triangulation* is a connected embedded planar graph in which every internal face is bounded by three edges and the outer face is bounded by a simple cycle.

**Lemma:** Let $G$ be a near-triangulation with outer face $C$ whose vertices, in clockwise order are $m,u_1,\ldots,u_k$.  Then $G$ has a composite-layerlike embedding $E$ and the first layer of $E$'s backbone is $m,u_1,\ldots,u_k$.

The proof is by induction on the number of vertices of $G$.  Place $m,u_1,\ldots,u_k$ on the first layer in that order.  If the outer face $C$ contains a chord joining $m$ to $u_i$, $i\not\in\{1,k\}$ then apply induction on the near triangulation $G_1$ in the interior of the cycle $m,u_1,\ldots,u_i$ and on the near-triangulation $G_2$ contained in the interior of the cycle $m,u_i,\ldots,u_k$.

Therefore, assume $C$ is chord-free. Then consider the graph $G'$ obtained by removing $C$ from $G$.  This graph is connected but not necessarily a near-triangulation; it's outer face may have cut vertices.




Consider the triangulations



Let $r>1$ be the smallest index such that $u_r$ is adjacent to $m$.




I think we can do this more easily.  Let



Here's what I think is happening. Let $G$ be a plane near-triangulation whose outer face vertices, in counterclockwise order are $m,u_1,\ldots,u_k$, where $m$ is some prescribed vertex.
The vertices $m,u_1,\ldots,u_k$ will be in the first layer of the backbone layed out in the order $m,u_1,\ldots,u_k$.

If we remove $m,u_1,\ldots,u_k$ from $G$, then we are left with a possibly-disconnected graph. Some of the components of this graph contain vertices incident to $m$.  Let these components be labelled $C_1,\ldots,C_p$ in the counterclockwise order they appear around $m$, and let $O_i$ be the outer face of C_i$.  The vertices of $O_1,\ldots,O_i$ are also in the backbone, layed out in the second layer, in this order, with the vertices of each $O_i$ ordered so that all vertices incident to $m$ appear before all the vertices not incident to $m$.


 say $C_1,\ldots,C_p$ contain one or more vertices incident to $m$.  Let $O_i$




# Section 5

This is where they prove Theorem 6, which is that every plane graph has $O(1)$ track number.  This is where I have a problem.

# Section 6
In this section, they prove how to get a $(\Q,\X,\D)$-well-placed layout for something called a *raising fan*.  This is later used in Section 7, I think.

# Section 7

In this section, they show how to find a skeleton in a region so that the skeleton has a $(\Q,\X,\D)$-well-placed layout.

[wang]: https://arxiv.org/abs/1708.02114
[dmw-sicomp]: http://cglab.ca/~morin/publications/gd/treewidth-sicomp.pdf
[dw-dmtcs]: https://www.emis.de/journals/DMTCS/pdfpapers/dm070111.pdf
[dpw-dmtcs]: https://arxiv.org/abs/cs/0407033
