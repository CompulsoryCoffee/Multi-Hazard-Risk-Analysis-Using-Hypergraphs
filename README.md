# Multi-Hazard Risk Analysis Using Hypergraphs

 

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Requirements](#requirements)
4. [License](#license)
5. [Citation](#citation)

---

## Overview

This project uses hypergraph theory to model and simulate the impacts of cascading multi-hazards. The 2015 Gorkha earthquake in Nepal is used as a case study, focusing on the interplay between earthquakes, landslides, and infrastructure vulnerabilities. The framework demonstrates the potential for:

- Capturing complex interactions between hazards.
- Efficient computation across large datasets.
- Generating scenario-based insights for disaster risk reduction.

---

## Repository Structure

```plaintext
   multi_hazard_hypergraph/
├── README.md               # Project documentation
├── LICENSE                 # License for the repository
├── scripts/                # Python scripts for analysis
│   ├── mcpu_ensemble_impacts_full30_withCutoff.py
│   ├── mods_geom_ops.py
│   └── mods_vulnerability_caseload_ensemble.py

```

---

## Requirements

The code requires the following dependencies:

- Python 3.10 or later
- GDAL
- GeoPandas
- NumPy
- xarray
- rioxarray
- tqdm
- matplotlib
- scipy
- joblib


## License

This project is licensed under the [MIT License](LICENSE).

---

## Citation

> Dunant, A., Robinson, T. R., et al. (2024). Impacts from cascading multi-hazards using hypergraphs: a case study from the 2015 Gorkha earthquake in Nepal. *Journal Name*. DOI: [DOI Placeholder]

```bibtex
@article{dunant2024hypergraph,
  author = {Dunant, Alexandre and Robinson, Tom R. and others},
  title = {Impacts from cascading multi-hazards using hypergraphs: a case study from the 2015 Gorkha earthquake in Nepal},
  journal = {Journal Name},
  year = {2024},
  doi = {DOI Placeholder}
}
```

---

