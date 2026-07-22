---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 2'
date: 2026-07-22
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-2/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

Let us now derive the **classical Maxwell–Boltzmann equilibrium distribution** from first principles (rather than simply stating it), prove why it is isotropic in the peculiar velocity, evaluate all of its velocity moments explicitly using Gaussian integrals, and show how the ideal-gas equation of state emerges directly from kinetic theory.

# Chapter 2 — The Maxwell–Boltzmann Equilibrium Distribution

## 2.1 What Does "Equilibrium" Mean?

Before introducing any formula, we should clarify the physical meaning of equilibrium.

Imagine a gas enclosed in a box with

- no external forces,
- no macroscopic flow,
- no temperature gradients,
- no density gradients.

Molecules continue to collide incessantly, but the **statistical state no longer changes with time**.

Thus,

$$
\frac{\partial f}{\partial t}=0.
$$

Moreover, because the gas is homogeneous,

$$
\nabla_x f=0.
$$

The Boltzmann equation

$$
\frac{\partial f}{\partial t} +\mathbf{v}\cdot\nabla_x f =Q(f)
$$

reduces to

$$
Q(f)=0.
$$

Thus the equilibrium distribution is precisely the distribution annihilated by the collision operator.

For the BGK model,

$$
Q(f) = -\frac{1}{\tau}(f-f^{eq})
$$

so equilibrium immediately implies

$$
f=f^{eq}.
$$

The real question is therefore:

> **What is the functional form of \\(f^{eq}\\)?**

---

## 2.2 Properties Required of Equilibrium

Without solving the Boltzmann equation, we already know several properties.

### (a) Positivity

Since \\(f\\) represents a density,

$$
f^{eq}>0.
$$

---

### (b) Isotropy

There is no preferred direction.

Therefore

$$
f^{eq} = f^{eq}(|\mathbf{c}|).
$$

Notice something important.

The equilibrium distribution **cannot depend on**

$$
\mathbf{v}
$$

directly.

Instead it depends on

$$
\boxed{\mathbf{c} = \mathbf{v}-\mathbf{u}.}
$$

because equilibrium is defined relative to the local fluid velocity.

This observation remains true for quantum gases.

---

### (c) Galilean Invariance

Suppose we observe the gas from another inertial frame moving with constant velocity \\(\mathbf{U}\\).

Then

$$
\mathbf{v}' = \mathbf{v}-\mathbf{U}
$$

$$
\mathbf{u}' = \mathbf{u}-\mathbf{U}.
$$

Hence

$$
\mathbf{c}' = \mathbf{v}'-\mathbf{u}' = \mathbf{c}.
$$

The peculiar velocity is invariant under Galilean transformations.

Therefore the equilibrium distribution automatically satisfies Galilean invariance.

This is another reason why kinetic theory is formulated using \\(\mathbf{c}\\).

---

## 2.3 Dependence on the Kinetic Energy

Because of isotropy,

$$
f^{eq} = F(c^2).
$$

Why \\(c^2\\)?

Because rotational invariance tells us the only scalar built from \\(\mathbf{c}\\) is

$$
c^2 = \mathbf{c}\cdot\mathbf{c}.
$$

Equivalently,

$$
\frac{1}{2}mc^2
$$

is the molecular kinetic energy measured in the local rest frame.

Thus equilibrium must be a function of the particle energy alone.

---

## 2.4 Why an Exponential?

There are several derivations of the Maxwellian. One uses entropy maximization, another uses the Boltzmann H-theorem. For our purposes, the entropy-maximization argument is particularly transparent.

We seek the distribution that maximizes the entropy

$$
S = -k_B \int f\ln f\,d^3v
$$

subject to the conserved quantities:

- particle number,
- momentum,
- energy.

Introduce Lagrange multipliers \\(\alpha\\), \\(\boldsymbol{\beta}\\), and \\(\gamma\\), and require

$$
\delta \left[ -k_B\int f\ln f\,d^3v -\alpha\int f\,d^3v -\boldsymbol{\beta}\cdot\int\mathbf{v} f\,d^3v -\gamma\int\frac{1}{2}mv^2f\,d^3v \right] =0.
$$

Taking the variation with respect to \\(f\\) gives

$$
-k_B(\ln f+1) -\alpha -\boldsymbol{\beta}\cdot\mathbf{v} -\gamma\frac{1}{2}mv^2 =0.
$$

Hence

$$
\ln f = A + \mathbf{B}\cdot\mathbf{v} - C v^2
$$

where (A), \\(\mathbf{B}\\), and \\(C\\) are constants related to the Lagrange multipliers.

Exponentiating,

$$
f = \exp(A) \exp(\mathbf{B}\cdot\mathbf{v}) \exp(-Cv^2).
$$

Completing the square in the exponent,

$$
-Cv^2+\mathbf{B}\cdot\mathbf{v} = -C(\mathbf{v}-\mathbf{u})^2+\text{constant}
$$

where

$$
\mathbf{u}=\frac{\mathbf{B}}{2C}.
$$

Thus the equilibrium distribution necessarily takes the Gaussian form

$$
f^{eq} = A \exp\left[-C(\mathbf{v}-\mathbf{u})^2\right].
$$

The constants (A) and \\(C\\) are determined by normalization and energy.

---

## 2.5 Determining the Constants

We now write

$$
f^{eq} = A \exp(-Cc^2).
$$

The constants are fixed by requiring

$$
\int f^{eq}\,d^3v = n
$$

and

$$
\frac{1}{2}m \int c^2f^{eq}\,d^3v = \frac{3}{2}nk_BT.
$$

The second relation is the classical equipartition theorem.

To evaluate these integrals, we need Gaussian moments.

---

## 2.6 Gaussian Integrals

Everything follows from the one-dimensional Gaussian integral

$$
\int_{-\infty}^{\infty} e^{-ax^2},dx = \sqrt{\frac{\pi}{a}}, \qquad a>0.
$$

Since the exponential factorizes,

$$
e^{-ac^2} = e^{-ac_x^2} e^{-ac_y^2} e^{-ac_z^2}
$$

the three-dimensional integral is simply

$$
\int e^{-ac^2}\,d^3c = \left( \sqrt{\frac{\pi}{a}} \right)^3 = \left(\frac{\pi}{a}\right)^{3/2}.
$$

Likewise,

$$
\int c^2 e^{-ac^2} \,d^3c = \frac{3}{2a} \left(\frac{\pi}{a}\right)^{3/2}.
$$

More generally, for later use in the Chapman–Enskog expansion,

$$
\int c_ic_j e^{-ac^2} \,d^3c = \frac{\delta_{ij}}{2a} \left(\frac{\pi}{a}\right)^{3/2}
$$

and

$$
\int c_ic_jc_k e^{-ac^2} \,d^3c = 0
$$

because the integrand is odd in at least one coordinate.

These Gaussian identities are the workhorses of the classical derivation. Their quantum counterparts will be replaced by Fermi–Dirac and Bose–Einstein integrals.

---

## 2.7 The Maxwellian

Applying the normalization conditions gives

$$
C=\frac{m}{2k_BT}
$$

and

$$
A = n \left( \frac{m}{2\pi k_BT} \right)^{3/2}.
$$

Therefore,

$$
\boxed{f^{eq}(\mathbf{x},\mathbf{v},t) = n \left( \frac{m}{2\pi k_BT} \right)^{3/2} \exp\left[ -\frac{m(\mathbf{v}-\mathbf{u})^2}{2k_BT} \right].}
$$

This is the **local Maxwell–Boltzmann equilibrium distribution**. The adjective "local" emphasizes that \\(n\\), \\(\mathbf{u}\\), and \\(T\\) are allowed to vary with \\(\mathbf{x}\\) and \\(t\\), even though the velocity dependence is Maxwellian at each point.

---

## 2.8 Equilibrium Moments

The definitions from Chapter 1 now become explicit.

Using the Gaussian identities,

$$
\int f^{eq}\,d^3v=n
$$

$$
m \int \mathbf{c},f^{eq}\,d^3v=0
$$

$$
m \int c_ic_jf^{eq}\,d^3v = nk_BT\,\delta_{ij}.
$$

Therefore,

$$
\boxed{P_{ij}^{eq} = p\,\delta_{ij}}
$$

where

$$
\boxed{p=nk_BT.}
$$

This is the ideal-gas equation of state emerging directly from kinetic theory.

Similarly,

$$
\frac{1}{2}m \int c^2f^{eq}\,d^3v = \frac{3}{2}nk_BT
$$

so the specific internal energy is

$$
\boxed{e=\frac{3}{2}\frac{k_BT}{m}.}
$$

Finally,

$$
\frac{1}{2}m \int c^2c_if^{eq}\,d^3v=0
$$

because the integrand is odd.

Hence

$$
\boxed{\mathbf{q}^{eq}=0.}
$$

---

## Summary

At equilibrium, the macroscopic fields derived from the Maxwellian are

$$
\rho = mn,\quad 
P_{ij} = p\,\delta_{ij},\quad 
p = nk_BT,\quad 
e = \frac{3}{2}\frac{k_BT}{m},\quad 
\mathbf{q} = 0.
$$

Several features of this chapter will carry over unchanged to the quantum case:

- The equilibrium distribution is still expressed in terms of the peculiar velocity \\(\mathbf{c}=\mathbf{v}-\mathbf{u}\\).
- It is still determined by maximizing an appropriate entropy under conservation of mass, momentum, and energy.
- The macroscopic fields are obtained from the same velocity moments.

The fundamental difference will be that the Gaussian factor
$$
\exp\left(-\frac{mc^2}{2k_BT}\right)
$$
is replaced by the Fermi–Dirac or Bose–Einstein occupation function. Consequently, every Gaussian integral we evaluated here becomes a quantum statistical integral, but the overall structure of the derivation remains the same.
