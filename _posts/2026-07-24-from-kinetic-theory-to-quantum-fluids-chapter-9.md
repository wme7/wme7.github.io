---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 9'
date: 2026-07-24
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-9/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

We now arrive at the final closure step: extracting the **quantum viscous stress tensor** and **quantum heat flux** from \\(f_q^{(1)}\\).

This chapter will look very familiar because the symmetry machinery from the classical case survives completely. The only thing that changes is the evaluation of scalar velocity moments.

A useful way to think about the whole quantum correction is:

$$
\boxed{\text{same tensors} + \text{different scalar integrals} = \text{quantum transport coefficients}.}
$$

---

# Chapter 9 — Quantum Stress Tensor and Heat Flux

## 9.1 Starting Point

We have obtained the first-order quantum correction:

$$
\boxed{f_q^{(1)} = \tau f_q^{eq}\Phi_q \left[ 2A_q \left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i + B_q(c^2)c_i\partial_iT \right].}
$$

The nonequilibrium stress tensor is

$$
\Pi_{ij} = m \int c_ic_j f_q^{(1)} \,d^3c.
$$

The heat flux is

$$
q_i = \frac{1}{2}m \int c^2c_i f_q^{(1)} \,d^3c.
$$

---

## 9.2 Quantum Isotropy

The equilibrium distribution is still isotropic:

$$
f_q^{eq}=F(c^2).
$$

The additional quantum factor

$$
\Phi_q = 1-\eta\frac{h^3}{g}f_q^{eq}
$$

is also only a function of \\(c^2\\).

Therefore all integrals have the same tensor decomposition rules as before.

For example,

$$
\int c_ic_jF(c^2)d^3c = \frac{\delta_{ij}}3 \int c^2F(c^2)d^3c
$$

and

$$
\int c_ic_jc_kc_lF(c^2)d^3c = \frac{1}{15} (\delta_{ij}\delta_{kl} +\delta_{ik}\delta_{jl} +\delta_{il}\delta_{jk}) \times \int c^4F(c^2)d^3c.
$$

The quantum statistics have not altered rotational symmetry.

---

## 9.3 The Quantum Shear Stress

Insert the shear part:

$$
\Pi_{ij}^{(s)} = 2m\tau A_q \partial_lu_k \int c_ic_j \left( c_kc_l-\frac{1}{3}c^2\delta_{kl} \right) f_q^{eq}\Phi_q\,d^3c .
$$

Define the quantum fourth moment:

$$
M_4^{(q)} = \int c^4f_q^{eq}\Phi_q\,d^3c.
$$

Using the tensor identities,

$$
\int c_ic_j \left( c_kc_l-\frac{1}{3}c^2\delta_{kl} \right) f_q^{eq}\Phi_qd^3c = \frac{M_4^{(q)}}{15} \left( \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk} -\frac{2}{3}\delta_{ij}\delta_{kl} \right).
$$

Therefore,

$$
\boxed{\Pi_{ij} = \mu_q \left( \partial_i u_j +\partial_j u_i -\frac{2}{3}\delta_{ij}\partial_k u_k \right).}
$$

The sign convention depends on whether \\(\Pi_{ij}\\) is defined as the full stress correction or the viscous stress. Using the usual Navier–Stokes convention,

$$
\boxed{\Pi_{ij}^{visc} = -\mu_q \left( \partial_i u_j +\partial_j u_i -\frac{2}{3}\delta_{ij}\partial_k u_k \right).}
$$

---

## 9.4 Quantum Viscosity Coefficient

The coefficient is

$$
\boxed{\mu_q = \frac{2}{15}m\tau A_qM_4^{(q)}.}
$$

This is the quantum replacement of the classical BGK result

$$
\mu=p\tau.
$$

The entire problem is now reduced to evaluating

$$
M_4^{(q)}.
$$

---

## 9.5 Evaluating Quantum Moments

The generic quantum moment is

$$
I_s = \int c^{2s} f_q^{eq}\Phi_q\,d^3c .
$$

The velocity integral can be transformed into an energy integral.

Define

$$
x= \frac{mc^2}{2k_BT}.
$$

Then

$$
c^2 = \frac{2k_BT}{m}x.
$$

The volume element becomes

$$
d^3c = 4\pi \left( \frac{2k_BT}{m} \right)^{3/2} \frac{1}{2} x^{1/2}dx .
$$

Thus,

$$
I_s \propto \int_0^\infty \frac{x^{s+1/2}} {z^{-1}e^x+\eta} \Phi_q,dx.
$$

The factor

$$
\Phi_q = 1-\eta f_q^{eq}
$$

has a useful identity:

$$
\boxed{f_q^{eq}\Phi_q = -z\frac{\partial f_q^{eq}}{\partial z}.}
$$

This allows the moment to be converted into derivatives of Fermi/Bose integrals.

Using integration identities, one obtains

$$
\boxed{M_4^{(q)} = 15n \left(\frac{k_BT}{m}\right)^2 \frac{ G_{5/2}^{(\eta)}(z) }{ G_{3/2}^{(\eta)}(z) }.}
$$

Therefore,

$$
\boxed{\mu_q = p_q\tau}
$$

for the single-relaxation-time quantum BGK model.

This is a beautiful result:

$$
\boxed{\text{BGK viscosity keeps the form }p\tau}
$$

but the pressure is now quantum.

---

## 9.6 Fermi and Bose Limits

## Classical dilute gas

For

$$
z\ll1
$$

$$
G_\nu(z)\rightarrow z
$$

so

$$
p_q\rightarrow nk_BT
$$

and therefore

$$
\boxed{\mu_q\rightarrow nk_BT\tau.}
$$

The classical BGK result returns.

---

## Degenerate Fermi gas

For

$$
z\gg1
$$

the Fermi integrals approach the Sommerfeld expansion:

$$
G_\nu^{(+)}(z) \sim \frac{(\ln z)^\nu}{\Gamma(\nu+1)} \left[ 1+O(T^2) \right].
$$

The viscosity becomes controlled by the Fermi energy scale rather than \\(k_BT\\).

---

## Bose gas

For bosons,

$$
\eta=-1.
$$

As

$$
z\rightarrow1^-
$$

the moments become sensitive to Bose condensation.

The viscosity behavior depends strongly on whether the gas is above or below the condensation temperature.

The simple normal-gas BGK model does not describe the condensate component; a two-fluid kinetic theory is required below \\(T_c\\).

---

## 9.7 Quantum Heat Flux

Now consider

$$
q_i = \frac{1}{2}m \int c^2c_i f_q^{(1)} d^3c .
$$

The shear contribution vanishes because it contains an odd number of \\(c_i\\).

Only the temperature-gradient term survives:

$$
q_i = -\kappa_q\partial_iT.
$$

The coefficient becomes

$$
\boxed{\kappa_q = \frac{m\tau}{2} \int c^4 B_q(c^2) f_q^{eq}\Phi_q d^3c .}
$$

After evaluating the quantum moments,

$$
\boxed{\kappa_q = \frac{5}{2} \frac{k_B}{m} p_q\tau ,\mathcal R_\eta(z)}
$$

where

$$
\boxed{\mathcal R_\eta(z)}
$$

is a dimensionless quantum correction factor constructed from ratios of quantum integrals.

For the classical limit,

$$
\mathcal R_\eta(z)\rightarrow1
$$

giving

$$
\boxed{\kappa = \frac{5}{2} \frac{k_B}{m}\mu .}
$$

---

## 9.8 Quantum Prandtl Number

The BGK Prandtl number becomes

$$
Pr_q = \frac{\mu_q c_p}{\kappa_q}.
$$

Unlike the classical BGK model, the heat capacity and thermal conductivity are both modified by quantum statistics.

Therefore,

$$
\boxed{Pr_q \neq1}
$$

in general.

The value depends on:

- fugacity \\(z\\),
- Fermi versus Bose statistics,
- temperature.

This is one of the experimentally relevant signatures of quantum kinetic transport.

---

## 9.9 Final Quantum Navier–Stokes Equations

We can now write the macroscopic equations.

## Continuity

$$
\boxed{\partial_t\rho+\nabla\cdot(\rho\mathbf{u})=0}
$$

---

## Momentum

$$
\boxed{\rho \frac{D\mathbf{u}}{Dt} = -\nabla p_q + \nabla\cdot\boldsymbol{\Pi}}
$$

with

$$
\boxed{\Pi_{ij} = -\mu_q \left( \partial_i u_j +\partial_j u_i -\frac{2}{3}\delta_{ij}\nabla\cdot\mathbf{u} \right).}
$$

---

## Energy

$$
\boxed{\partial_tE + \nabla\cdot (E\mathbf{u}+p_q\mathbf{u}) = \nabla\cdot(\boldsymbol{\Pi}\cdot\mathbf{u}) -\nabla\cdot(\kappa_q\nabla T).}
$$

This is the kinetic-theory quantum Navier–Stokes system.

---

## 9.10 The Main Lesson

The Chapman–Enskog derivation reveals a deep separation:

### Universal kinetic structure

$$
\boxed{\text{conservation laws} + \text{tensor symmetry}}
$$

does not care whether the gas is classical, fermionic, or bosonic.

### Statistical physics

$$
\boxed{\text{equation of state} + \text{transport coefficients}}
$$

contains all the quantum information.

---

The next chapter would be a very interesting one: a **side-by-side derivation table comparing classical BGK, Fermi BGK, and Bose BGK term by term**, including the equilibrium distribution, moments, viscosity, thermal conductivity, and the classical limit. This will make the similarities and differences completely transparent.