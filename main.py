import pandas as pd
from dowhy import CausalModel
import glob
import os


# Using all the chunks combined
# path = "/Users/vahidnesro/Documents/Jacobs University/Spring 2023/Thesis/thesis-env/data/chunks/"
# all_files = glob.glob(os.path.join(path, "*.csv"))
# df = pd.concat([pd.read_csv(f, dtype={'At1 (mm)': 'float64',
#                         'At2 (mm)': 'float64',
#                         'Ewltp (g/km)': 'float64',
#                         'Mt': 'float64',
#                         'ec (cm3)': 'float64',
#                         'ep (KW)': 'float64',
#                         'z (Wh/km)': 'float64'
#                         }) for f in all_files], ignore_index=True)

df = pd.read_csv("./final_prepared_dataset.csv", dtype={
                        'co2': 'float64',
                        'mass': 'float64',
                        'engine_capacity': 'float64',
                        'engine_power': 'float64',
                        }
                        ,  index_col=0)


print("imported dataset")
df = df.reset_index()
print(df)


diagram = ''' digraph {
bb="0,0,1,1";
co2 [outcome,pos="0.466,0.619"];
engine_capacity [pos="0.777,0.299"];
engine_power [pos="0.222,0.320"];
fuel_consumption [pos="0.381,0.396"];
fuel_type [exposure,pos="0.559,0.311"];
mass [pos="0.464,0.127"];
engine_capacity -> co2;
engine_capacity -> mass;
engine_power -> co2;
engine_power -> fuel_consumption;
fuel_consumption -> co2;
fuel_type -> co2;
fuel_type -> engine_capacity;
fuel_type -> engine_power;
fuel_type -> fuel_consumption;
mass -> co2;
mass -> fuel_consumption;
}
''' 
  

model = CausalModel(
    data=df,
    treatment= ["fuel_consumption"],
    outcome= ["co2"],
    graph=diagram.replace("\n", " "))



print("Model Created")
print(model._graph)
identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)

print(identified_estimand)


print("****************************************************")


estimate = model.estimate_effect(identified_estimand,
                                 method_name="backdoor.linear_regression", test_significance=True)


print(estimate)
print("Causal Estimate is " + str(estimate.value))

print("****************************************************")

refute_results_common_cause = model.refute_estimate(identified_estimand, estimate,
                                       method_name="random_common_cause")

print(refute_results_common_cause)

print("****************************************************")

refute_results_placebo = model.refute_estimate(identified_estimand, estimate,
                                       method_name="placebo_treatment_refuter")
print(refute_results_placebo)
print("****************************************************")

refute_results_subset = model.refute_estimate(identified_estimand, estimate,
                                       method_name="data_subset_refuter")
print(refute_results_subset)









