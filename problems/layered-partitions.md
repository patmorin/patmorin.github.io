---
layout: problem
title:  "Open Problems on Layered Partitions"
date:   2017-07-14
permalink: layered-partitions.html
categories: openproblem
---

# The Structure of $k$-Planar graphs

Vida, David, and I showed that $k$-planar graphs have layered $H$-partition of layered width $O(k^2)$ where $H$ has treewidth $O(k^3)$.  It would be nice to reduced the treewidth of $H$.

<div class="conjecture">
  Every $k$-planar graph has a layered $H$-partition of layered width $f(k)$ where $H$ has treewidth at most $C$.
</div>


# The Structure of $k$-Shortcut graphs

The following Conjecture is due to David Wood and would generalize our work on $k$-planar graphs.

<div class="conjecture">
  Let $G$ a graph with a layered $H$-partition of layered width $1$ in which $H$ has treewidth $c$ and let $G'\supseteq G$ be the supergraph of $G$ in which $vw\in E(G')$ if and only if $G$ contains a path of length at most $k$ whose internal vertices have degree at most $d$.  Then $G'$ has a layered $H'$-partition in which $H'$-partition of layered width $1$ in which $H'$ has treewidth at most $f(c,k,d)$.
</div>

# The Structure of $k$-nearest neighbour graphs in $\R^d$
Here's one from David Wood:

<div class="conjecture">
   Let $G$ be the $k$-nearest-neighbour graph of an $n$-point set in $\R^d$.  Then $G$ is a subgraph of $H\boxtimes P\boxtimes P\boxtimes\cdots\boxtimes P$ where $H=H(G)$ is a graph of treewidth at most $f(d,k)$, $P$ is a path, and the number of occurrences of $P$ in the product is $d-1$.
</div>

The conjecture is true for $d=1$ (easy) and $d=2$ (in our paper on the structure of $k$-planar graphs).  Here's another version I thought of that has more of a "universal graphs" flavour:

<div class="conjecture">
   Let $G$ be the $k$-nearest-neighbour graph of an $n$-point set in $\R^d$.  Then $G$ is a subgraph of $K\boxtimes P\boxtimes P\boxtimes\cdots\boxtimes P$ where $K$ is a clique of size at most $f(d,k)$, $P$ is a path, and the number of occurrences of $P$ in the product is $d$.
</div>
