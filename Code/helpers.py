import pandas as pd

def split_data_using_percentage(df, percentage, categories_column):
    sample_df = pd.DataFrame()
    columns = df.columns
    print(columns)
    print(df[df['id']])
    for column in columns:
        print(column)
        current_category_df = df[df["id"]]
        print(current_category_df)
#         current_category_size = len(current_category_df)
#         desired_samples = (percentage * current_category_size) / 100
#         print(f"Current Column: {column}")
#         print(f"Total size: {current_category_size}")
#         print(f"Extracted Samples: {desired_samples}")
#         print("======================================================")
#         sample_df = pd.concat([current_category_df.sample(n=desired_samples),sample_df])
    return sample_df