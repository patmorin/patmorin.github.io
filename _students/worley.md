---
layout: student
title:  "David Worley"
date:   2024-03-26
permalink: worley.html
categories: student
---
# April 2, 2024:

David presented the proof that a graph is levelled planar if and only if it has layered pathwidth 1 and gave a convincing argument that $s$-span levelled planar graphs have layered pathwidth $1$ and that $s$-span weakly-levelled planar graphs have layered pathwidth $2$.

Then we looked at [Therese's example](https://link.springer.com/article/10.1007/s00454-010-9310-z) of a graph of pathwidth $3$ that needs to use $\Omega(n)$ layers and has a dominant vertex.   David will look at it some more and check if it has layered pathwidth $2$ or $3$.  That's what we'll discuss next week.


# March 26, 2024:

Let $G$ be a planar graph and let $s(G)$ be the minimum value $s$ such that $G$ has a span-$s$ weakly levelled planar drawing.  Is the layered pathwidth of $G$ bounded by some function of $s(G)$?

The other direction is known to be untrue.  Biedl has examples of pathwidth-$3$ planar graphs $G$ with an apex vertex in which every layered drawing requires $\Omega(n)$ layers.  The existence of the apex vertex then implies that every $s(G)=\Omega(n)$.  Maybe one can say something about graphs of bounded degree.

At most you could get a bound of $s(G)=O(2^{\operatorname{lpw(G)}}/\operatorname{lpw(G)})$.  If you replace the apex (top) vertex in Biedl's example with a complete binary tree you get a planar graph of bounded degree, with pathwidth O(log n) in which every layered planar drawing has Omega(n) layers. I think this means that in any levelled planar drawing, some of the (binary tree) edges will have span at least Omega(n/log n).

Next week, David give a proof for the case $s=1$ that is contained in a paper of Dujmović, Eppstein, ?, and Wood.
