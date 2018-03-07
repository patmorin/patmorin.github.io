---
layout: problem
title:  "Unmatched Colourings"
date:   2017-07-14
permalink: unmatched-colouring.html
categories: openproblem
---
Let $\mathcal{B}=\langle B_\ell: \ell\in\N\rangle$ be an infinite sequence of bipartite graphs where each $B_\ell=(\{1,\ldots,\ell\},\\{\ell+1,\ldots,2\ell\\},E_\ell)$.  For a graph $G$ and a colouring $\varphi:V(G)\to\{1,\ldots,c\}$ of $G$ we say that $\varphi$ is $\mathcal{B}$-unmatched if, for every odd-length path $u_1,\ldots,u_{2\ell}$ in $G$, there is no perfect matching $M=\{(1,w_1),\ldots,(\ell,w_\ell)\}$ in $B_\ell$ where $\varphi(u_{i})=\varphi(u_{w_i)}$ for all $i\in\\{1,\ldots,\ell\\}$.

## Examples

If we take $E(B_{\ell})=\\{(1,\ell+1),(2,\ell+2),\ldots,(\ell,2\ell)\\}$ for every $\ell$, then a colouring is $\mathcal{B}$-unmatched if and only if it is non-repetitive.

If we take $E(B_{\ell})=\\{(1,2\ell),(2,2\ell-1),\ldots,(\ell,\ell+1)\\}$ for every $\ell$, then a colouring is $\mathcal{B}$-unmatched if and only if it is palindrome free.

If we take $B_\ell=K_{\ell,\ell}$ to be a complete bipartite graph for every $\ell$, then a colouring is $\mathcal{B}$-unmatched if and only if it is anagram-free.

## Easy Results

If the graphs in $\mathcal{B}$ are have maximum degree $d$, then an application of the entropy compression method can be used to show that any graph of maximum degree $\Delta$ has a $\mathcal{B}$-unmatched colouring using $O(d\Delta)$ colours. (This requires a results by [Alon and Friendland][alon-friendland] on the number of perfect matchings in a bipartite graph with a given degree sequence.)  More generally, if $\mathcal{B}$ is such that the number of perfect matchings in $B_\ell$ is upper-bounded by $a^\ell$, then this approach shows that $O(a\Delta)$ colours suffice.

If the graphs in $\mathcal{B}$ are matchings $(1,w_1),\ldots,(\ell,w_\ell)$ with the property that $|w_{i}-w_{i+1]| < c$ for some constant $c$ and all $i\in\{1,\ldots,\ell\}$ then I believe that any graph $G$ with layered separations of width $w$ has a $\mathcal{B}$-unmatched colouring using $O(w)$ colours.  Maybe this can be extended to settings where $\mathcal{B}$ is not a matching.  (Both these results would require some work to figure out exactly what properties we would need for colouring the layers.)

## Problems

In addition to all the open problems on non-repetitive colouring and anagram-free colouring, we can ask a

[alon-friendland]:http://www.tau.ac.il/~nogaa/PDFS/mincg3.pdf
