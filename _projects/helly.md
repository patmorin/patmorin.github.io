---
layout: project
title:  "Notes on Helly Properties of Graphs"
permalink: helly.html
categories: project
---

A family $\mathcal{F}$ of sets is *$d$-Helly* if every finite $(d+1)$-wise intersecting subfamily of $\mathcal{F}$ has a non-empty common intersection.  For example, the family of convex sets in $\R^d$ is $d$-Helly.  

This project is concerned with families of sets derived from subsets of vertices in a given graph $G$.  Some definitions:

For a (unweighted simple undirected) graph $G$, and two vertices $v,w\in V(G)$, let $d_G(v,w)$ be the length of the shortest path from $v$ to $w$ in $G$.  For a vertex $v\in V(G)$ and an integer $r$, define the *radius-$r$ ball centered at $v$* as $B_G(v,r) = \lbrace w\in V(G): d_G(v,w)\le r \rbrace$.
A graph $G$ is *ball $d$-Helly* if the family
\\[
    \mathcal{B}_G = \lbrace B_G(v,r): v\in V(G), r\in\N \rbrace
\\]
is $d$-Helly.

A *maximal clique* in a graph $G$ is a subset $C\subseteq V(G)$ such that $G[C]$ is a clique but $G[C\cup\lbrace w\rbrace]$ is not a clique for every $w\in V(G)\setminus C$.  Then $G$ is *clique $d$-Helly* if the family
\\[
  \mathcal{C}_G = \lbrace C\subseteq V(G): \text{$C$ is a maximal clique in $G$}   \rbrace
\\]
if $d$-Helly.

A graph $G$ is *subgraph-$d$-Helly* if the family
\\[
   \mathcal{S}_G = \lbrace S\subseteq V(G): \text{$G[S]$ is connected}   \rbrace
\\]
is $d$-Helly.


# Ball $1$-Helly Graphs
The class of ball $1$-Helly graphs is well understood.  For example Theorem 3.1 in [this paper by Bandelt and Chepoi](http://pageperso.lif.univ-mrs.fr/~victor.chepoi/survey_cm_bis.pdf) shows that the following statements are equivalent:

1. $G$ is ball $1$-Helly.
2. $G$ is retract of strong product of paths.
3. $G$ is a dismantlable clique-Helly graph.
4. $G$ is a pseudo-modular graph in which the family of unit balls is $1$-Helly.
5. For every vertex $v$ in a diametrical pair, there exists a vertex $w$ dominating $v$ and $G-\lbrace v\rbrace$ is an absolute retract.
6. For any $\pi:V(G)\to\R_{\ge 0}$, the eccentricity function $e_\pi:V(G)\to\R_{\ge 0}$ defined as $e_\pi(x)=\max\lbrace \pi(v)\cdot d_G(x,v): v\in V(G)\rbrace$ is unimodal.

*Retraction, Retracts, and Absolute Retracts:* A map $\varphi:V(G)\to V(G)$ is a *retraction* if $d_G(\varphi(v),\varphi(w))\le d_G(v,w)$ for every $v,w\in V(G)$.  The subgraph $G[\lbrace\varphi(v):v\in V(G) \rbrace]$ is called a *retract* of $G$.  (TODO: Define *absolute retract*.)

*Dismantlable:*  There exists an ordering $v_1,\ldots,v_n$ of $V(G)$ such that for every $i\in\lbrace 1,\ldots,n\rbrace$, there is a $j\in\lbrace 1,\ldots,i-1\rbrace$ such that $v_iv_j\in E(G)$ and $v_j$ dominates $v_i$ in $G[\lbrace v_1,\ldots,v_i\rbrace]$.

# Properties of Planar Ball $1$-Helly graphs

What can we say about planar graphs that are ball $1$-Helly?

**Lemma 1:** Let $G$ be a ball $d$-Helly graph, let $K$ be a clique in $G$, let $C_1,\ldots,C_k$ be the connected components of $G-K$ and, for each $i\in\lbrace 1,\ldots,k\rbrace$ let $G_i=G[V(C_1)\cup K]$.  Then $G_i$ is a ball $d$-Helly graph for each $i\in\lbrace 1,\ldots,k\rbrace$.

*Proof:* Let $b_1,\ldots,b_{n}$ be a set of $(d+1)$-wise intersecting balls in $G_i$ where $b_j=B_{G_i}(v_j,r_j)$ for each $j\in\lbrace 1,\ldots,n\rbrace$.
Let $b_1',\ldots,b_n'$ be the corresponding balls in $G$, so that $b_j'=B_G(v_j,r_j)$.  Since $K$ is a clique in $G$, $d_G(x,y)=d_{G_i}(x,y)$ for any pair of vertex $x,y\in V(G_i)$.  Therefore $b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  

Observe that, if $b_j'$ contains a vertex not in $G_i$ then $b_j'$ and $b_j$ contain $K$.  Since $G$ is $d$-Helly some vertex $v\in V(G_i)$ is in $b_j'$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  If $v\in V(G_i)$ then we are done since $v\in b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  If $v\not\in V(G_i)$ then we are also done since $K\subseteq b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  QED

**Theorem 1:**  Every ball $1$-Helly triangulation $G$ is a (planar) 3-tree.  

*Proof:* The proof is by induction on $n:=\|V(G)\|$.  The base case $n=3$ is trivial.  By Characterization 3 above, $G$ must be clique-Helly and have a dismantling $v_1,\ldots,v_n$. Let $w_1,\ldots,w_\delta$ be the neighbours of $v_n$ in $G$ in the order in which they appear in a planar embedding of $G$.  If $\delta=3$, then $G'=G-\lbrace v_n\rbrace$ is a triangulation and, by Lemma 1, $G'$ is ball $1$-Helly.  Therefore, by induction, $G'$ is a 3-tree and $G$ is obtained by attaching a vertex $v_n$ to 3-clique in $G'$, so $G$ is itself a 3-tree.

If $\delta\ge 4$ then, by the definition of dismantling, some vertex $w\in \lbrace v_1,\ldots,v_{n-1}\rbrace$ is adjacent to or is $w_i$ for each $i\in\lbrace 1,\ldots,d\rbrace$.  By planarity, it must be the case that $w=w_1$ (say). Therefore, $K=\lbrace w_1,v,w_3\rbrace$ is a clique and $G-K$ has two components: $C_1$ that contain $w_2$ and $C_2$ that contains $w_4$.  By Lemma 1, the triangulations $G_1=G[V(C_1)\cup K]$ and $G_2=G[V(C_2)\cup K]$ are each $d$-Helly so by induction, each is a planar 3-tree.  Therefore $G$ is obtained by gluing together the 3-trees $G_1$ and $G_2$ at a 3-clique so $G$ is itself a 3-tree.  QED

Note to self: I think the proof of Theorem 1 could be simpler and more general: Every dismantlable triangulation is a 3-tree.  The only step missing is a version of Lemma 1 where the condition $d$-Helly is replaced with dismantlable.
