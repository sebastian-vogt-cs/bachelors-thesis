from typing import Optional
import math
import sys

machine_epsilon = sys.float_info.epsilon


def autocorrelation(f: list[float], k: int) -> Optional[float]:
    assert len(f) > 0
    assert k > 0
    assert k < len(f)

    f_bar: float = sum(f) / len(f)
    numerator: float = 0.0
    denominator: float = 0.0
    for i in range(0, len(f) - k):
        numerator += (f[i] - f_bar) * (f[i + k] - f_bar)
    for i in range(0, len(f)):
        denominator += (f[i] - f_bar) * (f[i] - f_bar)

    if abs(denominator) < machine_epsilon:
        # The result is none iff the input walk is completely flat
        return None
    elif abs(numerator) < machine_epsilon:
        return 0
    else:
        return numerator / denominator


def neutrality_distance(f: list[float]) -> int:
    assert len(f) > 0

    dist: int = 1
    while dist < len(f) and abs(f[dist] - f[0]) < machine_epsilon:
        dist += 1
    return dist


def neutrality_volume(f: list[float]) -> int:
    assert len(f) > 0

    volume: int = 1
    current_fitness = f[0]
    for fitness in f:
        if abs(fitness - current_fitness) > machine_epsilon:
            current_fitness = fitness
            volume += 1
    return volume


def S(f: list[float], epsilon: float):
    deltas: list[float] = [f[i] - f[i - 1] for i in range(1, len(f))]
    string: list[int] = [-1 if x < -epsilon else 0 if abs(x) <= epsilon else 1 for x in deltas]
    return string


def count_occurances(string: list[int], p: int, q: int) -> int:
    occurances: int = 0
    for i in range(0, len(string) - 1):
        if string[i] == p and string[i + 1] == q:
            occurances += 1
    return occurances


def information_content(f: list[float]):
    epsilon_star = calculate_epsilon_star_for_information_content(f)
    return max(information_content_with_epsilon(f, 0),
               information_content_with_epsilon(f, epsilon_star / 128),
               information_content_with_epsilon(f, epsilon_star / 64),
               information_content_with_epsilon(f, epsilon_star / 32),
               information_content_with_epsilon(f, epsilon_star / 16),
               information_content_with_epsilon(f, epsilon_star / 8),
               information_content_with_epsilon(f, epsilon_star / 4),
               information_content_with_epsilon(f, epsilon_star / 2),
               information_content_with_epsilon(f, epsilon_star / 1))


def calculate_epsilon_star_for_information_content(f: list[float]):
    epsilon_star_lower = 0.0
    epsilon_star_higher = 1.0
    while epsilon_star_higher - epsilon_star_lower > machine_epsilon:
        mid = (epsilon_star_lower + epsilon_star_higher) / 2
        ic = information_content_with_epsilon(f, mid)
        if abs(ic) < machine_epsilon:
            epsilon_star_higher = mid
        else:
            epsilon_star_lower = mid
    return epsilon_star_higher


def information_content_with_epsilon(f: list[float], epsilon: float):
    string: list[int] = S(f, epsilon)
    assert len(string) == len(f) - 1

    n: int = len(string) - 1

    assert n > 0
    H: float = 0
    for p in range(-1, 2):
        for q in range(-1, 2):
            if p != q:
                npq: int = count_occurances(string, p, q)
                Ppq: float = npq / n
                if npq != 0:
                    H -= Ppq * math.log(Ppq, 6)
    return H


def density_basin_information(f: list[float], epsilon: float):
    string: list[int] = S(f, epsilon)
    assert len(string) == len(f) - 1

    n: int = len(string) - 1

    assert n > 0
    h: float = 0
    for p in range(-1, 2):
        npp: int = count_occurances(string, p, p)
        Ppp: float = npp / n
        if npp != 0:
            h -= Ppp * math.log(Ppp, 3)
    return h


def phi(i, j, k, n, s):
    if i > n:
        return k
    elif j == 0 and s[i - 1] != 0:
        return phi(i + 1, i, k + 1, n, s)
    elif j > 0 and s[i - 1] != 0 and s[i - 1] != s[j - 1]:
        return phi(i + 1, i, k + 1, n, s)
    else:
        return phi(i + 1, j, k, n, s)


def partial_information_content(f: list[float], epsilon: float) -> float:
    string: list[int] = S(f, epsilon)
    n: int = len(string)
    mu = phi(1, 0, 0, n, string)

    assert n > 0
    return mu / n


def number_of_levels(f: list[float]) -> float:
    levels = []
    n_levels = 0
    for val in f:
        if val not in levels:
            levels.append(val)
            n_levels += 1
    return n_levels
