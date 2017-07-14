---
layout: post
title:  "Triangles in Arrangements of (Pseudo)Circles"
date:   2017-07-14
permalink: triangles-in-circle-arrangements.html
categories: openproblem
---
An arrangment of $n$ circles is *simple* if any two circles are disjoint or intersect in exactly two points.
The arrangment is *intersecting* if every pair of circles is intersecting.

A *triangle* is an arrangement of circles is a face bouned by three circes. A *digon* (aka *lens*) is a face bounded by two circles.  Grünbaum made the following conjecture about pseudocircles, but it has been disproved by
[Felsner and Scheucher][felsner-scheucher].  It may still be true for circles though:

<div class="problem">
  Is it true that every simple intersecting digon-free arrangement of $n$ circles contains at least $2n-4$ triangles?
</div>

For the original problem (about pseudocircles), [Felsner and Scheucher][felsner-scheucher] give examples of simple intersecting digon-free arrangements of $n$ circles having only $16n/11 + o(n)$ triangles.  A lower bound of $4n/3$ due to Hershberger and Snoeyink is probably the right answer:

<div class="problem">
  Do there exist simple intersecting digon-free arrangments of $n$ pseudocircles with only $\lceil 4n/3\rceil$ triangles for infinitely many values of $n$?
</div>


[felsner-scheucher]: http://www.ist.tugraz.at/scheucher/publ/fs-aptd-17.pdf
