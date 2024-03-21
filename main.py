import pandas as pd

from experiment_specific.post_process import post_process

# BEFORE YOU RUN: Configure your path settings in path_settings/settings.py
#   To do this, change the name of settings_template.py file to settings.py 
#   and set the PATH_TO_CSV variable to the path of your CSV file.
#   a "path" is the location of a file on your computer.
from path_settings.settings import PATH_TO_CSV, SAVE_PATH

def main():
    # Load the CSV data using Pandas.
    df = pd.read_csv(PATH_TO_CSV)

    # As simple as it seems, the rest of this process is experiment specific. 
    # Look to and change the experiment_specific folder to fit your needs!
    processed_df = post_process(df)

    # Save the processed data to a new CSV file.
    processed_df.to_csv(SAVE_PATH + "processed_data.csv")


if __name__ == "__main__":
    main()