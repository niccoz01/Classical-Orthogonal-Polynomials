# Classical Orthogonal Polynomials
Classical orthogonal polynomials (ClOPs) are at the heart of some problems in physics, numerical analysis and many other areas. For example, Hermite polynomials give rise to the eigenstates of the quantum harmonic oscillator; another case can be found in the solution to the radial part of the Schrödinger equation for the hydrogen-like atom, which is a (generalized) Laguerre polynomial.

The ClOPs are solutions of the ODE: 

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7DA(x)%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20y_n%7D%7B%5Cmathrm%7Bd%7D%5E2%20x%7D%20&plus;%20B(x)%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20y_n%7D%7B%5Cmathrm%7Bd%7D%20x%7D%20&plus;%20%5Clambda_ny_n%20=%200)

where A(x) and B(x) are given. The polynomials and their corrisponding eigenvalues are given by the generalised Rodrigues formula:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7Dy_n=%5Cfrac%7B1%7D%7Bw(x)%7D%5Cfrac%7B%5Cmathrm%7Bd%7D%5En%20(w(x)A(x)%5En)%7D%7B%5Cmathrm%7Bd%7D%20x%5En%7D)

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%5Clambda_n=n%5CBig%5B%5Cfrac%7B%5Cmathrm%7Bd%7D%20B(x)%7D%7B%5Cmathrm%7Bd%7D%20x%7D&plus;%5Cfrac%7B1%7D%7B2%7D(n-1)%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20A(x)%7D%7B%5Cmathrm%7Bd%7D%5E2%20x%7D%5CBig%5D)

where w(x) is the so-called weight function given by:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7Dw(x)=%5Cfrac%7B1%7D%7BA(x)%7D%5Cexp%5Cint%7B%5Cfrac%7BB(x)%7D%7BA(x)%7Ddx)

and it obeys the relation:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%5Clangle%20P_n(x)%7CP_m(x)%20%5Crangle%20=%20%5Cint_%7Ba%7D%5E%7Bb%7DP_n(x)P_m(x)w(x)dx%20=%20c%5Cdelta_m_n)

where c is the normalisation constant.

## Requisites
The script is fully written in Python, version 3.8.3, which can be downloaded [here](https://www.python.org/downloads/release/python-383/). If you already have python you can check its version by typing in the command line:
```cmd
python --version
```
If you want to upgrade it:
```cmd
pip install python -- upgrade
```
In order to run the script, three additional modules are required:
* [SymPy](https://www.sympy.org/en/index.html): Python library for symbolic mathematics
* [Tabulate](https://pypi.org/project/tabulate/): Package which prints readable tables
* [Seaborn](https://seaborn.pydata.org/): Python data visualization library
It is possible to install all of them by simply typing:
```cmd
pip install sympy tabulate seaborn
```
## How to use
The usage consists in running the run.py with the appropriate parameters:
```cmd
python run.py --a 'A(x)' --b 'B(x)' --c 'C(x)'
```
N, the highest order polynomial that is wanted, is an optional argument:
```cmd
python run.py --a 'A(x)' --b 'B(x)' --c 'C(x)' --n N
```
Please note the following:
* A, B and C are strings i.e. they have to be between ' ' in order to be passed correctly
* The symbol representing the eigenvalue (generally called λ) is k (see examples below)
* It is not possible at the moment to have any constants e.g. α, β inside A, B and C
## Examples
- Hermite equation:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20y%7D%7B%5Cmathrm%7Bd%7D%20x%5E2%7D%20-2x%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20x%7D&plus;ky%20=%200)

```cmd
python run.py --a '1' --b '(-2*x)' --c 'k' --n 5
```
![Hermite polynomials](/images/Hermite.png)

- Legendre equation:
- 
![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7D(1-x%5E2)%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20y%7D%7B%5Cmathrm%7Bd%7D%20x%5E2%7D%20-2x%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20x%7D&plus;k(k&plus;1)y%20=%200)

```cmd
python run.py --a '(-x**2+1)' --b '(-2*x)' --c 'k(k+1)' --n 5
```
![Legendre polynomials](/images/Legendre.png)

- Laguerre (α=0) equation:

![equation](https://latex.codecogs.com/gif.image?%5Cdpi%7B110%7Dx%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%20y%7D%7B%5Cmathrm%7Bd%7D%20x%5E2%7D%20&plus;(1-x)%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20x%7D&plus;ky%20=%200)

```cmd
python run.py --a 'x' --b '(-x+1)' --c 'k' --n 5
```
![Laguerre polynomials](/images/Laguerre0.png)
