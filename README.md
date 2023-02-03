# Repository of my Bachelor's Thesis
This repository supplies the files and information needed to reproduce the experiments from my bachelor's thesis.
This readme contains all the information needed to reproduce my MATE runs on the cluster.
At the end of the file, an overview of all files and folders in this repo is given, which also explains what to do next.

## Other Repositories needed
The following repos and branches are needed to reproduce my work:
* MATE on the branches randomWalks and mioRuns
* MATE-Server on the branches randomWalks and mioRuns
* MATE-Commander on the branches randomWalksCluster and mioCluster
* For reproduction on your local Linux installation you could use the randomWalksLinux and mioLinux branches of the commander, but the explanations in this readme are only for cluster execution.
* AndroidAnalysis on the branches randomWalks and mioRuns

## Reproduction of the Random Walks on the Cluster
For reproducing the experiments, you need access to the university SLURM cluster.
The explanation for the reproduction assumes no MATE environment currently set up in your scratch folder.

* Create a `/scratch/<username>/sbatch_out` folder
* Create a `/scratch/<username>/save` folder
* Create a `/scratch/<username>/home` folder
* Clone the `mate-commander` repository into the `/scratch/<username>/home` folder
* Clone the `bachelors-thesis` repository into the `scratch/<username>` folder
* Copy the file `/scratch/<username>/bachelors-thesis/test_dir/test_dir_random_walks.zip` into `/scratch/<username>/home/`
* Unzip the zip in-place
* Clone the MATE-Repository into the `/scratch/<username>/home/test_dir` folder.   
* Place an empty `log` folder under `/scratch/<username>/home/test_dir`.
* Clone the MATE-Server-Repository into the `/scratch/<username>/home/test_dir/bin` folder
* Copy the file `/scratch/<username>/bachelors-thesis/bachelor-thesis-apps.zip` into `/scratch/<username>/home/test_dir`
* Unzip the zip in-place
* Create a `configs` folder within the directory `/scratch/<username>/home/test_dir`.
* Place an archive called  **android_env.tar.gz** into the `/scratch/<username>/home` folder.
* In `/scratch/<username>/home/mate-commander`, checkout the branch `randomWalksCluster`
* In `/scratch/<username>/home/test_dir/mate`, checkout the branch `randomWalks`
* In `/scratch/<username>/home/test_dir/bin/mate-server`, checkout the branch `randomWalks`
* In `/scratch/<username>/home/test_dir/bin`, execute the file `generate.sh`
* Open the file `/scratch/<username>/home/test_dir/generate_configs.py` with your favourite text editor.
* The configurations for the random walks with code-based fitness are in the dict `props_blocks` (has nothing to do with block coverage, is just called like that, because I once palanned on doing block coverage)
* The configurations for the random walks with branch distance are in the dict `props_branches`
* Beware that for the random walks, the whole run is stopped and continued 6 times, which means that in order to reach 751 iterations, the iteration number must be 125
* The rest of the configurations can be edited in the other dicts
* The last two dicts in this list of dicts are `remainingWdhsDistance` and `remainingWdhsNoDistance`, which contain the number of runs you want to do for each app for branch distance and code-based fitness respectively (code-based is called NoDistance here)
* Only the five apps that are included in the paper can be used, even though there are more apps listed in the template `generate_configs.py`. Please delete the other apps or set the number to 0. (The last 5 apps in the list are possible)
* For the other apps, set the number to the amount of runs you want to start for that app and fitness function
* After setting everything the way you want it (most things can be left the way they are, except the apps that do not work), exit the editor.
* Execute `cp -r bachelor-thesis-apps/apps appsBranch` in `/scratch/<username>/home/test_dir`
* Now execute `/scratch/<username>/test_dir/genereate_configs.py`
* Edit the file `/scratch/<username>/home/test_dir/batch_run.py`, so that the correct cluster nodes are used. The random walks are preferably executed on pontipine, but zeus works as well
* Execute `/scratch/<username>/home/test_dir/batch_run.py`

## Extraction of the Random Walks
* Clone the `AndroidAnalysis` repository into the `/scratch/<username>` folder
* Cd into the project and checkout the branch `randomWalks`
* Open the file `config.ini` and adjust the paths, mainly by exchanging my username with your's
* Set the `walk_len` to the length of your walks (if you specified an iteration number of x, the walk length is 6x + 1)
* Create the two folders you specified under `data_dir` and `svg_dir`
* Run `python3.9 main.py config.ini <run_id>`
* Ignore the output in `svg_dir`, the diagrams are generated in the jupyter notebooks
* For all successful runs, the random walks will be written to `data_dir`!
* The contents of data_dir can be copied into the `dataset/random_walks` subfolder of the bachelor's thesis repository. The jupyter notebooks will per-default search this folder for input data.
* It is normal that some runs will fail. Execute the `count.py` script to figure out, how many successful runs you already have per app and fitness function. Then you know how much runs you need to retry!

## Reproduction of the MIO Runs on the Cluster
* Create a `/scratch/<username>/sbatch_out` folder
* Create a `/scratch/<username>/save` folder
* Create a `/scratch/<username>/home` folder
* Clone the `mate-commander` repository into the `/scratch/<username>/home` folder
* Clone the `bachelors-thesis` repository into the `scratch/<username>` folder
* Copy the file `/scratch/<username>/bachelors-thesis/test_dir/test_dir_mio_runs.zip` into `/scratch/<username>/home/`
* Unzip the zip in-place
* Clone the MATE-Repository into the `/scratch/<username>/home/test_dir` folder   
* Place an empty `log` folder under `/scratch/<username>/home/test_dir`.
* Clone the MATE-Server-Repository into the `/scratch/<username>/home/test_dir/bin` folder
* Copy the file `/scratch/<username>/bachelors-thesis/bachelor-thesis-apps.zip` into `/scratch/<username>/home/test_dir`
* Unzip the zip in-place
* Create a `configs` folder within the directory `/scratch/<username>/home/test_dir`
* Place an archive called  **android_env.tar.gz** into the `/scratch/<username>/home` folder
* In `/scratch/<username>/home/mate-commander`, checkout the branch `mioCluster`
* In `/scratch/<username>/home/test_dir/mate`, checkout the branch `mioRuns`
* In `/scratch/<username>/home/test_dir/bin/mate-server`, checkout the branch `mioRuns`
* In `/scratch/<username>/home/test_dir/bin`, execute the file `generate.sh`
* Open the file `/scratch/<username>/home/test_dir/generate_configs.py` with your favourite text editor
* The configurations for the mio runs with code-based fitness are in the dict `props_blocks` (has nothing to do with block coverage, is just called like that, because I once palanned on doing block coverage)
* The configurations for the mio runs with branch distance are in the dict `props_branches`
* In contrast to the random walks, the iterations number for mio runs is the actual number of iterations
* The rest of the configurations can be edited in the other dicts
* The last two dicts in this list of dicts are remainingWdhsDistance and remainingWdhsNoDistance, which contain the number of runs you want to do for each app for branch distance and code-based fitness respectively (code-based is called NoDistance here)
* Only the five apps that are included in the paper can be used, even though there are more apps listed in the template `generate_configs.py`. Please delete the other apps or set the number to 0. (The last 5 apps in the list are possible)
* For the other apps, set the number to the amount of runs you want to start for that app and fitness function
* After setting everything the way you want it (most things can be left the way they are, except the apps that do not work), exit the editor.
* Now execute `/scratch/<username>/test_dir/genereate_configs.py`
* Edit the file `/scratch/<username>/home/test_dir/batch_run.py`, so that the correct cluster nodes are used. The random walks are preferably executed on ponipine, but zeus works as well
* Execute `/scratch/<username>/home/test_dir/batch_run.py`

## Extraction of the MIO Runs
* Clone the `AndroidAnalysis` repository into the `/scratch/<username>` folder
* Cd into the project and checkout the branch `mioRuns`
* Open the file `config.ini` and adjust the paths, mainly by exchanging my username with your's
* Set the `walk_len` to the length of your walks (if you specified an iteration number of x, the walk length is x + 1)
* Create the folder you specified under `mio_data`
* Run `python3.9 main.py config.ini <run_id>`
* For all successful runs, the mio runs will be written to `mio_data`!
* Currently, only the three apps that were used with MIO in the thesis result in successful runs. If you want to use the other two apps as well, you have to add them to the dict at the top of the `mio_runs.py` plugin and specify the (correct) number of branches for every app. The jupyter notebooks have never been tried with other apps than the three ones from the thesis though, so it is not guaranteed to work.
* The contents of mio_data can be copied into the `dataset/mio_runs` subfolder of the bachelor's thesis repository. The jupyter notebooks will per-default search this folder for input data.
