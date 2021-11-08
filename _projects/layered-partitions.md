---
layout: problem
title:  "Layered Partitions/Product Structure"
date:   2017-07-14
permalink: layered-partitions.html
categories: openproblem
---
$\DeclareMathOperator{\lw}{lw}\DeclareMathOperator{\tw}{tw}\DeclareMathOperator{\pw}{pw}$Remember that a *layered partition* $(\mathcal{L},\mathcal{P})$ of a graph $G$ consists of a layering $\mathcal{L}$ of $V(G)$ and a partition $\mathcal{P}$ of $V(G)$.  The *layered width* of the partition is defined as $\lw(\mathcal{L},\mathcal{P}):=\max\lbrace\|L\cap P\|:(L,P)\in\mathcal{L}\times\mathcal{P}\rbrace$.  We are interested in layered partitions that have small layered width and in which the treewidth of the quotient graph $H:=G/\mathcal{P}$ is small.

It is easy to check that $G$ has a layered partition $(\mathcal{L},\mathcal{P})$ with $\lw(\mathcal{L},\mathcal{P})\le w$ if and only if $G$ is isomorphic to a subgraph of $H\boxtimes P\boxtimes K_w$, where $H:=G/\mathcal{P}$, $P$ is a path, and $K_w$ is a clique on $w$ vertices.  The [*Planar Product Structure Theorem*](https://arxiv.org/abs/1904.04791) states that, for every planar graph $G$, there exists a planar graph $H$, $\tw(H)\le 8$, and a path $P$ such that $G\subseteq H\boxtimes P$.  A second version of the theorem states that for every planar graph $G$ there exists a planar graph $H$, $\tw(H)\le 3$, and a path $P$ such that $G\subseteq H\boxtimes P\boxtimes K_3$.

We say that a graph family $\mathcal{G}$ has *(treewidth/pathwidth) product structure* if every member of $\mathcal{G}$ is isomorphic to a subgraph of a strong product of a bounded treewidth/pathwidth graph and a path.

The planar product structure theorem has several generalizations and applications and there are a lot of open problems left and more applications to be found.

# Other Product Structure Theorems

The product structure theorem generalizes to Euler genus-$g$ graphs. In this generalization, the graph $H$ is an apex graph and the layered width of the partition is $O(g)$.  This can be generalized even further, all the way up to apex-minor free graphs, though the layered width is no longer explicitly bounded as a function of the forbidden minor.

## The Structure of $k$-Planar graphs

[Dujmović, Morin, and Wood](https://arxiv.org/abs/1907.05168) showed that $k$-planar graphs have layered $H$-partition of layered width $O(k^2)$ where $H$ has treewidth $O(k^3)$.  It would be nice to reduced the treewidth of $H$.

<div class="conjecture">
  There exists a constant $C$ such that every $k$-planar graph has a layered $H$-partition of layered width $f(k)$ where $H$ has treewidth at most $C$.
</div>

## The Structure of Disk Graphs of Bounded Ply

A *disk graph* is a graph whose vertices are closed disks in $\R^2$ and that contains an edge $uv$ if and only if $u\cap v\neq\emptyset$.  The *ply* of a disk graph is the maximum number of disks/vertices of $G$ that contain a single point. A *unit disk graph* is a disk graph whose vertices/disks all have the same radius.

<div class="conjecture">
  There exists a function $f:\N\to\N$ such that, for any unit disk graph $G$ of ply at most $k$, $G$ is a subgraph of $K_{f(k)}\boxtimes P\boxtimes P$.
</div>

The preceding conjecture is probably easy and so is its generalization to $d$ dimensions.  

**Update:** The $\R^d$ version of the preceding conjecture is proven in the paper by [Dvořák et al](https://arxiv.org/pdf/2001.08860.pdf) in Theorem 27.  The same paper, in Open Problem 29, asks a question closely related to the following conjecture:

<div class="conjecture">
  [Disproved] There exists a function $f:\N\to\N$ such that, for any disk graph $G$ of ply at most $k$, $G$ is a subgraph of $H\boxtimes P + K_{f(k)}$ for some graph $H$ of treewidth at most $f(k)$.
</div>

The following graph provides a counterexample.  Let $Q$ to be a touching unit disk representation of a $n\times n$ grid.  Add a set $A$ of $r\in \omega(1)$ disks to $Q$ that are pairwise disjoint but such that each disk intersects $r\in\omega(1)$ disks of $Q$.  (We can easily do this for some $r\in\Omega(\sqrt{n})$.)  The resulting disk graph $G$ has ply at most $3$ so, if the conjecture is true, then $G$ is a subgraph of $H\boxtimes P\boxtimes K_{f(3)}$ where $\tw(H)\le f(3)$.  Furthermore, for each $a\in A$, $Q[N_G(a)]\subseteq G[N_G[a]]$ contains an $\Omega(r)\times \Omega(r)$ grid, so $\tw(G[N_G[a]]) \in \Omega(r)$.  

If the conjecture is true, then there exists a homomorphism $\psi:G\to H\boxtimes P+K_{f(3)}$.  The diameter of $G[N_G[a]]$ is at most $2$.  Therefore, if $\psi$ maps all vertices of $N_G[a]$ to $H\boxtimes P$ then $\psi$ maps all vertices of $N_G[a]$ to $H\boxtimes P_3$ where $P_3$ is a subpath of $P$ containing at most $3$ vertices.  Therefore
\\[
  \Omega(r)\le \tw(G[N_G[a]])\le \tw(H\boxtimes P_3) \le 3\cdot \tw(H)
\\]
so $\tw(H)\in \Omega(r)\subseteq \omega(1)$, which is a contradiction since $\tw(H)\le f(3)\in O(1)$.  Therefore $\Psi$ must map some vertex of $N_G[a]$ to a vertex of $K_{f(3)}$.  But this is true for each $a\in A$, so it must be the case that $f(3)=|V(K_{f(3)})|\ge |A|=r\in\omega(1)$, also a contradiction. ∎

The preceding argument actually shows something considerably stronger.  Let $G_n$ denote the $n\times n + r$ vertex graph described above.  For any integer $b$ and any bounded-degree graph $R$, there exists an $n$ such that $G_n\not\subseteq H\boxtimes R + K_b$.  This includes the interesting case $R=P\boxtimes \cdots\boxtimes P$ where the number of factors in the product is a constant.  The key observation is that $\psi$ must take $N_G[a]$ onto a subgraph of $H\boxtimes R + K_b$ of diameter at most $2$. The bounded degree of $R$ ensures that this subgraph either includes a vertex of $K_b$ or has bounded treewidth. (In particular, the treewidth is bounded by $\tw(H)\cdot(\Delta^2+\Delta+1)$.)

Open Problem 29 in [this paper](https://arxiv.org/pdf/2001.08860.pdf) asks if every constant ply ball intersection graph in $\R^d$ can be expressed as clique-sums on graphs of the form $H\boxtimes R+K_b$.  I think the graph $G$ described above shows that the answer is no, but I first have to convince myself that clique-sums don't help to decompose $G$.

One might think of fixing the conjecture by restricting it to bounded-degree disk graphs.  That might work for disk graphs, but it won't work for ball intersection graphs in $\R^3$.  In $\R^3$ we can replace each vertex $a\in A$ with a complete binary tree $T_a$.  This gives a graph of maximum degree $5$ and ply $2$ and $\psi$ has to map $N_G[T_a]$ onto a subgraph of diameter $O(\log r)$.  By taking $r\in \Omega(\sqrt{n})$, the proof for $H\boxtimes P+K_{f(s)}$ finishes with $f(2)\in\Omega(\sqrt{n}/\log n)$.  The version for $H\boxtimes R+K_r$ finishes with $f(2)\ge \sqrt{n}/g(O(\log n))$ where $g$ is the *growth function* of $R$ (so $g(x)$ is the size of the largest ball of radius $x$ in $R$).  This disproves the conjecture when $g(x)\le 2^{o(x)}$.  In particular, it disproves the conjecture when $R$ has polynomial growth, which by the result of [Krauthgamer and Lee](https://doi.org/10.1007/s00493-007-2183-y), is equivalent to $R\subseteq P\boxtimes\cdots\boxtimes P$.


## The Structure of $k$-nearest neighbour graphs in $\R^d$
Here's one from David Wood:

<div class="conjecture">
   Let $G$ be the $k$-nearest-neighbour graph of an $n$-point set in $\R^d$.  Then $G$ is a subgraph of $H\boxtimes P\boxtimes P\boxtimes\cdots\boxtimes P$ where $H=H(G)$ is a graph of treewidth at most $f(d,k)$, $P$ is a path, and the number of occurrences of $P$ in the product is $d-1$.
</div>

The conjecture is true for $d=1$ (easy) and $d=2$ (in our paper on the structure of $k$-planar graphs).  Note that any complete binary tree is a $k$-nearest neighbour graph of a point set in $\R^2$, so the result of [Krauthgamer and Lee](https://doi.org/10.1007/s00493-007-2183-y) on graphs with polynomial growth doesn't apply.

~~Here's a stronger version that has more of a "universal graphs" flavour:~~

<div class="conjecture">
   Let $G$ be the $k$-nearest-neighbour graph of an $n$-point set in $\R^d$.  Then $G$ is a subgraph of $K\boxtimes P\boxtimes P\boxtimes\cdots\boxtimes P$ where $K$ is a clique of size at most $f(d,k)$, $P$ is a path, and the number of occurrences of $P$ in the product is $d$.
</div>

~~In addition to being a consequence of the [Krauthgamer and Lee](https://doi.org/10.1007/s00493-007-2183-y) result, the case $d=1$ is easy: If the points are $x_1<x_2<\cdots<x_n$, then consider the graph that contains the edges $x_{i+r}x_i$ for each $r\in\lbrace-k,\ldots,k\rbrace$ and each $i\in\lbrace 1,\ldots,n\rbrace$.  This graph contains the $k$-nearest neighbour graph and has bandwidth $O(k)$.  Having bandwidth $O(k)$ is equivalent to being a subgraph of $K_{O(k)}\boxtimes P$.  (David Wood pointed out the connection between $K_x\boxtimes P$ and bandwidth.)~~

~~The second conjecture is still open for all $d\ge 2$.  The argument for $d=1$ has a Yao graph flavour to it, which suggests we may be able to show that for every $k$-nearest neighbour graph $G$ of points in $\R^d$,  $G\subseteq K_{f(k,d)}\boxtimes P^{f(k,d)}$.~~  

The second conjecture is not true, even when $d=2$ and $k=1$. $K\subseteq P^{\|K\|}$, so $K\boxtimes P^{d}\subseteq P^{d+\|K\|}$.  The complete binary tree of height $h$ is a $1$-nearest neighbour graph of points in $\R^2$.  The growth rate of $K\boxtimes P^d$ is $r^{O(d)}$, but the growth rate of a complete binary tree is $2^{\Theta(r)}$.  The Krauthgamer and Lee result really does characterize subgraphs of $P^d$ (and hence $K\boxtimes P^d$) in terms of polynomial growth rate.  The main distinction is that some classes of dimension $\sigma$ (e.g., minor-closed) are subgraphs of $P^{O(\sigma)}$ while the general result only shows that they are subgraphs of $P^{O(\sigma\log\sigma)}$.



## The structure of $k$-quasiplanar graphs

A topological graph is $k$-quasiplanar if it contains no $k$-tuple of pairwise crossing edges.  An old conjecture states that, for every $k$, there exists a constant $c_k$ such that every $n$-vertex $k$-quasiplanar graph has at most $c_k n$ edges.   This is known to be true for $k\in\lbrace 3, 4\rbrace$.  (See [Suk](https://arxiv.org/pdf/1106.0958.pdf) for the $k=4$ case and [Ackerman and Tardos](https://www.sciencedirect.com/science/article/pii/S0097316506001397) for a nice proof of the $k=3$ case.)

We can't hope to have a product structure theorem even for $3$-quasiplanar graphs because a grid plus an apex vertex has diameter 2, treewidth $\Omega(\sqrt{n})$ and is 3-quasiplanar.  Still, I would like to know if some of the applications like queue-number and non-repetitive colouring still work for 3-quasiplanar.  The idea would be to identify a set of *exceptional vertices* that we can remove to get an $f(k)$-planar graph, solve the problem on the planar graph and then deal with these exceptional vertices separately.  

**Update (from David Wood):** 3-quasiplanar graphs include all thickness 2 graphs, which include 1-subdivisions of all complete graphs. So 3-quasiplanar graphs have unbounded queue-number and unbounded nonrepetitive chromatic number. In the language of Nesetril and Ossona de Mendez, they are somewhere dense. This is part of the reason why the conjecture that k-quasiplanar graphs have bounded average degree is so hard.

In light of the preceding update, this seems like a fruitless pursuit.  Also, the [disk intersection graph G described here](#the-structure-of-disk-graphs-of-bounded-ply) is $3$-quasiplanar. (It probably has unbounded queue number.)


## The structure of graphs with (hereditary) linear crossing numbers

$\DeclareMathOperator{\cr}{cr}$
For a drawing $\Gamma(G)$ of a graph $G$, let $\cr(\Gamma(G))$ denote the number of crossings in the drawing $\Gamma$.  (The number of triples $(e_1,e_2,p)\in E(G)\times E(G)\times\R^2$ such that the drawing of $e_1$ and $e_2$ each contain the point $p$.)  Call a graph drawing $G$ *$c$-good* if, for every $S\subseteq V(G)$, $\cr(\Gamma(G[S]))\le c\cdot|S|$.  Say that $G$ is *$c$-good* if there exists a $c$-good drawing of $G$.

<div class="conjecture">
  There exists $f:\N\to\N$ such that, for any $c$-good graph $G$, there exists a graph $H$ with $\tw(H)\le f(c)$ and a path $P$ such that $G$ is isomorphic to a subgraph of $H\boxtimes P$.
</div>

I thought we could weaken this conjecture to drawings with the following property: Each crossing $(e_1,e_2,p)$ can be charged to one of $e_1$ or $e_2$ in such a way that each edge of $G$ is assigned at most $k$ crossings.  However, David Wood points out that the ability to direct crossings in this way already has a name: [$k$-gap planarity](https://www.sciencedirect.com/science/article/abs/pii/S0304397518303670), and is equivalent to the statement ``every subgraph of the crossing graph has degree at most $2k$.'' So this version is equivalent (up to a factor of 2) to the definition of $k$-good.  This is all explained in Footnote 6 in [this paper](https://arxiv.org/pdf/2009.12989.pdf).

## The structure of sparse hereditary graph families

<!-- A graph class $\mathcal{G}$ is *subgraph-hereditary* if, for every $G\in\mathcal{G}$ and every subgraph $G'$ of $G$, $\mathcal{G}$ contains a graph isomorphic to $G'$.  A graph class $\mathcal{G}$ is *small* if, for every $n\in \N$, $G$ contains at most $2^O(n\log n)$ $n$-vertex graphs. -->

<div class="conjecture">
  Let $\mathcal{G}$ be a family of graphs that is closed under taking subgraphs and such that, for each $n\in\N$ there the number of labelled $n$-vertex members of $\mathcal{G}$ is $n!2^{O(n)}$.  Then, for every $n$-vertex graph $G\in\mathcal{G}$, there is a graph $H$ of bounded treewidth and a path $P$ such that $G$ is isomorphic to a subgraph of $H\boxtimes P$.
</div>

The planar product structure theorem is evidence for this conjecture, since planarity is preserved when taking subgraphs and there are only $n!2^{O(n)}$ $n$-vertex planar graphs.

**Note:** Labelled graphs may not be the right thing to count here. Perhaps unlabelled graphs would be more appropriate.

This is closely related to the [implicit graph conjecture](https://en.wikipedia.org/wiki/Implicit_graph#The_implicit_graph_conjecture).  The main difference is that we consider a family of graphs that is closed under taking subgraphs, not just induced subgraphs.  This, combined with upper bound on the number of $n$-vertex graphs implies that $n$-vertex graphs in the family have $O(n)$ edges.  Of course, this is a necessary condition for $G$ to be a subgraph of $H\boxtimes P$ since any $n$-vertex subgraph of $H\boxtimes P$ has only $O(n)$ edges.

**Update:** David Wood points out that the class of apex graphs is closed under taking subgraphs, has the right number of $n$-vertex members.  It also has no product structure theorem because it contains diameter-$2$ treewidth-$\Omega(\sqrt{n})$ graphs, so it's a counterexample.  

<!-- A first step in proving this conjecture would be to establish a relationship between strongly sublinear separators and such a graph family $\mathcal{G}$.  A fairly straightforward divide-and-conquer counting argument shows that a graph family $\mathcal{G}$ having strongly sublinear *edge* separators contains only $n!2^{O(n)}$ graphs of size $n$.

More importantly, suppose that some graph $G$ has a bipartite subgraph $(A,B,E)$ with $\|A\|=R$, $\|B\|=r$ and such that $A$ contains no twins.  Then, for any $x\in\lbrace 1,\ldots,R\rbrace$,  $G$ contains $\binom{R}{x}$ distinct subgraphs of size $x+r$.  For $R\gg r$ this is a contradiction since $\binom{R}{x} > (r+x)!2^{O(r+x)}$.  (It's certainly a contradiction for $R> r^{1+\epsilon}$.)  So this means that $G$ does not have twin-free "concentrators" -->



## The structure of outerplanar graphs

We can prove a baby product structure theorem for outerplanar graphs.  For a rooted ordered tree $T$, let $T^+$ be the graph obtained from $T$ by adding, for each node $v$ of $T$ a path that contains the children of $v$ in order.  Then, for every outerplanar graph $G$, there exists a tree $T$ such that $G$ is a subgraph of $T^+\boxtimes K_2$.  So $G$ is contained in the strong product of a graph tree-like thing and a single edge.  

**Update (Feb 2021):** I don't think the preceding paragraph is correct.  

I don't know of any applications of this result, but there must be some that generalize results for trees to outerplanar graphs.  A good first problem to consider is nonrepetitive colouring of outerplanar graphs.  The best bound is $12=4\times 3$ where the $3$ comes from non-repetitively colouring each BFS layer (a set of disjoint paths) and $4$ comes from a nonrepetitive palindrome-free colouring of the BFS layers themselves.

Another possibility to consider is anagram-free colouring. David and a student showed that every tree $T$ has an anagram-free colouring using at most $4\pw(T)$ colours.  Can we extend this to show that every outerplanar graph $G$ has an anagram-free colouring using $O(\pw(G))$ colours?  Probably not, because even $P\boxtimes K_2$ does not have bounded anagraph-free chromatic number ([Carmi, Dujmović, Morin](https://arxiv.org/pdf/1802.01646.pdf)).

<!-- ## The structure of simple $t$-trees

The preceding section mentions the result that every outerplanar graph is a subgraph of $T^+\boxtimes K_2$ where $T^+$ is "almost a tree".  This raises the following conjecture that I have spent no time thinking about:

**Conjecture:** Every simple $t$-tree $G$ is a subgraph of $H\boxtimes Q$ where $Q$ has constant size and $H$ is "almost a $(t-1)$-tree".

If I had to guess, I would say that the right definition of "almost a $(t-1)$-tree" is the following:  Start with a tree $T$ and, for each node $v$, add any set of edges to the children of $v$ so that you obtain a simple $(t-1)$-tree.


Of course, that conjecture is deliberately vague.   -->

## The structure of trees and $t$-trees

Is it true that every $n$-vertex tree $T$ is a subgraph of $H\boxtimes P$ where $\pw(H)\in O(\log n/\log\log n)$ and $P$ is a path?

Is it true that every $n$-vertex $t$-tree $G$ is a subgraph of $H\boxtimes P$ where $\pw(H)\in O(\log n/\log^{(t+1)} n)$?

These two questions are motivated by our [work vertex-ranking](https://arxiv.org/abs/2007.06455).

**Update:** The answer is no.  If $T$ is a complete binary tree of height $h$ and $T$ is a subgraph of $H\boxtimes P$, then $H$ contains a subdivision of a complete binary tree of height $\Omega(h)$.  It's a boring packing argument that projects $T$ onto $H$ and starts with: "Consider the $2^c$ depth $c$ nodes of $T$.  They project onto at least $2^c/c$ distinct nodes of $H$ and if $2^c/c \ge 3$, then at least one of those nodes is different from the projection of the root of $T$ onto $H$."  So $H$ contains at least:
1. the projection of the root of $T$
2. 2 paths of length at most c from the root to two distinct nodes.

And now continue like that while working out boring details....



# Layered Partitions versus Layered Decompositions

**Update:** We explored this topic and wrote [a paper](https://arxiv.org/abs/2105.01230) about it.

<!-- A graph $G$ has [*layered treewidth*](https://arxiv.org/pdf/1306.1595.pdf) at most $w$ if there exists a layering $\mathcal{L}$ of $G$ and a tree decomposition $(B_x:x\in V(T))$ of $G$ such that $\max\lbrace\|L\cap B_x\|\rbrace\le w$.  Layered treewidth was introduced before layered $H$-partitions and was used to solve many of the same problems but with worse bounds.  It's worth knowing whether or not the property of bounded layered treewidth is really different from the property of being a subgraph of $H\boxtimes P$ for some graph $H$ is bounded treewidth.

This is a topic I want to explore with Mehrnoosh. David, Jit, Vida, and I have been thinking about it for a while.


## Minor-closed graph classes

For minor-closed graph classes, the two properties are the same: A minor-closed graph family has bounded layered treewidth if an only if it excludes an apex graph as a minor.  This is exactly the same condition that characterizes minor-closed graph families with product structure theorems.  

## General graph classes

It's trivial to see that, if $G\subseteq H\boxtimes P$, then $G$ has layered treewidth at most $\tw(H)$: Use the tree decomposition of $H$ and replace each vertex of each bag with the part of $\mathcal{P}$ that it represents.  However, the converse is probably not true.  For every $t>0$, there exists a graph $G$ of layered treewidth 1 but $G$ is not a subgraph of $H\boxtimes P$ for any $H$ of treewidth less than $k$.  

There are some indirect ways to prove this (through other weird graph colouring parameters) but I think it can be proven directly by showing that there are large treewidth graphs whose subdivisions have bounded layered treewidth but do not have product structure.  This sidesteps the minor-closed issue described above since this gives graph families in which the subdivided graph $G'$ is a member, but the original graph $G$ is not, so these families are not minor-closed.

## Specialization to pathwidth

The same problem can be considered in the setting of pathwidth.  In this setting, trees are already problematic.  Any tree has bounded layered pathwidth: Use the standard path decomposition of the tree where the root appears in every bag and use a BFS layering from the root.   For product structure, this doesn't work.

## When are partitions and decompositions the same?

The examples of graphs that have small layered treewidth/pathwidth but do not have product structure theorems all have large expansion.  That is, there are balls of radius $r$ that contain $c^r$ vertices, for some $c>1$.  Is this necessarily the case?  Does every graph family with bounded layered treewidth/pathwidth and polynomial expansion have a treewidth/pathwidth product structure theorem?  The original product structure theorem paper settles the treewidth version of this question for minor-closed graph families (Theorem 32).  Our paper on minor-closed families with bounded layered pathwidth settles this question for minor-closed graph families. -->

# Applications
