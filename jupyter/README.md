## Prerequisites
* You need to know how to run jupyter notebooks.
* I prefer to run them in PyCharm or DataSpell and tested with these IDEs, but it should work with the vanilla jupyter
IDE
* If using a dark theme with a JetBrains IDE, disable 'Languages & Frameworks > Jupyter >
Invert image output for dark themes', so that the graphics are represented in the same colors as in the thesis
* It probably works with most python 3 installations, but you might need to install some extra packages
* I personally used a venv with python 3.11, at the end of the readme I listed all packages installed in my working
configuration

## Before Running the Notebooks
Before running anything, please open `modules/constant.py` and make sure that all paths are set correctly.
Importantly, you need to set the path to the `AndroidAnalysis` project
(preferably at revision b4925bcc6cc222cd6b999d1a5a203a2cfb10e55d, branch mioRuns, but other versions should work too)

## Order to Run the Notebooks in
1. generatemasterdata2: This pre-calculates the fitness landscape measures.
It can take some time.
Most other notebooks will not work without first running this.
You do not have to run it twice, since the results are saved to disk
2. Now, autocorrelation, neutralitdydistance, neutralityvolume, informationcontent 
and mio can be executed
3. RQ0 can be executed at any time, but it will take long, since it does not take advantage of pre-computed measures
4. before running the rest, mergemasterdata must be executed.
It can only be executed after step 1
5. randomwalks has to be executed after branch_selection

## Notes
* The branch_selection currently does nothing but save the branches, that were used in the case study in the thesis,
to a file.
In order to sample new branches, remove the third last cell.
Beware though, that in randomwalks the branches are hardcoded, so you have to adapt this file after sampling new
branches
* The tex-tables generated for the case study are not exactly the same that were used in the paper.
In the paper, the values might be hardcoded and in a different order or formatted differently.

## Python Packages
I would recommend to just trie and run the notebooks and install anything that is missing, but jut in case, I listed 
all the packages included in my working configuration (not all are needed probably)

    Package                  Version
    ------------------------ -----------
    anyio                    3.6.2
    argon2-cffi              21.3.0
    argon2-cffi-bindings     21.2.0
    arrow                    1.2.3
    asttokens                2.2.1
    attrs                    22.2.0
    backcall                 0.2.0
    beautifulsoup4           4.11.1
    bleach                   5.0.1
    cffi                     1.15.1
    comm                     0.1.2
    contourpy                1.0.6
    cycler                   0.11.0
    debugpy                  1.6.4
    decorator                5.1.1
    defusedxml               0.7.1
    entrypoints              0.4
    executing                1.2.0
    fastjsonschema           2.16.2
    fonttools                4.38.0
    fqdn                     1.5.1
    idna                     3.4
    ipykernel                6.19.4
    ipython                  8.7.0
    ipython-genutils         0.2.0
    ipywidgets               8.0.4
    isoduration              20.11.0
    jedi                     0.18.2
    Jinja2                   3.1.2
    joblib                   1.2.0
    jsonpointer              2.3
    jsonschema               4.17.3
    jupyter                  1.0.0
    jupyter_client           7.4.8
    jupyter-console          6.4.4
    jupyter_core             5.1.1
    jupyter-events           0.5.0
    jupyter_server           2.0.5
    jupyter_server_terminals 0.4.3
    jupyterlab-pygments      0.2.2
    jupyterlab-widgets       3.0.5
    kiwisolver               1.4.4
    MarkupSafe               2.1.1
    matplotlib               3.6.2
    matplotlib-inline        0.1.6
    mistune                  2.0.4
    nbclassic                0.4.8
    nbclient                 0.7.2
    nbconvert                7.2.7
    nbformat                 5.7.1
    nest-asyncio             1.5.6
    notebook                 6.5.2
    notebook_shim            0.2.2
    numpy                    1.24.1
    packaging                22.0
    pandas                   1.5.2
    pandocfilters            1.5.0
    parso                    0.8.3
    pexpect                  4.8.0
    pickleshare              0.7.5
    Pillow                   9.3.0
    pip                      22.3.1
    platformdirs             2.6.0
    prometheus-client        0.15.0
    prompt-toolkit           3.0.36
    psutil                   5.9.4
    ptyprocess               0.7.0
    pure-eval                0.2.2
    pycparser                2.21
    Pygments                 2.13.0
    pyparsing                3.0.9
    pyrsistent               0.19.2
    python-dateutil          2.8.2
    python-json-logger       2.0.4
    pytz                     2022.7
    PyYAML                   6.0
    pyzmq                    24.0.1
    qtconsole                5.4.0
    QtPy                     2.3.0
    rfc3339-validator        0.1.4
    rfc3986-validator        0.1.1
    scipy                    1.9.3
    seaborn                  0.12.1
    Send2Trash               1.8.0
    setuptools               60.2.0
    six                      1.16.0
    sniffio                  1.3.0
    soupsieve                2.3.2.post1
    stack-data               0.6.2
    terminado                0.17.1
    tinycss2                 1.2.1
    tornado                  6.2
    traitlets                5.8.0
    uri-template             1.2.0
    wcwidth                  0.2.5
    webcolors                1.12
    webencodings             0.5.1
    websocket-client         1.4.2
    wheel                    0.37.1
    widgetsnbextension       4.0.5
