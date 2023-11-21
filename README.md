[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fowler-lab/predict-pyrazinamide-resistance/HEAD?labpath=01-parse-original-data.ipynb)

# predict-pyrazinamide-resistance

The aim of this GitHub repository is to allow you to reproduce the results and figures of the following study

> Prediction of pyrazinamide resistance in Mycobacterium tuberculosis using structure-based machine learning approaches
>
> Joshua J Carter, Timothy M Walker, A Sarah Walker, Michael G. Whitfield, Glenn P. Morlock, Charlotte I. Lynch, Dylan Adlard, Timothy EA Peto, James E. Posey,  Derrick W Crook,  Philip W Fowler
>
> [https://doi.org/10.1101/518142](https://doi.org/10.1101/518142)

The above preprint has been submitted for peer-review and this README will be updated when the manuscript has been accepted for publication in a peer-reviewed journal.

The repository contains a series of jupyter notebooks. They form a sequence, starting with data tidying, transformation and joining before then feeding into a notebooks that reproduce the figures and thence the main results of the manuscript. Each is self-contained in the sense that you don't have to run the predecessors for it to work (since all the input/output files are also stored in the repository) but you can, if you wish, run them all the way through thereby reproducing everything.

## Jupyter notebooks

The first handles the data tidying, processing and joining to create the Training, Test, Validation and MIC datasets. They are numbered in the order that they need to be run.

* `01-parse-original-data.ipynb`
* `02-create-dataset-testtrain.ipynb`
* `03-create-dataset-validation.ipynb`
* `04-create-figure-1.ipynb`
* `05-add-features.ipynb`
* `06-create-figure-2.ipynb`

etc.

Some have flags set at the beginning that need changing and the notebook rerunning. For example, `filestem` at the start of `05-add-features.ipynb` needs to be one of `testtrain`, `validation-samples`, `validation-mutations` or `mic`. This is explained in the notebooks.

The notebooks that reproduce figures are clearly named e.g. `09-create-figure-3.ipynb`. All graphs are writen to disc (`pdf/`) graphs etc including those used in the Supplementary Information.

## Using

There are two options: (1) run in browser using `MyBinder` or (2) running locally. The first is easiest but, since several binaries are not installed, one cannot run `05-add-features`. To try running in browser please click the blue `launch|binder` button at the top of this README.

### Local installation

Whilst the majority of the dependencies are Python packages, two binaries are required by [`sbmlcore`](https://github.com/fowler-lab/sbmlcore) to add a few of the structural features, hence are needed to run `05-add-features.ipynb`. The other notebooks do not require them so can be run independently if you do not wish to install them.

* `stride` is a command line tool that calcualates the secondary structure of a protein from its PDB file. Please follow the download and installation instructions [here](https://webclu.bio.wzw.tum.de/stride/install.html)

* `msms` is another command line tool for calculating protein surfaces. One can download binaries from [here](https://ccsb.scripps.edu/msms/).

Both of these binaries need to be in your `$PATH` so that the Python code can locate and run them.

Since several of the Python packages have pinned versions to help ensure reproducibility, it is recommended to install within a virtual environment via

```
$ git clone git@github.com:fowler-lab/predict-pyrazinamide-resistance.git
$ cd predict-pyrazinamide-resistance
$ python3 -m venv pnca
$ source .venv/bin/activate
(pnca) $ python3 -m pip install --upgrade pip
(pnca) $ pip install -r requirements
```

Now you should be within the `pnca` virtual environment in a terminal and can e.g. launch VS Code to run the notebooks in turn.

**Philip W Fowler**

21 November 2023
