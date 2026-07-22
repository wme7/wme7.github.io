---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 13'
date: 2026-07-26
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-13/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

This is the point where the two threads we have developed—**quantum kinetic theory** and **wave-mechanical quantum hydrodynamics**—are brought together.

A small warning before we start: a fully rigorous derivation of a dissipative quantum Navier–Stokes equation with _both_ Bose/Fermi statistics and Bohm quantum pressure requires a specific quantum kinetic model (for example, a Wigner–Boltzmann equation with a chosen collision operator). There is no single universally accepted "quantum Navier–Stokes equation." What we derive here is the **structure obtained from a semiclassical Wigner–Chapman–Enskog expansion** and show where each term originates.

---

# Chapter 13 — Quantum Navier–Stokes–Wigner Equations: Combining Statistics, Dissipation, and Quantum Pressure

---

## 13.1 The Goal

We want a hydrodynamic equation containing three types of physics:

### 1. Thermodynamic pressure

from quantum statistics:

$$
p_q(n,T)
$$

with Bose/Fermi corrections.

---

### 2. Dissipation

from kinetic collisions:

$$
\Pi_{ij}^{visc}, \qquad q_i .
$$

---

### 3. Quantum coherence

from wave mechanics:

$$
Q = -\frac{\hbar^2}{2m} \frac{\nabla^2\sqrt n}{\sqrt n}.
$$

The final momentum equation should therefore have the schematic form:

$$
\boxed{\rho\frac{D u_i}{Dt} = -\partial_i p_q + \partial_j\Pi_{ij} = n\partial_i Q .}
$$

Each term has a different microscopic origin.

---

## 13.2 The Wigner–Boltzmann Equation

The starting point is the Wigner function:

$$
W(\mathbf{x},\mathbf{p},t).
$$

The evolution equation is:

$$
\boxed{\partial_tW + \frac{\mathbf{p}}{m}\cdot\nabla_xW = \nabla_xV\cdot\nabla_pW + \mathcal{M}_\hbar[W] = C[W].}
$$

Here:

- (C[W]) is the collision operator,
- \\(\mathcal{M}_\hbar\\) is the quantum correction.

The Moyal operator is

$$
\mathcal{M}_\hbar[W] = \sum_{l=1}^{\infty} \frac{(-1)^l}{(2l+1)!} \left( \frac{\hbar}{2} \right)^{2l} \nabla_x^{2l+1}V \cdot \nabla_p^{2l+1}W .
$$

The first correction is:

$$
\boxed{\mathcal{M}_\hbar \approx -\frac{\hbar^2}{24} \nabla_x^3V \cdot \nabla_p^3W .}
$$

The classical Boltzmann equation is recovered as:

$$
\hbar\rightarrow0.
$$

---

## 13.3 Hydrodynamic Moments of the Wigner Function

The definitions are analogous to kinetic theory.

Density:

$$
\boxed{n= \int W\,d^3p}
$$

Velocity:

$$
\boxed{nu_i = \int \frac{p_i}{m}W\,d^3p}
$$

Stress tensor:

$$
\boxed{P_{ij} = \int \frac{(p_i-mu_i)(p_j-mu_j)}{m} W\,d^3p}
$$

Heat flux:

$$
\boxed{q_i = \frac{1}{2} \int c^2c_iW\,d^3p}
$$

---

## 13.4 Zeroth Moment: Continuity Equation

Integrating the Wigner equation over momentum:

$$
\int d^3p,(\text{Wigner equation})
$$

gives:

$$
\boxed{\partial_t n + \nabla\cdot(n\mathbf{u}) = 0 .}
$$

The quantum corrections vanish because they are total derivatives in momentum space.

This is exactly the same conservation law obtained from BGK theory.

---

## 13.5 First Moment: Momentum Equation

Multiply by \\(p_i/m\\):

$$
\int \frac{p_i}{m} (\text{Wigner equation}) d^3p .
$$

The result is:

$$
\boxed{mn \frac{Du_i}{Dt} = -\partial_jP_{ij} = n\partial_iV + F_i^{Q}.}
$$

The pressure tensor now has two parts:

$$
\boxed{P_{ij} = P_{ij}^{kin} + P_{ij}^{Q}.}
$$

---

## 13.6 Separation of the Pressure Tensor

The kinetic part is:

$$
P_{ij}^{kin} = p_q\delta_{ij} + \Pi_{ij}.
$$

Here:

$$
p_q
$$

is the Bose/Fermi equation of state.

The viscous correction is:

$$
\boxed{\Pi_{ij} = -\mu_q \left( \partial_i u_j+ \partial_j u_i -\frac{2}{3}\delta_{ij}\nabla\cdot u \right).}
$$

This is exactly the Chapman–Enskog result.

---

## 13.7 Quantum Pressure Contribution

The coherent part is:

$$
\boxed{P_{ij}^{Q} = \frac{\hbar^2}{4m} \left( \frac{\partial_i n\partial_j n}{n} - \partial_i\partial_j n \right).}
$$

Taking the divergence:

$$
\partial_jP_{ij}^{Q} = n\partial_iQ.
$$

Therefore:

$$
\boxed{F_i^{Q} = -n\partial_iQ .}
$$

The momentum equation becomes:

$$
\boxed{mn \frac{D u_i}{Dt} = -\partial_i p_q + \partial_j\Pi_{ij} = n\partial_iQ .}
$$

This is the quantum Navier–Stokes–Wigner equation.

---

## 13.8 Energy Equation

The total energy density is:

$$
E = \frac{1}{2}mn u^2 + \epsilon_q + \epsilon_Q .
$$

The contributions are:

Classical kinetic energy:

$$
\frac{1}{2}mn u^2
$$

Quantum statistical internal energy:

$$
\epsilon_q = \epsilon(n,T)
$$

Quantum coherence energy:

$$
\boxed{\epsilon_Q = \frac{\hbar^2}{2m} |\nabla\sqrt n|^2 .}
$$

The energy equation becomes:

$$
\boxed{\begin{aligned} \partial_tE + \nabla\cdot \left[ (E+p_q)\mathbf{u} \right] =& \nabla\cdot(\Pi\cdot\mathbf{u}) \ & -\nabla\cdot q \ & +\text{quantum flux}. \end{aligned}}
$$

---

## 13.9 Final Quantum Navier–Stokes–Wigner System

We have:

## Continuity

$$
\boxed{\partial_t n+ \nabla\cdot(n\mathbf{u})=0}
$$

---

## Momentum

$$
\boxed{mn \frac{D\mathbf{u}}{Dt} = -\nabla p_q + \nabla\cdot\Pi = n\nabla Q}
$$

where

$$
\boxed{Q = -\frac{\hbar^2}{2m} \frac{\nabla^2\sqrt n}{\sqrt n}}
$$

and

$$
\boxed{\Pi_{ij} = -\mu_q \left( \partial_i u_j+\partial_j u_i -\frac{2}{3}\delta_{ij}\nabla\cdot u \right).}
$$

---

## Heat equation

$$
\boxed{q=-\kappa_q\nabla T .}
$$

---

## 13.10 Classical and Quantum Limits

## Classical limit

If:

$$
\hbar\rightarrow0
$$

then:

$$
Q\rightarrow0.
$$

The equation becomes:

$$
\boxed{\text{quantum BGK Navier–Stokes} \rightarrow \text{classical Navier–Stokes}.}
$$

---

## Collisionless quantum limit

If:

$$
\mu_q,\kappa_q\rightarrow0
$$

then:

$$
\boxed{\text{quantum Navier–Stokes} \rightarrow \text{quantum Euler/Gross–Pitaevskii hydrodynamics}.}
$$

---

## 13.11 Physical Interpretation of the Three Forces

The final momentum equation:

$$
mn\frac{D\mathbf{u}}{Dt} = -\nabla p_q + \nabla\cdot\Pi = n\nabla Q
$$

contains:

### Statistical pressure

$$
-\nabla p_q
$$

"particles resist compression."

---

### Viscous stress

$$
\nabla\cdot\Pi
$$

"collisions dissipate gradients."

---

### Quantum pressure

$$
-n\nabla Q
$$

"wavefunctions resist localization."

---

These are three fundamentally different mechanisms.

---

## 13.12 The Unified View

We can now summarize the whole journey:

$$
\boxed{\text{Boltzmann}}
$$

$$\downarrow$$

$$
\boxed{\text{BGK}}
$$

$$\downarrow$$

$$
\boxed{\text{Chapman–Enskog}}
$$

$$\downarrow$$

$$
\boxed{\text{Navier–Stokes}}
$$

then extend:

$$
+
$$

$$
\boxed{\text{Fermi/Bose statistics}}
$$

$$\downarrow$$

$$
\boxed{\text{quantum kinetic hydrodynamics}}
$$

and finally:

$$
+
$$

$$
\boxed{\text{Wigner coherence}}
$$

$$\downarrow$$

$$
\boxed{\text{quantum Navier–Stokes–Wigner equations}.}
$$

---

The next chapter could now explore an especially fascinating application:

**Chapter 14 — Ultracold Atomic Gases: Applying Quantum Navier–Stokes Theory to Unitary Fermi Gases and Bose–Einstein Condensates.**

This would connect the formal derivations to real systems where these equations are actually tested: viscosity minima, superfluidity, collective modes, and experimental measurements of quantum transport.
