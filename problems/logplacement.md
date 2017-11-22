---
layout: problem
title:  "Optimal Log Placement"
date:   2017-07-14
permalink: log-placement.html
categories: openproblem
---
The following problems are motivated by the problem of automatically placing log statements in order to differentiate execution paths, as in [this paper][ding].

We are directed graph $G$, with a single source $s$ and at least one sink and a probability distribution over all (directed) source to sink paths in $G$. This input is given to us as a list of pairs $(P_i,p_i)$ where $P_i$ is a source to sink path and $p_i>0$. Any source to sink path not in this list is assumed to have probability 0.

The input distribution has an entropy $H=\sum_{i}p_i\log(1/p_i)$.  It also induces weights on the vertices of $G$, where $w(v)=\sum_{i:v\in P_i} p_i$ is the probability that the chosen path includes $v$.  

For a set $V'\subset V(G)$ and a path $P$ in $G$, we use $P\cap V'$ to denote the subsequence of vertices in $P$ that are contained in $X$.  For a set $V'\subset V(G)$, define
\\[
   H(V') = \sum_{X\subseteq V'}\sum_{i:P_i\cap V'=X} p_i\log(1/p_i) \enspace ,
\\]
which measures the expected entropy after seeing $P_i\cap V'$.

<div class="problem">
  Find a set $V'\subset V(G)$ such that $H(V')=0$ and $\sum_{v\in V'} w(v)$ minimized.
</div>

<div class="problem">
  Given a $W>0$, find a set $V'\subset V(G)$ such that $\sum_{v\in V'} w(v)\le W$ and $H(V')$ is minimized.
</div>

To start, we can consider each of these problems when $G$ is acyclic.

[ding]:http://log20.dsrg.utoronto.ca/log20_sosp17_paper.pdf
