import json
import pandas as pd
import os

def load_data():
    try:
        with open("youtube.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open("youtube.json", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("List of All Videos:")
    print("-------------------")
    if not videos:
        print("❌ No videos found.")
        return
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. Title    : {video['Title']}")
        print(f"   Link     : {video['Link']}")
        print(f"   Duration : {video['Duration']}")
        print("   -------------------")

def add_videos(videos):
    title = input("Enter the Title: ").strip()
    link = input("Enter the Link: ").strip()
    duration = input("Enter the Duration: ").strip()
    videos.append({"Title" : title, "Link" : link, "Duration" : duration})
    print("\n ✅ Video is Successfully added..")
    save_data(videos)

def update_videos(videos):
    if not videos:
        print("\n❌ No videos available to update.")
        return
    try:
        list_all_videos(videos)
        index = int(input("\nEnter the Video Number to update: "))
        if 1 <= index <= len(videos):
            title = input("\nEnter the Title: ").strip()
            link = input("Enter the Link: ").strip()
            duration = input("Enter the Duration: ").strip()
            videos[index-1] = {"Title" : title, "Link" : link, "Duration" : duration}
            print("\n ✅ Updated Successfully!")
            save_data(videos)
        else:
            print("\n❌ Invalid Index!")
    except ValueError:
        print("\n❌ Please enter a valid number!")
        return

def delete_videos(videos):
    if not videos:
        print("\n❌ No videos available to delete.")
        return
    try:
        list_all_videos(videos)
        index = int(input("\nEnter the Video Number to be Deleted: "))
        if 1 <= index <= len(videos):
            del videos[index-1]
            print("\n ✅ Successfully Deleted!")
            save_data(videos)
        else:
            print("\n ❌ Invalid Index!")
    except ValueError:
        print("\n❌ Please enter a valid number!")
        return

def export_data(videos):
    if not videos:
        print("\n❌ No videos to export.")
        return
    filename = "youtube_videos.csv"
    try:
        df = pd.DataFrame.from_dict(videos)
        df.to_csv(filename, index=False)
        print(f"\n✅ Videos successfully exported to '{filename}'")
        os.startfile(filename)
    except Exception as e:
        print(f"\n❌ Error while exporting: {e}")
    

def main():
    videos = load_data()
    print("\n------ YouTube Video Manager ------")
    while True:
        print("\n-----------------------------------------------------------------")
        print("[1] List  [2] Add  [3] Update  [4] Delete  [5] Export  [6] Exit")
        print("Choose the Option ☝️")
        print("-----------------------------------------------------------------")
        choice = input("Enter the Choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                export_data(videos)
            case "6":
                print("\n------------------------------")
                print("| Thank You for visiting Us. |")
                print("------------------------------\n")
                break
            case _:
                print(" ❌ Invalid Choice!")         

if __name__ == "__main__":
    main()