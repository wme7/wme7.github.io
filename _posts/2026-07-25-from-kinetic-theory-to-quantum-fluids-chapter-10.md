---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 10'
date: 2026-07-25
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-10/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

This is a very good point in the derivation to stop and compare the three theories side by side, because the underlying architecture is now visible.

Before moving on, I will make one refinement to the previous chapter: the compact statement

$$
\mu_q=p_q\tau
$$

is a special feature of the simplest single-relaxation-time BGK closure. More general quantum kinetic models (with energy-dependent relaxation times, realistic collision integrals, or Bose/Fermi scattering kernels) do **not** necessarily preserve this simple relation. The Chapman–Enskog structure is robust, but the transport coefficients depend on the collision model. We will keep the BGK assumption throughout this comparison.

---

# Chapter 10 — Classical vs Fermi vs Bose Chapman–Enskog Theory

## 10.1 The Big Picture

The three theories describe the same physical process:

$$
\text{microscopic particle motion} \rightarrow \text{kinetic equation} \rightarrow \text{hydrodynamic equations}.
$$

The difference is the statistics of the particles:

|Gas|Exchange symmetry|Equilibrium statistics|
|---|---|---|
|Classical gas|distinguishable particles|Maxwell–Boltzmann|
|Fermi gas|antisymmetric wavefunction|Fermi–Dirac|
|Bose gas|symmetric wavefunction|Bose–Einstein|

The Chapman–Enskog machinery itself is almost unchanged.

---

## 10.2 Kinetic Equation Comparison

## Classical BGK

$$
\boxed{\partial_tf+v_i\partial_if = -\frac{1}{\tau}(f-f_{MB})}
$$

with

$$
f_{MB} = n \left( \frac{m}{2\pi k_BT} \right)^{3/2} e^{-\frac{mc^2}{2k_BT}}.
$$

---

## Fermi BGK

$$
\boxed{\partial_tf+v_i\partial_if = -\frac{1}{\tau}(f-f_F)}
$$

where

$$
\boxed{f_F = \frac{g}{h^3} \frac{1}{ z^{-1}e^{mc^2/(2k_BT)}+1 }}
$$

---

## Bose BGK

$$
\boxed{\partial_tf+v_i\partial_if = -\frac{1}{\tau}(f-f_B)}
$$

where

$$
\boxed{f_B = \frac{g}{h^3} \frac{1}{ z^{-1}e^{mc^2/(2k_BT)}-1 }}
$$

---

## 10.3 Chapman–Enskog Expansion

The expansion is identical:

$$
f = f^{(0)} + \varepsilon f^{(1)} +\cdots
$$

with

$$
f^{(0)} = f^{eq}.
$$

The first correction is always

$$
\boxed{f^{(1)} = -\tau (\partial_t+v_i\partial_i)f^{eq}.}
$$

The difference is entirely contained inside the equilibrium distribution.

---

## 10.4 The Classical Equilibrium Derivative

For Maxwell–Boltzmann statistics:

$$
Df_{MB} = f_{MB}D\ln f_{MB}.
$$

The logarithmic derivative gives:

$$
\boxed{D\ln f_{MB} = 2\beta \left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i + \frac{1}{T} c_i \left( \beta c^2-\frac{5}{2} \right) \partial_iT.}
$$

---

## 10.5 The Quantum Equilibrium Derivative

For Bose and Fermi gases:

$$
Df_q = -f_q(1-\eta f_q)D\ln X .
$$

The new factor is

$$
\boxed{1-\eta f_q}
$$

with

$$
\eta= \begin{cases} +1,&\text{Fermi},\\ -1,&\text{Bose}. \end{cases}
$$

Therefore:

### Fermions

$$
\boxed{1-f_F}
$$

reduces scattering into occupied states.

---

### Bosons

$$
\boxed{1+f_B}
$$

enhances occupation of already populated states.

---

## 10.6 Conservation Laws

A remarkable result:

All three theories give the same conservation structure.

## Mass

$$
\boxed{\partial_t\rho+ \nabla\cdot(\rho u)=0}
$$

---

## Momentum

$$
\boxed{\partial_t(\rho u_i) + \partial_j (\rho u_iu_j+P_{ij}) =0}
$$

---

## Energy

$$
\boxed{\partial_tE + \partial_i(Eu_i+P_{ij}u_j+q_i) =0}
$$

The collision invariants do not depend on statistics.

---

## 10.7 Equation of State Comparison

This is where the first major difference appears.

---

## Classical Gas

$$
\boxed{p=nk_BT}
$$

---

## Fermi Gas

$$
\boxed{p_F = \frac{gk_BT}{\lambda_T^3} G_{5/2}^{(+)}(z)}
$$

where

$$
G_\nu^{(+)}
$$

is the Fermi integral.

At low temperature:

$$
p_F \sim \frac{2}{5}nE_F.
$$

The pressure remains finite even as

$$
T\rightarrow0
$$

because of Pauli exclusion.

---

## Bose Gas

$$
\boxed{p_B = \frac{gk_BT}{\lambda_T^3} G_{5/2}^{(-)}(z)}
$$

Near condensation,

$$
z\rightarrow1^-
$$

and the thermodynamics becomes dominated by collective quantum behavior.

---

## 10.8 Velocity Moments

This is where the mathematics changes.

---

## Classical Moments

The Maxwellian gives:

$$
\int c^2f_{MB}d^3c = 3n\frac{k_BT}{m}
$$

and

$$
\int c^4f_{MB}d^3c = 15n \left( \frac{k_BT}{m} \right)^2 .
$$

---

## Quantum Moments

The same tensor identities hold:

$$
\int c_ic_jF(c^2)d^3c = \frac{\delta_{ij}}3I_2
$$

but

$$
I_2
$$

is now:

$$
\boxed{I_2 \propto G_{5/2}^{(\eta)}(z)}
$$

rather than a Gaussian integral.

---

## 10.9 Viscosity Comparison

## Classical BGK

$$
\boxed{\mu_{MB}=p\tau}
$$

---

## Fermi BGK

$$
\boxed{\mu_F=p_F\tau}
$$

within the single-relaxation-time approximation.

At high degeneracy:

- pressure increases due to Pauli exclusion,
- transport becomes controlled by the Fermi energy scale.

---

## Bose BGK

$$
\boxed{\mu_B=p_B\tau}
$$

Above condensation:

- Bose enhancement modifies collision rates,
- viscosity depends strongly on fugacity.

Below condensation:

- a single-component BGK description is insufficient.

---

## 10.10 Thermal Conductivity Comparison

The heat flux always has the form:

$$
\boxed{q_i=-\kappa\nabla_iT .}
$$

The coefficient differs.

---

## Classical

$$
\boxed{\kappa_{MB} = \frac{5}{2} \frac{k_B}{m} p\tau}
$$

---

## Quantum

$$
\boxed{\kappa_q = \frac{5}{2} \frac{k_B}{m} p_q\tau R_q(z)}
$$

where

$$
R_q(z)
$$

contains ratios of quantum statistical integrals.

---

## 10.11 Dilute Limit

The most important consistency check:

Let

$$
z\ll1.
$$

Then:

$$
G_\nu^{(+)}(z) \rightarrow z
$$

$$
G_\nu^{(-)}(z) \rightarrow z.
$$

Therefore:

$$
p_F,p_B \rightarrow nk_BT.
$$

The quantum factors become:

$$
1-\eta f_q\rightarrow1.
$$

Thus:

$$
\boxed{Fermi\rightarrow Classical}
$$

and

$$
\boxed{Bose\rightarrow Classical.}
$$

The Maxwell–Boltzmann theory is recovered smoothly.

---

## 10.12 Conceptual Summary Table

|Quantity|Classical|Fermi|Bose|
|---|---|---|---|
|Equilibrium|Maxwell|Fermi–Dirac|Bose–Einstein|
|Quantum factor|(1)|(1-f)|(1+f)|
|Pressure|\\(nk_BT\\)|\\(G_{5/2}^{(+)}\\)|\\(G_{5/2}^{(-)}\\)|
|Tensor structure|same|same|same|
|Stress tensor|Newtonian|Newtonian|Newtonian|
|Heat flux|Fourier|Fourier|Fourier|
|Moments|Gaussian|Fermi integrals|Bose integrals|
|Dilute limit|—|MB|MB|

---

## 10.13 The Deep Lesson

The Chapman–Enskog expansion separates two layers of physics:

## Layer 1 — Hydrodynamics

Determined by:

- conservation laws,
- symmetry,
- Galilean invariance.

This part is universal.

---

## Layer 2 — Statistics and collisions

Determined by:

- equilibrium occupation,
- quantum exchange symmetry,
- collision model.

This part determines:

- pressure,
- viscosity,
- thermal conductivity.

---

At this point we have built the complete bridge:

$$
\boxed{\text{Boltzmann/BGK} \rightarrow \text{Chapman–Enskog} \rightarrow \text{Navier–Stokes}}
$$

for:

$$
\boxed{\text{classical, Fermi, and Bose gases}.}
$$

---

A natural next chapter would be a more advanced one: **deriving the quantum Navier–Stokes equations in the degenerate limits**—the low-temperature Fermi gas and the near-condensation Bose gas—where the Fermi pressure, Pauli blocking, Bose enhancement, and quantum transport coefficients become especially interesting. This is where the connection to ultracold atomic gases, electron fluids, and quantum hydrodynamics becomes most direct.