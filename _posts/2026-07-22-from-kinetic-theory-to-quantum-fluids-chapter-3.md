---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 3'
date: 2026-07-22
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-3/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

Having derived the **classical Maxwell–Boltzmann equilibrium distribution** and its moments, let us now derive the macroscopic conservation laws from the Boltzmann equation.

# Chapter 3 — Derivation of the Macroscopic Conservation Laws

## 3.1 The BGK Equation

We begin with the classical BGK equation

$$
\boxed{\frac{\partial f}{\partial t} + v_i\frac{\partial f}{\partial x_i} = -\frac{1}{\tau} \left( f-f^{eq} \right)}
$$

where we use Einstein summation.

The unknown is

$$
f(\mathbf{x},\mathbf{v},t).
$$

The macroscopic variables are defined by velocity moments:

$$
\rho = m\int f\,d^3v
$$

$$
\rho u_i = m\int v_if\,d^3v
$$

$$
\rho e = \frac{1}{2}m \int c^2f\,d^3v.
$$

Our objective is to derive equations for these quantities.

---

## 3.2 Collision Invariants

Everything depends on one fundamental property.

Although collisions continually redistribute molecular velocities, they **cannot change**

- total mass,
- total momentum,
- total kinetic energy.

These are called the **collision invariants**.

Mathematically,

$$
\psi(\mathbf{v}) = 1,\; v_i,\; \frac{1}{2}v^2.
$$

The BGK operator must satisfy

$$
\boxed{\int \psi \left( f-f^{eq} \right) d^3v = 0}
$$

Notice something important.

The BGK operator itself does **not** conserve arbitrary moments.

It conserves only the moments associated with these three functions.

Everything else (stress, heat flux, higher moments) relaxes toward equilibrium.

This observation will later be equally true for the quantum BGK operator.

---

## 3.3 General Moment Equation

Rather than deriving each conservation law separately, let's derive them all at once.

Multiply the BGK equation by an arbitrary function

$$
m\psi(\mathbf{v})
$$

and integrate over velocity.

We obtain

$$
m \int \psi \frac{\partial f}{\partial t} \,d^3v + m \int \psi v_i \frac{\partial f}{\partial x_i} \,d^3v = -\frac{m}{\tau} \int \psi (f-f^{eq}) \,d^3v.
$$

Since the integration variable is velocity, derivatives with respect to \\(x_i\\) and \\(t\\) pass through the integral:

$$
\boxed{\frac{\partial}{\partial t} \left( m \int \psi f \,d^3v \right) + \frac{\partial}{\partial x_i} \left( m \int v_i\psi f \,d^3v \right) = -\frac{m}{\tau} \int \psi(f-f^{eq}) \,d^3v.}
$$

This is the **general moment equation**.

Every macroscopic conservation law is obtained by choosing a different collision invariant.

---

## 3.4 Mass Conservation

Choose

$$
\psi=1.
$$

The right-hand side vanishes because mass is conserved in collisions.

The first integral becomes

$$
m \int f\,d^3v = \rho.
$$

The second becomes

$$
m \int v_if\,d^3v = \rho u_i.
$$

Therefore

$$
\boxed{\frac{\partial\rho}{\partial t} + \frac{\partial(\rho u_i)}{\partial x_i}}
$$

This is exactly the continuity equation.

Notice that **no approximation has been made**.

---

## 3.5 Momentum Conservation

Now choose

$$
\psi=v_j.
$$

Again,

$$
\int v_j(f-f^{eq})\,d^3v
$$

The first moment gives

$$
m \int v_jf\,d^3v = \rho u_j.
$$

The flux term becomes

$$
m \int v_iv_jf\,d^3v.
$$

This integral requires some work.

---

## Decomposition of the Second Moment

Write

$$
v_i=u_i+c_i.
$$

Then

$$
v_iv_j = u_iu_j + u_ic_j + u_jc_i + c_ic_j.
$$

Multiply by \\(f\\) and integrate.

The cross terms vanish,

because

$$
\int c_if\,d^3v
$$

Hence

$$
m \int v_iv_jf\,d^3v = \rho u_iu_j + P_{ij}
$$

where

$$
P_{ij} = m \int c_ic_jf\,d^3v.
$$

Therefore,

$$
\boxed{\frac{\partial(\rho u_j)}{\partial t} + \frac{\partial}{\partial x_i} \left( \rho u_iu_j + P_{ij} \right)}
$$

This is the exact momentum equation.

Notice that viscosity has **not** yet appeared.

Everything is hidden inside

$$
P_{ij}.
$$

---

## 3.6 Energy Conservation

Now choose

$$
\psi=\frac{1}{2}v^2.
$$

The collision term again vanishes.

The conserved density becomes

$$
\frac{1}{2}m \int v^2f\,d^3v.
$$

Using

$$
v^2=u^2+2u_ic_i+c^2
$$

the cross term disappears,

giving

$$
\boxed{E = \frac{1}{2}\rho u^2 + \rho e.}
$$

This is the total energy density.

---

## Energy Flux

The flux is

$$
\frac{1}{2}m \int v^2v_if\,d^3v.
$$

This is the most difficult moment so far.

Instead of quoting the answer, let's derive it carefully.

Write

$$
v_i=u_i+c_i
$$

and

$$
v^2=u^2+2u_jc_j+c^2.
$$

Thus

$$
v^2v_i = (u^2+2u_jc_j+c^2)(u_i+c_i).
$$

Expanding gives six terms:

$$
u^2u_i
$$

$$
u^2c_i
$$

$$
2u_ju_ic_j
$$

$$
2u_jc_jc_i
$$

$$
u_ic^2
$$

$$
c^2c_i.
$$

Now integrate each separately.

---

### First term

$$
\frac{1}{2}m \int u^2u_if\,d^3v = \frac{1}{2}\rho u^2u_i.
$$

---

### Second term

Contains

$$
\int c_if\,d^3v=0.
$$

So it vanishes.

---

### Third term

Contains

$$
\int c_jf\,d^3v=0.
$$

It also vanishes.

---

### Fourth term

Gives

$$
u_j P_{ij}.
$$

---

### Fifth term

Since

$$
\frac{1}{2}m \int c^2f\,d^3v = \rho e
$$

it contributes

$$
\rho eu_i.
$$

---

### Sixth term

Produces the heat flux

$$
q_i = \frac{1}{2}m \int c^2c_if\,d^3v.
$$

---

Adding everything,

$$
\boxed{\frac{1}{2}m \int v^2v_if\,d^3v = Eu_i + P_{ij}u_j + q_i.}
$$

This decomposition is one of the central results of kinetic theory. It shows that the transport of energy consists of:

- convection of total energy,
- mechanical work done by the stress,
- heat conduction by random molecular motion.

---

## 3.7 Final Exact Conservation Laws

Collecting the three results,

## Mass

$$
\boxed{\partial_t\rho + \partial_i(\rho u_i)}
$$

---

## Momentum

$$
\boxed{\partial_t(\rho u_j) + \partial_i \left( \rho u_iu_j + P_{ij} \right)}
$$

---

## Energy

$$
\boxed{\partial_tE + \partial_i \left( Eu_i + P_{ij}u_j + q_i \right)}
$$

These equations are **exact consequences** of the BGK equation and require only that the collision operator preserves mass, momentum, and energy.

---

## 3.8 Where Are the Euler and Navier–Stokes Equations?

At this point, we have derived the macroscopic balance laws, but the system is **not closed**. There are 5 hydrodynamic unknowns in three dimensions—\\(\rho\\), the three components of \\(\mathbf{u}\\), and either \\(T\\) or \\(e\\)—yet the equations still contain the additional quantities

$$
P_{ij}, \qquad q_i
$$

which depend on the full distribution function \\(f\\).

This is the closure problem.

If we simply assume local equilibrium,

$$
f=f^{eq}
$$

then

$$
P_{ij}=p\,\delta_{ij},\qquad q_i=0
$$

and the equations reduce immediately to the **Euler equations**.

The Chapman–Enskog expansion addresses the next level of approximation. It computes the first deviation of \\(f\\) from equilibrium,

$$
f=f^{eq}+f^{(1)}+\cdots
$$

and thereby derives constitutive relations for \\(P_{ij}\\) and \\(q_i\\). Newton's law of viscosity and Fourier's law of heat conduction emerge from this calculation, completing the transition from kinetic theory to the Navier–Stokes equations.
