import multiprocessing
import requests

def downloadFile(url,name):
    print(f"Downloading Started {name}")
    response = requests.get(url)
    open(f"data/file-{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    proc = []
    for i in range(5):
        #downloadFile(url,i) #One by One downloading
        p = multiprocessing.Process(target=downloadFile, args = [url, i])
        p.start()
        proc.append(p)

    for p in proc:
        p.join()