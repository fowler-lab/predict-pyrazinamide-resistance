# predict-pyrazinamide-resistance

The aim of this GitHub repository is to allow you to reproduce the results and figures of the following study

> Prediction of pyrazinamide resistance in Mycobacterium tuberculosis using structure-based machine learning approaches
>
> Joshua J Carter, Timothy M Walker, A Sarah Walker, Michael G. Whitfield, Glenn P. Morlock, Timothy EA Peto, James E. Posey,  Derrick W Crook,  Philip W Fowler
>
> https://doi.org/10.1101/518142

At present, the above manuscript is being rewritten and therefore this repository is different to the above preprint. Once a new version of the manuscript is ready, the preprint will be updated and the manuscript submitted to a journal for review.

The repository contains a series of jupyter notebooks. They form a sequence, starting with data tidying, transformation and joining before then feeding into a notebooks that reproduce the figures and thence the main results of the manuscript. Each is self-contained in the sense that you don't have to run the predecessors for it to work (since all the input/output files are also stored in the repository) but you can, if you wish, run them all the way through thereby reproducing everything.

They are split into two sets. 

## 1. Data tidying, processing and aggregating

The first handles the data tidying, processing and joining to create the Training, Test, Validation and MIC datasets. They are numbered in the order that they need to be run.

* `0-parse-original-data.ipynb`
* `1-create-dataset-testtrain.ipynb`
* `1-create-dataset-validation.ipynb`
* `2-analyse-cryptic.ipynb`
* `3-add-features.ipynb`
* `4-split-testtrain.ipynb`

Some have flags set at the beginning that need changing and the notebook rerunning. For example, `filestem` at the start of `3-add-features.ipynb` needs to be one of `testtrain`, `validation` or `mic`. This is explained in the notebooks.

## 2. Reproducing figures, including training the Machine Learning models

These are handled by 

* `create-figure-1.ipynb`
* `create-figure-2.ipynb`
* `create-figure-3.ipynb`

and each also writes to disc (`pdf/`) graphs etc that are used in Supplementary Information.

Philip W Fowler
8 May 2023
