# 3.1 Introduction to Determinant

$n\geq{2}$ 이상일때 [n*n]행렬 $A_{ij}$의 행렬식은 $\pm{a}_{1j} * detA_{1j}$와 같다.  
즉 첫번째 행에서 $a_{11},a_{12},...a_{1n}$에 위의 연산을 연산을 반복하면 A의 determinant 구할 수 있다.  
($detA_{ij}$: 행렬 A에서 i행, j열을 제외하고 계산한 행렬식)  

$detA = a_{11}detA_{11} - a_{12}detA_{12} ... +(-1)^{n+1}a_{1n}detA_{1n}$  
$= \sum_{j=1}^{n} (-1)^{1+j}a_{1j}detA_{1j}$

Cofactor: 위의 연산에서 Cofactor $C_{ij}$는 $(-1)^{i+j}detA_{ij}$이다.(det를 쉽게 표기하는 방식이라 보면 된다)  
즉 $det A = "a_{11}detA_{11} - a_{12}detA_{12}+ ... +(-1)^{n+1} a_{1n}detA_{1n}"$은  
$"a_{11}C_{11} + a_{12}C_{12} +... + a_{1n}C_{1n}"$처럼 표현할 수 있다.

## Theorem 1  
[n*n]행렬의 행렬식은 어떠한 행이나 열의 cofactor expansion으로도 구할 수 있다.  
- 위와 같이 1번행이 아니라 어떠한 행에 cofactor expansion을 취해도 결과는 동일하다.  
$det A = a_{i1}detA_{i1} + a_{i2}detA_{i2} ... a_{in}detA_{in}$  
- 아래와 같이 특정 열에 취해도 결과는 동일하다.  
$det A = a_{1j}detA_{1j} + a_{2j}detA_{2j} ... a_{nj}detA_{nj}$   


## Theorem 2  
행렬 A가 triangular matrix일때 $det A$는 A의 주대각 원소의 곱이다.  
$\because$replacement는 det에 영향 x-> reduced echlon은 주대각 빼고 전부 0


# Properties of Determinants
## Theorem 3
정방행렬 A에 한번의 행연산(scailing, replacement, interchange)을 하여 행렬 B를 만든다고 생각해보자  
- Scailing: $detB = k\cdot detA$
- Replacement: $detB = detA$
- Interchange: $detB = -detA$  

이는 $detEA = (detE)(detA)$이기 때문이다.

## Theorem 4  
$detA\neq 0$이라면 A는 invertible하다.  

## Theorem 5  
A가 정방행렬일때 $detA^T =detA$  
사이즈가 2일때 $C_{j   , 1} = C_{1, j}$이고 3이상일때도 cofactor expansion으로 전개하면 [2*2]행렬의 집합으로 쪼개지므로   


## Theorem 6. Multiplicative property  
A와 B가 정방행렬일때  
$det AB = (detA)(detB)$  


# Cramer’s Rule, Volume, and Linear Transformations  
$A_i(\bf{b})$: 행렬 A의 i번째 column을 vector $\bf{b}$로 변경한 것이다.  
$$A_i(\bf{b}) = [\bf{a}_1, \bf{a}_2, b, ..., \bf{a}_n]$$    

## Theorem 7 Cramer's Rule  
invertible한 [n*n]행렬 A와 $\mathbb{R}^n$에 속한 b에 대하여 $A\bf{x} = \bf{b}$를 만족하는 unique solution $\bf{x}$의 각 원소는 다음과 같이 구할 수 있다.  
$$\bf{x}_i = \frac{detA_i(\bf{b})}{detA}$$  
x를 구하는게 아니라 x의 각 entry를 구하는 방법임을 주의하자  

1. $AI_i(\bf{x}) = A[e_1, ...,x, ... e_n]$
2. $[Ae_1, ..., Ax, ..., Ae_n]$
3. $[a_1, ..., Ax, ..., a_n]$
4. $A_i(\bf{b})$  

$(detA)(detI_i(\bf{x})) = detA_i(\bf{b})$  
$\therefore \bf{x}_i = \frac{detA_i(\bf{b})}{detA}$  

여기서 $detI_i(\bf{x})$는 $\bf{x}_i$와 같다.(replacement를 이용해 i row 원소만 남기고 나머지 제거)  
![alt text](image/image-5.png)

Using Cramer's Rule to know $A^{-1}$  
- $A\bf{x} = e_j$, $\bf{x} = A^{-1}e_j$ 여기서 x는 $A^{-1}$의 j번째 column임을 알 수 있다.  
- $A^{-1}$의 (i, j) entry = $\bf{x}_i$ = $\frac{detA_i(e_j)}{detA}$, 크래머 법칙을 사용해 $A^{-1}$의 특정 entry를 구할 수 있다.
- $detA_i(e_j) = (-1)^{j+i}detA_{ji} = C_{ji}$ A의 (j, i) enrty는 1, 그 column의 나머지는 0이므로 cofactor expansion이 간략화된다.

$\therefore A^{-1} = \frac{1}{detA}\begin{bmatrix}
 C_{11}&C_{21}  &...  &C_{n1} \\ 
 C_{12}&C_{22}  &  ...&C_{n2} \\ 
 ...&...  &...  &... \\ 
 C_{1n}&C_{2n}  &...  &C_{nn} 
\end{bmatrix}$ 이러한 형태를 classical adjoint of A 혹은 $adjA$로 칭한다.(얼핏 봐도 시간복잡도가 구리고 적용분야도 한정적이라 한다)

## Theorem 8.
정방행렬 A에 대하여  
$A^{-1} = \frac{1}{detA}adjA$  

## Theorem 9.
[2*2]행렬 A에 대하여 A의 column들로 이루어진 평행사변형의 넓이는 $|detA|$이다.  
똑같은 방법으로 평행육면체의 부피도 구할 수 있다.  

ex) $\begin{bmatrix}
2&6 \\
4&3
\end{bmatrix}$ 의 넓이를 구해보자  
replacement는 determinant를 변화시키지 않는데 이를 통해 적당히 바꾸면 $\begin{bmatrix}
2&0 \\
0&-9
\end{bmatrix}$요로코롬 되고 이 두 column으로 만들어진 사각형의 넓이는 18이다.  
처음 $\begin{bmatrix}
2&6 \\
4&3
\end{bmatrix}$행렬의 행렬식 역시 |2*3 - (24)| = 18으로 동일한 것을 알 수 있다.

## Theorem 10.
$\mathbb{R}^2$->$\mathbb{R}^2$로 보내는 행렬 A와 $\mathbb{R}^2$에 평행사변형 S가 있을때  
{area of T(S)} = $|det(A)|\cdot$ {area of S}  
평행사변형과 A 둘다 정방행렬이므로 정리 6($det AB = (detA)(detB)$)이 성립하기때문