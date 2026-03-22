#Authors: Ashutosh Shivakumar, Sean Banerjee
#Purpose: Provide summary statistics (mean, min, max, standard deviation) of head, left-hand, right-hand, and eye gaze from the VR system. 

import os
import pandas as pd
import statistics
import math
from prettytable import PrettyTable

def process_csv_files(root_folder, timestamp_col_name='timeStampNs'):
    samples_per_second_list = []

    #EyeGaze, Head, LeftHand, RightHand
    modalities = ["_0_0\\EyeGaze", "_0_0\\Head", "_0_0\\LeftHand", "_0_0\RightHand", "_0_3\\EyeGaze", "_0_3\\Head", "_0_3\\LeftHand", "_0_3\RightHand", "_3_0\\EyeGaze", "_3_0\\Head", "_3_0\\LeftHand", "_3_0\RightHand", "_3_3\\EyeGaze", "_3_3\\Head", "_3_3\\LeftHand", "_3_3\RightHand"]

    t = PrettyTable(['Treatment', 'Type of Data', 'Min', 'Max', 'Mean', 'SD'])

    for submodalities in modalities:
        print("")
        print("Processing..." + submodalities)
        samples_per_second_list.clear()
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if file_path.endswith(submodalities+".csv"):
                    
                    try:
                        df = pd.read_csv(file_path, delimiter=',(?![^\(]*[\)])', engine='python', index_col= False)

                        df[timestamp_col_name] = pd.to_datetime(df[timestamp_col_name], unit = 'ns')

                        df = df.set_index(timestamp_col_name)                        
                        df_resampled = df.resample('1s').size()

                        df_resampled_without_index = df_resampled.values
                        samples_per_second_list.append(df_resampled_without_index.mean())

                    except Exception as e:
                        print(f"  Error processing {filename}: {e}")
        
        #print("Number of Participants: ", len(samples_per_second_list))

        #Calculate minimum
        min_avg_value = min(samples_per_second_list)        
        #Calculate maximum
        max_avg_value = max(samples_per_second_list)
        #Calculate mean
        overall_mean = statistics.mean(samples_per_second_list)
        #Calculate standard deviation
        overall_standard_deviation = statistics.stdev(samples_per_second_list)
        
        if "_0_0" in submodalities:            
            if "Eye" in submodalities:
                row = ["00", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["00", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["00", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["00", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            
        elif "_0_3" in submodalities:
            if "Eye" in submodalities:
                row = ["03", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["03", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["03", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["03", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            
        elif "_3_0" in submodalities:
            if "Eye" in submodalities:
                row = ["30", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["30", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["30", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["30", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            
        else:
            if "Eye" in submodalities:
                row = ["33", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["33", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["33", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["33", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
        t.add_row(row)
        t.add_divider()
    print(t)

if __name__ == "__main__":
    #Data path is assumed to be 'VRData'
    root_folder_path = 'VRData'
    process_csv_files(root_folder_path)