---
layout: student
title:  "David Worley"
date:   2024-03-26
permalink: worley.html
categories: student
---

# March 26, 2024:

Let $G$ be a planar graph and let $s(G)$ be the minimum value $s$ such that $G$ has a span-$s$ weakly levelled planar drawing.  Is the layered pathwidth of $G$ bounded by some function of $s(G)$?

The other direction is known to be untrue.  Biedl has examples of pathwidth-$3$ planar graphs $G$ with an apex vertex in which every layered drawing requires $\Omega(n)$ layers.  The existence of the apex vertex then implies that every $s(G)=\Omega(n)$.  Maybe one can say something about graphs of bounded degree.

At most you could get a bound of $s(G)=O(2^{\operatorname{lpw(G)}}/\operatorname{lpw(G)})$.  If you replace the apex (top) vertex in Biedl's example with a complete binary tree you get a planar graph of bounded degree, with pathwidth O(log n) in which every layered planar drawing has Omega(n) layers. I think this means that in any levelled planar drawing, some of the (binary tree) edges will have span at least Omega(n/log n).

Next week, David give a proof for the case $s=1$ that is contained in a paper of Dujmović, Eppstein, ?, and Wood.
