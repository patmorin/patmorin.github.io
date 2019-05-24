---
layout: talk
title:  "Layered Partitions of $k$-Planar Graphs"
date:   2019-05-24
permalink: k-planar-talk.html
categories: talk
---

- The original planar result:
  - The PS-tree $K$
    - A triangulation $G$
    - An extra node $r$ and the BFS tree from $r$.
    - Inductive construction
    - Each node $x\in V(K)$ has a cycle $F_x$ and tripod $Y_x$
    - The $F_x$ is made up of vertices from at most 3 tripods in ancestors of $x$.
  - The tripod partition $P$ and graph $H=G/P$
  - The tree decomposition of $H$
  - The layering $L$ and the layered width
  - Statement in terms layered partitions: Every triangulation $G$ has a layered partition $(L,P)$ of layered-width 3 where $H=G/P$ has treewidth 3.

- Applications:
  - Queue-number, track-number non-repetitive chromatic number, $p$-centered chromatic number, layered treewidth, 3D-drawing volume

- The new $k$-planar result
  - Definition of $k$-planar graph (emphasize non-straight edges)
  - Theorem Statement: Every $k$-planar graph $G$ has a layered partition $(L,P)$ of layered width $O(k^2)$ where $H=G/P$ has treewidth $O(k^3)$.
  - Proof Sketch
    - Add dummy vertices and triangulate, to get a graph $G^+$.
    - Add surrounding $K_4$ and triangulate to get $G^{++}$.
    - Use PS-tree $K$ for $G^{++}$, $T$, and $r$.
    - The partition $P$ of $V(G)$:
      - Elements of $P$ are indexed by nodes of $K$, i.e., $P=\lbrace S_x: x\in V(K)\rbrace$
      - Each $v\in S_x$ iff $x$ is the lowest node that contains all edges incident to $v$ in its interior.
      - $P=\lbrace S_x: x\in V(K)\rbrace$ is clearly a partition
        - Analyze width of $P$.
          - First with respect to layering of $G^{++}$: $3\times 4\times (2k+3)$
          - Squish $(k+1)$ consecutive layers to get a layering of $G$: increases layered width by factor of $K+1$
          - Therefore $P$ has layered width $O(k^2)$
        - Analyze treewidth of $H=G/P$.
          - $V(H) = V(K)$
          - $xy\in E(H)$ iff $y$ is an ancestor of $x$ (or vice-versa)
          - Tree decomposition:
             - Underlying tree is $K$, so decomposition is $(B_x:x\in V(K))$
             - $K[y]$ is rooted at $y$
             - $K[y]$ contains the $xy$ path for every $xy\in E(H)$.
          - $B_x=\lbrace y : xy\in E(H)\rbrace$
          - Focus on root-to-$x$ path $x_0,\ldots,x_d$ in $K$ .
          - If $xx_\delta\in E(H)$, then we have $vw\in E(G)$ with $v\in S_x=S_{x_d}$ and $w\in S_{x_\delta}$
          - But both $v$ and $w$ are "contained" in the node $x$ of $K$
          - But $w\in S_{x_\delta}$ so there is an edge $ww'\in E(G)$ that is:
             - contained in the node $x_\delta$, i.e., $ww'$ is inside $F_{x_\delta}$
             - touches $x_\delta$'s tripod
          - Walking along $ww'$ gives a walk in $G^+$ that we call a $\delta$-walk.
          - $\|B_x\|\le \|\lbrace \delta\in\lbrace 0,\ldots,d-1\rbrace: \mbox{$\exists$ a $\delta$-walk}\rbrace\|$
          - Bound of $O(k^3)$ comes from (roughly):
            - x has $\le 3$ ancestors $x_a$, $x_b$, $x_c$ with $a>b>c$ and $x_a=d-1$.
           - walk can leave immediately to highest ancestor of $x_c$, but then has used up one crossing.
           - walk can leave immediately to $x_b$ but then has used one crossing and is restricted to staying inside $x_c$.
           - walk can leave immediately to $x_a$ but then is restricted to staying inside $x_b$. (this implies walk can only go to $x_{d-1},x_{d-2},\ldots,x_{d-k})$
           - Illustrate with a picture
