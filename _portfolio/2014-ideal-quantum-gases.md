---
title: "Exact Riemann Solver for Ideal Quantum Gases of Arbitrary Statistics"
excerpt: "Solve Shock Tube Problems for ideal quantum Bose and Fermi gases<br/><br/><img src='/files/figures/ideal_quantum_gases/sod_2d_gas_quantum_comparison.png'>"
collection: portfolio
---

![ideal_quantum_gas]({{ base_path }}/files/figures/ideal_quantum_gases/fermi_2d_gas_yang_hsieh_shi.png)

During my PhD, I studied the numerical solution of ideal quantum gases in both the Euler and Navier–Stokes hydrodynamic limits, and developed several codes to simulate their behavior with the Boltzmann–BGK model equation.

At the time, numerical descriptions of ideal monoatomic quantum gases were already well established. My challenge was to study and extend this work to model ideal quantum gases with internal degrees of freedom, such as spin and angular momentum.

To my surprise, earlier work in the group relied on kinetic models even when describing the hydrodynamic limit of these gases. Although all statistics lead to the same hydrodynamic limit—the Euler equations and the same Navier–Stokes equations—we had not taken the time to use these observations when studying the dynamics of these gases. (What a waste of time!)

I later found that we were not alone in this observation. [Jingwei Hu and Shi Jin](https://ins.sjtu.edu.cn/people/shijin/PS/KFVS.pdf) noted in Remark 3.2 of their paper that:
> One does not need to solve the Boltzmann–BGK model equation to study the hydrodynamic limit of these gases. Clearly any shock capturing method can be used.

In their work, a simple MUSCL shock-capturing method provided the reference solutions for the shock-tube problems they presented.

This reconfirmed my suspicions. Still, a shock-capturing method remained, to me, an approximation. That is not a bad approach per se, but it is not the exact solution of the problem. In my mind, if this idea holds true, any Riemann solver should be able to resolve a quantum shock-tube problem. The question is how?

It took me a while to see that the key step is to compute an **effective pressure**—*a quantum correction to the pressure field*. With that modification, I found out that any Riemann solver can solve the shock-tube problem for ideal quantum gases.

Building on this idea, I adapted Toro’s exact Riemann solver to the quantum-gas setting and managed to recover exact to several cases presented in the literature and extend with confidence my rarefied gas solver with internal degrees of freedom. 

The original Matlab code appeared in my Ph.D. thesis, but the National Taiwan University library locked it for ten years, and on top of that I had signed a non-disclosure agreement with the university. Enough time for some member of the university to expand on this work. In late 2025, my Ph.D. thesis was finally released to the public on DOI: [10.6342/NTU.2015.00509](https://doi.org/10.6342/NTU.2015.00509). 

On January 2026, I rewrote the solver as a Python application so that new practitioners can study the dynamics of ideal quantum gases more easily. I hope this will be a useful tool for the community.

The code is available on GitHub:
[Ideal Gases](https://github.com/wme7/ideal-gases)

It can also be installed from PyPI:
```bash
pip install ideal-gases[plot]
```
or with `uv`:
```bash
uv add ideal-gases
```

The package can be used as a Python library or as a command-line tool. The CLI is a simple wrapper around the library: it solves the shock-tube problem for ideal quantum gases and can output the results in several formats. For more details, please refer to the documentation at [Ideal Gases](https://github.com/wme7/ideal-gases).