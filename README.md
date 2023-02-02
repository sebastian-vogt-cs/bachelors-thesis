# Repository of my Bachelor's Thesis

## Reproduction of the Random Walks on the Cluster
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
* In `/scratch/<username>/home/test_dir/bin/mate-server`, execute the file `generate.sh`
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

## Extraction of the random walks
* Clone the AndroidAnalysis-Repository into the `/scratch/<username>` folder
* Cd into the project and checkout the branch `randomWalks`
* Open the file `config.ini` and adjust the paths, mainly by exchanging my username with your's
* Set the `walk_len` to the length of your walks (if you specified an iteration number of x, the walk length is 6x + 1)
* Create the two folders you specified under `data_dir` and `svg_dir`
* Run `python3.9 main.py config.ini <run_id>`
* Ignore the output in `svg_dir`, the diagrams are generated in the jupyter notebooks
* For all successful runs, the random walks will be written to `data_dir`!
* The contents of data_dir can be copied into the `dataset/random_walks` subfolder of the bachelor's thesis repository. The jupyter notebooks will per-default search this folder for input data.
* It is normal that some runs will fail. Execute the `count.py` script to figure out, how many successful runs you already have per app and fitness function. Then you know how much runs you need to retry!
