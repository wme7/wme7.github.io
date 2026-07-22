---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 11'
date: 2026-07-25
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-11/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

This is where the kinetic derivation connects with modern quantum fluids. Up to now we have treated quantum statistics as a modification of the equilibrium distribution. In this chapter we will explore what happens in the **strongly quantum regimes**, where the gas is no longer a small correction to the classical picture.

There are two fundamentally different limits:

1. **Degenerate Fermi gases**
    - dominated by Pauli exclusion,
    - finite pressure exists even at zero temperature,
    - transport is controlled by excitations near the Fermi surface.
2. **Degenerate Bose gases**
    - dominated by macroscopic occupation of quantum states,
    - Bose enhancement becomes extreme,
    - a condensate component appears and a single-fluid kinetic description becomes incomplete.

The interesting point is that the Chapman–Enskog framework still tells us _where_ these effects enter.

---

# Chapter 11 — Degenerate Quantum Fluids: Fermi and Bose Limits of Quantum Navier–Stokes

---

## 11.1 The Quantum Degeneracy Parameter

The crossover between classical and quantum behavior is controlled by

$$
\boxed{n\lambda_T^3}
$$

where

$$
\lambda_T= \frac{h}{\sqrt{2\pi mk_BT}}
$$

is the thermal wavelength.

Three regimes exist:

$$
n\lambda_T^3\ll1
$$

classical gas,

$$
n\lambda_T^3\sim1
$$

quantum gas,

$$
n\lambda_T^3\gg1
$$

strongly degenerate gas.

The Chapman–Enskog derivation remains formally valid as long as local equilibrium exists, but the thermodynamics and collision physics change dramatically.

---

## Part I — Degenerate Fermi Fluids

---

## 11.2 The Zero-Temperature Fermi Gas

For fermions,

$$
f_F = \frac{1} {z^{-1}e^{mc^2/(2k_BT)}+1}.
$$

At very low temperature,

$$
T\rightarrow0
$$

the distribution approaches a step function:

$$
\boxed{f_F(p) = \Theta(p_F-p)}
$$

where

$$
p_F = \hbar(3\pi^2n)^{1/3}
$$

is the Fermi momentum.

The particles fill all states up to the Fermi surface.

---

## 11.3 Fermi Pressure

The pressure becomes

$$
p_F = \frac{2}{5} nE_F
$$

where

$$
\boxed{E_F= \frac{p_F^2}{2m}}
$$

is the Fermi energy.

This is a remarkable result:

$$
\boxed{p_F\neq0 \quad\text{even when}\quad T=0.}
$$

The pressure is not thermal.

It is a purely quantum mechanical consequence of the Pauli exclusion principle.

---

## 11.4 Quantum Euler Equation for a Fermi Fluid

The momentum equation becomes

$$
\rho \frac{D u_i}{Dt} = -\partial_i p_F .
$$

Using

$$
p_F = \frac{2}{5}nE_F
$$

we obtain

$$
\boxed{\rho \frac{D\mathbf{u}}{Dt} = -\nabla \left( \frac{2}{5}nE_F \right).}
$$

This is the macroscopic manifestation of degeneracy pressure.

It appears in:

- electron gases in metals,
- white dwarf stars,
- neutron matter,
- ultracold Fermi atoms.

---

## 11.5 Fermi Surface and Transport

At low temperature, almost all states are blocked.

A collision can only occur if particles are excited near the Fermi surface.

The available phase space scales as

$$
\sim \left(\frac{k_BT}{E_F}\right)^2.
$$

Therefore,

$$
\boxed{\tau_F^{-1} \propto T^2.}
$$

This is the famous Fermi-liquid result.

Consequently,

$$
\boxed{\mu_F \propto \tau_F \propto T^{-2}.}
$$

The viscosity increases strongly as the temperature decreases.

---

## 11.6 The Fermi Heat Flux

Unlike viscosity, heat transport requires excitations.

At zero temperature:

$$
\boxed{\kappa_F\rightarrow0.}
$$

There are no thermal excitations available.

At low temperature:

$$
C_V \propto T
$$

and

$$
\kappa_F \sim C_V v_F^2\tau_F.
$$

Therefore,

$$
\boxed{\kappa_F \propto T^{-1}.}
$$

This is a hallmark of degenerate Fermi liquids.

---

## Part II — Degenerate Bose Fluids

---

## 11.7 Bose–Einstein Condensation

For bosons,

$$
f_B = \frac{1}{ z^{-1}e^{mc^2/(2k_BT)}-1 }.
$$

The fugacity satisfies

$$
0<z\le1.
$$

At the critical temperature:

$$
z\rightarrow1.
$$

The excited states cannot accommodate all particles.

The excess particles accumulate in the ground state:

$$
\boxed{N_0/N = 1- \left( \frac{T}{T_c} \right)^{3/2}.}
$$

This is Bose–Einstein condensation.

---

## 11.8 Why Single-Fluid BGK Breaks Down

The kinetic distribution describes thermal particles.

But the condensate is a coherent quantum state.

The system naturally separates into:

### Condensate

$$
n_0,\mathbf{u}_0
$$

### Thermal cloud

$$
n_T,\mathbf{u}_T
$$

Therefore the hydrodynamics becomes:

$$
\boxed{\text{two-fluid hydrodynamics}.}
$$

This is the foundation of Landau's theory of superfluidity.

---

## 11.9 Superfluid Equations

The condensate velocity is not determined by collisions.

Instead,

$$
\boxed{\mathbf{u}_s = \frac{\hbar}{m}\nabla\phi}
$$

where \\(\phi\\) is the condensate phase.

The superfluid component obeys

$$
\boxed{m \frac{\partial\mathbf{u}_s}{\partial t} + \nabla \left( \frac{1}{2}mu_s^2 +\mu \right) =0.}
$$

This is no longer a dissipative Navier–Stokes equation.

It is closer to an inviscid Euler equation.

---

## 11.10 Thermal Bose Component

The normal component still obeys kinetic theory.

Its transport coefficients involve Bose integrals:

$$
G_\nu^{(-)}(z).
$$

Near condensation:

$$
z\rightarrow1^-
$$

these integrals become strongly enhanced.

The collision term contains

$$
1+f_B
$$

which increases scattering into occupied states.

This leads to:

- enhanced scattering,
- unusual viscosity,
- anomalous thermal transport.

---

## 11.11 Quantum Navier–Stokes Structure

For a degenerate quantum gas we can write schematically:

$$
\boxed{\rho \frac{D\mathbf{u}}{Dt} = -\nabla p_q + \nabla\cdot\Pi_q}
$$

with

$$
\Pi_q = -\mu_q \left[ \nabla\mathbf{u} + (\nabla\mathbf{u})^T -\frac{2}{3}I\nabla\cdot\mathbf{u} \right].
$$

The new physics is entirely in:

$$
p_q
$$

$$
\mu_q
$$

$$
\kappa_q.
$$

---

## 11.12 Comparison of Extreme Limits

||Classical|Degenerate Fermi|Condensed Bose|
|---|---|---|---|
|Pressure source|thermal|Pauli exclusion|interactions/thermal cloud|
|\\(T=0\\) pressure|zero|finite|depends on interactions|
|Collisions|normal|Pauli blocked|Bose enhanced|
|Viscosity|finite|grows at low \\(T\\)|strongly modified|
|Heat conduction|classical|vanishes as \\(T\to0\\)|two-fluid transport|
|Hydrodynamics|Navier–Stokes|Fermi liquid|superfluid hydrodynamics|

---

## 11.13 The Deeper Connection

The Chapman–Enskog expansion reveals something subtle:

The Navier–Stokes equations are not fundamentally "classical."

Their structure comes from:

- conservation laws,
- symmetry,
- near-equilibrium expansion.

Those ingredients also exist in quantum gases.

What changes is the **equation of state and transport physics**.

The same mathematical skeleton can describe:

- air,
- electron fluids,
- neutron matter,
- ultracold atomic gases,

provided the appropriate kinetic equilibrium and collision physics are inserted.

---

## Where this leads next

A particularly interesting path would be:

**Chapter 12 — From Quantum BGK to Quantum Hydrodynamics: the connection with the Gross–Pitaevskii equation, Wigner functions, and quantum pressure terms.**

That chapter would address a subtle point: the Navier–Stokes equations derived here are _quantum statistical_ equations, but they do not yet contain the dispersive "quantum pressure" term familiar from Bose–Einstein condensates:

$$
-\frac{\hbar^2}{2m} \nabla \left( \frac{\nabla^2\sqrt n}{\sqrt n} \right).
$$

Understanding why that term is absent from BGK-based quantum hydrodynamics—and how it emerges from a different kinetic starting point—is one of the most interesting bridges between kinetic theory and modern quantum fluids.