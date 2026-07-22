---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 14'
date: 2026-07-26
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-14/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

We have reached the point where the formal machinery meets real quantum matter. Up to now we have built a hierarchy:
$$
\text{Boltzmann} \rightarrow \text{BGK} \rightarrow \text{Chapman–Enskog} \rightarrow \text{quantum transport} \rightarrow \text{quantum hydrodynamics}.
$$

Now we ask:

**Where do these equations actually describe nature?**

The answer is: some of the cleanest examples are found in **ultracold atomic gases**, where experimentalists can tune density, interaction strength, dimensionality, and statistics with extraordinary precision.

---

# Chapter 14 — Applications to Ultracold Quantum Gases: Fermi Liquids, Bose Condensates, and Quantum Transport

---

## 14.1 Why Ultracold Atoms Are Ideal Quantum Fluids

Traditional quantum fluids are difficult to study:

- electrons in solids interact with lattices and impurities,
- neutron matter exists only in extreme astrophysical environments,
- liquid helium has complicated strong interactions.

Ultracold atoms provide a nearly ideal laboratory because:

- atoms are electrically neutral,
- interactions are tunable,
- densities are controllable,
- temperatures can reach the nanokelvin regime.

The system can be engineered close to the ideal assumptions behind kinetic theory.

---

## 14.2 The Main Experimental Classes

There are three major systems.

---

## 1. Weakly interacting Bose gases

Example:

$$
^{87}\mathrm{Rb}, \qquad ^{23}\mathrm{Na}
$$

Description:

$$
\boxed{\text{Gross–Pitaevskii equation}}
$$

with quantum pressure and mean-field interactions.

---

## 2. Degenerate Fermi gases

Examples:

$$
^{6}\mathrm{Li}, \qquad ^{40}\mathrm{K}
$$

Description:

$$
\boxed{\text{Fermi-liquid hydrodynamics}}
$$

with Pauli blocking and Fermi pressure.

---

## 3. Unitary Fermi gases

The most interesting strongly interacting regime.

Here:

$$
a_s\rightarrow\infty
$$

where \\(a_s\\) is the scattering length.

The system has no interaction length scale except:

$$
n^{-1/3}.
$$

This produces universal quantum fluid behavior.

---

## Part I — Bose–Einstein Condensates

---

## 14.3 Weakly Interacting Bose Gas

For a dilute Bose gas:

$$
na_s^3\ll1.
$$

The many-body wavefunction is described by:

$$
\Psi(\mathbf{r},t).
$$

The governing equation is the Gross–Pitaevskii equation:

$$
\boxed{i\hbar\partial_t\Psi = \left[ -\frac{\hbar^2\nabla^2}{2m} + V + g|\Psi|^2 \right] \Psi}
$$

with:

$$
g= \frac{4\pi\hbar^2a_s}{m}.
$$

---

## 14.4 Hydrodynamic Form of the Condensate

Writing:

$$
\Psi=\sqrt n e^{iS/\hbar}
$$

we obtain:

## Continuity

$$
\boxed{\partial_tn+\nabla\cdot(nu)=0}
$$

---

## Euler equation

$$
\boxed{m\frac{Du}{Dt} = -\nabla \left( gn+V+Q \right)}
$$

where

$$
Q = -\frac{\hbar^2}{2m} \frac{\nabla^2\sqrt n}{\sqrt n}.
$$

The three terms represent:

|Term|Meaning|
|---|---|
|\\(gn\\)|interaction pressure|
|\\(V\\)|trapping force|
|\\(Q\\)|quantum pressure|

---

## 14.5 Collective Oscillations

A major experimental probe is collective motion.

Small perturbations:

$$
n=n_0+\delta n
$$

produce sound waves.

Linearizing:

$$
\omega^2 = c^2k^2
$$

with:

$$
\boxed{c = \sqrt{\frac{gn}{m}}}
$$

the Bogoliubov sound speed.

At short wavelengths, the quantum pressure dominates:

$$
\omega^2 = c^2k^2 + \frac{\hbar^2k^4}{4m^2}.
$$

The \\(k^4\\) term is a direct signature of quantum pressure.

---

## Part II — Degenerate Fermi Gases

---

## 14.6 Ideal Fermi Gas Hydrodynamics

For noninteracting fermions:

$$
p_F = \frac{2}{5}nE_F.
$$

The Euler equation is:

$$
\boxed{mn\frac{Du}{Dt} = -\nabla p_F}
$$

with:

$$
E_F= \frac{\hbar^2}{2m} (3\pi^2n)^{2/3}.
$$

The sound velocity is:

$$
\boxed{c_F = \sqrt{\frac{1}{m} \frac{\partial p_F}{\partial n}}}
$$

which gives:

$$
\boxed{c_F= \frac{v_F}{\sqrt3}.}
$$

---

## 14.7 Pauli Blocking and Transport

The collision rate is suppressed:

$$
\tau^{-1} \propto T^2.
$$

Why?

At low temperature:

Most states are occupied.

Only particles within:

$$
k_BT
$$

of the Fermi surface can scatter.

This dramatically changes viscosity.

---

## 14.8 Fermi-Liquid Viscosity

The kinetic estimate:

$$
\mu_F \sim nmv_F^2\tau_F
$$

becomes:

$$
\boxed{\mu_F \propto T^{-2}.}
$$

Thus colder Fermi liquids can become extremely viscous.

However, the ratio:

$$
\frac{\hbar\mu}{s}
$$

is often the more meaningful quantity.

---

## Part III — The Unitary Fermi Gas

---

## 14.9 The Unitary Limit

The scattering length becomes infinite:

$$
\boxed{|a_s|\rightarrow\infty.}
$$

The interaction range disappears from the problem.

The only scale is:

$$
k_F.
$$

Therefore the energy must be:

$$
E = \xi E_{FG}
$$

where \\(\xi\\) is the Bertsch parameter.

The pressure becomes:

$$
\boxed{p = \frac{2}{5}\xi nE_F.}
$$

---

## 14.10 Universal Hydrodynamics

Because the system has no microscopic scale:

$$
\eta
$$

(the shear viscosity) must scale as:

$$
\boxed{\eta = \hbar n \alpha(T/T_F)}
$$

where \\(\alpha\\) is dimensionless.

This is a powerful result.

The transport coefficient is determined entirely by:

$$
T/T_F.
$$

---

## 14.11 The Famous Low Viscosity Quantum Fluid

Experiments found that the unitary Fermi gas has extremely low viscosity relative to entropy:

$$
\boxed{\frac{\eta}{s}}
$$

becomes very small near the superfluid transition.

This behavior is similar in spirit to:

- quark–gluon plasma,
- strongly coupled electronic fluids.

---

## 14.12 Hydrodynamic Equations for a Unitary Fermi Gas

The equations resemble Navier–Stokes:

Continuity:

$$
\partial_tn+\nabla\cdot(nu)=0
$$

Momentum:

$$
\boxed{mn\frac{Du_i}{Dt} = -\partial_ip + \partial_j\Pi_{ij}}
$$

Energy:

$$
\boxed{\partial_tE+\nabla\cdot[(E+p)u] = \nabla\cdot(\Pi u) -\nabla\cdot q .}
$$

The difference is hidden in:

$$
p(n,T)
$$

$$
\eta(n,T)
$$

$$
\kappa(n,T).
$$

---

## 14.13 Connecting Back to Chapman–Enskog

The Chapman–Enskog picture predicts:

$$
\boxed{\text{equilibrium} \rightarrow \text{moments} \rightarrow \text{transport coefficients}.}
$$

For ultracold gases:

### Bose condensate:

Dominant physics:

$$
\hbar\nabla^2\sqrt n
$$

and interactions.

---

### Fermi liquid:

Dominant physics:

$$
E_F
$$

Pauli blocking, and Fermi surface excitations.

---

### Unitary gas:

Dominant physics:

strong correlations and universal scaling.

---

## 14.14 The Grand Comparison

|System|Dominant physics|Main equation|
|---|---|---|
|Classical gas|thermal motion|Navier–Stokes|
|Bose condensate|coherence|Gross–Pitaevskii|
|Ideal Fermi gas|exclusion|Fermi hydrodynamics|
|Unitary Fermi gas|strong correlations|quantum Navier–Stokes|
|Quantum kinetic gas|statistics + collisions|Chapman–Enskog|

---

## 14.15 The Main Lesson

The same hydrodynamic language describes very different microscopic worlds.

A pressure gradient:

$$
-\nabla p
$$

may represent:

- ordinary thermal pressure,
- Fermi degeneracy pressure,
- Bose interaction pressure,
- universal strongly interacting pressure.

A viscosity coefficient:

$$
\eta
$$

may arise from:

- ordinary collisions,
- quantum-limited scattering,
- many-body correlations.

The equations look similar because conservation laws are universal.

The physics is hidden inside the constitutive relations.

---

## Where we go next

A natural continuation is:

# Chapter 15 — Beyond BGK: Full Quantum Collision Operators and the Limits of Relaxation-Time Models

There we would examine:

- the Uehling–Uhlenbeck equation,
- quantum collision integrals,
- Bose enhancement and Pauli blocking inside collisions,
- why BGK is only an approximation,
- how true quantum transport coefficients are calculated.

That chapter would complete the journey from the simple BGK model all the way to modern quantum kinetic theory.
