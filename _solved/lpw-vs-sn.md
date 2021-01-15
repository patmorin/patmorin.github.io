---
layout: solved
title:  "Layered Pathwidth versus Stack Number"
date:   2018-07-24
permalink: lpw-vs-pn.html
categories: openproblem
tags: graphs layering
---

This is joint work with Vida Dujmović and Céline Yelle.  It's an easier verion of [this other problem](page-number-versus-layered-treewidth.html).

<div class="problem">
Prove that there exists some function $f:\N\to\N$ such that any graph with layered pathwidth at most $k$ has stack number at most $f(k)$.
</div>

# A Solution

$\DeclareMathOperator{\pn}{pn}\DeclareMathOperator{\lpw}{lpw}$
Let $G$ be a graph. A *layering* $L=\langle L_i: i\in\N\rangle$ of $G$ is a sequence of subsets that partition $V(G)$ with the property that, for every edge $vw\in E(G)$, if $u\in L_i$, then $w\in L_{i-1}\cup L_i\cup L_{i+1}$.  For a layering $L$ and a vertex $v\in V$, we use $L[v]$ to denote the unique index $i$ such that $v\in L_i$.

A *path decomposition* $B=\langle B_i: i\in\N\rangle$ of $G$ is a sequence of subsets of $V(G)$ called *bags* with the property that, (i) for every edge $vw\in E(G)$ there exists at least one bag $B_i$ containing both $v$ and $w$ and (ii) for every vertex $v\in V(G)$, the set $B[v]=\lbrace i:v\in B_i\rbrace$ is contiguous, i.e., it contains all integers in $\lbrace \min B[v],\ldots,\max B[v]\rbrace $.

$\DeclareMathOperator{\w}{w}$A *layered path decomposition* $(L,B)$ of $G$ is a layering $L$ of $G$ and a path decomposition $B$ of $G$.  The *width* of a layered path decomposition $(L,B)$ is $\w(L,B)=\max\lbrace|B_i\cap L_j|:i,j\in \N\rbrace$.
The *layered pathwidth* $\lpw(G)$ of $G$ is equal to the minimum width of any layered path decomposition of $G$.

A path decomposition $B$ of $G$ is *left-normal* if, for every distinct pair $v,w\in V$, $\min B[v] \neq \min B[w]$.  It is straightforward to verify that, for every layered path decomposition $(L,B)$ of $G$ there exists a layered path decomposition $(L,B')$ of $G$ in which $\w(L,B)=\w(L,B')$ and $B'$ is left-normal.  For a left-normal path decomposition of $G$ and two vertices $v,w\in V(G)$, we use the notation $v\prec_B w$ if $\min B[v]<\min B[w]$.
Note that, since $B$ is left-normal, $\prec_B$ is a total order.

For any edge $vw$ with $v\prec_B w$ we call $v$ the *left endpoint* of the edge and $w$ the *right endpoint*.  We use the convention of writing any edge with endpoints $v$ and $w$ as $vw$ where $v$ is the left endpoint and $w$ is the right endpoint.  

A $p$-page layout $(\prec,\varphi)$ of a graph $G$ consists of a total order $\prec$ on $V(G)$ and an assignment $\varphi:E(G)\to P$, where $P$ is a set of *pages* of cardinality $p$ with the property that, for any two edges $vw,xy\in E(G)$ with $v\prec x\prec w\prec y$, $\varphi(vw)\neq\varphi(xy)$.
The *page number* $\pn(G)$ of $G$ is the smallest value $p$ for which $G$ has a $p$-page layout.


<div class="theorem">
For any graph $G$, $\pn(G)\le 4\lpw(G)$.
</div>

<div class="proof" markdown="1">
  Consider a left-normalized layered path decomposition $(L,B)$ of $G$ of width at most $k$.  To construct a page layout of $G$ we first construct a total ordering $\prec$ on the vertices of $G$.  This ordering is constructed as follows:
  * If $v\in L_i$ and $w\in L_j$ with $i < j$, then $v\prec w$.
  * If $v,w\in L_i$ with $v \prec_B w$ then
     * $v\prec w$ if $i$ is even; or
     * $w\prec v$ if $i$ is odd.

  To define the colouring $\varphi$, we begin with a (greedy) vertex $k$-colouring $\varphi:V\to \lbrace 1,\ldots,k\rbrace$ so that, for any $i,j\in\N$, no two vertices in $B_i\cap L_j$ are assigned the same colour. This is easily done since the path decomposition $\langle B_i\cap L_j : i\in N\rangle$ has bags of size at most $k$.  

  We say that the edge $vw$ has *positive slope* if $L[v]=L[w]+1$ and has *negative slope* if $L[v]=L[w-1]$.  We colour the edge $vw$ with the colour $\varphi(vw)=(a,b,c)$ where $a=L[v]\bmod 2$, $b$ is a bit indicating whether $v$ has positive or negative slope, and $c$ is the colour $\varphi(v)$ of the left endpoint $v$.  This clearly uses only $2\times2\times k=4k$ colours so all that remains is to show that $(\prec,\varphi)$ is indeed a $4k$-page layout.  

  Consider two edges $vw$ and $xy$ (whose left-endpoints are $v$ and $x$, respectively) and suppose without loss of generality that $v\prec x\prec w\prec y$.  We must show that $\varphi(vw)\neq\varphi(xy)$.  There are several cases to consider. In each case, $i$ is an integer and we assume, without loss of generality that $i$ is even.

  1. $L[v]=L[x]=L[y]=i$. In this case $v\prec_B x\prec_B y$.  If $L[w]\neq i$, then either $w\prec x$ or $y\prec w$, which is not possible.  On the other hand, if $L[w]=i$, then $v \prec_B x\prec_B y\prec_B w$ so $v,x\in B_{\min B[y]}$, so $\varphi(v)\ne\varphi(x)$ and $\varphi(vw)$ and $\varphi(xy)$ differ in their third component.

  2. $L[v]=L[x]=i$, $L[w]=L[y]=i\pm 1$.  Without loss of generality, we can assume that $L[w]=L[y]=i+1$.  In this case the assumption that $v\prec x\prec w\prec y$ implies that $v \prec_B x \prec_B y\prec_B w$, and again $\varphi(vw)$ and $\varphi(xy)$ differ in their third component.

  3. $L[v] = L[y] = i$ and $L[x]=L[w]=i\pm 1$.  In this case, $vw$ has negative slope and $xy$ has positive slope or vice-versa, so $\varphi(vw)$ and $\varphi(xy)$ differ in their second component.  (Also, $L[v]\not\equiv L[x]\pmod 2$.)

  4. $L[v] = L[x]= i$, $L[w]=i-b$, $L[w]=i+b$ for some $b\in\lbrace 0,1\rbrace$.  In this case, again $vw$ and $xy$ have positive and negative slopes, so $\varphi(vw)$ and $\varphi(xy)$ differ in their second component.

  5. $L[v] = i-b$, $L[x]= i+b$, $L[w]=L[y]=i$ for some $b\in\lbrace 0,1\rbrace$.  In this case, again $vw$ and $xy$ have positive and negative slopes, so $\varphi(vw)$ and $\varphi(xy)$ differ in their second component.

  6. $L[v]=i-1$, $L[w]=L[x]=i$, $L[y]=i+1$.  In this case $L[v]\not\equiv L[x]\pmod 2$ so $\varphi(vw)$ and $\varphi(xy)$ differ in their first component.

Note that $v\prec x\prec w\prec y$ implies that $\lbrace L[v],L[w]\rbrace \cap \lbrace L[x],L[y]\rbrace \neq \emptyset$.  Therefore, the preceding is an exhaustive case analysis.
</div>
