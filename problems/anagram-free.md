---
layout: problem
title:  "Anagram-Free Colouring"
date:   2017-07-14
permalink: anagram-free.html
categories: openproblem
---
An even-length sequence $a=st$ is an *anagram* if $s=t$. A sequence is *anagram-free* if it does not contain any anagram as a contiguous subsequence.  A colouring of a graph $G$ is *anagram-free* if the colour sequence encountered on any simple path in $G$ is anagram-free.
Equivalently, a colouring is anagram-free if there is no path in $G$ whose colour sequence is an anagram.  The minimum number of colours in an anagram-free colouring of $G$ is called the *anagram-free chromatic number* of $G$ and is denoted $\pi_\alpha(G)$.

A classic result on combinatorics of the strings is that the $n$-vertex path $P_n$ has $\pi_\alpha(P_n)\le 4$ with equality for $n\ge 7$.

<div class="problem">
  What is the anagram-free chromatic number of the $2\times n$ grid?
</div>

Using divide-and-conquer, we obtain an anagram-free colouring of the $2\times n$ using $\log_2(n+1)$ colours. More generally, any graph $G$ of treewidth $k$ has an $\pi_\alpha(G)\in O(k\log n)$.  For graphs $G$ coming from hereditary families with treewidth $O(n^\delta)$, $0<\delta<1$, $\pi_\alpha(G)\in O(n^{\delta})$.  So, for examples, $\pi_\alpha(G)\in O(\sqrt{n})$ for any $n$-vertex planar graph $G$.  It is worth noting that this divide-and-conquer approach gives a stronger property: The smallest colour on any path occurs exactly once.

[Kamčev, Łuczak, and Sudakov][kamčev-ea] show that the anagram-free chromatic number of $n$-vertex binary trees can be $\Omega(\sqrt{\log n})$. See [Wilson and Wood][wilson-wood] for more results on trees.

<div class="problem">
  What is largest anagram-free chromatic number of any $n$-vertex tree?
</div>

[Wilson and Wood][wilson-wood] show that the anagram-free chromatic number of $n$-vertex planar graphs can be $\Omega(\log n)$.

<div class="problem">
  What is largest anagram-free chromatic number of any $n$-vertex planar graph?
</div>

[Wilson and Wood][wilson-wood] also show that any tree $T$ of pathwidth $k$ has $\pi_\alpha(T)\in O(k)$, thus avoiding the $O(\log n)$ factor of the divide-and-conquer algorithm.  They do this by choosing a path $P$ in $T$ whose removal disconnects $T$ into components that each have pathwidth at most $k-1$ and colouring $P$ using an anagram-free 4-colouring.  

Open Problem 1 is the first step in understanding what happens with graphs of pathwidth $k$.

[kamčev-ea]: https://arxiv.org/abs/1606.09062
[wilson-wood]: https://arxiv.org/abs/1607.01117
