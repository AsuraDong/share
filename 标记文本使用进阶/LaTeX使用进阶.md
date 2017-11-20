[toc]

## 1. 已支持
- 转义符号`\`：`$ {a,b,c}\neq\{a,b,c\} $`
- 占位符
```math
C_{1} \qquad {C_2}

C_{1} \quad {C_2}

C_{1} \ {C_2} 

```
- 下标
```math
C_{a} + C_{b,c}

C_{1} \ {C_2}

```
- 上标：`$ c_{1}^{2} = a^{2} + b^{2} $`
- 希腊字母：`$\lambda,\xi,\pi,\mu,\Phi,\Omega,\alpha, \beta, \gamma,\Gamma, \Delta $`
- 比较符号
```math
e^{x^2} \neq {e^x}^2

e^{x^2} \geq {e^x}^2

e^{x^2} = {e^x}^2

3>2
```
- 平方根
```math
\sqrt{x+y}

\sqrt[3]{x_{1}^{2}+x_{2}^{2}}
```
- 水平线:`$\overline{m+n} \quad \underline{m+n}$`

- 圆点
```math
a = b \cdot c

a+b+\cdots+z

```
- 向量
```math
\vec{AB}
```
- 函数名
```math
\arccos \cos \csc \arcsin \cosh \deg \arctan \cot \det \arg \coth \dim \sinh \sup \tan

\exp \ker \limsup \min \gcd \lg \ln \Pr \hom \lim \log \sec \inf \liminf \max \sin 

\tanh 
```
- 分数
```math
\sin \alpha = \frac{a}{c}

x^{\frac{1}{2}}

x^{1/2}

```
- 前缀符号（积分、求和、求乘积）
```math
\int_{0}^{\frac{\pi}{2}}

\sum_{i=1}^{n}

\prod_\epsilon

```
- 括号层次
```math
1+\left(\frac {1}{1-x^2}\right) ^3 \neq 1+(\frac {1}{1-x^2}) ^3

\Big( (x+y) (x-y) \Big)^{2}

\big(\Big(\bigg(\Bigg(

\big\}\Big\}\bigg\}\Bigg\}

\big\|\Big\|\bigg\|\Bigg\|
```


## 2. 未支持
- 水平括号:`$ \underbrace{a+b+\cdots+z}_{26}$`
- 定义向量：`$ \overleftarrow {AC} =\overleftarrow {AB} +\overleftarrow {BC} $ `
- 加重向量：`$ \bm{AB} $ `
- LaTeX的注释
- 垂直对齐
```math
\mathbf{X} =
	\left( \begin{array}{ccc}
	x\_{11} & x\_{12} & \ldots \\\
	x\_{21} & x\_{22} & \ldots \\\
	\vdots & \vdots & \ddots
	\end{array} \right)
```
