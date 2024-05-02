# 1.1 Systems of Linear Equations

선형방정식(Linear equations): $a_1x_1 + a_2x_3 + a_3x_3 + ... + a_nx_n = b$ 형태의 방정식  
A system of linear equations: 이러한 선형방정식의 집합(1개 이상)  

Solution set: linear system의 모든 해를 의미한다.  
두 linear system의 해가 같다면 **equivalent** 하다고 한다

linear system의 해는 총 3가지 경우로 정의가능한데
1. no solution
2. exactly one solution
3. infinetly many solution

1은 inconsistent, 2와3은 consistent하다.

Elementary row operations: 아래 3가지 연산을 통해 A 행렬을 B로 만들 수 있다면 둘을 **row equivalent** 하다고 칭한다.  
1. replacement
2. interchange
3. scailing

# 1.2 Row Reduction and Echelon Forms

Leading entry of row: 특정행에서 제일 왼쪽에 있는 non-zero entry  

Echelon form: 아래 두가지 조건을 만족하는 형태의 행렬을 의미
1. 모든 nonzero 행이 all zero 보다 위에 있으며
2. 각 행의 leading entry가 위쪽행보다 오른쪽에 있어야한다

Reduced echelon form: 위에 2개에 추가적으로 2개 조건을 필요로한다
1. leading entry가 모두 1이여야함
2. 각 leading entry가 행렬의 column의 유일한 nonzero entry이여야함

reduced echelon form의 leading entry위치를 pivot position이라한다.

## Theorem 1 
**Uniquness of the Reduced Echelon Form**  
Each matrix is row equivalent to one and only one reduced echelon matrix.

각 행렬을 reduced echelon form으로 행연산할시 unique하다.

general solution: basic variable과 free variable로 표현된 식 형태를 말한다.  

m * n행렬이 있을때 n이 커질수록 free variable이 많아진다.

## Theorem 2
**Existence and Uniqueness Theorem**  
augmented matrix의 right most column이 nonzero라면 inconsistent하다.  
consistent한 경우에 free V가 있다면 -> infinitely many solution을  
그렇지 않다면 -> unique solution을 가진다.

# 1.3 Vector equations

Linear combination: 아래처럼 보이는 식을 말한다
$$ y = c_1\mathbf{v_1} + c_2\mathbf{v_2} + ... + c_n\mathbf{v_n}$$ 
means linear combination of $\mathbf{v_1}, \mathbf{v_2}, ..., \mathbf{v_n}$ with weights $c_1, c_2, ..., c_p$  
vector equation이라는 표현이 이후 자주 쓰이지는 않는다 Linear combination이 특정 해를 만족하는 solution을 찾는 느낌이고 vector equation은 공간을 표현하는데 더 자주 쓰이는 느낌이다

span: 주어진 벡터를 이용해 만들 수 있는 모든 벡터의 집합

**아래 3개의 식은 모두 같은 의미이다**
1. Is a vector $\mathbf{b}$ in Span $\begin{Bmatrix}
 \mathbf{v_1}&\mathbf{v_2}  &\mathbf{v_3} 
\end{Bmatrix}$

2. Does the following vector equation have a solution?  
$$x_1\mathbf{v_1} + x_2\mathbf{v_2} + x_3\mathbf{v_3} = \mathbf{b}$$

3. Does the following augmented matrix have a solution?
$$\begin{bmatrix}
 \mathbf{v_1}&\mathbf{v_2}  &\mathbf{v_3} &\mathbf{b}  
\end{bmatrix}$$

# 1.4 The matrix equation

$A\mathbf{x}$: 행렬 A와 벡터 x의 곱, 선대에서 가장 흔하게 볼 수 있는 연산 형태이다.  

$$A\mathbf{x} = \begin{bmatrix}
 \mathbf{a_1}&\mathbf{a_2}  &\mathbf{a_3} 
\end{bmatrix} \begin{bmatrix}
x_1\\ 
x_2\\ 
x_3
\end{bmatrix} = x_1\mathbf{a_1} + x_2\mathbf{a_2} + x_3\mathbf{a_3}$$

$\mathbf{a}$가 벡터라는 점을 주의, 위 식은 x를 weight로 가지는 A의 linear combination으로 볼 수 있다.  
**x와 A위치가 바뀌면 안된다!**

위에서 3번 식(Does the following augmented matrix have a solution?)에 있는 augmented matrix 예제는 A가 v를 벡터로 가지는 matrix equation과 같은 form이라고 볼 수 있다. 물론 다른 항목도 비슷하게 생각할 수 있다.
$$\begin{bmatrix}
 \mathbf{v_1}&\mathbf{v_2}  &\mathbf{v_3} &\mathbf{b}  
\end{bmatrix}$$



## Theorem3
위쪽의 리스트에서 행렬식만 추가하면 된다
1. Is a vector $\mathbf{b}$ in Span $\begin{Bmatrix}
 \mathbf{v_1}&\mathbf{v_2}  &\mathbf{v_3} 
\end{Bmatrix}$

2. Does the following vecotr equation have a solution?  
$$x_1\mathbf{v_1} + x_2\mathbf{v_2} + x_3\mathbf{v_3} = \mathbf{b}$$

3. Does the following augmented matrix have a solution?
$$\begin{bmatrix}
 \mathbf{v_1}&\mathbf{v_2}  &\mathbf{v_3} &\mathbf{b}  
\end{bmatrix}$$

4. Does this matrix equation have a solution? 
$$ A\mathbf{x} = \mathbf{b}$$

## Theorem5  
$$A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$$
$$A(c\mathbf{u}) = c(A\mathbf{u})$$
첫번째 식은 두 벡터와 행렬의 연산을 간단히하는데 자주 나오므로 확실히 알고가야한다.  

# 1.6 Linear Independence

$A\bf{x} = 0$을 homogeneous system이라고 한다. 이 식은 무조건 하나 이상의 솔루션(trivial solution)을 가진다.

- 이러한 Linear combination "$x_1\mathbf{v_1} + ... + x_p\mathbf{v_p} = 0$" 을 만족하는 식 중 **trivial solution만**을 가지는 vector set을 linearly independent하다고 말한다.  
trivial solution: all coefficients are 0

- 반대로 "$x_1\mathbf{v_1} + ... + x_p\mathbf{v_p} = 0$" 이 식 에서 $x_1, ..., x_p$가 all zero가 아닌 weights가 있다면 linearly dependent하다.

- vector set이 zero vector가 아닌 하나의 벡터로 구성되어 있다면 선형 독립이다.

- 벡터 방정식에서 하나의 벡터가 다른 벡터의 조합으로 만들어 질 수 있는 경우 **linearly dependent**하다. ->**당연히 한 벡터가 다른 벡터의 multiple이라면 선형 종속이다**

## Theorem 7
두개 이상의 벡터가 선형 종속이라면 적어도 그 set안에 하나의 벡터는 다른 벡터의 선형 결합으로 표현될 수 있다.

$x_1\mathbf{v_1} + ... + x_3\mathbf{v_p} = 0$  
~$-v_1 + ... + c_p\mathbf{v_p} = 0$ 이때 $c_i$가 모두 0일 수 있으므로 vector set에 0벡터가 껴있는 경우 무조건 선형 종속이라는 것도 알 수 있다.

## Theorem 8
벡터 셋이 entry(벡터의 원소 수 = 행)보다 많은 벡터를 가지고 있다면 선형 종속이다.  
![alt text](image-2.png)  

이러한 케이스를 말하는 건데  
- p의 개수에 따라 이 식은 $\mathbb{R}^p$ space를 span 할 수 있을것이다(vector간 multiple이 아니라면), 만약 p의 개수가 n보다 커지게 되면 $\mathbb{R}^n$을 span하게 된다.  
- p의 개수가 n보다 커지면 reduced echelon form으로 만들면 free variable이 존재하게 되며 이는 Ax=0를 만족시킨다(not trivial solution)

## Theorem 9
vector set이 0벡터를 포함하면 무조건 선형 종속이다.

# 1.7 Introduction to Linear Transformation

Transformation: $\mathbb{R}^n$ 을 $\mathbb{R}^m$ 으로 보내는 function $T$

자주 사용하는 식 $A\mathbf{x} = \mathbf{b}$ 를 봤을때 A[m x n], x[n, 1] 일때 b[m, 1]로 바뀐다.(이건 A의 관점이 아니라 x의 관점에서 Transformation이 일어난 것이다)

## Linear transformation
$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$  
$T(c\mathbf{u}) = cT(\mathbf{u})$  
이 두조건을 만족하는 mapping $T$를 Linear transformation이라 한다.(이러한 성질을 **closed under addition and multiplication** 혹은 Linear한 성질을 지녔다고한다.)

# 1.8 The Matrix of a Linear Transformation
항등행렬 표기법: 

$I_2 = \begin{bmatrix}
1 &0 \\ 
 0&1 
\end{bmatrix}$ 의 각 column vector를 $e_1 = \begin{bmatrix}
1\\0 
\end{bmatrix}$ 과 $e_2 = \begin{bmatrix}
0\\1 
\end{bmatrix}$로 표기한다.

## Theorem 10
$T(\mathbf{x}) = A\mathbf{x}$ 는 모든 x에 대해 Unique하다.  

T는 Linear tranformation, A는 m*n 행렬이며 A는 아래와 같이 표현될 수 있다.  
$A = [T(\mathbf{e_1}) ... T(\mathbf{e_n})]$  
Linear transformation T에 대한 standard matrix로 표기한다.

$A\mathbf{x}$ 를 예로 들어 풀어쓰면  
T는 $T = [T(\mathbf{e_1}) ... T(\mathbf{e_n})]$ 형태로 표현할 수 있고 $T\mathbf{(x)}$ 는 $[T(\mathbf{e_1}) ... T(\mathbf{e_n})]x$ 이다.  
그리고 이 결과는 $A\mathbf{x}$와 같다. 즉, Transformation matrix는 identity matrix의 컬럼을 transformation한 벡터를 컬럼으로 사용한다는 뜻이다.

항등행렬의 column은 연산하는 행렬의 특정column으로 transform된다 즉 column을 그대로 유지한다.

onto $\mathbb{R}^m$: $\mathbb{R}^n$ 을 $\mathbb{R}^m$ 으로 보내는 $T$ 가 n차원 x를 m차원 b로 보내는 해가 최소한 하나라도 있는 경우(어떠한 b라도)  
one-to-one: $\mathbb{R}^n$ 을 $\mathbb{R}^m$ 으로 보내는 $T$ 가 n차원 x를 m차원 b로 보내는 해가 단 하나거나 없는 경우  

*one to one의 정의는 정의역, 치역의 원소들이 1:1로 mapping되야 한다. 즉! free variable이 존재하면 이 조건을 무조건 위반하게된다.*

## Theorem 11
$\mathbb{R}^n$ 을 $\mathbb{R}^m$ 으로 보내는 linear formation $T$는 trivial solution을 가질때에 one-to-one이다.

## Theorem 12  
$\mathbb{R}^n$ 을 $\mathbb{R}^m$ 으로 보내는 linear formation $T$ 와 이의 standard matrix A가 있을때

- A의 column이 $\mathbb{R}^m$을 span할때 T는 $\mathbb{R}^n$ onto $\mathbb{R}^m$ 이다.

- 그리고 $T$ 는 A가 선형독립일때 one-to-one이다. (cause only trivial solution)