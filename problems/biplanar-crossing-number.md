---
layout: problem
title:  "Biplanar Crossing Number"
date:   2017-07-14
permalink: biplanar-crossing-number.html
categories: openproblem erdos
---
Warning: János Pach posed this problem during a workshop.  It originally comes from László Székely.

$\DeclareMathOperator{\cr}{cr}$
Recall that the *crossing number*, $\cr(G)$, of a graph $G$ is the minimum number of crossings in any (not necessarily planar or straight line) drawing of a $G$.

For a graph $G=(V,E)$, if we partition its edges into to two classes $E_1=E'$ and $E_2=E\setminus E'$, we obtain two graphs $G_1=(V,E_1)$ and $G_2=(V,E_2)$. The \emph{biplanar crossing number}, $\cr_2(G)$ is defined as
\\[
    \cr_2(G) = \min\\{\cr(G_1)+\cr(G_2)\colon E'\subseteq E\\} \enspace .
\\]

This problem is about relating $\cr_2(G)$ and $\cr(G)$. Specifically, find $\sup_{G}\frac{\cr_2(G)}{\cr(G)}$ over all nonplanar graphs $G$. Here's what's known:
For every graph G,
\\[
     \cr_2(G) \le \frac{3}{8}\cr(G) \enspace,
\\]
and there are infinitely many graphs $G$ for which
\\[
    \frac{1}{4}\cr(G) \le \cr_2(G) \enspace .
\\]
The lower-bound follows from the existence of the so-called crossing number of constant.  An upper-bound of $\cr_2(G)\le\frac{1}{2}\cr(G)$ is immediate:  Randomly partition the edges among $G_1$ and $G_2$ and each crossing in the original drawing of $G$ survives with probability only $1/2$.  

The upper bound of $3/8$ is due to [Pach and others][pach-etal]:
Randomly partition the vertices into two sets $V_1$ and $V_2$ and let $E'$ be the set of edges with one endpoint in each set.  Now, a crossing involves 4 vertices and there are 16 ways to assign these to $V_1$ and $V_2$; 6 of these 16 ways preserve the crossing, and the others eliminate it. The key observation is that, in one of the graphs, $V_1$ and $V_2$ are disconnected, so they can be drawn separately, and this eliminates any crossing between $uv$ and $wx$ with $u,v\in V_1$ and $wx\in V_2$.  

[pach-etal]:https://arxiv.org/abs/1611.05746
