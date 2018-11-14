---
layout: problem
title:  "Queue Number versus Layered Treewidth"
date:   2017-07-14
permalink: qn-vs-ltw.html
categories: openproblem
---
$\DeclareMathOperator{\depth}{depth}$[Bekos et al][bekos-ea] have recently shown that planar graphs of bounded maximum degree have bounded queue number.  Can we generlize this result to bounded layered treewidth graphs of bounded degree?

Here's what we have and what we need  (I think).

Here's what we have:

A graph $G_2$ that consists of
1. a max-degree $\Delta$ tree $T$ whose leaves all have the same depth, $h$, plus
2. a perfect matching $M$ on the leaves of $T$.

Furthermore, $G_2$ has layered treewidth at most $k$ using the layering $L_i = \lbrace v\in V(T) : \depth_T(v)=h-i\rbrace$.

Here's what we need:

Total orders $(L_0,<_0),...,(L_h,<_h)$ [i.e., $<_i$ is a total order on $L_i$] such that:

1. $<_0$ defines an $O(1)$ page layout of $M$.
2. for each $i\in\lbrace 1,...,h-1\rbrace$, $T[L_i \cup L_{i+1}]$ has a two layer drawing with $L_j$ on the line $y=j$ ordered by $<_j$ and the edges of this drawing can be $O(1)$ coloured so that there are no monochromatic crossings.

The good news is that I know how to obtain the orders $<_0$ and $<_1$.  By the definition of layered treewidth, the restriction of this tree decomposition to $L_0\cup L_1$ has width at most $2k$.  The result of [Ganley and Heath][ganley-heath] then implies that $G_2[L_0\cup L_1]$ has a $(2k+1)$-page layout with ordering $<_{01}$. From this we can get the orderings:

1. $v<_0 w$ if $v,w\in L_0$ and $v<_{01}w$.
2. $v<_1 w$ if $v,w\in L_1$ and $w_{01}v$.




 the result of This gives a $2k+1$ page layout of $G[L_0\cup L_1]$.





[ganley-heath]:https://www.sciencedirect.com/science/article/pii/S0166218X00001785
[bekos-ea]:https://arxiv.org/abs/1811.00816
