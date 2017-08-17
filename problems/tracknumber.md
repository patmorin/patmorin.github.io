---
layout: problem
title:  "Plane Graphs on a Constant Number of Tracks"
date:   2017-07-14
permalink: track-number.html
categories: openproblem, synthesis
---
$\newcommand{\Q}{\mathcal{Q}}\newcommand{\X}{\mathcal{X}}\newcommand{\D}{\mathcal{D}}$This is a summary of Jiun-Jie Wang's new paper: [Layouts for Plane Graphs on Constant Number of Tracks][wang].  These notes are mainly to help me understand the paper.

# The Big Picture

Wang defines a recursive embedding of a planar graph onto layers called a *composite-layerlike* embedding.  Such embeddings have three parameters $(\Q,\X,\D)$.  The trick is to show that, for planar graphs, one can find a composite-layerlike embedding in which $\Q,\X,\D\in O(1)$.

How is this related to track layouts?  In a (improper) track layout $\Q=1$ (there are no pairs of nested edges within a layer), $\X=0$, (there are no X-crossings), and $\D$ is the edge *gap* (what [Dujmovic, Morin, and Wood][dmw-sicomp] call *span*), i.e., the largest $\|i-j\|$ such that an edge joins a track-$i$ vertex to a track-$j$ vertex.

**Note:** The other properties of improper track layouts, namely that intra-track edges are between consecutive vertices seem to follow from the fact that the composite-layerlike embedding is plane.

Recall that track layouts with edge gap $\D$ can be wrapped onto $2\D+1$ tracks \[[1, Lemma 3.4][dmw-sicomp]\]. It turns out that the same is true for composite-layerlike embeddings.  A composite-layerlike embedding can be wrapped into $O(\D)$ tracks, without increasing $\Q$ or $\X$.

Now, this is still not a track layout because it doesn't have $\Q=1$ or $\X=0$.  Somehow, Wang ignores this, though somewhere in the paper, there is a discussion about removing edges to eliminate X-crossings and arguing that this doesn't increase track number by much.  

Here's my understanding of the steps in the proof:

* Input: Plane graph $G$
* Let $G^1$ be a 1-subdivision of $G$.
* Get a composite-layerlike embedding, $E$, of $G^1$ (Theorem 4 in Section 4)
* Convert $E$ into a $(\Q,\X,\D)$-well-placed layout $E'$ (Theorem 10, last page)
* Convert $E'$ into a $(\Q,\X,O(\D))$-well-placed layout $E''$ on a constant number of tracks/layers (Theorem 2 in Section 2)
* Convert $E''$ into a track-layout $T$ of $G^1$ (Theorem 6). The proof of Theorem 6 says that Theorem 10 gives a track layout with $O(1)$ tracks, therefore the track number of $G^1$ is $O(1)$. A result of [Dujmovic and Wood][dw-dmtcs] therefore implies that $G$ has track number $O(1)$.

The problem I have is with the proof of Theorem 6, since Theorem 10 guarantees only a $(\Q,\X,\D)$-well-placed layout for $\Q,\X,\D\in O(1)$.  For this to be a track layout, it would have to have $\Q=1$ and $\X=0$. This leap, which occurs in the proof of Theorem 6, is unjustified.


# Key Definitions

These are my interpretations of some key definitions:

* A *layer* is a horizontal line.  Layers proceed downward, with higher numbered layers below lower numbered layers.
* A *layerlike graph* is a plane graph where the vertices are assigned to layers $1,\ldots,k$, and there is an ordering of the vertices on each layer with the restriction that edges always join two vertices on the same layer or on consecutive layers.
* A *downpointing triangle* in a layerlike graph is a cycle with all but one vertex on layer $i$ and the remaining vertex on layer $i+1$.
* A *bowl* in a layerlike graph is a cycle with all vertices on the same layer.
* A *composite-layerlike graph* is a plane graph that has a *backbone* $K$ that is a layerlike graph.  Each bowl $\heartsuit$ of $K$ can contain a composite-layerlike graph whose first layer is $\heartsuit$.  Each downpointing triangle $\triangledown$ of $K$ can contain a composite-layerlike graph whose first layer is the top layer of $\triangledown$.
This object should really be called a composite-layerlike embedding of a plane graph.

A *ladderlike graph* is an assignment of vertices to layers along with an ordering on the vertices within each layer. (Note: The term ladderlike graph is deprecated, it disappeared in v2 of the arxiv paper.) It doesn't have to be compatible with a plane embedding and edges may cross multiple layers.  There are two important structures in a ladderlike graph:

* A *nest* is a set of edges all of whose endpoints are on the same layer, and which are nested.
* An *X-cross* is a set of edges where each edge contains a vertex on layer-$i$ and a vertex on layer-$j$ and the ordered so that every pair of edges crosses.

A ladderlike graph has three parameters:

* $\mathcal{Q}$ is the size of the largest nest.
* $\mathcal{X}$ is the size of the largest X-cross
* $\mathcal{D}$ is the largest value $\|i-j\|$ such that there is an edge from that joins a layer-$i$ vertex and a layer-$j$ vertex.  This is called the *gap* of the edge.

We call such a graph (actually, embedding of a graph) *$(\Q,\X,\D)$-well-placed*.

# Theorem 2 (Should be called Lemma 1)

This theorem says that, if $G$ is $(\Q,\X,\D)$-well-placed, then $G$ can also be drawn as a $(\Q,\X,O(\D))$-well-placed graph with only $O(\D)$ layers.

The proof of this (Which I haven't checked carefully, but isn't hard) is to wrap the graph onto $2\D$ layers.  The fact that the edge span is $\D$ ensures that this wrapping doesn't create any larger nests or X-crosses. This is basically the original wrapping argument from \[[1][dmw-sicomp]\].

# Section 3

This section discusses how to take a composite-layerlike (embedding of a planar) graph and turn it into a $(\Q,\X,\D)$-well-placed embedding with $\Q,\X,\D\in O(1)$.  Part of this Section includes Conjecture 1, which is later proved in Section 7.

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
