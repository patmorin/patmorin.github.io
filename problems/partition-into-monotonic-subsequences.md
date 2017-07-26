---
layout: problem
title:  "Partitioning a Sequence in Monotonic Subsequences"
date:   2017-07-15
permalink: monotonic-subsequences.html
categories: openproblem
---
This problem appears on Page 21 of the geometric range searching survey by [Agarwal and Erickson](http://jeffe.cs.illinois.edu/pubs/pdf/survey.pdf).
<div class="problem">
  What is the fastest algorithm for partitioning a sequence $x_1,\ldots,x_n$ of $n$ comparable numbers into $O(\sqrt{n})$ monotonic subsequences.
</div>

The [Erdős–Szekeres Theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem) implies that this problem has a solution.  [Bar-Yehuda and Fogel](http://www.cs.technion.ac.il/users/wwwb/cgi-bin/tr-get.cgi/1990/CS/CS0640.pdf) show that this problem can be solved in $O(n^{3/2})$ time.  Is there a near-linear time algorithm?
