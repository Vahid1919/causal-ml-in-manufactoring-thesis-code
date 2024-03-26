import matplotlib.pyplot as plt
import pandas as pd
from prepare_dataset import prepare
import numpy as np

df = pd.read_csv("./chunks/chunk10.csv", low_memory=False)



df = prepare(df)


def scatter_plot_with_correlation_line(x, y, graph_filepath):
    # Create scatter plot
    plt.scatter(x, y, c="#c23424")

    # Add correlation line
    axes = plt.gca()
    m, b = np.polyfit(x, y, 1)
    X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.xlabel('Mass')
    plt.ylabel('Co2 Emissions')
    plt.plot(X_plot, m*X_plot + b, '-')

    # Save figure
    plt.show()
    # plt.savefig(graph_filepath, dpi=900, format='png', bbox_inches='tight')



scatter_plot_with_correlation_line(df['mass'], df["co2_nedc"], 'scatter_plot.png')




































# # print(df)


# # plt.plot(df['mass'], [df['co2_nedc'], df['mass']])
# # plt.show()



# plt.scatter(df['mass'], df['co2_nedc'])
# # df.plot(x='mass', y='co2_nedc')
# plt.xlabel('Mass')
# plt.ylabel('Co2 Emissions')

# print(plt.show())
# plt.savefig(graph_filepath, dpi=300, format='png', bbox_inches='tight')

# # for label in cols.columns[:-1]:
# #   plt.hist(df[df["class"]][label], color="blue", label="gamma", alpha=0.7, density=True)
# #   plt.hist(df[df["class"]][label], color="red", label="hydron", alpha=0.7, density=True)
# #   plt.title(label)
# #   plt.ylabel("Probability")
# #   plt.xlabel(label)
# #   plt.legend()
# #   plt.show()




 # cols = pd.read_csv("./chunks/chunk11.csv", nrows=50)

# cols = prepare(cols)