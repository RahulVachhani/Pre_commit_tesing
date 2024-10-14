import requests

# This will fetch the Product information
# def fetch_api_data():
#     try:

#         url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'
#         response = requests.get(url)
#         data = response.json()


#         if data['success'] and 'data' in data:
#             title = data['data']['title']
#             disc = data['data']['description']
#             price = data['data']['price']
#             image = data['data']['images'][0]
#             img = requests.get(image)
#             with open(f'images/{title}.jpg','wb') as f:
#                 f.write(img.content)
#             return title,disc,price
#         else:
#             raise Exception("Not any data")
#     except Exception as e:
#         print(e)


# if __name__ == "__main__":
#     title, disc, price = fetch_api_data()
#     print(f"The Title : {title}\n The Description : {disc}\n The Price : {price}")


# This will fetch the youtube data


def fetch_api_data():
    try:
        url = "https://api.freeapi.app/api/v1/public/youtube/videos"
        response = requests.get(url)
        data = response.json()

        if data["success"] and "data" in data:
            title = data["data"]["data"][4]["items"]["snippet"]["channelTitle"]
            image = data["data"]["data"][4]["items"]["snippet"]["thumbnails"]["high"]["url"]
            img = requests.get(image)
            with open(f"images/{title}.jpg", "wb") as f:
                f.write(img.content)
            return title
        else:
            raise Exception("Not any data")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    title = fetch_api_data()
    print(f"The Title : {title}")
