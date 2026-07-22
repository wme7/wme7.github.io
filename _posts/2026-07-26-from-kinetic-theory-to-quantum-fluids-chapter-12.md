---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 12'
date: 2026-07-26
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-12/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

This chapter takes us into a subtle but very important distinction in quantum fluid theory.

So far we have derived **quantum Navier–Stokes equations from quantum kinetic theory**. These equations contain quantum statistics through:

- Bose–Einstein or Fermi–Dirac equilibrium,
- quantum equation of state,
- quantum transport coefficients.

However, they do **not automatically contain the dispersive quantum correction**

$$
-\frac{\hbar^2}{2m} \nabla \left( \frac{\nabla^2\sqrt n}{\sqrt n} \right)
$$

usually called the **quantum pressure** or **Bohm potential** term.

Why?

Because the Chapman–Enskog expansion we performed starts from a **phase-space distribution** and describes particles through local statistical equilibrium. The quantum pressure originates from a different aspect of quantum mechanics: the **coherence of the wavefunction itself**.

This chapter builds the bridge between these two descriptions.

---

# Chapter 12 — From Quantum Kinetic Theory to Quantum Hydrodynamics

## 12.1 Two Meanings of "Quantum Hydrodynamics"

The phrase _quantum hydrodynamics_ is used for two related but distinct theories.

---

## A) Quantum statistical hydrodynamics

Derived from:

$$
\boxed{\text{quantum Boltzmann/BGK equation}}
$$

through Chapman–Enskog expansion.

It gives:

$$
\boxed{\text{Navier–Stokes equations with quantum statistics}}
$$

The quantum information enters through:

$$
p(n,T)
$$

$$
\mu(n,T)
$$

$$
\kappa(n,T).
$$

---

## B) Wave-mechanical quantum hydrodynamics

Derived from:

$$
\boxed{\text{Schrödinger equation}}
$$

or

$$
\boxed{\text{Gross–Pitaevskii equation}}
$$

using the Madelung transformation.

It gives:

$$
\boxed{\text{Euler equations with quantum pressure}.}
$$

The quantum information enters through:

$$
\hbar.
$$

---

These are not competing theories.

They describe different physics.

---

## 12.2 Starting from the Schrödinger Equation

Consider a single particle:

$$
i\hbar \frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2\psi + V\psi .
$$

Write the wavefunction as

$$
\boxed{\psi(\mathbf{r},t) = \sqrt{n(\mathbf{r},t)} e^{iS(\mathbf{r},t)/\hbar}.}
$$

This is the Madelung transformation.

The density is:

$$
|\psi|^2=n.
$$

The velocity is identified as:

$$
\boxed{\mathbf{u} = \frac{\nabla S}{m}.}
$$

---

## 12.3 The Continuity Equation

Substituting into the imaginary part of Schrödinger's equation gives:

$$
\boxed{\frac{\partial n}{\partial t} + \nabla\cdot(n\mathbf{u}) = 0}
$$

This is identical to the kinetic-theory continuity equation.

So both approaches agree here.

---

## 12.4 The Momentum Equation

The real part gives:

$$
\frac{\partial S}{\partial t} + \frac{(\nabla S)^2}{2m} + V + Q = 0
$$

where

$$
\boxed{Q = -\frac{\hbar^2}{2m} \frac{\nabla^2\sqrt n}{\sqrt n}}
$$

is the quantum potential.

Taking a gradient:

$$
m \frac{D\mathbf{u}}{Dt} = -\nabla(V+Q).
$$

Therefore,

$$
\boxed{m n \frac{D\mathbf{u}}{Dt} = -n\nabla V = n\nabla Q .}
$$

The last term is the quantum pressure contribution.

---

## 12.5 The Quantum Pressure Tensor

The quantum force can be written as a stress divergence:

$$
-n\nabla Q = -\partial_jP_{ij}^{Q}.
$$

The quantum stress tensor is:

$$
\boxed{P_{ij}^{Q} = \frac{\hbar^2}{4m} \left[ \frac{\partial_i n\partial_j n}{n} - \partial_i\partial_j n \right].}
$$

This is a completely different object from the kinetic pressure tensor:

$$
P_{ij} = m\int c_ic_j f\,d^3c.
$$

The first comes from wave coherence.

The second comes from particle motion.

---

## 12.6 Why BGK Does Not Produce Quantum Pressure

The BGK equation evolves:

$$
f(\mathbf{x},\mathbf{v},t).
$$

The microscopic variables are:

$$
\mathbf{x},\mathbf{v}.
$$

The phase of the wavefunction,

$$
S(\mathbf{x},t)
$$

is not present.

Therefore the information required to create:

$$
\nabla^2\sqrt n
$$

is absent.

The quantum BGK equation knows about:

- occupation numbers,
- exchange statistics,
- Pauli blocking,
- Bose enhancement.

It does not know about:

- phase coherence,
- interference,
- wavefunction curvature.

Therefore:

$$
\boxed{\text{Quantum statistics} \neq \text{wave-mechanical quantum effects}.}
$$

---

## 12.7 The Wigner Function: The Bridge

To include both effects, we introduce the Wigner function:

$$
W(\mathbf{x},\mathbf{p},t).
$$

It is a quantum phase-space distribution.

Unlike the classical distribution:

$$
f(x,p)
$$

it can contain negative regions because it retains phase information.

The Wigner equation is:

$$
\frac{\partial W}{\partial t} + \frac{\mathbf{p}}{m}\cdot\nabla_xW = \mathcal{Q}[W]
$$

where

$$
\mathcal{Q}
$$

is the quantum Moyal operator.

Expanding the Moyal term:

$$
\mathcal{Q} = -\nabla V\cdot\nabla_pW + \frac{\hbar^2}{24} \nabla^3V\cdot\nabla_p^3W +\cdots
$$

The classical limit is:

$$
\hbar\rightarrow0.
$$

---

## 12.8 Wigner Hydrodynamics

Taking moments of the Wigner equation gives:

## Continuity

$$
\boxed{\partial_tn+\nabla\cdot(nu)=0}
$$

---

## Momentum

$$
\boxed{mn \frac{Du_i}{Dt} = -\partial_jP_{ij} = n\partial_iV + F_i^{Q}.}
$$

The quantum force is generated by the higher-order Wigner moments.

In the pure condensate limit:

$$
F_i^{Q} = -n\partial_iQ.
$$

---

## 12.9 Gross–Pitaevskii Equation

For a weakly interacting Bose condensate:

$$
\boxed{i\hbar\partial_t\psi = \left( -\frac{\hbar^2\nabla^2}{2m} + V + g|\psi|^2 \right)\psi .}
$$

The interaction parameter is:

$$
g= \frac{4\pi\hbar^2a_s}{m}
$$

where \\(a_s\\) is the scattering length.

Applying the Madelung transformation gives:

Continuity:

$$
\partial_tn+\nabla\cdot(nu)=0.
$$

Momentum:

$$
\boxed{m \frac{Du}{Dt} = -\nabla \left( gn + V + Q \right).}
$$

The terms are:

|Term|Origin|
|---|---|
|\\(gn\\)|particle interactions|
|\\(V\\)|external potential|
|\\(Q\\)|quantum coherence|

---

## 12.10 Comparing the Two Quantum Hydrodynamics

||Quantum BGK|Gross–Pitaevskii|
|---|---|---|
|Starting point|kinetic equation|wave equation|
|Variable|\\(f(x,v)\\)|\\(\psi(x)\\)|
|Statistics|BE/FD|usually Bose condensate|
|Pauli blocking|yes|no|
|Bose enhancement|yes|no|
|Quantum pressure|no|yes|
|Viscosity|yes|negligible|
|Dissipation|yes|no|

---

## 12.11 The Complete Picture

A realistic quantum fluid may require **all three ingredients**:

## 1. Quantum statistics

$$
f_{FD/BE}
$$

controls equilibrium.

---

## 2. Collisions

$$
C[f]
$$

controls viscosity and heat transport.

---

## 3. Coherence

$$
\hbar\nabla^2\sqrt n
$$

controls quantum pressure.

A unified theory attempts to combine them:

$$
\boxed{\text{Wigner} + \text{quantum collision operator} + \text{Chapman–Enskog expansion}}
$$

This is an active research area.

---

## 12.12 Final Conceptual Map

We can now distinguish three levels:

$$
\boxed{\text{Boltzmann}}
$$

classical particles:

$$
f_{MB}
$$

↓

$$
\boxed{\text{Quantum BGK}}
$$

quantum statistics:

$$
f_{FD/BE}
$$

↓

$$
\boxed{\text{Wigner/Gross–Pitaevskii}}
$$

quantum coherence:

$$
\hbar\text{-dependent pressure}.
$$

---

The next natural chapter is a very rich one:

**Chapter 13 — Deriving the quantum Navier–Stokes–Wigner equations: combining quantum statistics, viscosity, and the Bohm quantum pressure term.**

That chapter will attempt to put the two worlds together: a dissipative quantum fluid equation containing both

$$
-\nabla p_q
$$

$$
\nabla\cdot\Pi_q
$$

and

$$
-\frac{\hbar^2}{2m} \nabla \left( \frac{\nabla^2\sqrt n}{\sqrt n} \right).
$$

This is the point where kinetic theory, quantum mechanics, and fluid dynamics truly meet.
