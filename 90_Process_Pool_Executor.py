import concurrent.futures
import requests

def downloadFile(url,name):
    print(f"Downloading Started {name}")
    response = requests.get(url)
    open(f"data/pic-{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")


url = "https://picsum.photos/2000/3000"
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(50)]
    l2 = [i for i in range(50)]
    result = executor.map(downloadFile, url, l1,l2)
    for r in result:
        print(r)
