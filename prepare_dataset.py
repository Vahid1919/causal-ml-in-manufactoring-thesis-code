import pandas as pd

def prepare (df) :
    # PREPARING DATASET
    cols = [
        "ID",
        "Country",
        "VFN",
        "Mp",
        "Mh",
        "Man",
        "MMS",
        "Tan",
        "T",
        "Va",
        "Ve",
        "Mk",
        "Cn",
        "Ct",
        "Cr",
        "r",
        "m (kg)",
        "Mt",
        "Enedc (g/km)",
        "Ewltp (g/km)",
        "W (mm)",
        "At1 (mm)",
        "At2 (mm)",
        "Ft",
        "Fm",
        "ec (cm3)",
        "ep (KW)",
        "z (Wh/km)",
        "IT",
        "Ernedc (g/km)",
        "Erwltp (g/km)",
        "De",
        "Vf",
        "Status",
        "year",
        "Date of registration",
        "Fuel consumption ",
        "Electric range (km)",
    ]


    # Remove unnecesary columns -- replaced with usecols during import
    to_remove = [
        "ID",
        "Country",
        "VFN",
        "Mp",
        "Mh",
        "Man",
        "MMS",
        "Tan",
        "T",
        "Va",
        "Ve",
        "Mk",
        "Cn",
        "Ct",
        "Cr",
        "r",
        "m (kg)",
        "Enedc (g/km)",
        "IT",
        "Fm",
        "Ernedc (g/km)",
        "Erwltp (g/km)",
        "De",
        "Vf",
        "Status",
        "year",
        "z (Wh/km)",
        "Date of registration",
        "Electric range (km)",
    ]

    # for column in to_remove:
    #     df = df.drop(column, axis=1)


    # Rename Columns
    df = df.rename(
        columns={
            "Mt": "mass",
            "Ewltp (g/km)": "co2",
            "W (mm)": "wheel_base",
            "At1 (mm)": "axle_width_steer",
            "At2 (mm)": "axle_width_other",
            "Ft": "fuel_type",
            "ec (cm3)": "engine_capacity",
            "ep (KW)": "engine_power",
            "Fuel consumption ": "fuel_consumption",
        }
    )
    print("Renamed Columns")


    # Change fuel_type into numbers
    # petrol - 1 | diesel - 2 | electric - 3 | petrol/electric - 4 | 
    # lpg - 5 | diesel/electric  - 6 | ng - 7 | e85 - 8 | hydrogen - 9 |

    dict = {
        "petrol": 1,
        "diesel": 2,
        "electric": 3,
        "petrol/electric": 4,
        "lpg": 5,
        "diesel/electric": 6,
        "ng": 7,
        "NG-biomethane" : 7,
        "e85": 8,
        "hydrogen": 9
    }

    # Fix capitalization inconsistency
    def to_lower(x):
        if(type(x) == type(float(1))):
            x = None
        x = x.lower()
        return x

    # print(df['fuel_type'])
    df["fuel_type"] = df["fuel_type"].apply(to_lower)

    df["fuel_type"] = df["fuel_type"].map(dict)


    print("Mapped Fuel Type")


    # # # Remove rows with NaN values using apply and dropna
    # # df = df.apply(lambda row: row.dropna(), axis=1)
    # for index, row in df.iterrows():
    #     if row['fuel_type'] == 4 or row['fuel_type'] == 6:
    #         df.drop(index)

    # print("Removed Electric Cars")
   

    # df = df[df['z (Wh/km)'].isna()]
    # df = df.drop('z (Wh/km)', axis=1)

    # print("Removed Electric Power Column")

    # # Drop rows with empty data
    # df.dropna(
    #     axis=0,
    #     how='any',
    #     inplace=True
    # )

    # print("Dropped Empty Rows")

    
    return df