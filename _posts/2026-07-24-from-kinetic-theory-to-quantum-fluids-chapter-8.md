---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 8'
date: 2026-07-24
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-8/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

We now proceed to repeat the Chapter 5 calculation for \\(f_q^{eq}\\) and derive the explicit quantum \\(f_q^{(1)}\\).

# Chapter 8 — Explicit Quantum Chapman–Enskog Correction \\(f_q^{(1)}\\)

## 8.1 The Quantum BGK Expansion

We start from the quantum BGK equation:

$$
\partial_t f+v_i\partial_i f = -\frac{1}{\tau}(f-f_q^{eq}).
$$

The Chapman–Enskog expansion is

$$
f = f_q^{(0)} + \varepsilon f_q^{(1)} +\cdots .
$$

As before, the zeroth-order equation gives

$$
\boxed{f_q^{(0)}=f_q^{eq}.}
$$

The first-order equation is

$$
\boxed{f_q^{(1)} = -\tau (\partial_{t_1}+v_i\partial_i) f_q^{eq}.}
$$

The entire problem is therefore evaluating the streaming derivative of the quantum equilibrium distribution.

---

## 8.2 Quantum Local Equilibrium Distribution

We write

$$
\boxed{f_q^{eq} = \frac{g}{h^3} \frac{1}{ z^{-1} e^{\beta_E mc^2/2} +\eta }}
$$

where

$$
\beta_E=\frac{1}{k_BT}
$$

and

$$
\eta= \begin{cases} +1,&\text{Fermi gas},\\ -1,&\text{Bose gas}. \end{cases}
$$

It is useful to define

$$
X = z^{-1}e^{\beta_E mc^2/2}.
$$

Then

$$
f_q^{eq} = \frac{g}{h^3} \frac{1}{X+\eta}.
$$

---

## 8.3 The Quantum Generalization of the Logarithmic Derivative

For the Maxwellian we used

$$
Df^{eq} = f^{eq}D\ln f^{eq}.
$$

For quantum statistics this is slightly modified.

Differentiate:

$$
D f_q^{eq} = -\frac{g}{h^3} \frac{DX}{(X+\eta)^2}.
$$

But

$$
f_q^{eq} = \frac{g}{h^3} \frac{1}{X+\eta}.
$$

Therefore,

$$
D f_q^{eq} = -f_q^{eq} \frac{DX}{X+\eta}.
$$

Now,

$$
\frac{X}{X+\eta} = \frac{h^3}{g}f_q^{eq}X
$$

is inconvenient, so we introduce the quantum occupation factor

$$
\boxed{\Phi_q = 1-\eta\frac{h^3}{g}f_q^{eq}.}
$$

For fermions:

$$
\Phi_F=1-\frac{h^3}{g}f_q^{eq}
$$

and for bosons:

$$
\Phi_B=1+\frac{h^3}{g}f_q^{eq}.
$$

Then the derivative becomes

$$
\boxed{Df_q^{eq} = -f_q^{eq}\Phi_q,D\ln X.}
$$

This is one of the key differences from the classical theory.

---

## 8.4 Physical Meaning of the Quantum Factor

The factor

$$
\boxed{\Phi_q = 1-\eta f}
$$

(up to normalization conventions) is the **Bose enhancement / Pauli blocking factor**.

For collisions:

- Fermions:
$$
1-f
$$
    suppresses transitions into occupied states.
- Bosons:
$$
1+f
$$
    enhances transitions into occupied states.

This factor is the kinetic origin of quantum statistical effects.

In the dilute limit,

$$
f_q^{eq}\ll1
$$

and therefore

$$
\Phi_q\rightarrow1.
$$

We recover the classical calculation.

---

## 8.5 Differentiating the Quantum Exponent

We have

$$
X=z^{-1}e^{mc^2/(2k_BT)}.
$$

Taking the logarithm:

$$
\ln X = -\ln z + \frac{mc^2}{2k_BT}.
$$

Therefore,

$$
D\ln X = -D\ln z + D \left( \frac{mc^2}{2k_BT} \right).
$$

The second term is identical to the classical calculation.

The new term is

$$
D\ln z.
$$

---

## 8.6 The Role of Fugacity

The fugacity is

$$
z=e^{\mu/(k_BT)}.
$$

Therefore,

$$
\ln z = \frac{\mu}{k_BT}.
$$

Hence

$$
D\ln z = D \left( \frac{\mu}{k_BT} \right).
$$

Unlike the classical case, chemical potential becomes an independent thermodynamic variable.

This is where quantum hydrodynamics differs fundamentally from the dilute gas.

---

## 8.7 Thermodynamic Derivative Identities

The hydrodynamic variables are now

$$
n,\quad T,\quad u_i.
$$

The chemical potential is not independent; it is determined by

$$
n=n(T,z).
$$

For an ideal quantum gas,

$$
n= \frac{g}{\lambda_T^3} G_{3/2}^{(\eta)}(z).
$$

Taking the logarithm,

$$
\ln n = \ln g -\frac{3}{2}\ln\lambda_T^2 + \ln G_{3/2}^{(\eta)}(z).
$$

Since

$$
\lambda_T\propto T^{-1/2}
$$

we obtain

$$
d\ln n = \frac{3}{2}d\ln T + d\ln G_{3/2}^{(\eta)}.
$$

The derivative identity is

$$
\boxed{z\frac{d}{dz}G_\nu^{(\eta)}(z) = G_{\nu-1}^{(\eta)}(z).}
$$

Therefore,

$$
d\ln G_{3/2} = \frac{G_{1/2}}{G_{3/2}} d\ln z.
$$

Hence

$$
\boxed{d\ln z = \frac{G_{3/2}}{G_{1/2}} \left( d\ln n -\frac{3}{2}d\ln T \right).}
$$

This replaces the simple classical relation between density, temperature, and the Maxwellian normalization.

---

## 8.8 Streaming Derivative

Now we repeat the classical calculation.

The operator is

$$
D = \frac{D_h}{Dt} + c_i\partial_i.
$$

The quantity

$$
D\ln X
$$

contains:

1. density gradients,
2. temperature gradients,
3. velocity gradients.

After substituting the Euler equations for a quantum ideal gas,

$$
\frac{D_hn}{Dt} = -n\nabla\cdot u
$$

$$
\frac{D_hu_i}{Dt} = -\frac{1}{mn}\partial_ip_q
$$

and

$$
\frac{D_hT}{Dt} = -\frac{2}{3}T\nabla\cdot u
$$

the same cancellation mechanism occurs.

The result can be organized as

$$
\boxed{\begin{aligned} D f_q^{eq} =& -f_q^{eq}\Phi_q \Bigg[ 2A_q \left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i \ & + B_q(c^2) c_i\partial_iT \Bigg]. \end{aligned}}
$$

The coefficients \\(A_q\\) and \\(B_q\\) depend on the quantum thermodynamics.

---

## 8.9 Quantum First-Order Distribution

Therefore,

$$
\boxed{\begin{aligned} f_q^{(1)} =& \tau f_q^{eq}\Phi_q \Bigg[ 2A_q \left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i \ & + B_q(c^2)c_i\partial_iT \Bigg]. \end{aligned}}
$$

This is the quantum analogue of the classical result.

The important structural statement is:

$$
\boxed{\text{Quantum statistics modify coefficients, not tensor structure.}}
$$

The shear mode is still:

$$
c_ic_j-\frac{1}{3}c^2\delta_{ij}
$$

and the heat mode is still a vector proportional to

$$
c_i\times\text{function}(c^2).
$$

---

## 8.10 Classical Limit Check

Let

$$
z\ll1.
$$

Then

$$
G_\nu^{(\eta)}(z)\rightarrow z
$$

and

$$
\Phi_q\rightarrow1.
$$

Therefore,

$$
A_q\rightarrow\beta_E
$$

and

$$
B_q(c^2) \rightarrow \frac{1}{T} \left( \beta_E c^2-\frac{5}{2} \right).
$$

Thus,

$$
f_q^{(1)} \rightarrow f^{(1)}_{MB}.
$$

The classical Chapman–Enskog correction is recovered exactly.

---

## 8.11 What Remains to Be Done

We now have the quantum nonequilibrium distribution.

The next chapter will perform the final step:

$$
P_{ij} = m\int c_ic_j f_q^{(1)}\,d^3c
$$

and

$$
q_i = \frac{1}{2}m\int c^2c_i f_q^{(1)}\,d^3c.
$$

The tensor reductions are identical to Chapter 6, but the scalar moments become

$$
G_{5/2}^{(\eta)}, \quad G_{7/2}^{(\eta)}, \quad G_{9/2}^{(\eta)}
$$

and the transport coefficients become:

$$
\boxed{\mu_F,\mu_B}
$$

and

$$
\boxed{\kappa_F,\kappa_B}
$$

with explicit dependence on fugacity.

The next chapter will therefore be the quantum analogue of Chapter 6: deriving the **Fermi and Bose corrections to viscosity and thermal conductivity**, and showing explicitly how the classical BGK result emerges as the dilute limit.
