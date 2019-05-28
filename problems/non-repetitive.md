---
layout: problem
title:  "Non-Repetitive Colouring"
date:   2018-07-14
permalink: non-repetitive.html
categories: openproblem
---
**Defunct:** Some of this question is defunct, now, because of this theorem of [Dujmović et al](https://arxiv.org/abs/1904.05269):

<div class="theorem">
  If a graph $G$ has a layered $H$-partition with layered width $1$ where $\DeclareMathOperator{\tw}{tw}\tw(H)\le t$, then $\pi(G)\le 4^{t+1}$.
</div>

Every graph from an apex-minor-free family has such a layered $H$-partition (where $t$ depends on the apex-minor) and so do $k$-planar graphs (where $t$ depends on $k$.)  See [Dujmović et al.](https://arxiv.org/abs/1904.04791) and [Dujmović, Morin, and Wood](), respectively.



---
---

# The Original Question
A string $s=s_1,\ldots,s_{2k}$ is a *repetition* if $s_1,\ldots,s_k=s_{k+1},\ldots,s_{2k}$.  A colouring $\varphi:V(G)\to\\{1,\ldots,c\\}$ of a graph $G$ is *non-repetitive* if, for every path $v_1,\ldots,v_{2k}$ in $G$, the string $\varphi(v_1),\ldots,\varphi(2k)$ is not a repetition.  The non-repetitive chromatic number $\pi(G)$ of $G$ is the smallest number of colours in any non-repetitive colouring of $G$.

<div class="problem">
  What is the maximum non-repetitive chromatic number of any $n$-vertex planar graph?
</div>

The best upper bound of $O(\log n)$ is due to [Dujmović][dujmovic].  The only known lower bound is constant.

For maximum-degree $\Delta$ graphs, [Dujmović et al][dujmovic-etal] showed that $\pi(G)=(1+o(1))\Delta^2$ and the best known lower bound is $\Omega(\Delta^2/\log\Delta)$.  The proof of the upper-bound uses entropy compression and at the heart of it, it relies on the simple fact that the number of paths of length $2k$ that contain any vertex $v$ is at most $k\Delta^{2k}$.  In [our paper on random trees][random-trees] we showed that, in a $d$-degenerate graph, the average (over all $v\in V(G)$) number of paths of length $2k$ that contain $v$ is $O(k(d\Delta)^k)$.

<div class="problem">
  Prove that the non-repetitive chromatic number of any maximum degree $\Delta$ $d$-degenerate graphs is $O(d\Delta)$.
</div>

One way that I had hoped to achieve this was with the following lemma:

<div class="lemma">
  Every $d$-degenerate graph $G$ with maximum degree $\Delta$ has a vertex $v$ such that, for every $\ell\in\N$, the number of paths that start at $v$ and have length $\ell$ is at most $2^{\ell+1}(2d\Delta)^{\ell/2}$.
</div>

<div class="proof" markdown="1">
  The result in our paper on random trees states that the total number of paths of length $\ell$ in $G$ is at most $2n(2d\Delta)^{\ell/2}$.
  For each $\ell\in\N$, let $X(\ell)$ denote the number of vertices of $G$ that
  are the first vertex of more than $2^{\ell+1}(2d\Delta)^{\ell/2}$ paths.  Then we have
  \\[
       X(\ell)\cdot2^{\ell+1}(2d\Delta)^{\ell/2} \le n2(2d\Delta)^{\ell/2}
  \\]
  which implies
  \\[
       X(\ell) \le n/2^{\ell} \enspace .
  \\]
  But now,
  \\[  \sum_{\ell=1}^{n-1} X(\ell) \le \sum_{\ell=1}^{n-1} n/2^{\ell} < n  
  \\]
</div>

Unfortunately, the preceding lemma is not enough to prove the result we want. It allows us to order the vertices of $G$ in some order $v_1,\ldots,v_n$ so that, for every $\ell\in\N$, in $G[\\{v_1,\ldots,v_i\\}]$, the number of paths of length $2k$ that contain $v_i$ is at most $O(k(2d\Delta)^{k})$.  However, now when the random colouring fails at $v_i$ because of some path $P$, we must recolour all the vertices of $P$. However, for some vertex $v_j\in P$, $j<i$ we have no upper bound on the number of paths of length $2k$ that contain $v_j$ in $G[\\{v_1,\ldots,v_i\\}\setminus V(P)]$.




[dujmovic]:https://arxiv.org/abs/1302.0304
[dujmovic-etal]:https://arxiv.org/abs/1112.5524
[random-trees]:https://arxiv.org/abs/1707.00083
