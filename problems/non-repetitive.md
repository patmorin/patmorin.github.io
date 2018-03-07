---
layout: problem
title:  "Non-Repetitive Colouring"
date:   2018-07-14
permalink: non-repetitive.html
categories: openproblem
---
A string $s=s_1,\ldots,s_{2k}$ is a *repetition* if $s_1,\ldots,s_k=s_{k+1},\ldots,s_{2k}$.  A colouring $\varphi:V(G)\to\\{1,\ldots,c\\}$ of a graph $G$ is *non-repetitive* if, for every path $v_1,\ldots,v_{2k}$ in $G$, the string $\varphi(v_1),\ldots,\varphi(2k)$ is not a repetition.  The non-repetitive chromatic number $\pi(G)$ of $G$ is the smallest number of colours in any non-repetitive colouring of $G$.

<div class="problem">
  What is the maximum non-repetitive chromatic number of any $n$-vertex planar graph?
</div>

The best upper bound of $O(\log n)$ is due to [Dujmović][dujmovic].  The only known lower bound is constant.

For maximum-degree $\Delta$ graphs, [Dujmović et al][dujmovic-etal] showed that $\pi(G)=(1+o(1))\Delta^2$ and the best known lower bound is $\Omega(\Delta^2/\log\Delta)$.  The proof of the upper-bound uses entropy compression and at the heart of it, it relies on the simple fact that the number of paths of length $2k$ that contain any vertex $v$ is at most $k\Delta^{2k}$.  In [our paper on random trees][random-trees] we showed that, in a $d$-degenerate graph, the average (over all $v\in V(G)$) number of paths of length $2k$ that contain $v$ is $O(k(d\Delta)^k)$.

<div class="problem">
  Prove that the non-repetitive chromatic number of any maximum degree $\Delta$ $d$-degenerate graphs is $O(d\Delta)$.
</div>

One way to achieve this would be to prove that every $n$-vertex maximum-degree $\Delta$ $d$-degenerate graph $G$ has a vertex ordering $v_1,\ldots,v_n$ with the property that, for each $i\in\\{1,\ldots,n\\}$ and all $\ell$, the number of paths in $G[v_1,\ldots,v_i]$ of length $\ell$ that begin at $v_i$ is $O((d\Delta)^{\ell/2})$.  For a fixed value of $\ell$, this is easy to show. The tricky part is finding an ordering that works for all $\ell$ simultaneously.


[dujmovic]:https://arxiv.org/abs/1302.0304
[dujmovic-etal]:https://arxiv.org/abs/1112.5524
[random-trees]:https://arxiv.org/abs/1707.00083
