from pathlib import Path

import numpy as np
import pandas as pd
from pandas import DataFrame
from joblib import Parallel, delayed
import modules.constants as const


def __get_tuple_list_from_file(file, measure_function):
    name1 = const.CODE_BASED
    name2 = const.BRANCH_DISTANCE
    tuples = []
    matrix = np.loadtxt(file, delimiter=",")
    i = 0
    for row in matrix:
        autocor = measure_function(row)
        if autocor is not None:
            if "noDistance" in file.name:
                tuples.append((name1, autocor))
            else:
                tuples.append((name2, autocor))
        i += 1
    return tuples


def get_measure_dataframe(measure_function, measure_name):
    data_path = Path(const.RANDOM_WALK_DATA_PATH)

    x = "Fitness function"

    file_list = data_path.glob('*')

    tuples_unflat = \
        Parallel(n_jobs=4)(delayed(__get_tuple_list_from_file)(file, measure_function) for file in file_list)

    tuples = sum(tuples_unflat, [])

    df = DataFrame.from_records(data=tuples, columns=[x, measure_name])
    return df


def __get_random_walks_in_tuple_form():
    """
    Generates a list of tuples of the form
    (<run_id>_<job_id>_<app_name>_<fitness_function>, <objective>, <fitness_sequence>)
    """

    data_path = Path(const.RANDOM_WALK_DATA_PATH)

    fitness_sequences = []

    file_list = data_path.glob('*')
    for file in file_list:
        matrix = np.loadtxt(file, delimiter=",")
        i = 0
        for row in matrix:
            fitness_sequences.append((file.name, i, row))
            i += 1

    return fitness_sequences


def get_sequences_per_objective_and_fitness_function():
    """
    Generates a dictionary of the form
    <app_name><objective> -> <fitness_function> -> [fitness_sequence]
    """

    fitness_sequences = __get_random_walks_in_tuple_form()

    dict = {}

    for tup in fitness_sequences:
        run_id = tup[0].split("_")[0]
        job_id = tup[0].split("_")[1]
        app_name = tup[0].split("_")[2]
        fitness_function = tup[0].split("_")[3]
        objective = tup[1]
        fitness_sequence = tup[2]

        objective_identifier = app_name + str(objective)

        if not objective_identifier in dict.keys():
            dict[objective_identifier] = {}

        if not fitness_function in dict[objective_identifier].keys():
            dict[objective_identifier][fitness_function] = []

        dict[objective_identifier][fitness_function].append(fitness_sequence)
    return dict


def apply_measure_to_dict(dict, m):
    """
    Takes a dict of the form <app_name><objective> -> <fitness_function> -> [fitness_sequence] and a measure m
    and return one of the form <app_name><objective> -> <fitness_function> -> [m(fitness_sequence)]
    """
    return_dict = {}

    for objective in dict:
        return_dict[objective] = {}
        for fitness_function in dict[objective]:
            return_dict[objective][fitness_function] = []
            for fitness_sequence in dict[objective][fitness_function]:
                return_dict[objective][fitness_function].append(m(fitness_sequence))

    return return_dict


def __extract_data_from_mio_run_file_name(file_name):
    """
    Takes a MIO run file name and returns run_id, app_name, fitness_function as strings
    """
    file_name_split_by_underscore = file_name.split("_")

    run_id = file_name_split_by_underscore[0] + "_" + file_name_split_by_underscore[1]
    app_name = file_name_split_by_underscore[2]
    fitness_function = file_name_split_by_underscore[3]
    for i in range(4, len(file_name_split_by_underscore)):
        fitness_function += "_" + file_name_split_by_underscore[i]
    return run_id, app_name, fitness_function


def __beautify_ff(ff):
    """
    Beautify the representation of the fitness function.
    """
    if ff == "BRANCH_DISTANCE_MULTI_OBJECTIVE":
        return const.BRANCH_DISTANCE
    else:
        return const.CODE_BASED


def get_mio_runs():
    """
    Return the MIO runs in a dataframe with the columns fitness function, objective and success
    :return:
    """

    data_path = Path(const.MIO_RUNS_PATH)

    fitness_functions = []
    objectives = []
    successes = []

    for file in data_path.glob("*"):
        file_name = file.name

        run_id, app_name, fitness_function = __extract_data_from_mio_run_file_name(file_name)

        objective = 0
        for line in open(file, 'r').readlines():
            fl = float(line)
            success = 0

            assert fl == 0.0 or fl == 1.0
            if fl == 1.0:
                success = 1

            fitness_functions.append(__beautify_ff(fitness_function))
            objectives.append(app_name + str(objective))
            successes.append(success)

            objective += 1

    df = pd.DataFrame()

    df[const.FITNESS_FUNCTION] = fitness_functions
    df[const.OBJECTIVE] = objectives
    df[const.SUCCESS] = successes

    return df
