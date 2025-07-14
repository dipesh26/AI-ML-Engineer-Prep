import sqlite3

con = sqlite3.connect("youtube_video.db")
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            duration TEXT NOT NULL
            )
            ''')

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    print("\n")
    print("List of All Videos:")
    print("-------------------")
    for row in cur.fetchall():
        video_id, title, duration = row
        # print(row)
        print(f"{video_id}. Title    : {title}")
        print(f"   Duration : {duration}")
        print("   -------------------")

def add_videos():
    title = input("Enter the Title: ").strip()
    duration = input("Enter the Duration: ").strip()
    cur.execute("INSERT INTO videos (title, duration) VALUES (?,?)", (title, duration))
    con.commit()
    print("\n ✅ Video added Successfully..")

def update_videos():
    list_all_videos()
    video_id = input("Enter video Number to Update: ")
    new_title = input("Enter the Title: ").strip()
    new_duration = input("Enter the Duration: ").strip()
    cur.execute("UPDATE videos SET title = ?, duration = ? WHERE id = ?",(new_title, new_duration, video_id))
    con.commit()
    print("\n ✅ Updated Successfully!")

def delete_videos():
    list_all_videos()
    video_id = input("Enter video Number to be Deleted: ")
    cur.execute("DELETE FROM videos WHERE id = ?",(video_id))
    con.commit()
    print("\n ✅ Successfully Deleted!")

def main():
    print("\n------ YouTube Video Manager with Database ------")
    while True:
        print("\n----------------------------------------------------")
        print("[1] List  [2] Add  [3] Update  [4] Delete  [5] Exit")
        print("Choose the Option ☝️")
        print("----------------------------------------------------")
        choice = input("Enter the choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_videos()
            case "3":
                update_videos()
            case "4":
                delete_videos()
            case "5":
                print("\n------------------------------")
                print("| Thank You for visiting Us. |")
                print("------------------------------\n")
                break
            case _:
                print("❌ Invalid Choice! ")

    con.close()

if __name__ == "__main__":
    main()