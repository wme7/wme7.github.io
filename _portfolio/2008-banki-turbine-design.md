---
title: "Design of a Banki Waterwheel Prototype"
excerpt: "Bachelor thesis: design of a Banki waterwheel for a micro-hydro power plant<br/><br/><img src='/files/figures/banki_turbine/final.bmp'>"
collection: portfolio
---

In 2008, for my bachelor thesis in mechanical engineering, I teamed with Yuri Posada and worked on the design of a [Banki–Michell turbine](https://en.wikipedia.org/wiki/Cross-flow_turbine) intended as a micro-hydro power plant. As with many engineering problems, the project started with a simple question: how could we improve the performance of an existing installation?

We began with flow simulations of the distributor—the nozzle that guides water into the waterwheel—comparing open and nearly closed operating conditions. The pressure and velocity fields below show how the inlet flow changes between those two cases.

| Pressure (Pa) | Velocity (m/s) |
|:---:|:---:|
| ![]({{ base_path }}/files/figures/banki_turbine/pressure_open.png) | ![]({{ base_path }}/files/figures/banki_turbine/velocity_open.png) |
| ![]({{ base_path }}/files/figures/banki_turbine/pressure_closing.png) | ![]({{ base_path }}/files/figures/banki_turbine/velocity_closing.png) |

At the time, we could not find a two-phase flow solver capable of simulating the waterwheel itself. So we used the distributor results as a first-order estimate of the energy entering the turbine and of the losses along individual blades. It was a crude model, but it was enough to move from analysis into design.

The first conceptual prototype followed the classical Ossberger layout closely, with only modest changes to the blade geometry aimed at extracting more energy from the flow at the conditions of the existing plant.

![banki_turbine]({{ base_path }}/files/figures/banki_turbine/banki_proto1.png)

Prototype 1.0, based on conditions at the existing power plant.

Even that approximate model made one loss mechanism hard to ignore: once water enters the turbine, a substantial share of its energy is spent hitting the shaft that supports the waterwheel. That observation led to a second design question—could we improve performance by removing the through-shaft support altogether?

![banki_turbine]({{ base_path }}/files/figures/banki_turbine/banki_proto2.png)

Final prototype under ideal operating conditions.

The idea was to carry the waterwheel without a continuous shaft through the flow path, and to test whether the remaining structure was strong enough to support the wheel in operation.

![banki_turbine]({{ base_path }}/files/figures/banki_turbine/banki_proto3.png)

We found that the design could hold. A half-cut of the prototype shows how simple the internal structure really is; the exploration was mainly about whether the wheel could run without a split shaft supporting it from the center.

![banki_turbine]({{ base_path }}/files/figures/banki_turbine/halfcut.bmp)

Half-cut of the prototype, showing the internal structure.

That structural answer was only part of the story. Manufacturing details and maintenance procedures still needed careful work before such a design could be practical in the field. Working through those trade-offs—between simulation limits, conceptual redesign, and what can actually be built—was one of the most formative lessons of my training as a mechanical engineer.

Thesis presentation available (in Spanish) [here]({{ base_path }}/files/slides/UCA_banki_turbine_thesis.pdf).
