---
layout: problem
title:  "Layered Pathwidth and Non-Repetitive Chromatic Number"
date:   2017-07-14
permalink: lpw-vs-nrcn.html
categories: openproblem
---
$\DeclareMathOperator{\lpw}{lpw}\DeclareMathOperator{\ltw}{ltw}$

For a graph $G$, let $\lpw(G)$, $\ltw(G)$, and $\pi(G)$ denote the layered pathwidth, layered treewidth, and non-repetitive chromatic number of $G$, respectively.

<div class="problem">
  Does there exist some $f:\N\to\N$ such that, for all graphs $G$, $\pi(G)\le f(\lpw(G))$?
</div>

[Dujmovic et al][dujmovic-ea] show that $\pi(G) \le \ltw(G)\cdot\log n$ for all $n$-vertex graphs $G$.

# Some Ideas

Here is a wild idea.  Let $k=\lpw(G)$  Consider the layered path decomposition of $G$ and use it to assign a total order $\prec$ on the vertices of $G$ that is consistent with the partial order given by the path decomposition.  Assume, further, that $G$ is edge-maximal, so that if two vertices $v$ and $w$ appear in a common bag and their layers differ by at most 1, then $vw$ is an edge of $G$.

In this way, the edges incident to a particular vertex $v$ are ordered. Let $E'$ be the set of edges in $G$ obtained by collecting, for each vertex $v$, the first and last $10k$ edges incident to $v$.  Now, note that $G'=(V,E')$ has maximum degree $20k$ and can therefore be nonrepetitively coloured using $O(k^2)$ colours.

Consider now the graph $\bar{G}'=(V,E(G)\setminus E')$.  I claim that $\bar{G}'$ has treewidth $f(k)$ and therefore, by a result of [K&uuml;ndgen and Pelsmajer][kundgen-pelsmajer] it has a non-repetitive $4^{f(k)}$-colouring.

The hope is that, maybe the product of these two colourings gives a non-repetitive colouring of $G$.


[dujmovic-ea]:http://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i1p51
[kundgen-pelsmajer]:https://www.sciencedirect.com/science/article/pii/S0012365X0700667X?via%3Dihub
