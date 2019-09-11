---
layout: problem
title:  "Interference in Random Point Sets"
date:   2017-07-14
permalink: interference.html
categories: openproblem
---
In a geometric graph, $G$, each node $v$ has a *transmission radius*
\\[
     r(v) = \max\\{\|vw\| : vw\in E(G)\\}
\\]
equal to the distance to its furthest neighbour.  This defines a *transmission disk*
\\[
     d(v) = \\{ p : \|vp\|\le r(v)\\} \enspace .
\\]
The (receiver-centric) *interference* at a point $p$ is defined as the number of transmission disks that contain $p$
\\[
   I_G(p) = |\\{v\in V(G):p\in d(v)\\}| \enspace ,
\\]
and the (maximum receiver-centric) *interference* of $G$ is
\\[
   I(G) = \max\\{I_G(p) : p\in\R^2\\} \enspace .
\\]
Finally, the interference of a finite point set $V$ is
\\[
   \min\\{I(G):\text{$V(G)=V$ and $G$ is connected}\\} \enspace .
\\]
<div class="problem">
  What is $\E[I(V)]$ when $V$ consists of $n$ points independently and uniformly distributed in $[0,1]$?
</div>

[Devroye and Morin][devroye-morin] show that $\E[I(V)] \in O(\log^{1/3}n)$ and that
$\E[I(V)] \in \Omega(\log^{1/4}n)$.

[devroye-morin]: https://arxiv.org/abs/1202.5945
