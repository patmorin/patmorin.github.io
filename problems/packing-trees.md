---
layout: post
title:  "Packing Trees"
date:   2017-07-15
permalink: packing-trees.html
categories: openproblem
---
Andre van Renssen and other shows that, in any $n$ point set, we can construct two edge-disjoint plane spanning trees $T_1$ and $T_2$ so that the longest edge in any tree is at most 3 times the length of the longest edge in the minimum spanning tree.  (Actuallly, every edge except one is at most twice the length of the minimum MST edge.)

If you don't care about edge lengths, then Garcia (2015) has an easy construction that gives $k$ plane trees from $3k$ points in general position (it's a sweep around a centerpoint).

Let $\beta$ be the longest edge in the MST.  Andre and others have a version that is distributed (each node needs only to know its neighbours at distance $O(k\beta)$ and that can build $k$ trees with maximum edge length at most $O(k\beta)$.  (It's a grid construction.)  Everything is tight except for the constants.

There is a family of problems here, where instead of trees, we ask for plane paths, spanners,...
