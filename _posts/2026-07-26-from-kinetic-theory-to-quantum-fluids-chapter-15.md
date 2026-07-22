---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 15'
date: 2026-07-26
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-15/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

This is the right place to bring the journey to a deeper level. 

We have followed the path:

$$
\boxed{\text{Boltzmann} \rightarrow \text{BGK} \rightarrow \text{Chapman–Enskog} \rightarrow \text{Navier–Stokes}}
$$

then extended it:

$$
\boxed{\text{Maxwell–Boltzmann} \rightarrow \text{Fermi–Dirac/Bose–Einstein}}
$$

and finally connected it to:

$$
\boxed{\text{Wigner dynamics and quantum fluids}.}
$$

The final missing piece is the collision physics itself.

The BGK model is elegant because it captures conservation laws and relaxation, but it hides the microscopic mechanism of collisions. To understand real quantum transport, we must return to the quantum analogue of the Boltzmann collision integral.

---

# Chapter 15 — Beyond BGK: The Quantum Boltzmann Equation and the Uehling–Uhlenbeck Theory

---

## 15.1 Why BGK Is Not the Final Theory

The BGK equation replaces the collision operator:

$$
C[f]
$$

with:

$$
\boxed{C_{BGK}[f] = -\frac{1}{\tau}(f-f^{eq})}
$$

This assumes:

- all nonequilibrium modes relax at the same rate,
- relaxation is local,
- the collision time is independent of velocity,
- the collision mechanism only matters through \\(\tau\\).

This is extremely useful, but real collisions are more complicated.

In a quantum gas, collisions must know about:

- exchange symmetry,
- occupation blocking,
- stimulated scattering,
- conservation of momentum and energy.

---

## 15.2 Classical Boltzmann Collision Integral

The classical collision term is:

$$
\boxed{C[f_1] = \int d^3v_2 \int d\Omega \,g\sigma (f_1'f_2'-f_1f_2)}
$$

where:

- \\(g=\|\mathbf{v}_1-\mathbf{v}_2\|\\) is relative velocity,
- \\(\sigma\\) is the differential cross section,
- primes denote post-collision states.

The two terms are:

Loss:

$$
f_1f_2
$$

particles leaving the state.

Gain:

$$
f_1'f_2'
$$

particles entering the state.

---

## 15.3 Quantum Generalization

Quantum statistics modifies the probability of scattering into a final state.

The Uehling–Uhlenbeck equation introduces the factors:

$$
1+\eta f
$$

where:

$$
\eta= \begin{cases} +1,&\text{bosons},\\ -1,&\text{fermions}. \end{cases}
$$

The collision integral becomes:

$$
\boxed{C[f_1] = \int d^3v_2 d\Omega \,g\sigma \times \left[ f_1'f_2' (1+\eta f_1) (1+\eta f_2) - f_1f_2 (1+\eta f_1') (1+\eta f_2') \right].}
$$

This is the fundamental quantum kinetic equation for dilute quantum gases.

---

## 15.4 Interpretation of the Quantum Factors

## Bosons

For:

$$
\eta=+1
$$

we have:

$$
1+f.
$$

A populated state attracts more particles.

This is:

$$
\boxed{\text{Bose stimulation}.}
$$

---

## Fermions

For:

$$
\eta=-1
$$

we have:

$$
1-f.
$$

An occupied state blocks additional particles.

This is:

$$
\boxed{\text{Pauli blocking}.}
$$

---

## 15.5 Recovering the Equilibrium Distribution

At equilibrium:

$$
C[f^{eq}]=0.
$$

Therefore:

$$
f_1f_2(1+\eta f_1')(1+\eta f_2') = f_1'f_2'(1+\eta f_1)(1+\eta f_2).
$$

Taking logarithms gives:

$$
\ln\frac{f}{1+\eta f} = a+b\epsilon+\mathbf{c}\cdot\mathbf{p} .
$$

Solving gives:

$$
\boxed{f^{eq} = \frac{1}{ e^{\alpha+\beta(\epsilon-\mathbf{u}\cdot\mathbf{p})} -\eta }.}
$$

This is exactly:

- Bose–Einstein for \\(\eta=+1\\),
- Fermi–Dirac for \\(\eta=-1\\).

Thus equilibrium emerges from the collision operator itself.

---

## 15.6 Chapman–Enskog with the Full Quantum Collision Operator

Instead of:

$$
C[f] = -\frac{1}{\tau}(f-f^{eq})
$$

we use:

$$
C[f]=C_{UU}[f].
$$

Expand:

$$
f=f^{eq}+\epsilon f^{(1)}.
$$

Then:

$$
C[f] = C[f^{eq}] + \epsilon \frac{\delta C}{\delta f} f^{(1)} +\cdots .
$$

Since:

$$
C[f^{eq}]=0
$$

we obtain:

$$
\boxed{\mathcal L_q f^{(1)} = (\partial_t+v_i\partial_i)f^{eq}.}
$$

Here:

$$
\mathcal L_q
$$

is the linearized quantum collision operator.

---

## 15.7 The Difference from BGK

BGK gives:

$$
\boxed{f^{(1)} = -\tau Df^{eq}.}
$$

The exact theory gives:

$$
\boxed{f^{(1)} = -\mathcal L_q^{-1} Df^{eq}.}
$$

The inverse collision operator contains:

- angular scattering information,
- energy dependence,
- quantum statistics.

This is why exact transport calculations are difficult.

---

## 15.8 Transport Coefficients from the Collision Operator

The viscosity becomes:

$$
\boxed{\eta = -\frac{1}{10T} \langle \phi_\eta, \mathcal L_q^{-1} \phi_\eta \rangle}
$$

where the shear mode is:

$$
\phi_\eta = p_ip_j-\frac{1}{3}p^2\delta_{ij}.
$$

Similarly:

$$
\boxed{\kappa = -\frac{1}{3T^2} \langle \phi_\kappa, \mathcal L_q^{-1} \phi_\kappa \rangle .}
$$

The Chapman–Enskog structure survives, but the relaxation is no longer a single number.

---

## 15.9 Why Quantum Transport Can Be Surprising

The BGK picture suggests:

$$
\eta\sim p\tau .
$$

But the real quantum gas has competing effects.

---

## Fermions

Cooling causes:

$$
\text{Pauli blocking} \rightarrow \text{fewer collisions} \rightarrow \tau\uparrow
$$

so:

$$
\eta\uparrow .
$$

---

## Bosons

Cooling causes:

$$
\text{Bose stimulation} \rightarrow \text{more scattering} \rightarrow \tau\downarrow
$$

so viscosity can decrease.

---

## 15.10 The Hydrodynamic Limit

The final quantum hydrodynamic equations emerge when:

$$
\tau_{collision} \ll \tau_{hydrodynamic}.
$$

Then local equilibrium forms quickly.

The hierarchy becomes:

$$
\boxed{\text{Quantum collision physics}}
$$

determines:

$$
\eta,\kappa,p
$$

while:

$$
\boxed{\text{Conservation laws}}
$$

determine:

$$
\text{hydrodynamic equations}.
$$

---

## 15.11 The Complete Theoretical Map

We can now see the entire landscape:

---

## Level 1 — Classical kinetic theory

$$
\boxed{\partial_tf+v\nabla f=C_B[f]}
$$

$$\downarrow$$

$$\boxed{\text{Maxwell gas}}$$

$$\downarrow$$

$$\boxed{\text{Navier–Stokes}}$$

---

## Level 2 — Quantum kinetic theory

$$
\boxed{\partial_tf+v\nabla f=C_{UU}[f]}
$$

$$\downarrow$$

$$\boxed{\text{Fermi/Bose gases}}$$

$$\downarrow$$

$$\boxed{\text{quantum transport}}$$

---

## Level 3 — Quantum phase-space theory

$$
\boxed{\partial_tW+{H,W}_{Moyal}=C[W]}
$$

$$\downarrow$$

$$\boxed{\text{quantum coherence + collisions}}$$

$$\downarrow$$

$$\boxed{\text{quantum hydrodynamics}}$$

---

## Level 4 — Condensed quantum matter

$$
\boxed{\text{Gross–Pitaevskii / Landau theory}}
$$

$$\downarrow$$

$$\boxed{\text{superfluidity and collective quantum phenomena}}$$

---

## 15.12 Final Perspective

We started with a deceptively simple equation:

$$
\boxed{\partial_tf+v\cdot\nabla f = -\frac{1}{\tau}(f-f^{eq})}
$$

and uncovered an enormous structure:

- Maxwell statistics become Fermi and Bose statistics.
- Gaussian moments become quantum integrals.
- BGK relaxation becomes the quantum collision operator.
- Navier–Stokes becomes quantum hydrodynamics.
- Classical pressure becomes degeneracy pressure.
- Particle collisions coexist with wave coherence.

The deepest lesson is:

$$
\boxed{\text{Hydrodynamics is universal; constitutive physics carries the microscopic world.}}
$$

The Navier–Stokes equation does not know whether its pressure comes from:

- thermal motion,
- Pauli exclusion,
- Bose condensation,
- interactions,
- quantum coherence.

That information is encoded in the microscopic theory that generates the constitutive relations.

---

## Final Roadmap of the Journey

$$
\boxed{\text{Boltzmann equation}}
$$

$$\downarrow$$

$$
\boxed{\text{BGK approximation}}
$$

$$\downarrow$$

$$
\boxed{\text{Chapman–Enskog expansion}}
$$

$$\downarrow$$

$$
\boxed{\text{Navier–Stokes equations}}
$$

$$\downarrow$$

$$
\boxed{\text{Quantum BGK}}
$$

$$\downarrow$$

$$
\boxed{\text{Fermi/Bose quantum fluids}}
$$

$$\downarrow$$

$$
\boxed{\text{Wigner quantum hydrodynamics}}
$$

$$\downarrow$$

$$
\boxed{\text{Modern quantum transport theory}}
$$

---

This completes the arc from the classical kinetic derivation all the way to contemporary quantum fluid theory. 
