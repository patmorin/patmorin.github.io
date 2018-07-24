---
layout: problem
title:  "Layered Patwidth versus Stack Number"
date:   2018-07-24
permalink: lpw-vs-pn.html
categories: openproblem
---

This is joint work with Vida Dujmović and Céline Yelle.

<div class="problem">
Prove that there exists some function $f:\N\to\N$ such that any graph with layered pathwidth at most $k$ has stack number at most $f(k)$.
</div>

# Preliminary Steps

$\DeclareMathOperator{\w}{w}$Let $V$ be a set whose elements we call *vertices*. A *path decomposition* $B$ of $V$ is a sequence $\langle B_i:\in\N\rangle$ of subsets of $V$ called *bags* with the property that, for any $v\in V$, the indices $B[v]:=\lbrace i\in \N:v\in B_i\rbrace$ form a contiguous subsequence of $\N$.  A *layering* of $V$ is a partition $L$ of $V$ into sets $\langle L_i:i\in\N\rangle$ called *layers*. For a layering $L$ and a vertex $v\in V$, we use $L[v]$ to denote the unique index $i$ such that $v\in L_i$.  

A *layered path decomposition* $(L,B)$ of $V$ is a layering $L$ of $V$ and a path decomposition $B$ of $V$.  Any path decomposition $(L,B)$ of $V$ and has an associated graph $G(L,B)$ where
$V(G)=V$ and $vw\in E(G)$ if and only if $|L(v)-L(w)|\le 1$ and there exists at least one $i\in N$ such that $u,w\in B_i$.  The *width* of a layered decomposition
$(L,B)$ is $\w(L,B)=\max\lbrace|B_i\cap L_j|:i,j\in \N\rbrace$.

For a graph $G=(V,E)$, the *layered pathwidth* of $G$ is equal to the minimum width of any layered path decomposition $(L,B)$ of $V$ such that $G(L,B)$ contains $G$ as a subgraph. For each $k\in N$, let $\mathcal{F}_k$ denote the family of graphs of layered pathwidth at most $k$.

A path decomposition $B$ of $V$ is *left-normal* if, for every distinct pair $v,w\in V$, $\min B[v] \neq \min B[w]$.  It is straightforward to verify that, for every layered path decomposition $(L,B)$ there exists an layered path decomposition $(L,B')$ in which $G(L,B)=G(L,B')$, $\w(L,B)=\w(L,B')$ and $B'$ is left-normal.

For any left-normal layered path decomposition $(L,B)$ of $V$ and any two edges $vw$ and $xy$ of $G(L,B)$, we say that $vw$ and $xy$ *cross* if $L[v]=L[x]$, $L[w]=L[y]$, $\min B[x] < \min B[v]$ and $\min B[y] > \min B[w]$.  For a left-normal path decomposition $(L,B)$, define the *crossing graph* $H(L,B)$ to be the graph whose vertex set consists of edges in $G(L,B)$ and in which two vertices are adjacent if and only if they cross.

To solve our open problem, it would be enough to show that, if $(L,B)$ has width at most $k$, then the crossing graph is $H(L,B)$ is $f(k)$-colourable.  This is equivalent to showing that the drawing in which each $v\in V$ is drawn at $(\min B[v],L[v])$ has *thickness* $f(k)$.

We can prove the following results about the crossing graph $H(L,B)$.

<div class="lemma"> If $(L,B)$ is a layered path decomposition of width at most $k$, then $H(L,B)$ contains no clique of size $f(k)$.
</div>

<div class="lemma"> If $(L,B)$ is a layered path decomposition of width at most $k$, then $H(L,B)$ contains no biclique of size $f(k)$.
</div>
