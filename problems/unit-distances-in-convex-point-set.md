---
layout: problem
title:  "Unit Distances in Convex Point Sets"
date:   2017-07-14
permalink: unit-distances-in-convex-point-sets.html
categories: openproblem erdos
---
Erdős posed the following question, but it was asked to me by [Ahmad Biniaz](http://cglab.ca/~biniaz/):

<div class="problem">
  What is the maximum number of unit distances determined by a set of $n$ points in convex position?
</div>

[Füredi][furedi] was the first to prove an $O(n\log n)$ upper bound.  Simpler proofs of the $O(n\log n)$ upper bound were later given by [Braß and Pach](brass-pach) and  [Braß, Károlyi and Valtr][brass-karolyi-valtr] ([alternate link](https://libgen.pw/download.php?id=946469)).

[Edelsbrunner][edelsbrunner] gives a lower bound construction of a convex set of $n$ points that determines $2n-7$ unit distances.  Even improving the constant in this lower bound would be a contribution.

[furedi]: https://doi.org/10.1016/0097-3165(90)90074-7
[brass-pach]:https://doi.org/10.1006/jcta.2000.3133
[edelsbrunner]:https://doi.org/10.1016/0097-3165(91)90042-F
[brass-karolyi-valtr]:https://link.springer.com/chapter/10.1007/978-3-642-55566-4_12
