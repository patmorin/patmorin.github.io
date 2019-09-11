---
layout: problem
title:  "Layered Pathwidth and Non-Repetitive Chromatic Number"
date:   2017-07-14
permalink: lpw-vs-nrcn.html
categories: openproblem
---
$\DeclareMathOperator{\lpw}{lpw}\DeclareMathOperator{\ltw}{ltw}\DeclareMathOperator{\pw}{pw}$

This is a problem given to me by Vida Dujmović, that might be suitable to work on with our student Celine Yelle.

For a graph $G$, let $\lpw(G)$, $\ltw(G)$, and $\pi(G)$ denote the layered pathwidth, layered treewidth, and non-repetitive chromatic number of $G$, respectively.

<div class="problem">
  Does there exist some $f:\N\to\N$ such that, for all graphs $G$, $\pi(G)\le f(\lpw(G))$?
</div>

[Dujmovic et al][dujmovic-ea] show that $\pi(G) \le \ltw(G)\cdot\log n$ for all $n$-vertex graphs $G$.

# David's Exercise


The following is all wrong. The problem is that, if the top-left vertex is adjacent to everything in row 2, then in the lower-right $n/2\times n/2$ grid, the two layerings coincide so we really only have one layering.


David asked about the following family $\mathcal{F}=\bigcup_{r\in\N}\mathcal{F}_r$ of planar graphs, which has layered pathwidth $O(1)$. For any $r\in\N$, let $[r]=\lbrace 0,\ldots,r-1\rbrace$.  For every graph $G\in\mathcal{F}_r$, the vertex set is $V_r=[r]^2$. For every $G\in\mathcal{F}_r$, the *horizontal edges* $\lbrace (a,b)(a+1,b):a\in[r-1],\,b\in[r]\rbrace$ are present. In addition to these edges, any maximal subset of the edges in $\lbrace(a,b)(a',b+1):a,a'\in[r],\, b\in[r-1]\rbrace$ is present subject to the graph having a non-crossing straight-line planar drawing with each vertex $(a,b)$ drawn at position $(a,b)$. In other words, $G$ is obtained from the $r\times r$ square grid by deleting the internal vertical edges and triangulating all of the resulting internal faces (each of which is a $r\times 2$ rectangle with $2r$ vertices on its boundary).  

For each $G\in\mathcal{F}_i$, we call $Y_i=\lbrace (a,i): a\in[r]\rbrace$ the $i$th *row* of $G$ and $X_i=\lbrace (i,b):i\in[r]\rbrace$ the $i$th *column* of $G$. Observe that $Y_1,\ldots,Y_r$ is a layering of $G$, but $X_1,\ldots,X_r$ is not.

We now define a nonrepetitive 64-colouring of $G$.  Consider the layering $G_0,\ldots,G_{r-1}$ where $G_i$ contains all vertices at distance $i$ from $\lbrace (1,1),\ldots,(1,r)\rbrace$. In other words, for every vertex $v\in G_i$, the shortest path from $v$ to the leftmost column $X_0$ has length $i$.  (Note that we could have been define $Y_i$ similarly; for every $v\in R_i$, the shortest path from $v$ to the topmost row $R_0$ has length $i$). We call $G_i$ the $i$th *group* of $G$. For any vertex $v=(a,b)$ of $G$, let $x(v)=a$ and $y(v)=b$ and $g(v)$ denote the unique index $i$ such that $v\in G_i$.  So, $v\in X_{x(v)}\cap Y_{y(v)}\cap G_{g(v)}$.

Observe that, for each row $Y_t$, the function $f_t(x)=g((x,i))$ is a non-decreasing function of $x$.  In particular, for any $x_1<x_2$, if $q=g((x_1,i))=g((x_2,i))$ then $g(x,i)=q$ for all $x\in\lbrace x_1,\ldots,x_2\rbrace$.

Now, consider some nonrepetitive anagram-free string $s_0,\ldots,s_{r-1}$ over the alphabet $[4]$.  We colour each vertex $v=(a,b)\in G$ with the product colour $\varphi(v)=(s_{x(v)},s_{y(v)},s_{g(v)})$.   This obviously uses only 64 colours.  This is also obviously a proper colouring since if some edge $vw$ is horizontal then $s_{x(v)}\ne s_{x(w)}$, otherwise $s_{y(v)}\neq s_{y(w)}$.  

Recall the lemma in Kundgen and Pelsmajer which states that, for any walk $w_0,\ldots,w_{2k-1}$ over the path $0,\ldots,r-1$, the string $s_{w_0},\ldots,w_{w_{2k-1}}$ is a repetition if and only if $w_0,\ldots,w_{2k-1}$ is a repetition.

Now, suppose $P=v_0,\ldots,v_{2k-1}$ is a path in $G$.  For each $i\in[2k]$ let $v_i=(x_i,y_i)$ and $g_i=g(v_i)$.  Suppose $P$ is repetitively coloured. Then, since each row $Y_i$ of $G$ is nonrepetitively coloured, we know that $P$ contains vertices from at least two different rows.  

Note that $y_0,\ldots,y_{2k-1}$ and $g_0,\ldots,g_{2k-1}$ are each walks over the path $0,\ldots,r-1$.  Therefore, by the Kundgen-Pelsmajer Lemma, for every $i\in[k]$,  $y_i=y_{k+i}$ and $g_i=g_{k+i}$.  That is, $v_i$ and $v_{k+i}$ are in the same row and within that row, they are in the same group.


<div class="lemma">
  For every $t\in[r]$ and every $i_1,i_2\in\lbrace i : y_i = t\rbrace$,
  $g_{i_1}=g_{i_2}$.
</div>

<div class="proof" markdown="1">
  This should follow from the planarity of $G$, so that $P$ is an open meander with respect to the line $y=t$ along with the fact that $f_t(x)$ is monotone.
</div>

Then I think we're almost done.



# Bounded Pathwidth: A Warm-Up

I have some hope that the following proof can generalize to layered pathwidth.

<div class="theorem">
  For any graph $G$ with $\pw(G)\le k$, $\pi(G)\le 4k^2$.
</div>

<div class="proof" markdown="1">
   Consider some path decomposition $B=B_1,\ldots,B_r$ of $G$ of width $k$ and assume that no two bags in this decomposition are identical.  We do a 2-part product colouring. The first-part is the standard $k$-colouring of $G$ in which two vertices receive different colours if they appear in the same bag.  The second part is a $4k$-colouring that we now define.

   Define groups of vertices $V_1,\ldots,V_r$ of $G$ as follows.  Let $B^1=B$. Consider the largest index $i_1$ such that some vertex $v\in B_1$ is also in $B_{i_1}$.  We let $V_1=B_{i_1}$ and let $B^2=B_1\setminus V_1,\ldots,B_m\setminus V_1$ and then proceed inductively on $B^2$ starting at $i_1+1$, i.e., we find the largest index $i_2$ such that a vertex $v\in B^2_{i_1+1}$ appears in $B^2_{i_2}$, set $V_2=B^2_{i_2}$, and so on.

   This process completes after $t$ steps, once $i_t=r$.  At this point $B^t$ defines $r-1$ disjoint subgraphs $G_1,\ldots,G_{t-1}$, where $G_j$ is the subgraph of $G$ induced by the union of all vertices in $B^t_{i_j+1},\ldots,B^t_{i_{j+1}-1}$ [TODO: Off-by-one error here.].  Note that each such $G_j$ has pathwidth at most $k-1$.

   For the second part of our colouring, we let $s_1,\ldots,s_t$ be a palindrome-free non-repetitive string on 4 symbols and we colour all elements in $V_i$ with colour $s_i$.  We then inductively colour each graph $G_1,\ldots,G_{t-1}$ using new colours, for a total of $4k$ colours.  Thus, our product colouring uses $4k^2$ colours.

   To see why this colouring is non-repetitive, consider some path $P=v_1,\ldots,v_{2r}$. If $P$ does not use any vertices in $V_1,\ldots,V_t$, then we can apply induction on $k$.  If $P$ does use vertices in $V_1,\ldots,V_t$ recall that this means that, if $v_i\in V_j$ for $i<r$, then $v_{r-1+i}\in V_j$ (this is a Lemma of [Kundgen and Pelsmajer][kundgen-pelsmajer]).  But this is a contradiction since all vertices in $V_j$ appear in a common bag and therefore $v_i$ and $v_{r+i-1}$ receive different colours in the first part of the colouring.
</div>

Note that the choice of $i_1,i_2,\ldots,i_t$ is not unique in this proof.  In particular, we could have chosen $i_1$ to be any smaller value as long as $B_{i_1}$ and $B_{i_2}$ have no vertices in common.

# A Lemma (Broken)

Here we establish a lemma that should make it possible to use an entropy-encoding argument to prove our result.

Let $k=\lpw(G)$  Consider some layered path decomposition $(\mathcal{B},\mathcal{L})$ of $G$ having width $k$.  For any vertex $v\in V(G)$, let $i(v)=i(v,\mathcal{B})=\min\lbrace i:v\in B_i\rbrace$. Without loss of generality, assume that for any two distinct vertices $v,w\in V(G)$, $i(v)\neq i(w)$.  Let $\prec$ denote the total order on $V(G)$ in which $v\prec w$ if and only if $i(v) < i(w)$.

Let $\varphi:V(G)\to\lbrace 1,\ldots,k\rbrace$ be a colouring of $G$ that assigns distinct colours to any two vertices $v,w\in V(G)$ such that $L[v]=L[w]$ and $B[v]\cap B[w]\neq\emptyset$.  This colouring can be obtained by $k$-colouring $G[L_i]$ for each $i\in\N$, which is possible since $G[L_i]$ has pathwidth $k$.

For a path $P=v_0,\ldots,v_\ell$ in $G$, the *trace* $T(P)$ of $P$ is a sequence of $\ell$ triples
$T(P)=t_1,\ldots,t_\ell$, where each $t_i=(h_i,v_i,\varphi_i)$ defined as follows:
\\[
   h_i = \begin{cases}
     -1 & \text{if $v_i\prec v_{i-1}$} \newline
     +1 & \text{otherwise}
   \end{cases}i
\\]
\\[
   v_i = \begin{cases}
     -1 & \text{if $L[v_i]< v_{i-1}$} \newline
     0 & \text{if $L[v_i]= v_{i-1}$} \newline
     +1 & \text{otherwise}
   \end{cases}
\\]
\\[
      \varphi_i = \varphi(v_i) \enspace .
\\]
Intuitively, $h_i$ and $v_i$ describe the step from $v_{i-1}$ to $v_i$, where $h_i$ tells us whether the step goes left or right and $v_i$ describes whether the step goes up, down, or stays at the same layer.

<div class="lemma">
   Let $v$ be any vertex of $G$ and let $t_1,\ldots,t_\ell$ be a trace, and let $\mathcal{P}$ be the set of all paths $P$ in $G$ whose first vertex is $v$ and whose trace is $t(P)=t_1,\ldots,t_\ell$.  Then the union of all edges in $P$ is a tree.
</div>

<div class="proof" markdown="1">
   Let $v=x_0,x_1,\ldots,x_\ell$ and $v=y_0,y_1,\ldots,y_\ell$ be any two paths in $\mathcal{P}$.
   It is sufficient to show that, for all $j\in\lbrace 1,\ldots,\ell\rbrace$, if $x_{j-1}\neq y_{j-1}$, then $x_j\neq y_j$.  To see this, assume without loss of generality that $x_{j-1}\prec y_{j-1}$, and that $h_j=+1$.  Let $x=x_{j-1}$, $y=y_{j-1}$ and assume, for the sake of contradiction that $z=x_j=y_j$.  

   By direct assumption $x\prec y$ and by the assumption that $h_j=+1$, $y\prec z$ so by transitivity $x\prec y\prec z$.  In particular, this implies that $B_{i(z)}$ contains $x$, $y$, and $z$.
   However, $L[x]=L[y]=L[v]+\sum_{\tau=1}^{j-1} v_\tau$ and $\varphi(x)=\varphi(y)=\varphi_i$.  But this is a contradiction since the colouring $\varphi$ would not assign the same colour to $x$ and $y$.
</div>

Let $v\in V(G)$ be any vertex of $G$ and let $T=t_1,\ldots,t_{2\ell-1}$ be a trace.  We say that $T$ is *repetitive for $v$* if,

1. $\varphi(v)=\varphi_{\ell}$;
2. for every $j\in\lbrace 1,\ldots,\ell-1\rbrace $, $h_j=h_\ell+j$ and $v_j=v_{\ell+j}$; and
3. $\sum_{\tau=1}^\ell v_\tau = 0$.

The following lemma is FALSE:
<div class="lemma">
  Let $v\in V(G)$ be any vertex of $G$, let $T=t_1,\ldots,t_{2\ell-1}$ be any trace that is repetitive for $v$, and let $\mathcal{P}$ be the set of all paths that begin at $v$ and that have trace $T$.  Then $|\mathcal{P}|=O(\ell k^\ell)$.
</div>


[dujmovic-ea]:http://www.combinatorics.org/ojs/index.php/eljc/article/view/v20i1p51
[kundgen-pelsmajer]:https://www.sciencedirect.com/science/article/pii/S0012365X0700667X?via%3Dihub
