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
    return normalized_data, data_min, data_max

def denormalizing_data(normalized_data, data_min, data_max):
    original_data = normalized_data * (data_max - data_min) + data_min
    print("\n✅ Data Denormalized successfully.")
    return original_data

def display_data(data, headers):
    print("--------------------------")
    print("\t".join(headers))
    for row in data:
        print("\t".join(f"{val:.2f}" for val in row))

def save_data(data, headers):
    file_name = "Normalized & cleaned data.csv"
    np.savetxt(file_name, data, delimiter=",", header=",".join(headers), comments='', fmt="%.2f")
    print(f"\n✅ Data Exported successfully to \"{file_name}\".")

def main():
    print(f"\n{"="*10} Numpy Data Cleaner {"="*10}")
    while True:
        print(f"\n{"➖"*20}")
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
            normalized_data, data_min, data_max = normalizing_cleaned_data(cleaned_data)
            
            print("\nNormalized & Cleaned Data:")
            display_data(normalized_data, headers)

            seen_original = False
            saved = False

            while True:
                print("\n---------------------------------")
                if not seen_original:
                    print("🔸[y] See Original Cleaned Data")
                if not saved:
                    print("🔸[s] Save to .csv file")
                print("🔸[n] New")
                print("🔸[e] To Exit")
                print("---------------------------------")
                
                option = str(input("\nSelect the Options ⬆️  : ")).strip().lower()
                if not option:
                    print("\n❗ Option Can't be empty.")
                    continue
                elif option == 'y' and not seen_original:
                    original_data = denormalizing_data(normalized_data, data_min, data_max)
                    print("\nOriginal Cleaned Data:")
                    display_data(original_data, headers)
                    seen_original = True
                elif option == 's' and not saved:
                    save_data(normalized_data, headers)
                    saved = True
                elif option == 'n':
                    break
                elif option == 'e':
                    print(f"\n{"-"*10} Thank you for Visiting {"-"*10}\n")
                    exit()
                else:
                    print("\n❌ Invalid Option!")
        
        except FileNotFoundError as f:
            print("\n❗",f)

if __name__ == "__main__":
    main()