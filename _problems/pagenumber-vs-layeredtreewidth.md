---
layout: problem
title:  "Page Number Versus Layered Treewidth"
date:   2017-07-14
permalink: page-number-versus-layered-treewidth.html
categories: openproblem graphs layeredwidth
category: problem
---
[David Wood](http://users.monash.edu.au/~davidwo/) asked me this question in June 2017.  It asks about finding a relationship between the page number of a graph and its layered treewidth.  (A definition of layered treewidth can be found in [Section 2 of this paper](https://arxiv.org/pdf/1306.1595.pdf).)

<div class="problem">
  Is the page number of every graph bounded a function of its layered treewidth?
</div>

The simplest case is graphs of layered treewidth 1, which can be visualized as follows: Take the product of a tree $T$ and a path of length $k$.  The resulting graph naturally has some *tree edges* ($k$ copies of each edge in $T$) and *non-tree* edges.  Next perform arbitrary edge contractions on the tree edges to obtain a graph $G$.  Every graph of layered treewidth 1 is a subgraph of a graph that can be obtained this way, so it suffices to bound the page number of $G$.

The general case is probably far from trivial.  It would imply, for example, that $k$-planar graphs have bounded page number.  We were able to solve the [special case where $G$ has small layered pathwidth](lpw-vs-pn.html).

## Update (May 2019)

In view of the recent developments with layered $H$-partitions, it probably makes as much sense to ask this question about graphs have layered $H$-partitions of bounded layered width in which $H$ has bounded treewidth.

In fact, it might make the most sense to find a structural decomposition like $H$-partitions (but maybe using a DFS rather than a BFS tree).
