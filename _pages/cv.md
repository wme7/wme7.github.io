---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Applied Mechanics, National Taiwan University (NTU), 2015 GPA: 3.85
* M.S. in Applied Mechanics, National Taiwan University (NTU), 2012 GPA: 3.93
* Chinese Language Studies, National Taiwan Normal University (NTNU), 2010
* B.S. in Mechanical Engineering, Universidad Centroamericana José Simeón Cañas (UCA), 2008 GPA: 8.23
* Technical High School Diploma in Mechanics, Instituto Técnico Ricaldone (ITR), 2002 GPA: 9.2

Work experience
======
* Senior Research Engineer, Cenaero ASBL
  * 2022 - present
  * GPU port and optimization of FIDELIO (WINGS-II) with CUDA C++ and HIP/ROCm
  * Developed a GPU-accelerated FV-LB solver for rarefied gas flows (MaiSoVI)
  * Assessed GPU particle / MPM methods for mechanical engineering (VirtualLab)

* Postdoctoral Researcher ANR MAMIES, Institut Pprime — University of Poitiers
  * 2022 - 2022
  * Experimental–computational work on time-reversal aeroacoustics for the MAMIES project
  * Project lead: Vincent Valeau

* Postdoctoral Researcher FEDER/NAE, ISAE-ENSMA — Institut Pprime
  * 2020 - 2021
  * High-order immersed boundary methods (IBM) for aeroacoustics in Xcompact3d
  * Project leads: Véronique Fortuné and David Marx

* Postdoctoral Researcher ANR MAMIES, Institut Jean Le Rond d'Alembert — Sorbonne University
  * 2019 - 2020
  * CFD/CAA algorithms; DG solvers and data assimilation / time-reversal for acoustic sources
  * Project leads: Régis Marchiano and Vincent Valeau

* Postdoctoral Researcher NSC, Institute of Biomedical Engineering and Nanomedicine (NHRI)
  * 2016 - 2018
  * Multi-GPU WENO solvers for nonlinear acoustic propagation (CUDA, MPI, OpenMP)
  * Project lead: Maxim Solovchuk

* Junior Mechanical Designer, Ingendehsa S.A. de C.V.
  * 2008 - 2009
  * Design of valves, cranes, and pressurized pipelines for hydroelectric plants
  * AutoCAD and Autodesk Inventor parameterized models linked to Excel calculations

Skills
======
Languages: Spanish (Native), English (C2), Chinese (B1), French (A2)
Programming: Python 3, MATLAB, Mathematica, C/C++, Fortran, LaTeX, Git, Bash, CMake
Libraries: CUDA, HIP/ROCm, MPI, MPI-IO, HDF5, OpenMP, PETSc
Tools: Visual Studio Code, Vim, Emacs, Jupyter, NSight Compute, valgrind
Interests: CFD, computational aeroacoustics (CAA), thermoacoustics, data assimilation, time reversal, WENO/FVM/FDM/FEM/DG, GPU computing

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Honors
======
* 2018 Best Paper Presentation Award, National Health Research Institutes (NHRI)
* 2014 Engineering Faculty Fellowship, National Taiwan University (NTU)
* 2011 Best Individual Project, Institute of Applied Mechanics, NTU
* 2009 Taiwan Scholarship Recipient, Ministry of Foreign Affairs of Taiwan
* 2008 Top Graduate in Mechanical Engineering, Salvadorian Association of Mechanical Electrical and Industrial Engineers

Qualifications
======
* Qualification for Associate Professor (Maître de Conférences), Section 60, 2022
