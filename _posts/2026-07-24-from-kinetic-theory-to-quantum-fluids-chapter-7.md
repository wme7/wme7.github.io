---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 7'
date: 2026-07-24
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-7/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---


We have now completed the classical derivation up to the Navier–Stokes closure. This gives us a very useful reference point, because the quantum derivation will not be a completely new calculation—it will be a **deformation of the classical calculation**.

The central question we will answer is:

> If the particles obey Bose–Einstein or Fermi–Dirac statistics instead of Maxwell–Boltzmann statistics, how does the Chapman–Enskog derivation change?

The short answer is:

- The **kinematic structure** of the derivation is almost unchanged.
- The **equilibrium distribution** changes.
- The **velocity moments** change.
- The **equation of state and transport coefficients** become functions of quantum statistics.

Let's begin.

---

# Chapter 7 — Quantum Kinetic Theory: From BGK to Quantum Hydrodynamics

## 7.1 Why Classical Kinetic Theory Must Be Modified

The classical Boltzmann distribution assumes that particles are distinguishable and that occupation numbers of phase-space states are small.

This requires the gas to be dilute in the quantum sense:

$$
n\lambda_T^3\ll1
$$

where

$$
\lambda_T = \frac{h}{\sqrt{2\pi mk_BT}}
$$

is the thermal de Broglie wavelength.

When

$$
n\lambda_T^3\sim1
$$

the wave nature of particles becomes important.

The classical Maxwell–Boltzmann distribution

$$
f^{eq}_{MB} = n \left( \frac{m}{2\pi k_BT} \right)^{3/2} e^{-\frac{mc^2}{2k_BT}}
$$

is no longer correct.

The occupation of quantum states must be included.

---

## 7.2 Quantum Statistics: Bose and Fermi Symmetry

Identical particles are not distinguishable.

The many-particle wavefunction must satisfy:

### Bosons

Particles with integer spin satisfy

$$
\Psi(\ldots,x_i,\ldots,x_j,\ldots) = -\Psi(\ldots,x_j,\ldots,x_i,\ldots).
$$

They may occupy the same quantum state.

Examples:

- photons,
- helium-4 atoms,
- many composite particles.

---

### Fermions

Particles with half-integer spin satisfy

$$
\Psi(\ldots,x_i,\ldots,x_j,\ldots) = -\Psi(\ldots,x_j,\ldots,x_i,\ldots).
$$

They obey the Pauli exclusion principle.

Examples:

- electrons,
- neutrons,
- helium-3 atoms.

---

This symmetry modifies the equilibrium occupation number.

---

## 7.3 The Quantum Equilibrium Distribution

The equilibrium distribution is obtained by maximizing the **quantum entropy**, not the classical Boltzmann entropy.

The result is

$$
\boxed{f^{eq}_q = \frac{g}{h^3} \frac{1} {\exp \left[ \frac{\frac{1}{2}m c^2-\mu}{k_BT} \right] +\eta}.}
$$

Here:

$$
\eta= \begin{cases} +1,&\text{fermions},\[4pt] -1,&\text{bosons}, \end{cases}
$$

and

- \\(g\\) is the internal degeneracy (spin states),
- \\(\mu\\) is the chemical potential.

The variable

$$
c=v-u
$$

is still the peculiar velocity.

This is important:

$$
\boxed{\text{The Galilean structure is unchanged.}}
$$

The equilibrium is still isotropic in the local rest frame.

---

## 7.4 Classical Limit

The Maxwellian must emerge when quantum effects disappear.

Define the fugacity

$$
z=e^{\mu/(k_BT)}.
$$

Then

$$
f^{eq}_q = \frac{g}{h^3} \frac{1} {z^{-1}e^{\frac{mc^2}{2k_BT}}+\eta}.
$$

If

$$
z\ll1
$$

then

$$
z^{-1}e^{mc^2/(2k_BT)}\gg1.
$$

Therefore,

$$
\frac{1}{z^{-1}e^x+\eta} \approx ze^{-x}.
$$

Hence

$$
f^{eq}_q \rightarrow \frac{gz}{h^3} e^{-\frac{mc^2}{2k_BT}}.
$$

After normalization, this becomes the Maxwellian.

Therefore,

$$
\boxed{\text{Maxwell–Boltzmann theory is the dilute limit of quantum kinetic theory.}}
$$

---

## 7.5 The Quantum BGK Equation

The classical BGK equation was

$$
\partial_tf+v_i\partial_if = -\frac{1}{\tau}(f-f^{eq}).
$$

The natural quantum analogue is

$$
\boxed{\partial_tf+v_i\partial_if = -\frac{1}{\tau} (f-f^{eq}_q).}
$$

At first sight, this looks identical.

However, there is an important subtlety.

For the classical BGK model,

$$
f^{eq}
$$

is the Maxwellian.

For the quantum model,

$$
f^{eq}_q
$$

must be the Bose–Einstein or Fermi–Dirac distribution.

Also, conservation requires

$$
\int \begin{pmatrix} 1\ v_i\ \frac{1}{2}v^2 \end{pmatrix} (f-f_q^{eq}) \,d^3v
$$

The relaxation must preserve:

- particle number,
- momentum,
- energy.

Exactly the same collision invariants survive.

---

## 7.6 Quantum Macroscopic Variables

The definitions remain unchanged:

Number density:

$$
\boxed{n = \int f\,d^3v.}
$$

Velocity:

$$
\boxed{nu_i = \int v_i f\,d^3v.}
$$

Internal energy:

$$
\boxed{ne = \frac{1}{2}m \int c^2f\,d^3v.}
$$

Stress tensor:

$$
\boxed{P_{ij} = m \int c_ic_jf\,d^3v.}
$$

Heat flux:

$$
\boxed{q_i = \frac{1}{2}m \int c^2c_if\,d^3v.}
$$

The reason is simple:

These are definitions of moments, not consequences of Maxwell–Boltzmann statistics.

---

## 7.7 Quantum Euler Equations

Because the collision invariants are unchanged, taking moments of the quantum BGK equation gives exactly the same conservation laws:

Mass:

$$
\partial_t\rho+\partial_i(\rho u_i)=0.
$$

Momentum:

$$
\partial_t(\rho u_j) + \partial_i(\rho u_i u_j+P_{ij}) =0.
$$

Energy:

$$
\partial_tE+ \partial_i(Eu_i+P_{ij}u_j+q_i)=0.
$$

The difference appears only when we impose equilibrium.

For classical gases:

$$
P_{ij}^{eq}=nk_BT\delta_{ij}.
$$

For quantum gases:

$$
P_{ij}^{eq}=p_q\delta_{ij}
$$

where

$$
\boxed{p_q\neq nk_BT.}
$$

The equation of state is modified by quantum statistics.

---

## 7.8 Quantum Thermodynamic Integrals

All equilibrium moments can be expressed using the quantum integral

$$
\boxed{G_\nu^{(\eta)}(z) = \frac{1}{\Gamma(\nu)} \int_0^\infty \frac{x^{\nu-1}} {z^{-1}e^x+\eta} dx.}
$$

where:

- \\(\eta=+1\\): Fermi–Dirac,
- \\(\eta=-1\\): Bose–Einstein.

The important moments become:

Number density:

$$
\boxed{n = \frac{g}{\lambda_T^3} G_{3/2}^{(\eta)}(z).}
$$

Pressure:

$$
\boxed{p_q = \frac{gk_BT}{\lambda_T^3} G_{5/2}^{(\eta)}(z).}
$$

Energy density:

$$
\boxed{\rho e = \frac{3}{2}p_q.}
$$

Therefore,

$$
\boxed{p_q = n k_BT \frac{ G_{5/2}^{(\eta)}(z) }{ G_{3/2}^{(\eta)}(z) }.}
$$

This ratio is the first major quantum correction.

For the classical limit,

$$
G_\nu(z)\rightarrow z
$$

so

$$
p_q\rightarrow nk_BT.
$$

---

## 7.9 The Chapman–Enskog Expansion Again

Now comes the important comparison.

We again write

$$
\boxed{f = f_q^{(0)} + \varepsilon f_q^{(1)} +\cdots.}
$$

The zeroth-order equation gives

$$
\boxed{f_q^{(0)} = f_q^{eq}.}
$$

The first-order equation gives

$$
\boxed{f_q^{(1)} = -\tau (\partial_{t_1}+v_i\partial_i) f_q^{eq}.}
$$

This equation is **formally identical** to the classical one.

The difference is entirely contained inside

$$
f_q^{eq}.
$$

---

## 7.10 What Will Change in the Next Steps?

When we repeat the Chapter 5 calculation, we will again differentiate

$$
\ln f_q^{eq}.
$$

The result will again separate into:

### Shear mode

$$
\left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i
$$

producing viscosity.

---

### Heat mode

$$
c_i(\text{function of }c^2)\partial_iT
$$

producing heat conduction.

---

The tensor structure survives.

The only changes are:

Classical:

$$
\int c^{2n}f_{MB}\,d^3c
$$

becomes

Quantum:

$$
\int c^{2n}f_{FD/BE}\,d^3c.
$$

Those integrals introduce the functions

$$
G_{1/2},G_{3/2},G_{5/2},G_{7/2},\ldots
$$

into the transport coefficients.

---

## Chapter 7 Summary

We have established the quantum counterpart of the kinetic foundation:

|Classical|Quantum|
|---|---|
|Maxwellian|Bose/Fermi distribution|
|Boltzmann entropy|Quantum entropy|
|\\(p=nk_BT\\)|\\(p=p(n,T,z)\\)|
|Gaussian moments|Quantum statistical integrals|
|Same conservation laws|Same conservation laws|
|Same Chapman–Enskog structure|Same Chapman–Enskog structure|

The next chapter will repeat the Chapter 5 calculation for

$$
f_q^{eq} = \frac{g}{h^3} \frac{1} {z^{-1}e^{mc^2/(2k_BT)}+\eta}
$$

and derive the explicit quantum \\(f_q^{(1)}\\). The algebra is more subtle because derivatives of the fugacity and chemical potential appear, but the same cancellations and tensor decomposition will occur. After that, we will calculate the **Fermi and Bose corrections to viscosity and thermal conductivity**.
