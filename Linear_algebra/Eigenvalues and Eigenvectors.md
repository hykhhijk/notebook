# 4.1 Eigenvectors and eigenvalues 
## Eigenvector
- [n*n]행렬 A와 scalar$\lambda$에 대하여 $Ax=\lambda x$를 만족하는 벡터 $\bf{x}$를 A의 eigenvector라고 한다.
- 또한 scalar$\lambda$는 A의 eigenvalue라 칭한다.  
- x를 $\lambda$에 corresponding한 eigenvector로 칭한다.  
- 여기서 x는 nonzero,  $\lambda$는 scalar여야한다. 즉 $Ax=\lambda x$는 nontrivial solution을 가진다.

$\lambda=0$이 가능한데 이때 위 식은 다음과 같이 변하고$A\bf{x}=0$ eigenvector는 nonzero이다.

## Eigenspace  
$\lambda$는 $(A-\lambda I)x=0$이 nontrivial solution을 가질때 A의 eigenvalue가 될 수 있다.  
$A-\lambda I$의 null space는 $\lambda$에 대한 A의 Eigenspace이다.

## Theorem 1.
Triangular matrix의 eigenvalue들은 주대각 원소들과 같다.  
triangle일때는 각 주대각 원소-$\lambda$=0이 free variable을 만드는 즉 null space의 존재조건이기 때문


## Theorem 2.
$v_1,..., v_n$이 eigenvalues $\lambda_ 1,..., \lambda_ n$에 correspond 할때  
set$\{v_1,..., v_n\}$는 linearly independent하다.  

$Ax=\lambda x$에서 좌항은 $\lambda_ 1,..., \lambda_ n$만큼 벡터가 scaining되고 우항은 특정 $\lambda_p$만큼 scaining되는데 이 둘이 동일하려면 trivial solution을 가져야한다.  

# 4.2 The Characteristic Equation
특정 방정식이라 하는 얜데 이건 $\lambda$가 [n*n]행렬 A의 eigenvalue 되기 위해 만족해야하는 식이다.  
$$det(A-\lambda I) = 0$$   
[n*n]행렬을 기준으로 n차 방정식을 푸는것과 유사하며 $(x_{11}-\lambda)...(x_{nn}-\lambda)$ 처럼 주대각-λ를 구하면 된다.

## Similarity
A와 B모두 [n*n]형태의 행렬일때 아래의 조건을 만족하면 A is similar to B  
$P^{-1}AP = B$를 만족하는 invertible matrix가 있을때 즉, $A=PBP^{-1}$이 존재할때

## Theorem 3.  
행렬 A와 B가 similar하다면 그 둘은 똑같은 characteristic polynomial을 가졌다. 즉, 같은 eigenvalue를 가진다.


# 4.3 Diagonalization  
행렬 A가 diagonal matrix와 similar하다면 즉 $A=PDP^{-1}$이라면 A는 diagonalizable하다.  

이걸 어따 써먹냐면 
- $A=PDP^{-1}$
- $A^2=PD(P^{-1}P)DP^{-1}$
-  $A^2=PD^2P^{-1}$ 

즉 $A^k=PD^kP^{-1}$ 

## Theorem 4. The Diagonalization Theorem
[n*n]행렬 A가 n개의 선형독립 eigenvector를 가지고 있다면 diagonalizable하다.  
$A=PDP^{-1}$에서 P는 eigenvector n개의 집합이며 대각행렬 D는 그 eigenvector들에 correspond한 eigenvalue들이다.

$A=PDP^{-1}$이걸 $AP=PD$이렇게 생각할 수 있는데  
이때 $Av_1 = \lambda_1v_1 ... Av_n = \lambda_nv_n$ 으로 볼 수 있다.  
따라서 D는 A의 선형 독립인 eigenvector의 집합이다.

## How to Diagonalization$
1. eigenvalue를 찾는다
2. 각 eigenspace의 basis를 찾는다
3. n개의 independent eigenvector인지 확인한다
4. P와 D를 만든다

1은 $det(A-\lambda I) = 0$을 만족하는 eigenvalue를 찾는 polynomial을 푸는것이고  
2는 A에 eigenvalue를 넣어 eigenvector들을 찾는다.  
이후 eigenvalue와 eigenvector수가 맞는지 independent인지 체크하고 P와 D를 만들면 끝! 

## Theorem 5.
[n*n]행렬은 n 개의 다른 eigenvalue를 가지고 있다면 diagonalizable하다.  

## Theorem 6.
[n*n]행렬의 eigenvalue들 $\lambda_1, \lambda_2..., \lambda_p$가 있을때 모든 eigenvalue에 대응하는 eigenvector들은 그 eigenvalue의 multiplicity와 동일하다.  

한마디로 eigenvalue's multiplicity = dimension of eigenspace

# 4.4 Eigenvectors and Linear Transformation




# 4.5 Complex Eigenvalues  
실수에서 허수공간으로 확장하는 파트인데 강의 봐도 모르는건 빠른 컷