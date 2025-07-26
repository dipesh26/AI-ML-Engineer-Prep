import numpy as np
import warnings

def clean_missing_values(data):
    if np.isnan(data).sum() == 0:
        print("\n✅ No missing values found.")
        return data
    
    col_mean = np.nanmean(data, axis=0)
    indices = np.where(np.isnan(data))
    data[indices] = np.take(col_mean, indices[1])
    data = np.round(data, 2)
    
    print("✅ Missing values cleaned...")
    return data

def normalizing_cleaned_data(cleaned_data):
    data_min = np.min(cleaned_data)
    data_max = np.max(cleaned_data)
    
    normalized_data = (cleaned_data - data_min) / (data_max - data_min)
    print("✅ Data Normalized...")
    return normalized_data, data_max, data_min

def denormalizing_data(normalized_data, data_max, data_min):
    original_data = normalized_data * (data_max - data_min) + data_min
    print("\n✅ Data Denormalized successfully.")
    return original_data

def main():
    print(f"\n{"="*10} Numpy Data Cleaner {"="*10}")
    while True:
        print(f"\n{"-"*30}")
        user_input = input("Enter the File name: ").strip()
        if not user_input:
            print("\n❗File name can't be empty.")
            continue
        try:
            with open(user_input, 'r') as f:
                headers = f.readline().strip().split(',')
            
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', category=UserWarning)
                load_file = np.genfromtxt(user_input, delimiter=',', skip_header=1)
            
            if load_file.size == 0:
                print("\n❗File is empty or only contains headers.")
                continue
            
            print("\n✅ File loaded...")
            
            cleaned_data = clean_missing_values(load_file)
            normalized_data, data_max, data_min = normalizing_cleaned_data(cleaned_data)
            
            print("\nNormalized & Cleaned Data:")
            print("--------------------------")
            print("\t".join(headers))
            for row in normalized_data:
                print("\t".join(f"{val:.2f}" for val in row))
            
            option = str(input("\nSee Original Cleaned Data? [y]: ")).strip().lower()
            if option == 'y':
                original_data = denormalizing_data(normalized_data, data_max, data_min)
                print("\nOriginal Cleaned Data:")
                print("----------------------")
                print("\t".join(headers))
                for row in original_data:
                    print("\t".join(f"{val:.2f}" for val in row))
                print("\n")
                break
            else:
                print("\n")
                exit()
        
        except FileNotFoundError as f:
            print("\n❗",f)

if __name__ == "__main__":
    main()