---
layout: student
title:  "Hussein Houdrouge"
date:   2024-03-26
permalink: houdrouge.html
categories: student
---
$\DeclareMathOperator{\td}{td}$

# April 2, 2024:

It turns out that Chun-Hung Liu [completely solved last week's problem](https://link.springer.com/article/10.1007/s00493-024-00081-8), so we decided to look into the following problem posed by [Dvořák and Wood](https://arxiv.org/abs/2208.10074).


**Question:**
For any hereditary graph class $\mathcal{G}$ admitting $O(n^{1-\epsilon})$ balanced separators, does there exist a constant $c=c(\mathcal{G})$ such that every $n$-vertex graph $G\in \mathcal{G}$ is contained in $H\boxtimes K_m$, where $\text{treewidth}(H)\leqslant c$ and $m\in O(n^{1-\epsilon})$?

Illingworth--Scott--Wood solved this question for for $K_t$-minor-free graphs with $\epsilon=\frac12$ and $c=t-2$. It may even be true that $c=c(\mathcal{G})$ is a function of $\epsilon$ only, which was recently proved for $K_t$-minor-free graphs by Distel--Dujmović--Eppstein--Hickingbotham--Joret--Micek--Morin--Seweryn--Wood with $c=4$.

There are many natural geometric graph classes where this problem is open:

- Touching graphs of 3-D spheres, which admit  $O(n^{2/3})$ balanced separators  [MTTV].
- Eppstein--Gupta defined a graph $G$ to be \emph{$k$-crossing-degenerate} if $G$ has a drawing in the plane such that the associated crossing graph is $k$-degenerate. They showed that such graphs have $O(k^{3/4}n^{1/2})$ separation-number. The above question is open for $k$-crossing-degenerate graphs. The same question applies for $k$-gap-planar graphs [Bae et al.].
- String graphs on $m$ edges, which admit  $O(m^{1/2})$ balanced separators [Lee]?
- Graphs with layered tree-width $k$, which admit $O(\sqrt{kn})$ balanced separators [DMW].
- See [SW,DMN] for more examples of geometric intersection graphs where this question is unsolved and interesting.

Z. Dvořák, D. R. Wood.
Product structure of graph classes with strongly sublinear separators, 2023, https://arxiv.org/abs/2208.10074

[MTTV] Gary L. Miller, Shang-Hua Teng, William Thurston, and Stephen A. Vavasis.
Separators for sphere-packings and nearest neighbor graphs. J. ACM, 44(1):1–29, 1997

M. Distel, V. Dujmović, D. Eppstein, R. Hickingbotham, G. Joret, P. Micek, P. Morin, M. T. Seweryn, D. R. Wood.
Product structure extension of the Alon–Seymour–Thomas theorem, 2022.
https://arxiv.org/abs/2212.08739

F. Illingworth, A. Scott, D. R. Wood.
Product structure of graphs with an excluded minor.
Trans. Amer. Math. Soc., to appear.
https://arxiv.org/abs/2104.06627

[EG] David Eppstein and Siddharth Gupta. Crossing patterns in nonplanar road networks.
In Proc. 25th ACM SIGSPATIAL Int’l Conf. on Advances in Geographic Information Systems, pp. 40:1–9. 2017

Sang Won Bae, Jean-François Baffier, Jinhee Chun, Peter Eades, Kord Eickmeyer, Luca Grilli, Seok-Hee Hong, Matias Korman, Fabrizio Montecchiani, Ignaz Rutter, and Csaba D. Tóth. Gap-planar graphs. Theor. Comput. Sci., 745:36–52, 2018

James R. Lee. Separators in region intersection graphs. 2016, arXiv:1608.01612.

[DMW] Vida Dujmović, Pat Morin, and David R. Wood. Layered separators in minor-closed
graph classes with applications. J. Combin. Theory Ser. B, 127:111–147, 2017

[DMN] Zdeněk Dvořák, Rose McCarty, and Sergey Norin. Sublinear separators in
intersection graphs of convex shapes. SIAM J. Disc. Math., 35(2):1149–1164, 2021.

[SW] Warren D. Smith and Nicholas C. Wormald. Geometric separator theorems &amp;
applications. In Proc. 39th Annual Symp. on Foundations of Comput. Sci. (FOCS ’98),
pp. 232–243. IEEE, 1998

# March 26, 2024:

**Conjecture:** (Nesetril and Ossona de Mendez) Let $\mathcal{X}$ be the class of $X$-minor-free graphs for some connected graph $X$.  Then the degenerate chromatic number of $\mathcal{X}$ is at most $\td(X)-1$.

Universal graphs of treedepth $k$ (the closure of complete $b$-ary trees of vertex-height $k$) show that this result is tight.  Any colouring of such a tree with $k-2$ colours will have a colour class that induces a graph of maximum degree at least $b$.

 [Norin, Scott, Seymour, and Wood](https://arxiv.org/abs/1708.02370) show that the degenerate chromatic number of $\mathcal{X}$ is at most $2^{\td(X)}$.  

 Next week, Hussein will show me this proof.
