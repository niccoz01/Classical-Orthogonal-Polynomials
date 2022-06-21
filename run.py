import argparse
import SturmLiouville
from sympy import parse_expr

# Add arguments to the parser
ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")
ap.add_argument("--a", type=str, dest='A', nargs='*', help="A(x)", required=True)
ap.add_argument('--b', type=str, dest='B', nargs='*', help="B(x)", required=True)
ap.add_argument('--c', type=str, dest='C', nargs='*', help="C(x)", required=True)
ap.add_argument("--n", type=int, dest='N', help="An integer to sepcify the number of polynomials to be calculated", default = 3)

# Parsering the arguments using SymPy
pa = ap.parse_args()
A = pa.A
A = parse_expr(A[0])
B = pa.B
B = parse_expr(B[0])
C = pa.C
C = parse_expr(C[0])
N = pa.N


SturmLiouville.sl(A, B, C, N) 
