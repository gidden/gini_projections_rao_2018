# Overview

The raw data as projected by the historical model is found in
`input_ginis_ssp5.csv` which contains Gini values outside of [15, 65].

Data is then "smoothed" such that all values lie between [15, 65] and smoothly
approach these asymptotes. The process for making this calculation is shown in
`methodology.ipynb` and consists of matching an exponential the the derivative
of the original data in cases where that original data contained values outside
of the threshold. The actual operation is then performed with `smooth_all.ipynb`
and `smooth.py` which produces `adjusted_multi_single.csv`, the dataset used in
the manuscript.

All figures generated from this dataset are included in `si_plots.ipynb`.

There are also a number of analysis notebooks showing off different ways to
slice and dice the data, including:

- `gini_gdp_pc_plot_by_country.ipynb`
- `gini_gdp_pc_plot_by_region.ipynb`

