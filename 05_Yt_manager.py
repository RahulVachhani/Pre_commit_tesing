import json


def loader():
    with open("a.txt", "r") as file:
        data = json.load(file)
        return data


def show_all_video(videos):
    for i, j in enumerate(videos, start=1):
        print(f"{i}. {j}")


def add_video(videos):
    name = input("Enter the video name : ")
    time = input("Enter the duartion of video : ")
    videos.append({"name": name, "time": time})
    with open("a.txt", "w") as file:
        json.dump(videos, file)


def update_video(videos):
    show_all_video(videos)
    index = int(input("Enter the number you want no update : "))
    data = videos.pop(index - 1)
    print(data)
    data["name"] = input("Enter the updated name : ")
    data["time"] = input("Enter the updated time : ")
    videos.insert(index - 1, data)
    with open("a.txt", "w") as file:
        json.dump(videos, file)


videos = loader()

# add_video(videos)

update_video(videos)
show_all_video(videos)
