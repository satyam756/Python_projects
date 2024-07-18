# imports 

import json

# load data
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    # finally:
    #     pass


# Helper method
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


# list all videos 
def list_all_videos(videos):
    # for video in videos:
    #     print(f"{video}")
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f" {index}. {video['name']}, Duration: {video['time']} ")
    # print("\n")
    print("*" * 70)

# add a video
def add_video(videos):
    name = input("Enter a video name: ")
    time1 = input("Enter video time: ")
    videos.append({'name': name, 'time': time1})
    save_data_helper(videos)

# update video
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        new_val = input("Enter the new video name: ")
        time = input("Enter the time: ")
        videos[index-1] = {'name': new_val, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected!")
# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter a video number to be deleted"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected!")


# Starting point
def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. add a youtube videos")
        print("3. update a youtube videos details")
        print("4. delete a youtube video")
        print("5. Exit the app")

        choice = int(input("Enter a choice: "))

        if choice == 1:
            list_all_videos(videos)
        elif choice == 2:
            add_video(videos)
        elif choice == 3:
            update_video(videos)
        elif choice == 4:
            delete_video(videos)
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
            break

        # match choice:
        #     case 1:
        #         list_all_videos(videos)
        #     case 2:
        #         add_video(videos)
        #     case 3:
        #         update_video(videos)
        #     case 4:
        #         delete_video(videos)
        #     case 5:
        #         break
        #     case _:
        #         print("invaild choice")
        #         break

# Dunder - Entry point
if __name__ == "__main__":
    main()