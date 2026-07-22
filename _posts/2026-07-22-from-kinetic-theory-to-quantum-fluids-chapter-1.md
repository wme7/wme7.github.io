---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 1'
date: 2026-07-22
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-1/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

Since I was a PhD student in kinetic theory, one question that got stuck in my mind was:
> *How does a microscopic description forget information and become a macroscopic fluid*?

This is not a simple question. In my academic and research path, I realized that the answer connects Boltzmann, irreversible thermodynamics, quantum statistics, and quantum coherence. This is why I decided to write this series of posts to share my understanding of this question.

This is really a question about where the arrow of time and dissipation come from, given that the microscopic laws (classical or quantum) are time-reversible. The short answer: nothing is _actually_ forgotten at the fundamental level — _it just becomes practically inaccessible_. 

In the following series of posts, I will guide you through the journey of how I managed to guive my own answer to this question. Let's begin!

# Chapter 1 — Classical BGK Kinetic Theory

## 1.1 The One-Particle Distribution Function

Consider a dilute monatomic gas.

A complete microscopic description would require the positions and velocities of all \\(N\\) particles,

$$
(\mathbf{x}_1,\mathbf{v}_1,\ldots,\mathbf{x}_N,\mathbf{v}_N)
$$

which lives in a \\(6N\\)-dimensional phase space.

For macroscopic systems,

$$
N\sim10^{23}
$$

so this description is impractical.

Instead, kinetic theory introduces the **one-particle distribution function**

$$
f(\mathbf{x},\mathbf{v},t).
$$

The interpretation is

> \\(f(\mathbf{x},\mathbf{v},t)\,d^3x\,d^3v\\) is the expected number of particles whose position lies in \\(d^3x\\) around \\(\mathbf{x}\\) and whose velocity lies in \\(d^3v\\) around \\(\mathbf{v}\\).

Therefore,

- position is continuous,
- velocity is continuous,
- time is continuous.

The distribution function is therefore a scalar field over the six-dimensional phase space.

---

## 1.2 Dimensions of \\(f\\)

Since

$$
dN=f\,d^3x\,d^3v
$$

and \\(dN\\) is dimensionless,

$$
[f] = \frac{\text{particles}} {\text{volume}\times(\text{velocity})^3}.
$$

Equivalently,

$$
[f] = \frac{s^3}{m^6}.
$$

Keeping track of units is useful later when constructing equilibrium distributions and evaluating moments.

---

## 1.3 Macroscopic Quantities as Velocity Moments

The microscopic variable is

$$
f(\mathbf{x},\mathbf{v},t).
$$

Macroscopic fields are obtained by integrating over all velocities.

This is the fundamental bridge between kinetic theory and continuum mechanics.

---

### Density

Integrating over velocity gives

$$
n(\mathbf{x},t) = \int f\,d^3v
$$

where \\(n\\) is the particle number density.

Mass density is

$$
\rho = mn = m\int f\,d^3v.
$$

---

### Mean Velocity

The momentum density is

$$
\rho\mathbf{u} = m \int \mathbf{v}f\,d^3v.
$$

Hence

$$
\boxed{\mathbf{u} = \frac{1}{n} \int \mathbf{v}f\,d^3v.}
$$

Notice that the velocity appearing in the kinetic equation and the macroscopic velocity are **not** the same object:

- \\(\mathbf{v}\\): microscopic particle velocity (integration variable),
- \\(\mathbf{u}\\): average fluid velocity.

This distinction is central to the Chapman–Enskog derivation.

---

### Peculiar Velocity

We now introduce one of the most important quantities in kinetic theory:

$$
\boxed{\mathbf{c} = \mathbf{v}-\mathbf{u}.}
$$

The vector \\(\mathbf{c}\\) is called the **peculiar velocity**, **thermal velocity**, or **random velocity**.

It measures the deviation of an individual molecule's velocity from the bulk flow.

Every molecular velocity is decomposed into

$$
\boxed{\mathbf{v} = \mathbf{u} + \mathbf{c}.}
$$

This decomposition cleanly separates:

- ordered motion (\\(\mathbf{u}\\)),
- random thermal motion (\\(\mathbf{c}\\)).

Almost every calculation in Chapman–Enskog is expressed in terms of \\(\mathbf{c}\\), because equilibrium distributions are isotropic in the peculiar velocity.

---

### Why is the mean peculiar velocity zero?

Using the definition,

$$
\int \mathbf{c}f\,d^3v = \int (\mathbf{v}-\mathbf{u})f\,d^3v.
$$

Substitute the definitions of \\(n\\) and \\(\mathbf{u}\\):

$$
n\mathbf{u} - \mathbf{u}n = 0
$$

Therefore,

$$
\boxed{\int \mathbf{c}f\,d^3v = 0}
$$

This identity will repeatedly eliminate terms in later derivations.

---

## 1.4 Internal Energy

The molecular kinetic energy is

$$
\frac{1}{2}mv^2.
$$

Decompose

$$
\mathbf{v} = \mathbf{u} +\mathbf{c}.
$$

Then

$$
v^2 = u^2 + 2\mathbf{u}\cdot\mathbf{c} + c^2.
$$

Integrating,

$$
\frac{1}{2}m \int v^2f\,d^3v = \frac{1}{2}\rho u^2 + \frac{1}{2}m \int c^2f\,d^3v
$$

because

$$
\int \mathbf{c}f\,d^3v=0.
$$

Thus the total kinetic energy naturally separates into

- bulk kinetic energy,
- internal thermal energy.

We therefore define the internal energy density as

$$
\boxed{\rho e = \frac{1}{2}m \int c^2f\,d^3v.}
$$

This is another key result: **internal energy is the kinetic energy of the random molecular motion**, not of the bulk flow.

---

## 1.5 Pressure Tensor

The next velocity moment is

$$
\boxed{P_{ij} = m \int c_ic_jf\,d^3v.}
$$

This is the **pressure tensor** (or stress tensor in kinetic theory).

Physically,

- diagonal terms represent normal stresses (pressure),
- off-diagonal terms represent shear stresses.

At equilibrium, isotropy implies

$$
P_{ij} = p\delta_{ij}.
$$

Away from equilibrium,

$$
P_{ij} = p\delta_{ij} + \Pi_{ij}
$$

where

$$
\Pi_{ij}
$$

is the viscous stress that we will derive through the Chapman–Enskog expansion.

---

## 1.6 Heat Flux

The third-order moment is

$$
\boxed{q_i = \frac{1}{2}m \int c^2c_if\,d^3v.}
$$

This represents the transport of internal energy by random molecular motion.

At equilibrium,

$$
q_i=0
$$

because the equilibrium distribution is isotropic and the integrand is odd in \\(\mathbf{c}\\).

Nonzero heat flux is therefore entirely a **nonequilibrium phenomenon**, just like viscosity.

---

## Summary of the Fundamental Velocity Moments

|Moment|Definition|Physical meaning|
|---|---|---|
|\\(n\\)|\\(\int f\,d^3v\\)|Number density|
|\\(\rho\\)|\\(m\int f\,d^3v\\)|Mass density|
|\\(\mathbf{u}\\)|\\(\frac{1}{n}\int \mathbf{v}f\,d^3v\\)|Mean velocity|
|\\(\rho e\\)|\\(\frac{1}{2}m\int c^2f\,d^3v\\)|Internal energy density|
|\\(P_{ij}\\)|\\(m\int c_ic_jf\,d^3v\\)|Pressure tensor|
|\\(q_i\\)|\\(\frac{1}{2}m\int c^2c_if\,d^3v\\)|Heat flux|

---

This chapter establishes the kinetic quantities that will appear throughout the derivation. A point worth emphasizing—because it will become even more important in the quantum case—is that **nothing here depends on the form of the equilibrium distribution**. These definitions are purely kinematic.

That observation is one of the reasons a side-by-side classical/quantum treatment is so powerful: in the quantum derivation, every definition introduced above remains unchanged. The only ingredient that changes is the equilibrium distribution \\(f^{eq}\\), and consequently the values of the velocity moments computed from it.

In the next chapter, we'll derive the **classical Maxwell–Boltzmann equilibrium distribution** from first principles (rather than simply stating it), prove why it is isotropic in the peculiar velocity, evaluate all of its velocity moments explicitly using Gaussian integrals, and show how the ideal-gas equation of state emerges directly from kinetic theory. Those calculations will later serve as the template for replacing Gaussian integrals with Fermi–Dirac and Bose–Einstein integrals in the quantum derivation.
