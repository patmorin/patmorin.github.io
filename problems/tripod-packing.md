---
layout: problem
title:  "Tripod Packing"
date:   2017-07-13 09:32:53 -0400
permalink: tripod-packing.html
categories: openproblem hard
---
What is the maximum number of tripods that can be packed
in a $n\times n\times n$ cube?  The current best upper
bound is $n^2/e^{\Omega(\log^\star n)}$.  The current best
lower-bound is $\Omega(n^{1.546})$.  See Section 4.3 of
[this paper][turan-type].


[turan-type]: https://arxiv.org/abs/1706.10193

# An Approach Using $\epsilon$-Nets

For any $a,b,c\in\N$, a $a \times b\times c$ a *tripod packing* $T$ is a subset of $[a]\times[b]\times[c]$ with the property that, for any pair $x,y\in T$, $x_i > y_i$ for at least two values of $i\in\lbrace 1,2,3\rbrace$ or $x_i < y_i$ for at least two values of $i\in\lbrace 1,2,3\rbrace$.

For an $n\times n\times n$ tripod packing $T$ and any $z\in[n]$, let $T_z=\lbrace (x,y):(z,y,z)\in T\rbrace$ and observe that $T_1,\ldots,T_n$ is a partition of $T$.
Let $C_z(T)=\bigcup_{(x,y)\in T_z} \lbrace x,y\rbrace$

We say that $N\subset\lbrace 1,\ldots,n\rbrace$ is an $\epsilon$-net for $T$ if, for every $z\in \lbrack n\rbrack$, such that $\|T_z\|\ge\epsilon n$, $C_z(T)\cap N\neq\emptyset$.

<div class="conjecture">
   There exists some $f:\N\to\N$ such that every $\epsilon>0$ and every $n\times n\times n$ tripod packing has an $\epsilon$-net $N$ of size at most $f(\lceil 1/\epsilon\rceil)$.
</div>

If this were true, then we could use it to prove an upper bound on the size of $n\times n\times n$ tripod packings, as follows.  Suppose $T$ is an $n\times n\times n$ tripod packing of size at least than $2\epsilon n^2$.  For every $z$ such that $\|T_z\| \le \epsilon n$, remove $T_z$ from $T$ to obtain a tripod packing $T'$ of size at least $\epsilon n^2$ in which $\|T'_z\| =0$ or $\|T'_z\|\ge \epsilon n$ for every $z\in[n]$.

Let $N$ be an $\epsilon$-net for $T'$ and consider the subgrid $N
