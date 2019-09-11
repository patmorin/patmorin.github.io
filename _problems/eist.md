---
layout: problem
title:  "Edge-independent Spanning Trees"
date:   2017-07-14
permalink: eist.html
categories: openproblem
---
Two spanning-trees $T_1$ and $T_2$ of a graph $G$ both rooted at a node $u\in V(G)$ are *edge independent* if, for every $v\in V(G)\setminus\\{u\\}$, the path in $T_1$ from $u$ to $v$ is disjoint from the path in $T_2$ from $u$ to $v$.

<div class="problem">
   Prove the following: For every $k$-edge connected graph $G$ and every $u\in V(G)$, $G$ has $k$ pairwise edge independent spanning trees rooted at $u$.
</div>

This problem is a conjecture that appears in Itai and Rodeh (A. Itai and M. Rodeh, The multi-tree approach to reliability in distributed networks, Inform.
Comput., vol. 79, pp. 43–59, 1988.) and in Zehavi and Itai (A. Zehavi and A. Itai, Three tree-paths, J. Graph Theory, vol. 13, no. 2, pp. 175–188, 1989.)  It has been proven for several classes of graphs including planar graphs, product graphs, chordal rings, augmented cubes, and many more. It is also known to be true for $k\le 4$.
