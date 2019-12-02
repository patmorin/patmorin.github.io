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
of balls in $G$ is $d$-Helly.

A graph $G$ is *neighbourhood $d$-Helly* if the family
\\[
    \mathcal{N}_G = \lbrace B_G(v,1): v\in V(G) \rbrace
\\]
of unit balls in $G$ is $d$-Helly.

A *maximal clique* in a graph $G$ is a subset $C\subseteq V(G)$ such that $G[C]$ is a clique but $G[C\cup\lbrace w\rbrace]$ is not a clique for every $w\in V(G)\setminus C$.  Then $G$ is *clique $d$-Helly* if the family
\\[
  \mathcal{C}_G = \lbrace C\subseteq V(G): \text{$C$ is a maximal clique in $G$}   \rbrace
\\]
is $d$-Helly.

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

What can we say about planar graphs that are ball $d$-Helly?

**Lemma A:** A triangulation is dismantlable if and only if it is a 3-tree.

*Proof:* For every $t\in\N$, every $t$-tree $G$ is dismantlable since every $t$-tree is either a $(t+1)$-clique or contains a vertex $v_n$ whose neighbours form a clique and such that $G-\lbrace v_n\rbrace$ is a $t$-tree.  Thus, every planar 3-tree is dismantable.  Next we show that every dismantlable triangulation is a 3-tree.

Let $G$ be a dismantlable triangulation and let $v_1,\ldots,v_n$ be a dismantling of $G$. Let $\delta$ be the degree of $v_n$ and let $w_1,\ldots,w_\delta$ be the neighbours of $v_n$ in $G$ in the order in which they appear in a planar embedding of $G$.

If $\delta=3$, then $G'=G-\lbrace v_n\rbrace$ is a triangulation and $G'$ is dismantlable (using the dismantling $v_1,\ldots,v_{n-1}$).  Therefore, by induction, $G'$ is a 3-tree and $G$ is obtained by attaching a vertex $v_n$ to a 3-clique in $G'$, so $G$ is itself a 3-tree.

If $\delta\ge 4$ then, by the definition of dismantling, some vertex $w\in \lbrace v_1,\ldots,v_{n-1}\rbrace$ is adjacent to or is $w_i$ for each $i\in\lbrace 1,\ldots,\delta\rbrace$.  By planarity, it must be the case that $w=w_i$ for some $i\in\lbrace 1,\ldots,\delta\rbrace$.  Without loss of generality, assume $w=w_1$. Therefore, $K=\lbrace w_1,v,w_3\rbrace$ is a separating triangle and $G-K$ has two components: $C_0$ that contain $w_2$ and $C_1$ that contains $w_4$. Consider the two triangulations $G_0=G[V(C_0)\cup K]$ and $G_1=G[V(C_1)\cup K]$.  

We claim that $G_a$ is dismantlable for each $a\in\lbrace 0,1\rbrace$.  In particular, the subsequence $v_{i_1},\ldots,v_{i_\ell}$ of $v_1,\ldots,v_n$ containing only those vertices in $V(G_a)$ is a dismantling of $G_a$.  To see this, consider $v_{i_j}$ for some $j\in\lbrace 2,\ldots,\ell\rbrace$.  Now, $N_{G[v_1,\ldots,v_{i_j}]}(v_{i_j})\supseteq N_{G_a[v_{i_1},\ldots,v_{i_j}]}(v_{i_j})$ and there exists a vertex $v_k$, $k\in\lbrace 1,\ldots,v_{i_j-1}\rbrace$ that dominates $v_{i_j}$ in $G[v_1,\ldots,v_{i_j}]$. If $v_k\in V(G_a)$ then $v_k\in \lbrace v_{i_1},\ldots,v_{i_j-1}\rbrace$ and we are done.  Otherwise, $v_k\in V(C_{1-a})$ and is therefore not adjacent to any vertex in $V(C_a)$.  Since $v_k$ is adjacent to $v_{i_j}$, $v_{i_j}$ must therefore be a vertex in $K$. Therefore, $N_{G_a[v_{i_1},\ldots,v_{i_j}]}(v_{i_j})\subseteq K$.  But since $K$ is a clique, $v_{i_j}$ is dominated in $G_a[v_{i_1},\ldots,v_{i_j}]$ by some other vertex in $K$.

Therefore each of $G_0$ and $G_1$ is a dismantlable triangulation so, by induction, each is a 3-tree.  Therefore $G$ is obtained by gluing together the 3-trees $G_0$ and $G_1$ at a 3-clique so $G$ is itself a 3-tree. ∎

**Theorem 1:** Every ball 1-Helly triangulation $G$ is a planar 3-tree.

*Proof:* By Characterization 3 in the previous section every ball 1-Helly graph is dismantlable so, by Lemma A, every ball 1-Helly triangulation is a planar 3-tree.   ∎

<!--
Every 3-tree is dismantlable so, using Characterization 3, we need only show that every *planar* 3-tree is clique 1-Helly. We can prove this by induction on $n:=\|V(G)\|$.  The base case $n=3$ is trivial.  Consider a degree-3 vertex $v$ of $G$.  Then $v$ and its neighbours $v_1,v_2,v_3$ form a clique $K$ and  $G'=G-\lbrace v\rbrace$ is a planar 3-tree.  By induction $G'$ is clique 1-Helly.  

Now, consider a set $K_1,\ldots,K_n$ of pairwise intersecting cliques in $G$.  If none of these cliques is $K$, then these are also cliques in $G'$ so $\bigcap_{i=1}^n K_n\neq\emptyset$ and we are done.  On the other hand, if one of these cliques, say $K_n=K$, then consider the *parent clique* $K'$ of $K$, which is the only clique aside from $K$ that contains $v_1,v_2,v_3$.  Now observe that, since $v\notin K_i$ for any $i\in\lbrace 1,\ldots,n-1\rbrace$, $K'\cap K_i\supseteq K\cap K_i$ for each $i\in\lbrace 1,\ldots,n-1\rbrace$.  Therefore $K_1,\ldots,K_{n-1},K'$ is pairwise intersecting and, since $K'$ is a clique in $G'$, $\emptyset\neq \bigcap_{i=1}^{n-1}K_i\cap K'=\bigcap_{i=1}^n K_i$. -->

The interesting thing about Theorem 1 is that not every planar 3-tree is ball 1-Helly.  In fact, the 3-tree with cliques $K_0=\lbrace1,2,3,4\rbrace$,
$K_1=\lbrace 1,2,4,a\rbrace$, $K_2=\lbrace 1,3,4,b\rbrace$, $K_3=\lbrace 2,3,4,c\rbrace$, $K_4=\lbrace 2,3,c,x\rbrace$ is no 2-Helly.  The unit balls centered at $a$, $b$, and $x$ are pairwise intersecting but empty common intersection.  It should be possible to completely characterize the 1-Helly planar 3-trees.



<!-- **Conjecture F:** There are only finitely-many 1-Helly triangulations.  

*Proof Idea:* Planar 3-trees (also called stellated-triangulations are simple and have a tree-decomposition where the underlying tree is a 3-ary tree.  I suspect that if this underlying tree has height more than 3, then the underlying tree is not 1-Helly.   ∎ -->

# Some Lemmata about Ball $d$-Helly Graphs


The following pair of observations is used in the proof of [Theorem 2.2 of Bandelt and Prisner](https://doi.org/10.1016/0095-8956(91)90004-4).

**Observation 0:** Let $G$ be a graph and let $xy\in E(G)$ be an edge such that $y$ dominates $x$. Then for every ball $b$ of $G-\lbrace x\rbrace$, there is a ball $b'$ of $G$ such that $b=b'\setminus \lbrace x\rbrace$.

**Proof:** Since $y$ dominates $x$, $d_G(v,w)=d_{G-\lbrace x\rbrace}(v,w)$ for every $v,w\in V(G-\lbrace x\rbrace)$.  Therefore, for any $v,w\in V(G-\lbrace x\rbrace)$ and any $r\in\N$, $w\in B_{G-\lbrace x\rbrace }(v,r)$ if and only if $w\in B_G(v,r)$.   ∎

**Observation 0':** Let $G$ be a ball $d$-Helly graph and let $xy\in E(G)$ be an edge such that $y$ dominates $x$. Then $G-\lbrace x\rbrace$ is ball $d$-Helly.

*Proof:* Let $b_1,\ldots,b_n$ is a set of balls in $G-\lbrace x\rbrace$ that is $(d+1)$-wise intersecting. Then the corresponding balls $b_1',\ldots,b_n'$ in $G$ are $(d+1)$-wise intersecting so, since $G$ is $d$-Helly, $\bigcap_{i=1}^n b_i'$ is non-empty. If $\bigcap_{i=1}^n b_i'$ contains $v\neq x$, then, by
Observation 0, $\bigcap_{i=1}^n b_i$ contains $v$ and we are done. If $\bigcap_{i=1}^n b_i'$ contains $x$ then each of $b_1',\ldots,b_n'$ must have radius at least 1 since none of $b_1',\ldots,b_n'$ is centered at $x$. Therefore each of $b_1',\ldots,b_n'$ has radius at least one and contains $x$.  Therefore each of $b_1',\ldots,b_n'$ also contains $y$.  By Observation 0,
$\bigcap_{i=1}^n b_i$ contains $y$.  ∎

**Observation 1:** Let $H$ be a graph is neighbourhood $d$-Helly but not neighbourhood $(d-1)$-Helly and let $G$ and be obtained by adding two apex vertices $v_1$ and $v_2$ to $H$.  Then $G$ is neighbourhood $(d+1)$-Helly but not neighbourhood $d$-Helly.

*Proof:*  First we show that $G$ is not neighbourhood $d$-Helly.  Since $H$ is not neighbourhood $(d-1)$-Helly, there exists a $d$-wise intersecting set of unit balls  $\lbrace B_H(v_i,1): i\in\lbrace 1,\ldots,n\rbrace\rbrace$ such that $\bigcap_{i=1}^n B_H(v_i,1)=\emptyset$.   We use the shorthands $b_{H,i}:=B_H(v_i,1)$ and $b_{G,i}=B_G(v_i,1)$.

Observe that, for any two vertices $x,y\in V(H)$, $d_H(x,y)=d_G(x,y)$. Therefore, $b_{G,i}\cap V(H) = b_{H,i}$ for each $i\in\lbrace 1,\ldots,d+2\rbrace$.  Therefore, $\bigcap_{i=1}^n b_{G,i} \subseteq V(G)\setminus V(H)$.  Now consider the two balls $b_1=B_G(v_1,1)$ and $b_2=B_G(v_2,1)$ and observe that $b_1\cap b_2=V(H)$.  Let $A:=\lbrace b_{G,1},\ldots,b_{G,n}, b_1,b_2\rbrace$.

So
\\[
  \bigcap_{b\in A} b  = \left(\bigcap_{i=1}^n b_{G,i}\right) \cap (b_1\cap b_2)
                      \subseteq (V(G)\setminus V(H))\cap V(H) =\emptyset \enspace .
\\]
We claim that $A$ is $(d+1)$-wise intersecting.  Indeed, consider any $(d+1)$-element subset $X\subseteq A$. If $X$ contains neither $b_1$ nor $b_2$, then there is nothing to prove since $b_{G,i}\supseteq b_{H_i}$ and $b_{H,1},\ldots,b_{H,n}$ is $(d+1)$-wise intersecting. Otherwise $X=Y\cup Z$ where $Y\subseteq\lbrace b_1,b_2\rbrace$ and $Z\subseteq\lbrace b_{G,1},\ldots,b_{G,n}\rbrace$ is $(d+1)$-wise intersecting.  Therefore,
\\[
  \bigcap_{b\in A} b = \left(\bigcap_{b\in Y}^n b\right) \cap \left(\bigcap_{b\in Z} b\right)
  = V(H)\cap \left(\bigcap_{b_{G,i}\in Z} b_{G,i}\right)
  \supseteq
   V(H)\cap \left(\bigcap_{b_{G,i}\in Z} b_{H,i}\right)
  = \bigcap_{b_{G,i}\in Z} b_{H,i} \neq \emptyset \enspace .
\\]
So $A$ is $(d+1)$-wise intersecting and $\cap A=\emptyset$, so $G$ is not neighbourhood $d$-Helly.


Next we show that $G$ is $(d+1)$-Helly.  Let $B\subseteq \mathcal{N}\_G$ be a $(d+2)$-wise intersecting set of unit balls in $G$.  Then $B\setminus\lbrace b_1,b_2\rbrace$ is also $(d+2)$-wise intersecting so $\bigcap_{b\in B\setminus\lbrace b_1,b_2\rbrace} b$ is non-empty and contains at least one vertex of $H$.  Therefore
\\[ \cap B= \bigcap_{b\in B\setminus\lbrace b_1,b_2\rbrace} b\cap (b_1\cap b_2)=\bigcap_{b\in B\setminus\lbrace b_1,b_2\rbrace} b\cap V(H)
\\]
is non-empty.   ∎



# Structure of Ball 2-Helly Graphs

**Lemma Z1:** Let $G$ be a ball 2-Helly graph, let $C$ be a cycle in $G$ of length $2k$, $k\ge 2$, let $vw,\bar{w}\bar{v}\in E(C)$ be antipodal edges of $C$ (so that $d_C(v,\bar{v})=d_C(w,\bar{w})=k$).  Then there exists $x\in V(G)$ such that $d_G(x,v),d_G(x,w)\le 1$ and $d_G(x,\bar{v}),d_G(x,\bar{w})\le k-1$.

**Proof:**  Consider the balls $B_C(v,1)$, $B_C(w,1)$, $B_C(\bar{v},k-1)$, $B_C(\bar{w},k-1)$.  These four balls in $C$ are $3$-wise intersecting and each ball is a subset of the corresponding ball in $G$, so there is some vertex $x\in V(G)$ in each of them.   ∎

**Lemma Z2:** Let $G$ be a ball 2-Helly graph, let $C$ be a cycle in $G$ of length $2k+1$, $k\ge 2$, let $\bar{w}{v}\in E(C)$ be an edge of $C$, let $z\in V(C)$ be antipodal to $\bar{w}\bar{v}$ (so that $d_C(z,\bar{v})=d_C(z,\bar{w})=k$), and let $v,w\in V(C)$ be the neighbours of $z$.  Then there exists $x\in V(G)$ such that $d_G(x,z),d_G(x,v),d_G(x,w)\le 2$ and $d_G(x,\bar{v}),d_G(x,\bar{w})\le k-1$.

**Proof:**  Consider the five balls $B_C(z,2)$, $B_C(v,2)$, $B_C(w,2)$, $B_C(\bar{v},k-1)$, $B_C(\bar{w},k-1)$.  These four balls in $C$ are $3$-wise intersecting and each ball is a subset of the corresponding ball in $G$, so there is some vertex $x\in V(G)$ in each of them.   ∎

<!-- **Lemma XX:** Let $G$ be a ball 2-Helly graph and let $u,v,w,z\in V(G)$ be such that $vz,zw\in E(G)$, $d_G(u,v)=d_G(u,w)=k$ and $d_G(u,z)=k+1$.  Then there exists $x\in V(G)$ such that $d_G(u,x)=k-1$ and $x$ is adjacent to both $v$ and $w$.

**Proof:** Let $y\in V(G)$ be the vertex that maximizes the value $k'$ such that $d_G(u,y)=k'$ and $d_G(y,v)=d_G(y,w)=k-k'$.  Let $r=k-k'$, let $P_{yv}=a_0,\ldots,a_r$ be a shortest path from $y$ to $v$,
let $P_{yw}=b_0,\ldots,b_r$ be a shortest path from $y$ to $w$, and let $C$ be the cycle formed by $P_{yv}$, $P_{yw}$, and $P_{vw}=v,z,w$.  Then $C$ has length $2(r+1)$.  If $r=1$, then the 2-Helly property applied to $B_G(u,k'+1)$, $B_G(v,1)$, $B_G(w,1)$, and $B_G(z,1)$ implies that some vertex $x$ is adjacent to every vertex in $V(C)$, including $v$ and $w$.

Otherwise, Lemma Z1 implies that some vertex $q$ with $d_G(u,q)=k'+1$, $d_G()



$y$ Let $C$ be the cycle obtained by taking the union of shortest paths $P_{yv}$, $P_{yw}$ from $y$ to $v$, and $y$ to $w$, respectively along with the path $vzy$.  Then $C$ is a cycle of length $2(k-k'+1)$.   -->





<!-- **Lemma B:** Every ball 2-Helly graph $G$ is dismantlable.

*Proof:* The proof is by induction on $n:=\|V(G)\|$.  The case $n=1$ is trivial.
For $n>1$, we claim that $G$ has a dominated vertex $z$.  To see this, consider any vertex $x\in V(G)$, let $z$ be a vertex that maximizes $r=d_G(x,z)$ and let $y$ the second-to-last vertex on a shortest path $P$ from $x$ to $z$.  We claim that $y$ dominates $z$.  To see why, let $v\neq y$ be any neighbour of $z$.  Then $r-1\le d_G(x,v)\le r$.  

Consider the last vertex $y'$ on $P$ such that $d_G(x,y')+d_G(y',v)\le r$.  Notice that the path along $P$ from $y'$ to $z$, the edge $zv$ and the shortest path from $y'$ to $v$ is an isometric cycle in $G$  **Not True; consider a 4-cycle plus a dominant vertex**.  If $y'\neq y$ then this cycle has length at least 4, in which case $G$ is not 2-Helly. Therefore $y'=y$ and $yv$ is an edge of $G$.

Therefore, $yz\in E(G)$ and $yv\in E(G)$ for every neighbour $v$ of $z$, i.e, $y$ dominates $z$.  By Observation 0', the graph $G-\lbrace z\rbrace$ is 2-Helly and therefore, by induction it has a dismantling $v_1,\ldots,v_{n-1}$ so $v_1,\ldots,v_{n-1},z$ is a dismantling of $G$.  ∎


**Theorem 2:** Every ball 2-Helly triangulation $G$ is a planar 3-tree.

*Proof:* By Lemma B, $G$ is dismantlable.  Therefore, by Lemma A, $G$ is a planar 3-tree.  ∎ -->






<!-- The following observation is used in the proof of [Theorem 2.2 of Bandelt and Prisner](https://doi.org/10.1016/0095-8956(91)90004-4).

**Observation 0:** Let $G$ be a graph and let $xy\in E(G)$ be an edge such that $y$ dominates $x$. Then for every ball $b$ of $G-\lbrace x\rbrace$, there is a ball $b'$ of $G$ such that $b=b'\setminus \lbrace x\rbrace$.

**Proof:** Since $y$ dominates $x$, $d_G(v,w)=d_{G-\lbrace x\rbrace}(v,w)$ for every $v,w\in V(G-\lbrace x\rbrace)$.  Therefore, for any $v,w\in V(G-\lbrace x\rbrace)$ and any $r\in\N$, $w\in B_{G-\lbrace x\rbrace }(v,r)$ if and only if $w\in B_G(v,r)$.   ∎

**Observation 0':** Let $G$ be ball $d$-Helly graph and let $xy\in E(G)$ be an edge such that $y$ dominates $x$. Then $G-\lbrace x\rbrace$ is ball $d$-Helly.

*Proof:* Let $b_1,\ldots,b_n$ is a set of balls in $G-\lbrace x\rbrace$ that is $(d+1)$-wise intersecting. Then the corresponding balls $b_1',\ldots,b_n'$ in $G$ are $(d+1)$-wise intersecting so, since $G$ is $d$-Helly, $\bigcap_{i=1}^n b_i'$ is non-empty. If $\bigcap_{i=1}^n b_i'$ contains $v\neq x$, then, by
Observation 0, $\bigcap_{i=1}^n b_i$ contains $v$ and we are done. If $\bigcap_{i=1}^n b_i'$ contains $x$ then each of $b_1',\ldots,b_n'$ must have radius at least 1 since none of $b_1',\ldots,b_n'$ is centered at $x$. Therefore each of $b_1',\ldots,b_n'$ has radius at least one and contains $x$.  Therefore each of $b_1',\ldots,b_n'$ also contains $y$.  By Observation 0,
$\bigcap_{i=1}^n b_i$ contains $y$.  ∎


**Lemma 1:** Let $G$ be a ball $d$-Helly graph, let $K$ be a clique in $G$, let $C_1,\ldots,C_k$ be the connected components of $G-K$ and, for each $i\in\lbrace 1,\ldots,k\rbrace$ let $G_i=G[V(C_1)\cup K]$.  Then $G_i$ is a ball $d$-Helly graph for each $i\in\lbrace 1,\ldots,k\rbrace$.

*Proof:* Let $b_1,\ldots,b_{n}$ be a set of $(d+1)$-wise intersecting balls in $G_i$ where $b_j=B_{G_i}(v_j,r_j)$ for each $j\in\lbrace 1,\ldots,n\rbrace$.
Let $b_1',\ldots,b_n'$ be the corresponding balls in $G$, so that $b_j'=B_G(v_j,r_j)$.  Since $K$ is a clique in $G$, $d_G(x,y)=d_{G_i}(x,y)$ for any pair of vertex $x,y\in V(G_i)$.  Therefore $b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  

Observe that, if $b_j'$ contains a vertex not in $G_i$ then $b_j'$ and $b_j$ contain $K$.  Since $G$ is $d$-Helly some vertex $v\in V(G_i)$ is in $b_j'$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  If $v\in V(G_i)$ then we are done since $v\in b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  If $v\not\in V(G_i)$ then we are also done since $K\subseteq b_j'\cap V(G_i)=b_j$ for each $j\in\lbrace 1,\ldots,n\rbrace$.  ∎

**Theorem 1:**  Every $1$-Helly triangulation $G$ is a (planar) 3-tree.  

*Proof:* The proof is by induction on $n:=\|V(G)\|$.  The base case $n=3$ is trivial.  

By Characterization 3, $G$ is dismantlable, so let $v_1,\ldots,v_n$ be a dismantling of $G$. Let $\delta$ be the degree of $v_n$ and let $w_1,\ldots,w_\delta$ be the neighbours of $v_n$ in $G$ in the order in which they appear in a planar embedding of $G$.  If $\delta=3$, then $G'=G-\lbrace v_n\rbrace$ is a triangulation and, by Lemma 1 (or even Observation 0'), $G'$ is ball $1$-Helly.  Therefore, by induction, $G'$ is a 3-tree and $G$ is obtained by attaching a vertex $v_n$ to a 3-clique in $G'$, so $G$ is itself a 3-tree.

If $\delta\ge 4$ then, by the definition of dismantling, some vertex $w\in \lbrace v_1,\ldots,v_{n-1}\rbrace$ is adjacent to or is $w_i$ for each $i\in\lbrace 1,\ldots,\delta\rbrace$.  By planarity, it must be the case that $w=w_i$ for some $i\in\lbrace 1,\ldots,\delta\rbrace$.  Without loss of generality, assume $w=w_1$. Therefore, $K=\lbrace w_1,v,w_3\rbrace$ is a clique and $G-K$ has two components: $C_1$ that contains $w_2$ and $C_2$ that contains $w_4$.  By Lemma 1 (or Observation 0'), the triangulations $G_1=G[V(C_1)\cup K]$ and $G_2=G[V(C_2)\cup K]$ are each $1$-Helly so by induction, each is a planar 3-tree.  Therefore $G$ is obtained by gluing together the 3-trees $G_1$ and $G_2$ at a 3-clique so $G$ is itself a 3-tree.  ∎ -->
