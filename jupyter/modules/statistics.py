import math

import scipy.stats
import sys
import modules.constants as const
sys.path.append(const.ANDROID_ANALYSIS_PROJECT_ROOT)
from analysis.util.statistics import vargha_delaney_A
from scipy.stats import fisher_exact


def calculate_mann_whitney_p_values_for_measure_dict(dict):
    """
    Takes a dict of the form <app_name><objective> -> <fitness_function> -> [measure]
    and returns one of the form <app_name><objective> -> (p_value, effect_size)

    If one of the two measure sets contains no values, the resulting p-value is None.
    If the two measure sets do not contain the same amount of elements, the effect size is None.
    """
    return_dict = {}

    for objective in dict:
        assert len(dict[objective].keys()) == 2

        measure_list1 = [x for x in dict[objective]["noDistance"] if x is not None]
        measure_list2 = [x for x in dict[objective]["distance"] if x is not None]
        p_value = None
        effect_size = None
        if not (len(measure_list2) == 0 or len(measure_list1) == 0):
            p_value = scipy.stats.mannwhitneyu(measure_list1, measure_list2, alternative="two-sided")[1]
            if len(measure_list2) == len(measure_list1):
                estimate, magnitude = vargha_delaney_A(measure_list1, measure_list2)
                effect_size = estimate
        return_dict[objective] = (p_value, effect_size)
    return return_dict


def calculate_mann_whitney_p_value(measures_code_based, measures_branch_distance):
    measures_code_based = [x for x in measures_code_based if x is not None and not math.isnan(x)]
    measures_branch_distance = [x for x in measures_branch_distance if x is not None and not math.isnan(x)]

    p_value = None
    effect_size = None
    if not (len(measures_branch_distance) == 0 or len(measures_code_based) == 0):
        p_value = scipy.stats.mannwhitneyu(measures_code_based, measures_branch_distance, alternative="two-sided")[1]
        if len(measures_branch_distance) == len(measures_code_based):
            estimate, magnitude = vargha_delaney_A(measures_code_based, measures_branch_distance)
            effect_size = estimate
    return p_value, effect_size


def calculate_fisher_exact_p_value_and_odds_ratio(a, b, n):
    """
    :param a: The number of successes for algorithm A
    :param b: The number of successes for algorithm B
    :param n: The number of runs
    :return: statistic and pvalue in an object (statistic is the odds ratio)
    """
    return fisher_exact([[a, n-a], [b, n-b]])


def calculate_odds_ratio(a, b, n, rho):
    """
    :param a: The number of successes for algorithm A
    :param b: The number of successes for algorithm B
    :param n: The number of runs
    :param: rho: The summand to handle zero occurence cases
    :return: The odds ratio
    """
    return ((a + rho) / (n + rho - a)) / ((b + rho) / (n + rho - b))
