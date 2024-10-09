# This is program for download the images from the url and create the new file in given directory or folder

import requests
import multiprocessing


def downloadFile(url, name):
    print(f"The image {name} downloading :")

    response = requests.get(url)
    open(f"images/{name}.jpg", "wb").write(response.content)

    print(f"The image {name} download complates :")


url = "https://picsum.photos/900/1200"

pro = []
for i in range(5):
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pro.append(p)

for i in pro:
    i.join()
