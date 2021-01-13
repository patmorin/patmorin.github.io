---
layout: problem
title:  "Pattern Matching on Generalized Strings"
date:   2021-01-13
permalink: pm.html
categories: openproblem
---
A *generalized string* is a sequence of subsets of some alphabet $\Sigma$.  A generalized string $p_1,\ldots,p_m$ *matches* a generalized string $s_1,\ldots,s_n$ at position $i$ if $p_j\cap s_{i+j-1}\neq\emptyset$ for each $j\in\{1,\ldots,m\}$.  Given $s$ and $p$, how fast can we find all matches of $p$ in $s$?

The hope is to generalize the $O(n\log m)$ time FFT-based algorithm that works for the special case when each character is either a singleton or a $\Sigma$:

A. Kalai, Efficient pattern-matching with don’t cares. In Proceedings of the 13th Annual ACM-SIAM Symposium on Discrete Algorithms, 655–656, Philadelphia, PA, USA, 2002.
