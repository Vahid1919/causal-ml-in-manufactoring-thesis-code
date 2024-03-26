import pandas as pd
import glob
import os



whole_df = pd.DataFrame()
chunksize = 10 ** 6
for chunk in pd.read_csv("./prepared_dataset.csv", chunksize=5000):
    # chunk is a DataFrame. To "process" the rows in the chunk:
        chunk.drop(["wheel_base", "axle_width_steer", "axle_width_other"], axis=1, inplace=True)
        for index, row in chunk.iterrows():
            if row['fuel_type'] == 4 or row['fuel_type'] == 6:
                chunk.drop(index)
                print(index)

        chunk = chunk[chunk['z'].isna()]
        chunk = chunk.drop('z', axis=1)

        print("Removed Electric Power Column")

        # Drop rows with empty data
        chunk.dropna(
            axis=0,
            how='any',
            inplace=True
        )

        whole_df = pd.concat([whole_df, chunk], ignore_index=True)
        print("Finished Chunk")

whole_df.to_csv("final_prepared_dataset.csv", index=False)