# Paths
ANDROID_ANALYSIS_PROJECT_ROOT = '/home/sebastian/projects/mate_projects/androidanalysis'
RANDOM_WALK_DATA_PATH = '../dataset/random_walks'
DIAGRAM_OUT_PATH = 'out'
MIO_RUNS_PATH = '../dataset/mio_runs'

# Other constants
REPETITIONS = 20

CODE_BASED = "Code-based fitness"
BRANCH_DISTANCE = "Branch distance"

FITNESS_FUNCTION = "Fitness function"
OBJECTIVE = "Objective"
SUCCESS = "Success"
P_VALUE = "P-value"

NEUTRALITY_DISTANCE = "Neutrality distance"
NEUTRALITY_VOLUME = "Neutrality volume"
INFORMATION_CONTENT = "Information content"


def AUTOCORRELATION(k: int):
    return "Autocorrelation for k = " + str(k)
