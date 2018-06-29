---
layout: problem
title:  "Anagram-Free Colouring"
date:   2017-07-14
permalink: anagram-free.html
categories: openproblem
---
An even-length sequence $a=st$ is an *anagram* if $s$ is a permutation of $t$. A sequence is *anagram-free* if it does not contain any anagram as a contiguous subsequence.  A colouring of a graph $G$ is *anagram-free* if the colour sequence encountered on any simple path in $G$ is anagram-free.
Equivalently, a colouring is anagram-free if there is no path in $G$ whose colour sequence is an anagram.  The minimum number of colours in an anagram-free colouring of $G$ is called the *anagram-free chromatic number* of $G$ and is denoted $\pi_\alpha(G)$.

A classic result on combinatorics of the strings is that the $n$-vertex path $P_n$ has $\pi_\alpha(P_n)\le 4$ with equality for $n\ge 7$.

<div class="problem">
  What is the anagram-free chromatic number of the $2\times n$ grid?
</div>

Using divide-and-conquer, we obtain an anagram-free colouring of the $2\times n$ using grid $\log_2(n+1)$ colours. More generally, any graph $G$ of treewidth $k$ has an $\pi_\alpha(G)\in O(k\log n)$.  For graphs $G$ coming from hereditary families with treewidth $O(n^\delta)$, $0<\delta<1$, $\pi_\alpha(G)\in O(n^{\delta})$.  So, for examples, $\pi_\alpha(G)\in O(\sqrt{n})$ for any $n$-vertex planar graph $G$.  It is worth noting that this divide-and-conquer approach gives a stronger property: The smallest colour on any path occurs exactly once.  This stronger type of colouring is known as a *vertex ranking*.

[Kamčev, Łuczak, and Sudakov][kamčev-ea] show that the anagram-free chromatic number of $n$-vertex binary trees can be $\Omega(\sqrt{\log n/\log\log n})$. See [Wilson and Wood][wilson-wood] for more results on trees.

<div class="problem">
  What is largest anagram-free chromatic number of any $n$-vertex tree?
</div>

[Wilson and Wood][wilson-wood] and [Kamčev, Łuczak, and Sudakov][kamčev-ea]
show that the anagram-free chromatic number of $n$-vertex planar graphs can be $\Omega(\log n)$.  [Carmi, Dujmović and Morin][carmi-dujmovic-morin] use a different construction (with pathwidth 3) that proves the same $\Omega(\log n)$ lower bound.

<div class="problem">
  What is largest anagram-free chromatic number of any $n$-vertex planar graph?
</div>

We do not even know a bound of $o(\sqrt{n})$ for the $\sqrt{n}\times\sqrt{n}$ grid. I would be willing to bet that there are $n$-vertex planar graphs with anagram-free chromatic number $\Omega(n^\epsilon)$ for some $\epsilon >0$.

[Wilson and Wood][wilson-wood] also show that any tree $T$ of pathwidth $k$ has $\pi_\alpha(T)\in O(k)$, thus avoiding the $O(\log n)$ factor of the divide-and-conquer algorithm.  They do this by choosing a path $P$ in $T$ whose removal disconnects $T$ into components that each have pathwidth at most $k-1$ and colouring $P$ using an anagram-free 4-colouring.  Their result doesn't generalize from trees to graphs: [Carmi, Dujmović and Morin][carmi-dujmovic-morin] show that there are $kn$-vertex graphs of pathwidth $k$ that require $\Omega(k\log n)$ colours.

# Relations to Other Colouring Problems

- Every non-repetitive colouring is a proper colouring, so $\chi(G)\le \pi(G)$
- Every anagram-free colouring is non-repetitive, so $\pi(G)\le \pi_\alpha(G)$
- A *linear colouring* is a colouring in which every path contains a colour that occurs exactly once. Every linear colouring is anagram-free, so $\pi_\alpha(G)\le \chi_{\mathrm{lin}}(G)$; see [Kun, O'Brien, and Sullivan](https://arxiv.org/abs/1802.09665) who introduced linear colourings
- A *centered colouring* is a colouring in which every connected subgraph contains
  a unique colour. Every centered colouring is a linear colouring, so $\chi_{\mathrm{lin}}(G) \le \chi_{\mathrm{cen}}(G)$
- The *treedepth* of a graph $G$ is the minimum height of any tree $T$ with the property that, for each $uw\in E(G)$, $u$ is an ancestor of $w$ in $T$.  The treedepth and the centered chromatic number is the same, so $\DeclareMathOperator{\td}{td}\td(G) = \chi_{\mathrm{cen}}(G)$; see Lemma 4.2 in [Nešetřil and Ossona de Mendez](https://doi.org/10.1016/j.ejc.2005.01.010)
- A *vertex ranking* is a colouring in which every path between two endpoints of the same colour contains a vertex of larger colour.  It turns out that vertex rankings and centered colourings are equivalent, so $\chi_{\mathrm{cen}}(G) = \chi_{\mathrm{vr}}(G)$; see Lemma 4.1 in [Nešetřil and Ossona de Mendez](https://doi.org/10.1016/j.ejc.2005.01.010)

Summarizing:
\\[
  \chi(G) \le \pi(G) \le \pi_\alpha(G) \le \chi_{\mathrm{lin}}(G)
   \le \chi_{\mathrm{cen}}(G) = \td(G)=\chi_{\mathrm{vr}}(G)
\\]

We know that bounded degree graphs have constant non-repetitive chromatic number but that their anagram-free chromatic number can be nearly linear, so these two parameters are obviously very different.

One property of centered colourings are that the set of unique colours of $G$ form a cut-set.  Using this fact, it is not hard to show that, for $k\le n$, the $k\times n$ grid, $G_{k\times n}$, has $\chi_{\mathrm{cen}}(G_{k\times n}) \in\Omega(k\log(n/k))$.

# Unmatchable colourings

Call a colouring *unmatchable* if every path has a colour that occurs an odd number of times. Clearly every unmatchable colouring is anagram-free, but not ever unmatchable colouring is a linear colouring. So the *unmatchable chromatic number* sits between the anagram-free and linear- chromatic numbers.

<div class="problem">
  What is the unmatchable chromatic number of $P_n$, the $n$ vertex path?
</div>


# Partial results

In any graph with layered separations of size $\ell$, we can colour with $O(p\ell\log n)$ colours so that each path of length at most $p$ is anagram-free.

In a similar vein, I think that in any graph of maximum degree $\Delta$ we can use entropy compression to colour with $O(p\Delta)$ colours so that any path of length at most $p$ is anagram-free.


[kamčev-ea]: https://arxiv.org/abs/1606.09062
[wilson-wood]: https://arxiv.org/abs/1607.01117
[carmi-dujmovic-morin]: https://arxiv.org/abs/1802.01646
