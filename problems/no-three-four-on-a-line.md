---
layout: post
title:  "General Position Subsets"
date:   2017-07-14
permalink: no-three-four-on-a-line.html
categories: openproblem erdos hard
---
$\newcommand{\S}{\mathcal{S}}$This is a famous open problem, due to Erdős and certainly very hard.  I've played around with some probabilistic arguments but gotten nowhere further than the simple lower bounds.

For each $r\in\N$, let $\S\_r$ denote the class of point sets in $\R^2$ with no $r$ points on a line and let
\\[
   f(n) = \min_{S\in\S_4}\max_{R\in\S_3}|R\cap S| \enspace .
\\]
<div class="problem">
  Determine the asymptotic behaviour of $f(n)$.
</div>
There are several easy proofs that $f(n)\in\Omega(\sqrt{n})$, that is, every $n$ point set with no four points collinear contains a subset of size $\Omega(\sqrt{n})$ in general position.  [Füredi][furedi] upped this bound to $\Omega(\sqrt{n\log n})$ and showed a lower bound of $o(n)$.  The best upper bound currently is $O(n/\sqrt{\log^* n})$, which is also in the same paper of Füredi combined with the best version of the Hales-Jewett Theorem.

[Pór and Wood][por-wood]'s expository paper contains many generalizations and open problems.  The recent paper by [Cardinal, Toth, and Wood][cardinal-etal] has some extensions to higher dimensions.

[furedi]:http://www.math.uiuc.edu/~z-furedi/PUBS/furedi_3-indep-sets-on-plane.pdf
[cardinal-etal]:https://dx.doi.org/10.1007/s00022-016-0323-5
[por-wood]:http://dx.doi.org/10.20382/jocg.v1i1a3
