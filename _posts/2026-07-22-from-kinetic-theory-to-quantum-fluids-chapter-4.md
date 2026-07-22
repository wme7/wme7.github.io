---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 4'
date: 2026-07-22
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-4/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

To derive the Navier–Stokes equations from the Boltzmann equation, we need to introduce the Chapman–Enskog expansion. Let's begin.

# Chapter 4 — The Chapman–Enskog Expansion

## 4.1 Why Do We Need an Expansion?

At the end of Chapter 3, we obtained the exact macroscopic equations

$$
\begin{align} 
\partial_t \rho + \partial_i(\rho u_i) &=0,\\
\partial_t(\rho u_j)+\partial_i(\rho u_i u_j+P_{ij}) &=0,\\
\partial_t E+\partial_i(Eu_i+P_{ij}u_j+q_i) &=0.
\end{align}
$$

These equations are exact, but they are **not closed** because

$$
P_{ij} \quad\text{and}\quad q_i
$$

are still unknown.

To determine them, we need an approximation to the distribution function \\(f\\).

The key physical observation is that in ordinary gases, **collisions are very frequent**. A molecule typically collides many times before macroscopic quantities such as density or temperature change appreciably.

Consequently,

> the distribution function should remain **close to local equilibrium** almost everywhere.

This is the fundamental assumption behind the Chapman–Enskog method.

---

## 4.2 The Knudsen Number

To quantify "close to equilibrium," we introduce a dimensionless parameter.

The **mean free path** \\(\lambda\\) is the average distance traveled between collisions.

The **macroscopic length scale** \\(L\\) is the characteristic scale over which density, velocity, or temperature vary.

Their ratio defines the **Knudsen number**

$$
\boxed{\mathrm{Kn} = \frac{\lambda}{L}.}
$$

Its physical meaning is immediate:

- \\(\mathrm{Kn}\ll1\\): many collisions occur before macroscopic quantities change appreciably.
- \\(\mathrm{Kn}\sim1\\): kinetic effects become important.
- \\(\mathrm{Kn}\gg1\\): collisions are rare, and continuum mechanics breaks down.

For the derivation of the Navier–Stokes equations, we assume

$$
\boxed{\mathrm{Kn}\ll1.}
$$

We therefore introduce a formal small parameter

$$
\varepsilon\equiv\mathrm{Kn}.
$$

The Chapman–Enskog expansion is an asymptotic expansion in powers of \\(\varepsilon\\).

---

## 4.3 What Is Being Expanded?

Since the gas is close to equilibrium, we write

$$
\boxed{f = f^{(0)} +\varepsilon f^{(1)} +\varepsilon^2f^{(2)} +\cdots.}
$$

Here

- \\(f^{(0)}\\) is the local equilibrium distribution,
- \\(f^{(1)}\\) is the first nonequilibrium correction,
- \\(f^{(2)}\\) is the second correction,
- etc.

Notice something subtle.

We are **not** assuming that the distribution itself is small.

Rather,

$$
f^{(1)} = O(\varepsilon)
$$

because deviations from equilibrium are small.

The hierarchy is

$$
f^{(0)} \gg f^{(1)} \gg f^{(2)}.
$$

---

## 4.4 Why Expand the Derivatives?

This is the part that often seems mysterious.

Suppose we substitute only

$$
f=f^{(0)}+\varepsilon f^{(1)}
$$

into the BGK equation.

The streaming operator

$$
\partial_t + v_i\partial_i
$$

acts on both \\(f^{(0)}\\) and \\(f^{(1)}\\), mixing different orders of \\(\varepsilon\\).

The resulting equations cannot be separated consistently.

The resolution is to recognize that **macroscopic evolution itself occurs on multiple time scales**.

---

## Microscopic Time

The collision time is approximately

$$
\tau.
$$

This is the shortest time scale.

After a few collision times, the gas rapidly relaxes toward equilibrium.

---

## Macroscopic Time

Density and temperature evolve much more slowly.

The characteristic macroscopic time is

$$
T \sim \frac{L}{U}
$$

where \\(U\\) is a characteristic fluid velocity.

Since

$$
\lambda = \tau v_{th}
$$

we find

$$
\frac{\tau}{T} \sim \frac{\lambda}{L} = \mathrm{Kn}.
$$

Thus the evolution naturally separates into fast and slow components.

---

## 4.5 Multiple Time Scales

Instead of treating time as a single variable, Chapman and Enskog introduced several formally independent time scales:

$$
t_1,\; t_2,\; t_3,\ldots
$$

related to the physical time by

$$
t_1=\varepsilon t
$$

$$
t_2=\varepsilon^2 t
$$

$$
t_3=\varepsilon^3 t
$$

and so on.

Using the chain rule,

$$
\boxed{\partial_t = \varepsilon\partial_{t_1} + \varepsilon^2\partial_{t_2} + \varepsilon^3\partial_{t_3} +\cdots.}
$$

This is **not** introducing new physical times; it is a bookkeeping device that lets us organize the asymptotic expansion consistently.

---

## 4.6 Spatial Scaling

Macroscopic spatial variations are also slow.

Therefore

$$
\boxed{\nabla = \varepsilon\nabla_1.}
$$

Why only one spatial scale?

Because the Navier–Stokes approximation requires only first-order spatial gradients. Higher-order theories (such as Burnett and super-Burnett equations) often introduce additional spatial scales.

---

## 4.7 Expanding the BGK Equation

The BGK equation is

$$
\partial_t f + v_i\partial_i f = -\frac{1}{\tau}(f-f^{eq}).
$$

Substitute

$$
f = f^{(0)} +\varepsilon f^{(1)} +\varepsilon^2f^{(2)} +\cdots
$$

along with

$$
\partial_t = \varepsilon\partial_{t_1} + \varepsilon^2\partial_{t_2} +\cdots
$$

and

$$
\partial_i = \varepsilon\partial_{i1}.
$$

The left-hand side becomes

$$
\left( \varepsilon\partial_{t_1} + \varepsilon^2\partial_{t_2} +\cdots \right) \left( f^{(0)} +\varepsilon f^{(1)} +\cdots \right) \ + v_i \left( \varepsilon\partial_{i1} \right) \left( f^{(0)} +\varepsilon f^{(1)} +\cdots \right).
$$

The right-hand side is

$$
-\frac{1}{\tau} \left[ f^{(0)} +\varepsilon f^{(1)} +\cdots = f^{eq} \right].
$$

We now collect equal powers of \\(\varepsilon\\).

---

## 4.8 Zeroth Order: \\(O(1)\\)

On the left-hand side, there is **no** term of order \\(O(1)\\), because every derivative carries a factor of \\(\varepsilon\\).

The right-hand side gives

$$
-\frac{1}{\tau} (f^{(0)}-f^{eq}).
$$

Therefore,

$$
\boxed{f^{(0)} = f^{eq}.}
$$

This is the first major result of the Chapman–Enskog method.

The leading-order distribution is **exactly the local Maxwellian**.

Notice how naturally this emerges: we did not assume it a priori; it is enforced by the dominant balance between collisions and streaming when \\(\mathrm{Kn}\ll1\\).

---

## 4.9 First Order: \\(O(\varepsilon)\\)

The terms of order \\(\varepsilon\\) on the left-hand side are

$$
\partial_{t_1}f^{(0)} + v_i\partial_{i1}f^{(0)}.
$$

The right-hand side contributes

$$
-\frac{1}{\tau} f^{(1)}.
$$

Hence

$$
\boxed{\left( \partial_{t_1} + v_i\partial_{i1} \right) f^{(0)} = -\frac{1}{\tau} f^{(1)}.}
$$

Since \\(f^{(0)}=f^{eq}\\),

$$
\boxed{f^{(1)} = -\tau \left( \partial_{t_1} + v_i\partial_{i1} \right) f^{eq}.}
$$

This compact expression contains all the information needed to derive viscosity and heat conduction.

---

## 4.10 Second Order: \\(O(\varepsilon^2)\\)

Although we won't use it immediately, it is useful to record the next equation:

$$
\boxed{\partial_{t_2}f^{(0)} + \left( \partial_{t_1} + v_i\partial_{i1} \right) f^{(1)} = -\frac{1}{\tau} f^{(2)}.}
$$

This order becomes relevant when deriving Burnett corrections, but the Navier–Stokes equations require only the first-order correction \\(f^{(1)}\\).

---

## Summary of the Chapman–Enskog Hierarchy

We have obtained the hierarchy

$$
\boxed{f^{(0)}=f^{eq}}
$$

$$
\boxed{f^{(1)} = -\tau (\partial_{t_1}+v_i\partial_{i1}) f^{eq}}
$$

$$
\boxed{f^{(2)} = -\tau \left[ \partial_{t_2}f^{eq} + (\partial_{t_1}+v_i\partial_{i1})f^{(1)} \right].}
$$

These equations form the foundation of the remainder of the derivation.

---

## An Important Observation

At this stage, **we still have not computed \\(f^{(1)}\\)**. We only have a formal expression involving derivatives of the equilibrium distribution. To obtain the viscous stress tensor and heat flux, we must evaluate

$$
(\partial_t + v_i\partial_i)f^{eq}.
$$

This turns out to be the technically demanding part of the entire derivation. The equilibrium distribution depends on the hydrodynamic fields \\(n\\), \\(T\\), and \\(\mathbf{u}\\), so applying the derivative requires repeated use of the chain rule, followed by elimination of the time derivatives using the Euler equations.

This is the point where many presentations skip several pages of algebra. I suggest we do the opposite: in the next chapter, we'll derive \\(f^{(1)}\\) explicitly, one derivative at a time, keeping every intermediate step visible. That detailed calculation will reveal exactly how the viscous stress tensor and Fourier's law emerge from kinetic theory.