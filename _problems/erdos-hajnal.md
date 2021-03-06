---
layout: problem
title:  "Erdős-Hajnal for Graphs of Bounded VC-Dimension"
date:   2017-07-14
permalink: erdos-hajnal.html
categories: openproblem
---
[Fox, Pach, and Suk][fox-pach-suk] recently proved the following lower bound:

<div class="theorem">
  Every $n$-vertex graph with constant VC-dimension contains a clique or an independent set of size $e^{(\log n)^{1-o(1)}}$.
</div>

The original [Erdős-Hajnal Conjecture][e-h-conjecture] asserts that the bound should be $e^\alpha\log n$ for some $\alpha >0$.

<div class="problem">
  Give a tight bound for the preceding theorem.
</div>

In terms of upper bounds, the same authors proved:

<div class="theorem">
  For every $s\ge 3$, there exists $n$-vertex graphs of constant VC-dimension that contains no $K_s$ and no independent set of size $c n^{\frac{2}{s+1}}\log n$.
</div>

More likely, though, are that I could find applications of these results, since geometric intersection graphs tend to have bounded VC-dimension.  

Related to this is the notion of semi-algebraic hypergraphs (graphs whose vertices are points in $\R^d$ and in which a hyper edge $vw$ is present iff the coordinates of $v$ and $w$ satisfy some semi-algebraic condition.  Semi-algebraic graphs have bounded VC-dimension, but the actually satisfy stronger conditions:

<div class="theorem">
  There exists a constant $\delta >0$ such that every $n$-vertex semi-algebraic graph of bounded complexity contains a complete or an empty bipartite graph whose two parts each have size at least $\delta n$.
</div>

This seems useful. Maybe it has some applications to [Stein's Tripod-Packing Problem](tripod-packing.html)?

[fox-pach-suk]:https://arxiv.org/abs/1710.03745
[e-h-conjecture]:https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Hajnal_conjecture
