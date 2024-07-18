import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
 ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)", (name,time))
    conn.commit()
    # cursor.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()
    # cursor.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()
    # cursor.commit()



def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all youtube videos")
        print("2. add a youtube videos")
        print("3. update a youtube videos details")
        print("4. delete a youtube video")
        print("5. Exit the app")
        choice = int(input("Enter a choice: "))

        if choice == 1:
            list_videos()
        elif choice == 2:
            name = input("Enter a movie name: ")
            time = input("Enter movie time: ")
            add_video(name,time)
        elif choice == 3:
            list_videos()
            video_id = input("Enter Video ID to update: ")
            name = input("Enter a movie name: ")
            time = input("Enter movie time: ")
            update_video(video_id,name,time)
        elif choice == 4:
            list_videos()
            video_id = input("Enter Video ID to delete: ")
            delete_video(video_id)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
            break

    conn.close()

if __name__ == '__main__':
    main()


# https://www.youtube.com/watch?v=SWPJwE0TVXw&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=24