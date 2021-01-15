---
layout: problem
title:  "Free Collinear Sets"
date:   2017-07-14
permalink: free-collinear-sets.html
categories: openproblem
tags: solved
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

This problem is solved!  The full paper is submitted to SODA and there will be an upcoming arxiv submission.
