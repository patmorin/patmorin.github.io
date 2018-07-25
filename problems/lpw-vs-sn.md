---
layout: problem
title:  "Layered Patwidth versus Stack Number"
date:   2018-07-24
permalink: lpw-vs-pn.html
categories: openproblem
---

This is joint work with Vida Dujmović and Céline Yelle.  It's an easier verion of [this other problem](page-number-versus-layered-treewidth.html).

<div class="problem">
Prove that there exists some function $f:\N\to\N$ such that any graph with layered pathwidth at most $k$ has stack number at most $f(k)$.
</div>

# A Solution

$\DeclareMathOperator{\pn}{pn}\DeclareMathOperator{\lpw}{lpw}$
Let $G$ be a graph. A *layering* $L=\langle L_i: i\in\N\rangle$ of $G$ is a sequence of subsets that partition $V(G)$ with the property that, for every edge $vw\in E(G)$, if $u\in L_i$, then $w\in L_{i-1}\cup L_i\cup L_{i+1}$.  For a layering $L$ and a vertex $v\in V$, we use $L[v]$ to denote the unique index $i$ such that $v\in L_i$.

A *path decomposition* $B=\langle B_i: i\in\N\rangle$ of $G$ is a sequence of subsets of $V(G)$ called *bags* with the property that, (i) for every edge $vw\in E(G)$ there exists at least one bag $B_i$ containing both $v$ and $w$ and (ii) for every vertex $v\in V(G)$, the set $B[v]=\lbrace i:v\in B_i\rbrace$ is contiguous.

$\DeclareMathOperator{\w}{w}$A *layered path decomposition* $(L,B)$ of $G$ is a layering $L$ of $G$ and a path decomposition $B$ of $G$.  The *width* of a layered path decomposition $(L,B)$ is $\w(L,B)=\max\lbrace|B_i\cap L_j|:i,j\in \N\rbrace$.
The *layered pathwidth* $\lpw(G)$ of $G$ is equal to the minimum width of any layered path decomposition of $G$.

A path decomposition $B$ of $G$ is *left-normal* if, for every distinct pair $v,w\in V$, $\min B[v] \neq \min B[w]$.  It is straightforward to verify that, for every layered path decomposition $(L,B)$ of $G$ there exists a layered path decomposition $(L,B')$ of $G$ in which $\w(L,B)=\w(L,B')$ and $B'$ is left-normal.  For a left-normal path decomposition of $G$ and two vertices $v,w\in V(G)$, we use the notation $v\prec_B w$ if $L[v]=L[w]$ and $\min B[v]<\min B[w]$.  Note that, for each layer $L_i$, $\prec_B$ is a total order over $L_i$ and therefore $\prec_B$ is a partial order over $V(G)$.

When we have a path decomposition $(L,B)$ of $G$ we say that an edge $vw$ is an *intra-layer edge* if $L[v]= L[w]$, otherwise $vw$  is an *inter-layer edge*. For any left-normal layered path decomposition $(L,B)$ of $G$ and any two (inter-layer) edges $vw, xy\in E(G)$, we say that $vw$ and $xy$ *cross* if $L[v]=L[x]\neq L[w]=L[y]$, $v\prec_B x$ and $y\prec_B w$.  

<div class="lemma">
  If a graph $G$ has a left-normalized layered path decomposition $(L,B)$ of width $k$, then inter-layer edges of $G$ can be coloured with $k^2$ colours so that any two edges that cross are assigned different colours.
</div>

<div class="proof" markdown="1">
   First we find a $k$-colouring $\varphi:V\to \lbrace 1,\ldots,k\rbrace$ so that, for any $i,j\in\N$, no two vertices in $B_i\cap L_j$ are assigned the same colour.  This is easily done since the path decomposition $\langle B_i\cap L_j : i\in N\rangle$ has bags of size at most $k$.  Any inter-layer edge $vw\in E(G)$ with $v\in L_j$ and $w\in L_{j+1}$ is then coloured with the pair $(\varphi(v),\varphi(w))$.

   This colouring obviously uses at most $k^2$ colours so all that remains is to show that this colouring avoids monochromatic crossings.  Consider two edges $vw$ and $xy$ with $L[v]=L[x]=j$ and $L[w]=L[y]=j+1$ that receive the same colour.  Since $\varphi(v)=\varphi(x)$, there is no  bag containing both $v$ and $x$.  Similarly, since $\varphi(w)=\varphi(y)$, there is no bag containing both $w$ and $y$. Therefore, if $\min B[v] < \min B[x]$, it must be the case $\min B[w] < \min B[y]$ since, otherwise there would be no bag containing both $v$ and $w$ or no bag containing both $x$ and $y$. Therefore, any two edges that receive the same colour do not cross.
</div>

A $p$-page layout $(\prec,\varphi)$ consists of a total order $\prec$ on $V(G)$ and an assignment $\varphi:E(G)\to P$, where $P$ is a set of *pages* of cardinality $p$.
The page number $\pn(G)$ of $G$ is the smallest value $p$ for which $G$ has a $p$-page layout.


<div class="theorem">
If $G$ is a graph with $\lpw(G)\le k$, then $\pn(G)\le 2k^2+k$.
</div>

<div class="proof" markdown="1">
  Consider a left-normalized layered path decomposition $(L,B)$ of $G$ of width at most $k$.  To construct a page layout of $G$ we first construct a total ordering $\prec$ on the vertices of $G$.  This ordering is constructed as follows:
  * If $v\in L_i$ and $w\in L_j$ with $i < j$, then $v\prec w$.
  * If $v,w\in L_i$ with $v \prec_B w$ then
     * $v\prec w$ if $i$ is even; or
     * $w\prec v$ if $i$ is odd.

  To assign edges to pages we begin with the colouring of inter-layer edges defined by the previous lemma.  In this colouring, each edge is assigned a pair in $\lbrace1,\ldots,k\rbrace^2$.  For each inter-layer edge $vw$ with $v\in L_j$ and $w\in L_{j+1}$ whose colour was $(a,b)$ we reassign it the colour $(j\bmod 2, a, b)$.

  It remains to colour the intra-layer edges. For each intra-layer edge $vw$ with $v\prec_B w$ we assign $vw$ the colour $\varphi(v)$.  

  This concludes the description of our edge colouring. The colours assigned to intra-layer edges are $\lbrace1,\ldots,k\rbrace$ and the colours assigned to inter-layer edges are $\lbrace 0,1\rbrace\times \lbrace 1,\ldots,k\rbrace^2$ for a total of $2k^2+k$ colours.  What remains is to show is that this is a valid assignment of edges to pages, i.e., that there does not exist any pair of edges $vw$ and $xy$ that are assigned the same colour and such that $v\prec x\prec w\prec y$.  There are several cases to consider:
  1. If $vw$ and $xy$ are intra-layer edges and $L[v]=L[w] < L[x]=L[y]$, then $v,w\prec x,y$, so $vw$ and $xy$ can be assigned to the same page.
  2. If $vw$ and $xy$ are intra-layer edges and $L[v]=L[w]=L[x]=L[y]$ then $v\prec x\prec w\prec y$ and the existence of the edge $vw$ requires that there is a bag $B_i$ containing both $v$ and $x$, so $\varphi(v)\neq \varphi(x)$ and therefore $vw$ is assigned a different colour than $xy$.
  3. If $vw$ is an intra-layer edge and $xy$ is an inter-layer edge then $vw$ is coloured with an integer and $xy$ is coloured with a triple of integers.
  4. If $vw$ and $xy$ are inter-layer edges with $L[v]=L[x]$ and $L[w]=L[y]$ and
  $v\prec x\prec w\prec y$ then $vw$ and $xy$ cross, so they receive different colours.
  5. If $vw$ and $xy$ are inter-layer edges with $L[v]+1=L[w]=L[x]=L[y]-1$ then the first element in $vw$'s color is $L[v]\bmod 2$ while the first element in $xy$'s colour is $L[x]\bmod 2= L[v]+1\bmod 2$.
  6. If $vw$ and $xy$ are inter-layer edges with $L[v]+1=L[w] < L[x] = L[y]-1$, then $v,w\prec xy$ so that $vw$ and $xy$ can be assigned to the same page.
