---
layout: problem
title:  "Free Collinear Sets"
date:   2017-07-14
permalink: free-collinear-sets.html
categories: openproblem erdos
---
Let $G=(V,E)$ be a graph that has a crossing-free straight-line drawing in which a subset $X=\\{v_1,\ldots,v_k\\}$ of its vertices are drawn on the x-axis, in this order. We call $X$ a *collinear set*.  We say that $X$ is *free* if, for every $x_1<x_2<\cdots<x_k$, there exists a crossing-free straight-line drawing of $G$ where $v_i$ is drawn at $(x_i,0)$ for each $i\in\\{1,\ldots,k\\}$.

<div class="conjecture">
  Every collinear set is free.
</div>

This is a really strong conjecture.  Maybe too strong. Here is a weaker version that would be just as useful.

<div class="conjecture">
  Every collinear set of size $k$ has a subset of size $\Omega(k)$ that is free.
</div>

It is known that every collinear set of size $k$ has a free collinear subset of size $\Omega(\sqrt{k})$.  Proving either of these conjectures, or even improving the $\Omega(\sqrt{k})$ lower bound, would have applications to untangling and universal point subsets.

# Some Progress

At [WoGaG 2018](http://cglab.ca/~morin/misc/bb2018/) a group of us made some progress on this problem.  Here are some sketch of the sketchy results.

<div class="lemma">
  Let $G$ be an embedded quadrangulation. Then there exists a simple closed curve that intersects each edge of $G$ exactly once.
</div>

<div class="proof">
  Take an Euler tour of the dual of $G$ (a 4-regular graph).  This gives a curve that may not be simple since it may cross through one side of a face and out the opposite side. Remove these crossings by using one of the two possible swaps (the one that keeps the tour connected).
</div>

<div class="lemma">
  Let $G$ be an embedded quadrangulation and let $f$ be some face of $G$. Then $G$ has orientation of its edges so that every vertex has in-degree 2 except the four vertices of $f$, which have in-degree 1.
</div>

<div class="proof">
  Consider the curve defined in the proof of the previous lemma.  Cut the curve at some point in $f$ and walk clockwise along the curve in the forward direction.  The first time the curve crosses an edge $e$ incident to some vertex $u$ orient $e$ towards $u$.  Now repeat the same procedure walking counterclockwise.  Obviously each vertex has in-degree 2. Less obviously, each edge is oriented in only one direction, except the 4 edges of $f$ which are oriented in both directions.  Remove one of these oriented cycles.
</div>

<div class="lemma">
  Let $G$ be an embedded quadrangulation, let $f$ be some face of $G$ and let $C$ be a simple closed curve that interesects each edge of $G$ exactly once.  Select any point of $C$ in $f$ and walk along $C$ clockwise encountering the edges $e_1,\ldots,e_k$. Let $x_1<x_2<\cdots<x_k$ be a sequence of numbers. Then $G$ has a straight-line plane drawing in which, for each $i\in\\{1,\ldots,k\\}$, the edge $e_i$ intesects the $x$-axis at $x_i$.
</div>

<div class="proof">
  The preceding lemma and a bit of algrebra show that this can be modelled as a set of (linear?) equations that have four free variables.
</div>
