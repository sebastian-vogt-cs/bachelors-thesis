from pandas import DataFrame
from matplotlib import pyplot as plt
import seaborn as sns

from pathlib import Path


def violin_plot_two_fold(dataset1: list, dataset2: list, name1: str, name2: str, x: str, y: str, output_file: Path):
    """
    dataset1: list of values for left violin plot
    dataset2: list of values for right violin plot
    name1: label for the left violin plot
    name2: label for the right violin plot
    x: label for the x axis
    y: label for the y axis
    """

    tuples = []
    for value in dataset1:
        tuples.append((name1, value))
    for value in dataset2:
        tuples.append((name2, value))

    df = DataFrame.from_records(data=tuples, columns=[x, y])

    fig = plt.figure()
    sns.set_theme(style="darkgrid")
    ax = sns.violinplot(data=df, x=x, y=y, linewidth=2, color="#bdbdbd", order=[name1, name2])
    medians = [df.groupby([x])[y].median()[name1], df.groupby([x])[y].median()[name2]]
    nobs = [df[x].value_counts()[name1], df[x].value_counts()[name2]]
    nobs = [str(val) for val in nobs]
    nobs = ["n = " + i for i in nobs]

    pos = range(len(nobs))
    for tick, label in zip(pos, ax.get_xticklabels()):
        ax.text(pos[tick], medians[tick] + 0.03, nobs[tick],
                horizontalalignment='center',
                size='small',
                color='w',
                weight='semibold')
    plt.savefig(output_file)
    df.to_csv(Path(output_file.name + "df.txt"))
    plt.close(fig)
