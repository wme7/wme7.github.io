---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 6'
date: 2026-07-24
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-6/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

Most books state identities like
$$
\int c_i c_j c_k c_l e^{-\beta c^2}\,d^3c = A(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
$$
without proving them. That is unfortunate, because these tensor identities are **the entire mathematical engine** behind the Navier–Stokes constitutive laws.

Even more importantly, when we later move to quantum gases, **the tensor algebra remains unchanged**—only the scalar coefficients (the radial integrals) are modified. Understanding this chapter deeply will make the quantum derivation almost mechanical.

---

# Chapter 6 — Evaluation of Velocity Moments and the Emergence of the Constitutive Laws

## 6.1 The Objective

From the previous chapter, we obtained

$$
f=f^{eq}+f^{(1)}
$$

with

$$
\boxed{f^{(1)} = -2\tau\beta f^{eq} \left( c_ic_j-\frac{1}{3}c^2\delta_{ij} \right) \partial_j u_i -\tau f^{eq} \frac{1}{T} c_i \left( \beta c^2-\frac{5}{2} \right) \partial_iT.}
$$

We now substitute this into

$$
P_{ij} = m\int c_ic_jf\,d^3c
$$

and

$$
q_i = \frac{1}{2}m \int c^2c_if\,d^3c.
$$

The equilibrium part is already known,

$$
P_{ij}^{eq}=p\delta_{ij}, \qquad q_i^{eq}=0.
$$

Therefore, only \\(f^{(1)}\\) contributes to the dissipative corrections.

---

## 6.2 Why Isotropy Simplifies Everything

Before computing any integrals, we should understand their structure.

The Maxwellian depends only on

$$
c^2.
$$

Therefore,

$$
f^{eq}=F(c^2)
$$

for some scalar function \\(F\\).

Consequently, every integral has the form

$$
\int (\text{polynomial in }c_i) F(c^2) \,d^3c.
$$

Because \\(F\\) is rotationally invariant, the result must also be rotationally invariant.

This simple observation almost determines every integral before we calculate it.

---

## 6.3 Zeroth-Order Integral

The simplest example is

$$
I_0 = \int F(c^2)\,d^3c.
$$

There is no free index.

Therefore,

$$
I_0 = \text{scalar}.
$$

Nothing more can be said.

---

## 6.4 Second-Order Tensor Integral

Now consider

$$
I_{ij} = \int c_ic_jF(c^2)\,d^3c.
$$

Because the integral is isotropic,

there is only one possible second-rank isotropic tensor,

$$
\delta_{ij}.
$$

Hence

$$
\boxed{I_{ij} = A\delta_{ij}}
$$

for some scalar (A).

We determine (A) by taking the trace.

Taking \\(i=j\\),

$$
I_{ii} = 3A.
$$

But

$$
I_{ii} = \int c^2F(c^2)\,d^3c.
$$

Therefore

$$
\boxed{A = \frac{1}{3} \int c^2F(c^2)\,d^3c.}
$$

Thus

$$
\boxed{\int c_ic_jF(c^2)\,d^3c = \frac{\delta_{ij}}3 \int c^2F(c^2)\,d^3c.}
$$

This identity is used repeatedly.

---

## 6.5 Fourth-Order Tensor Integral

Now we encounter the integral responsible for viscosity,

$$
I_{ijkl} = \int c_ic_jc_kc_l F(c^2)\,d^3c.
$$

Again,

rotational symmetry almost determines the answer.

There are only three isotropic fourth-rank tensors,

$$
\delta_{ij}\delta_{kl}
$$

$$
\delta_{ik}\delta_{jl}
$$

$$
\delta_{il}\delta_{jk}.
$$

Therefore,

$$
\boxed{I_{ijkl} = A ( \delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk} ).}
$$

The only question is:

what is (A)?

---

## 6.6 Determining the Constant

Contract indices,

setting

$$
i=j
$$

and

$$
k=l.
$$

Then

$$
I_{iikk} = 15A.
$$

On the other hand,

$$
I_{iikk} = \int c^4 F(c^2)\,d^3c.
$$

Hence

$$
\boxed{A = \frac{1}{15} \int c^4F(c^2)\,d^3c.}
$$

Therefore,

$$
\boxed{\begin{aligned} \int c_ic_jc_kc_l F(c^2)\,d^3c = \frac{1}{15} & \left( \delta_{ij}\delta_{kl} +\delta_{ik}\delta_{jl} +\delta_{il}\delta_{jk} \right) \ &\times \int c^4F(c^2)\,d^3c. \end{aligned}}
$$

This is the fundamental isotropic tensor identity behind viscosity.

---

## 6.7 Odd Moments

Consider

$$
\int c_ic_jc_k F(c^2)\,d^3c.
$$

Changing variables

$$
\mathbf{c}\rightarrow-\mathbf{c}
$$

changes the sign of the integrand,

while leaving

$$
F(c^2)
$$

unchanged.

Therefore,

$$
\boxed{\int c_ic_jc_kF(c^2)\,d^3c = 0}
$$

Likewise,

every odd moment vanishes.

---

## 6.8 Viscous Stress

Now we compute

$$
\Pi_{ij} = m \int c_ic_jf^{(1)}\,d^3c.
$$

The temperature-gradient contribution contains five powers of \\(c\\), so it vanishes by odd parity. Only the velocity-gradient term contributes:

$$
\Pi_{ij} = -2m\tau\beta \partial_lu_k \int c_ic_j \left( c_kc_l -\frac{1}{3}c^2\delta_{kl} \right) f^{eq}\,d^3c.
$$

We evaluate the two integrals separately.

Using the fourth-order identity,

$$
\int c_ic_jc_kc_lf^{eq}\,d^3c = \frac{M_4}{15} \left( \delta_{ij}\delta_{kl} + \delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk} \right)
$$

where

$$
M_4 = \int c^4f^{eq}\,d^3c.
$$

Similarly,

$$
\int c_ic_jc^2f^{eq}\,d^3c = \frac{\delta_{ij}}3M_4.
$$

Substituting,

$$
\Pi_{ij} = -\frac{2m\tau\beta M_4}{15} \left( \partial_iu_j +\partial_ju_i -\frac{2}{3}\delta_{ij}\partial_ku_k \right).
$$

The remaining task is to evaluate the scalar moment \\(M_4\\).

---

## 6.9 Computing the Scalar Fourth Moment

Rather than evaluating the Gaussian integral from scratch, we exploit the fact that the Cartesian components of the Maxwellian are independent Gaussian random variables.

For one component,

$$
\langle c_x^2\rangle = \frac{k_BT}{m}, \qquad \langle c_x^4\rangle = 3\left(\frac{k_BT}{m}\right)^2.
$$

Since

$$
c^2=c_x^2+c_y^2+c_z^2
$$

we have

$$
c^4 = (c_x^2+c_y^2+c_z^2)^2.
$$

Expanding,

$$
c^4 = c_x^4+c_y^4+c_z^4 +2c_x^2c_y^2 +2c_x^2c_z^2 +2c_y^2c_z^2.
$$

Using independence,

$$
\langle c_x^2c_y^2\rangle = \langle c_x^2\rangle \langle c_y^2\rangle = \left(\frac{k_BT}{m}\right)^2.
$$

Therefore,

$$
\begin{aligned} \langle c^4\rangle &= 3\times3\left(\frac{k_BT}{m}\right)^2 + 6\left(\frac{k_BT}{m}\right)^2 \ &= 15\left(\frac{k_BT}{m}\right)^2. \end{aligned}
$$

Multiplying by the number density,

$$
\boxed{M_4 = 15n \left( \frac{k_BT}{m} \right)^2.}
$$

This is a very useful result because it isolates the entire Gaussian calculation into a single scalar coefficient.

---

## 6.10 Newton's Law of Viscosity

Substituting \\(M_4\\) into the expression for \\(\Pi_{ij}\\), and recalling that

$$
\beta=\frac{m}{2k_BT}
$$

we find

$$
2\beta\frac{M_4}{15} = 2\cdot\frac{m}{2k_BT}\cdot n\left(\frac{k_BT}{m}\right)^2 = n\frac{k_BT}{m}.
$$

Multiplying by \\(m\tau\\),

$$
m\tau\left(n\frac{k_BT}{m}\right) = nk_BT,\tau = p\tau.
$$

Therefore,

$$
\boxed{\Pi_{ij} = -\mu \left( \partial_i u_j +\partial_j u_i -\frac{2}{3}\delta_{ij}\,\partial_k u_k \right)}
$$

with

$$
\boxed{\mu = p\tau.}
$$

This is **Newton's law of viscosity**, and the dynamic viscosity emerges directly from the BGK relaxation time.

---

## A note about the heat flux

By symmetry, the evaluation of

$$
q_i=\frac{m}{2}\int c^2 c_i f^{(1)}\,d^3c
$$

proceeds in much the same way, but it requires a **sixth-order velocity moment** because \\(q_i\\) involves \\(c^2 c_i\\) and the temperature-dependent part of \\(f^{(1)}\\) contributes another factor of \\(c^2 c_i\\). The relevant scalar moment is

$$
\int c^6 f^{eq}\,d^3c = 105\,n\left(\frac{k_BT}{m}\right)^3
$$

and the tensor reduction again follows from isotropy.

Working through that calculation yields Fourier's law,

$$
\boxed{q_i=-\kappa\,\partial_iT}
$$

with the BGK thermal conductivity

$$
\boxed{\kappa=\frac{5}{2}\frac{k_B}{m},\mu =\frac{5}{2}\frac{k_B}{m},p\tau.}
$$

This result corresponds to a **Prandtl number**

$$
\mathrm{Pr} =\frac{\mu c_p}{\kappa} =1
$$

whereas a monatomic ideal gas has the physical value \\(\mathrm{Pr}=2/3\\). This discrepancy is a well-known limitation of the single-relaxation-time BGK model and motivates more sophisticated kinetic models such as the ES-BGK and Shakhov models.

---

## Looking ahead to the quantum case

This chapter contains the key conceptual bridge to quantum kinetic theory.

Notice that **none of the tensor algebra** depended on the Maxwellian. The only place where classical statistics entered was through the scalar moments,

$$
\int c^2 f^{eq}\,d^3c,\qquad \int c^4 f^{eq}\,d^3c,\qquad \int c^6 f^{eq}\,d^3c.
$$

For a Fermi–Dirac or Bose–Einstein equilibrium, the isotropic tensor decompositions are **identical**. Only these scalar radial integrals change, becoming combinations of Fermi–Dirac or Bose–Einstein integrals. That is why the structure of the quantum Navier–Stokes equations mirrors the classical ones so closely, even though the transport coefficients acquire a rich dependence on fugacity and quantum statistics.

This observation will become one of the central themes when we begin the quantum derivation.