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
