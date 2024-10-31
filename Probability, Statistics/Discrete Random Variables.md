### Random variable notation
X의 Range: $\text{Range}(X) \text{ or } R_X$  

### PMF notation
$P_X(x) = P(X = x), \quad x \in R_X$


### Bernoulli Distribution
$X \sim \text{Bernoulli}(p)$
$$P_X(x) = \begin{cases} 
p, & x = 1 \\ 
1 - p, & x = 0 \\ 
0, & \text{otherwise} 
\end{cases}
$$

### Geometric Distribution
$X \sim \text{Geometric}(p)$
$$P_X(i) = \begin{cases} 
p(1 - p)^{i - 1}, & i = 1, 2, \dots \\ 
0, & \text{otherwise} 
\end{cases}
$$

### Binomial Distribution
$X \sim \text{Binomial}(n, p)$
$$P_X(i) = \begin{cases} 
\binom{n}{i} p^i (1 - p)^{n - i}, & i = 0, 1, \dots, n \\ 
0, & \text{otherwise} 
\end{cases}
$$

### Pascal Distribution
$X \sim \text{Pascal}(m, p)$
$$P_X(i) = \begin{cases} 
\binom{i - 1}{m - 1} p^m (1 - p)^{i - m}, & i = m, m + 1, \dots \\ 
0, & \text{otherwise} 
\end{cases}
$$

### Hypergeometric Distribution
$X \sim \text{Hypergeometric}(b, r, n)$
$$P_X(i) = \begin{cases} 
\frac{\binom{b}{i} \binom{r}{n - i}}{\binom{b + r}{n}}, & i \in R_X \\ 
0, & \text{otherwise} 
\end{cases}
$$

### Poisson Distribution
$X \sim \text{Poisson}(\lambda)$, n>50 이거나 np<5일때 주로 사용한다.
$$P_X(i) = \begin{cases} 
\frac{e^{-\lambda} \lambda^i}{i!}, & i = 0, 1, 2, \dots \\ 
0, & \text{otherwise} 
\end{cases}
$$

### CDF Definition
$F_X(x) = P(X \leq x), \text{ for all } x \in \mathbb{R}.$

### Expected value
$E[X] = \sum_{x_k \in R_X} x_k P(X = x_k)$ 즉 $x_k P_X(x_k)$

### PMF들의 E[X]
**Bernoulli(p): p,  Geometric(p): $\frac{1}{p}$,  Poisson(λ): $\lambda e^{-\lambda} e^{\lambda}$**  
**Binomial(n, p): $np$, Pascal(m, p): $\frac{m}{p}$, Hypergeometric(b, r, n): $np$**

### Variance
$$\text{Var}(X) = E\left[ (X - \mu_X)^2 \right]$$
$$\text{Var}(X) = E[X^2] - \mu_X^2$$

### Standard deviation
$$\sigma_X = \sqrt{\text{Var}(X)}$$

### PMF들의 Var(X)
**Bernoulli(p): $p(1-p)$,  Geometric(p): $\frac{1-p}{p^2}$,  Poisson(λ): $\lambda$**  
**Binomial(n, p): $np(1-p)$, Pascal(m, p): $m\frac{1-p}{p^2}$, Hypergeometric(b, r, n): $np(1 - p) \left(1 - \frac{n - 1}{b + r - 1}\right)$**

### Composite function  
$$\text{define } Y = g(X) = g \circ X : S \to \mathbb{R}$$  
$$ R_Y = \{ g(x) \mid x \in R_X \}$$

### Law of the Unconsciout Statistician(LOTUS)
$E[Y] = E[g(X)] = \sum_{x_k \in R_X} g(x_k) P_X(x_k)$, P(x_k)의 확률을 그대로 가져가면서 x_k만 변경함
