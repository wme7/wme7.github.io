---
title: 'From Kinetic Theory to Quantum Fluids: A Guided Journey Through the Emergence of Hydrodynamics -- Chapter 5'
date: 2026-07-22
permalink: /posts/2026/07/from-kinetic-theory-to-quantum-fluids-chapter-5/
tags:
  - Kinetic Theory
  - Quantum Fluids
  - Hydrodynamics
---

We have now arrived at what I consider the centerpiece of the entire Chapman–Enskog derivation. From this point onward, every line of algebra has a direct physical interpretation.

Our goal is to compute

$$
f^{(1)} = -\tau\left(\partial_{t_1}+v_i\partial_i\right)f^{eq}
$$

where

$$
f^{eq} = n\left(\frac{m}{2\pi k_BT}\right)^{3/2} \exp\left(-\frac{mc^2}{2k_BT}\right)
$$

and

$$
c_i=v_i-u_i.
$$

At first glance, this looks like a simple differentiation problem. In reality, it is not, because **\\(f^{eq}\\) depends on the spacetime coordinates only through the hydrodynamic fields**

$$
n(\mathbf{x},t),\qquad T(\mathbf{x},t),\qquad u_i(\mathbf{x},t).
$$

The microscopic velocity \\(v_i\\) is an independent integration variable and is **not** differentiated with respect to space or time.

---

# Chapter 5 — Explicit Evaluation of \\(f^{(1)}\\)

## 5.1 Writing the Maxwellian in a Convenient Form

The first trick is to differentiate the logarithm instead of the distribution itself.

Write

$$
f^{eq}=A(n,T)e^{-\beta c^2}
$$

where

$$
A = n \left(\frac{m}{2\pi k_BT}\right)^{3/2}
$$

and

$$
\beta=\frac{m}{2k_BT}.
$$

Taking the logarithm,

$$
\boxed{\ln f^{eq} = \ln n +\frac{3}{2}\ln\left(\frac{m}{2\pi k_B}\right) -\frac{3}{2}\ln T -\beta c^2.}
$$

The constant term disappears upon differentiation.

Hence

$$
\boxed{(\partial_t+v_i\partial_i)f^{eq} = f^{eq} (\partial_t+v_i\partial_i)\ln f^{eq}.}
$$

This converts one complicated derivative into several simpler ones.

---

## 5.2 Differentiating the Logarithm

We now compute

$$
D \equiv (\partial_t+v_i\partial_i)\ln f^{eq}.
$$

Using the expression above,

$$
D = \frac{1}{n}Dn -\frac{3}{2T}DT -D(\beta c^2)
$$

where, for compactness, we define the streaming operator

$$
D\equiv\partial_t+v_i\partial_i.
$$

Everything now reduces to evaluating the last term.

---

## 5.3 Derivative of \\(\beta\\)

Since

$$
\beta=\frac{m}{2k_BT}
$$

we have

$$
\boxed{D\beta = -\frac{\beta}{T}DT.}
$$

Therefore

$$
D(\beta c^2) = c^2D\beta + \beta Dc^2.
$$

Substituting,

$$
D(\beta c^2) = -\frac{\beta c^2}{T}DT + \beta Dc^2.
$$

So the remaining task is to compute \\(Dc^2\\).

---

## 5.4 Derivative of the Peculiar Velocity

Recall

$$
c_i=v_i-u_i.
$$

The molecular velocity \\(v_i\\) is an independent variable of the distribution function. Therefore

$$
Dv_i=0.
$$

This is an important point. The streaming operator differentiates with respect to the spacetime coordinates (\\(\mathbf{x},t\\)) while holding the microscopic velocity fixed.

Hence

$$
Dc_i = -Du_i.
$$

Expanding,

$$
Du_i = \partial_tu_i + v_j\partial_ju_i.
$$

Thus

$$
\boxed{Dc_i = (\partial_tu_i + v_j\partial_ju_i).}
$$

---

## 5.5 Derivative of \\(c^2\\)

Since

$$
c^2=c_ic_i
$$

we obtain

$$
Dc^2 = 2c_iDc_i.
$$

Substituting the previous result,

$$
Dc^2 = -2c_i (\partial_tu_i + v_j\partial_ju_i).
$$

Now use

$$
v_j=u_j+c_j.
$$

Then

$$
\boxed{Dc^2 = -2c_i \left[ (\partial_t+u_j\partial_j)u_i + c_j\partial_ju_i \right].}
$$

At this point, something very important happens.

The operator

$$
\partial_t+u_j\partial_j
$$

is the **material derivative**

$$
\frac{D_h}{Dt}
$$

which follows the motion of the fluid.

Thus

$$
\boxed{Dc^2 = -2c_i \left( \frac{D_hu_i}{Dt} + c_j\partial_ju_i \right).}
$$

We have naturally separated the derivative into

- fluid acceleration,
- local velocity gradients.

This decomposition will ultimately produce the viscous stress tensor.

---

## 5.6 Collecting the Terms

Substituting into the logarithmic derivative gives

$$
D\ln f^{eq} = \frac{1}{n}Dn -\frac{3}{2T}DT +\frac{\beta c^2}{T}DT +2\beta c_i \left( \frac{D_hu_i}{Dt} + c_j\partial_ju_i \right).
$$

Or, after grouping the temperature terms,

$$
\boxed{D\ln f^{eq} = \frac{Dn}{n} + \left( \frac{\beta c^2}{T} -\frac{3}{2T} \right) DT + 2\beta c_i \frac{D_hu_i}{Dt} + 2\beta c_ic_j\partial_ju_i.}
$$

This is the first major milestone. Every derivative of the Maxwellian has now been expressed in terms of derivatives of the hydrodynamic fields.

---

## 5.7 Why We Cannot Stop Here

At this stage, \\(f^{(1)}\\) still contains the unknown quantities

$$
Dn,\qquad DT,\qquad \frac{D_hu_i}{Dt}.
$$

These are **time derivatives** of the macroscopic fields. If we left them in the expression, then \\(f^{(1)}\\) would not be an explicit constitutive relation.

The Chapman–Enskog method therefore uses the **leading-order (Euler) equations** to eliminate these time derivatives in favor of spatial gradients. This is a crucial step because viscosity and heat conduction are driven by **gradients**, not by independent time derivatives.

The Euler equations at order \\(O(\varepsilon)\\) provide exactly the relations we need:

1. **Continuity equation**
$$
\frac{D_h n}{Dt} = -n\,\partial_i u_i.
$$
2. **Momentum equation**
$$
\frac{D_h u_i}{Dt} = -\frac{1}{\rho}\,\partial_i p.
$$
3. **Energy equation**
$$
\frac{D_h T}{Dt} = -\frac{2}{3}T\,\partial_i u_i
$$
>    for a monatomic ideal gas.

Notice that these involve the **material derivative**
$$
\frac{D_h}{Dt}=\partial_t+u_i\partial_i
$$
whereas our streaming operator is
$$
D=\partial_t+v_i\partial_i =\frac{D_h}{Dt}+c_i\partial_i.
$$

This distinction is essential. In the next section, we'll rewrite every occurrence of \\(Dn\\) and \\(DT\\) as

$$
Dn=\frac{D_hn}{Dt}+c_i\partial_i n
$$

and similarly for \\(DT\\), before substituting the Euler equations. Only after that substitution will the beautiful tensor structure emerge, separating naturally into:

- a traceless symmetric part proportional to
$$
c_ic_j-\frac{1}{3}c^2\delta_{ij}
$$

which gives **Newton's law of viscosity**, and

- a vector part proportional to
$$
c_i\left(c^2-\frac{5k_BT}{m}\right)
$$

which gives **Fourier's law of heat conduction**.

This decomposition is the mathematical point where the Navier–Stokes constitutive laws emerge directly from kinetic theory. It is also the place where the quantum derivation will later diverge: the tensor algebra remains identical, but the Gaussian moment identities used to evaluate the coefficients will be replaced by Fermi–Dirac or Bose–Einstein integrals.

Excellent. We are now at the most algebraically intensive part of the derivation. If we do this carefully, the rest of the Chapman–Enskog calculation will almost "fall out" of the mathematics.

This is also the point where I want to be **slightly more rigorous than most textbooks**. Many derivations simply substitute the Euler equations without clearly distinguishing between the two different derivatives

$$
D=\partial_t+v_i\partial_i
$$

and

$$
\frac{D_h}{Dt}=\partial_t+u_i\partial_i.
$$

Keeping these separate until the appropriate moment makes the derivation much cleaner.

## 5.8 Decomposing the Streaming Operator

Recall that

$$
v_i=u_i+c_i.
$$

Therefore,

$$
\boxed{D = \partial_t+v_i\partial_i = \frac{D_h}{Dt} + c_i\partial_i.}
$$

This identity is extremely important.

The material derivative follows the motion of the fluid element.

The second term,

$$
c_i\partial_i
$$

represents how a molecule samples spatial gradients because its microscopic velocity differs from the bulk velocity.

This decomposition is one of the conceptual keys to Chapman–Enskog theory.

---

## 5.9 Applying the Decomposition to \\(Dn\\)

Using the identity above,

$$
Dn = \frac{D_h n}{Dt} + c_i\partial_i n.
$$

The Euler continuity equation gives

$$
\boxed{\frac{D_h n}{Dt} = -n\,\partial_i u_i.}
$$

Hence

$$
\boxed{Dn = -n\,\partial_i u_i + c_i\partial_i n.}
$$

Dividing by \\(n\\),

$$
\boxed{\frac{Dn}{n} = -\partial_i u_i + c_i\partial_i(\ln n).}
$$

Notice how the time derivative has disappeared.

Only spatial gradients remain.

---

## 5.10 Applying the Decomposition to \\(DT\\)

Similarly,

$$
DT = \frac{D_hT}{Dt} + c_i\partial_iT.
$$

The Euler energy equation gives

$$
\boxed{\frac{D_hT}{Dt} = -\frac{2}{3}T\,\partial_i u_i.}
$$

Therefore,

$$
\boxed{DT = -\frac{2}{3}T\,\partial_i u_i + c_i\partial_iT.}
$$

Again,

time derivatives have disappeared.

---

## 5.11 Fluid Acceleration

The remaining unknown is

$$
\frac{D_hu_i}{Dt}.
$$

The Euler momentum equation is

$$
\rho \frac{D_hu_i}{Dt} = -\partial_ip.
$$

Thus

$$
\boxed{\frac{D_hu_i}{Dt} = -\frac{1}{\rho}\partial_ip.}
$$

Later,

we shall rewrite

$$
\partial_ip = k_BT\,\partial_in + nk_B\,\partial_iT
$$

which separates density and temperature gradients.

---

## 5.12 Substitute into the Derivative of the Maxwellian

Recall that

$$
D\ln f^{eq} = \frac{Dn}{n} + \left( \frac{\beta c^2}{T} -\frac{3}{2T} \right) DT + 2\beta c_i \frac{D_hu_i}{Dt} + 2\beta c_ic_j\partial_ju_i.
$$

Substituting the previous results,

$$
\begin{aligned}
D\ln f^{eq} 
=& -\partial_ku_k + c_k\partial_k\ln n + \left( \frac{\beta c^2}{T} -\frac{3}{2T} \right) \left( -\frac{2}{3}T\partial_ku_k + c_k\partial_kT \right) \\
&+ \frac{2\beta}{\rho} c_i\partial_ip + 2\beta c_ic_j\partial_ju_i.
\end{aligned}
$$

Everything now depends only on spatial gradients.

---

## 5.13 Simplifying the Divergence Terms

Collect the terms proportional to

$$
\partial_ku_k.
$$

From the first contribution,

$$
-\partial_ku_k.
$$

From the temperature term,

$$
-\frac{2}{3} \left( \beta c^2 -\frac{3}{2} \right) \partial_ku_k.
$$

Adding,

$$
-\partial_ku_k = \frac{2}{3}\beta c^2\partial_ku_k + \partial_ku_k.
$$

The constant pieces cancel exactly.

Therefore,

$$
\boxed{-\frac{2}{3}\beta c^2 \,\partial_ku_k.}
$$

This cancellation is one of the elegant features of the Chapman–Enskog expansion.

---

## 5.14 Expanding the Pressure Gradient

Since

$$
p=nk_BT
$$

we have

$$
\partial_ip = k_BT\,\partial_in + nk_B\,\partial_iT.
$$

Using

$$
\rho=mn
$$

and

$$
2\beta=\frac{m}{k_BT}
$$

we find

$$
\frac{2\beta}{\rho} \partial_ip = \frac{1}{n}\partial_in + \frac{1}{T}\partial_iT.
$$

Therefore

$$
-\frac{2\beta}{\rho} c_i\partial_ip = -c_i\partial_i\ln n = \frac{c_i}{T}\partial_iT.
$$

Now something beautiful happens.

---

## 5.15 Another Exact Cancellation

Recall the density-gradient term from earlier,

$$
+c_i\partial_i\ln n.
$$

It cancels identically with the pressure-gradient contribution.

Thus,

**there is no explicit density gradient remaining**.

This is a remarkable result:

$$
\boxed{\nabla n \quad\text{disappears completely.}}
$$

This cancellation is not accidental. It reflects the fact that, in a single-component ideal gas, density gradients by themselves do not drive dissipative fluxes at first order. The remaining gradients will organize into velocity gradients (producing viscous stresses) and temperature gradients (producing heat conduction).

---

## 5.16 The Remaining Expression

After these simplifications, we obtain

$$
D\ln f^{eq} = 2\beta c_ic_j\partial_ju_i -\frac{2}{3}\beta c^2\partial_ku_k + \left( \frac{\beta c^2}{T} -\frac{5}{2}\frac{1}{T} \right) c_i\partial_iT.
$$

The coefficient (-5/2) comes from combining

$$
-\frac{1}{T}c_i\partial_iT
$$

with

$$
-\frac{3}{2}\frac{1}{T}c_i\partial_iT.
$$

---

## 5.17 The Emerging Tensor Structure

The first two terms can be combined into

$$
2\beta \left( c_ic_j -\frac{1}{3}c^2\delta_{ij} \right) \partial_ju_i.
$$

Notice that the tensor

$$
\boxed{c_ic_j -\frac{1}{3}c^2\delta_{ij}}
$$

is:

- symmetric,
- traceless,
- quadratic in the peculiar velocity.

It is the unique second-rank irreducible tensor that can be formed from the vector \\(\mathbf{c}\\). This is precisely the microscopic structure associated with shear stress.

Similarly, the temperature-gradient term can be written as

$$
\boxed{\frac{1}{T} c_i \left( \beta c^2-\frac{5}{2} \right) \partial_iT.}
$$

Here, the vector

$$
\boxed{c_i \left( \beta c^2-\frac{5}{2} \right)}
$$

is odd in \\(\mathbf{c}\\) and orthogonal (in the sense of velocity moments) to the collision invariants. It is the unique third-order structure responsible for heat transport.

---

## 5.18 The Final Expression for \\(f^{(1)}\\)

Since

$$
f^{(1)} = -\tau f^{eq} D\ln f^{eq}
$$

we arrive at

$$
\boxed{f^{(1)} = -2\tau\beta f^{eq} \left( c_ic_j -\frac{1}{3}c^2\delta_{ij} \right) \partial_ju_i -\tau f^{eq} \frac{1}{T} c_i \left( \beta c^2-\frac{5}{2} \right) \partial_iT.}
$$

This is the explicit first-order correction to the Maxwellian.

---

## Why this result is so important

Everything from this point on becomes an exercise in evaluating velocity moments:

- inserting the first term into
$$
P_{ij}=m\int c_ic_j f\,d^3c
$$

yields **Newton's law of viscosity**,

- inserting the second term into
$$
q_i=\frac{m}{2}\int c^2 c_i f\,d^3c
$$

yields **Fourier's law of heat conduction**.

Moreover, this formula reveals something profound that will carry over almost unchanged to the quantum case. The **tensorial structure** of \\(f^{(1)}\\)—the traceless quadratic tensor associated with shear and the odd cubic vector associated with heat flow—is dictated by symmetry and conservation laws, not by the specific form of the equilibrium distribution. When we later replace the Maxwellian by the Fermi–Dirac or Bose–Einstein equilibrium, these tensor structures will remain the same. The only change will be in the velocity moments: Gaussian integrals will be replaced by Fermi–Dirac or Bose–Einstein integrals, leading to modified transport coefficients while preserving the overall form of the constitutive laws.
