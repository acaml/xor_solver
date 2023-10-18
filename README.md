# xor_solver

**Description:** A tool to solve systems of XOR equations.

## System Representation

The system of XOR equations can be represented using a matrix and a vector:

Equations:

1. \(a \oplus c = 1\)
2. \(b \oplus c = 0\)
3. \(a \oplus c \oplus d = 1\)

Matrix representation:

\[
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 1 \\
    1 & 1 & 1 \\
\end{bmatrix}
\]

Vector representation:

\[
\begin{bmatrix}
    1 \\
    0 \\
    1 \\
\end{bmatrix}
\]

This system can be solved using the provided matrix and vector.
