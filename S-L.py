import sympy as sym
from sympy import Symbol, Derivative, Function, integrate, E, simplify
from sympy.plotting.plot import plot
from tabulate import tabulate
from sympy.plotting import plot
import seaborn as sns

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
sns.set_theme()

x = Symbol('x')
y = Function('y')(x)
y_x = Derivative(y, x)
y_xx = Derivative(y, x, x)
k = Symbol('k')     # Please use k as symbol for the eigenvalues
n = Symbol('n')     # Subscript n-th eigenvalue/eigenfunction


def p_n(A, B, n):
    '''Function which generates the eigenvalues and their corresponding polynomials and plots the latters.
    
    
    Args:
        A : Coefficient of y_xx
        B : Coefficient of y_x
        n : last polynomial order (n=3 default)
    
    Returns:
        tab : table containing k_0, k_1,..., k_n and P_0, P_1,..., P_n
    '''
    # Finding the integrating factor (p) and the corresponding weight function (w)
    BA = integrate(B/A, x)
    p = E**BA               
    w = simplify(p/A)       

    # Creating the list of polynomials (l) and the list of eigenvalues (m) and combine them to form a table
    l = []
    m = []
    A2 = sym.diff(sym.diff(A))
    table = [['n', 'Polynomial', 'Eigenvalue']]
    for i in range(0,n+1):
        to_diff = w*(A**i)
        j = 0
        while j<=i-1:
            to_diff = sym.diff(to_diff)
            j = j+1

        l.append(simplify(to_diff/w)) 
        m.append(i*(sym.diff(B)+0.5*(i-1)*A2))

        t = [i, l[i], m[i]]
        table.append(t)

    # Plotting the polynomials 

    p0 = plot(l[0], xlim = (-5,5), ylim = (-10, 10), show = False)
    for g in range(1, len(l)):
        pg = plot(l[g], xlim = (-5,5), ylim = (-10, 10), show = False)
        p0.append(pg[0])
    
    p0.show()

    tab = tabulate(table, headers='firstrow', tablefmt='fancy_grid')

    return tab


def sl(A, B, C, N = 3):
    '''Function which puts the input (second-order ODE) into Sturm-Liouville form.
    Note that y' and y'' must be written as y_x and y_xx respectively.
    Example: 
    y_xx - 2*x*y_x + k*y = 0   [Hermite equation].
    In this case LHS = y_xx - 2*x*y_x + k*y and RHS = 0
    
    Args:
        LHS : left-hand side of the ODE
        RHS : right-hand side of the ODE
        N (optional) : Number of polynomials 
    
    Returns:
        fc : final conclusion containing the Sturm-Liouville form of the input, a 
             table with the first N polynomials/eigenvalues and the general expression
             for the n-th polynomial and the n-th eigenvalues.
    '''

    if A==0:
        fc = '''The input must must have a non-zero A(x).
Furthermore, one of the following conditions must be met:
1) A(x) is actually quadratic, B(x) is linear, A(x) has two distinct real roots, 
   the root of B(x) lies strictly between the roots of A(x), and the leading 
   terms of A(x) and B(x) have the same sign.
2) A(x) is not actually quadratic, but is linear, B(x) is linear, the roots of A(x) 
   and B(x) are different, and the leading terms of A(x) and B(x) have the same 
   sign if the root of B(x) is less than the root of A(x), or vice versa.
3) A(x) is just a nonzero constant, B(x) is linear, and the leading term of B(x) 
   has the opposite sign of A(X).
'''
        return print(fc)
    else:
        BA = integrate(B/A, x)
        p = E**BA
        w = simplify(p/A)
        q = simplify(w*C)
        py_x = Function(f'''[{p}y\']''')(x)
        sl = Derivative(py_x, x) + q*y + k*w*y
        full_solns = p_n(A,B,N)
        k_general = n*(sym.diff(B)+0.5*(n-1)*sym.diff(sym.diff(A)))
        wAn = simplify(w*(A**n))
        P_general = 1/w*Derivative(wAn,(x,n))

        fc = f'''The Sturm-Liouville form of the ODE is: {sl} = 0. 
It has weight function w(x) = {w} and integrating factor p(x) = {p}.
The n-th eigenvalue is: k_n = {k_general}
The n-th polynomial is: P_n = {P_general}
The first {N} eigenvalues and their corresponding polynomials are:
{full_solns}
Please note that these polynomials may differ up to a common factor.'''
        return print(fc)
