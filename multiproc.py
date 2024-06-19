import requests
from multiprocessing import Process, Pool
import time
from sys import argv

urls = ['https://yandex-images.clstorage.net/d4q7Lh233/081c91_klh/93FFHoeJ6ADcQELrDBv7QRYAnckaqjHAFOl3iSLzoxc05K6gNM8_7-NcazfUVi1dD1Rj8c4WEN8fWT2zUuleZeJ0AVLDyfZcigpVvwQY_kMLXd7YBvA1nQ6rK9A2qq9IPLaUzE26TYGUPxRB_n42WVdWZ-vYUQSzc01jzxO1M3niW2AKr6O8Cd5RL8IGIct3OHyG4gb_PoUWwi_VNcOXN2TAmcZcvGaNlCQPdfVcAH9Sdnj8t2E-ml4FeNIzhyxIz1ppBbSeghfXYi3oIg36bzpXpsUk9B6UOdcs2Sr3khhUzY3Uba9or78LGnPuUyt8TkZW2pN6EJRvIWLzG7kgWsJmWiyQqZEG-n4a-Cw-z0wtaaPfB8M_nQTAOfwj3Js5fseo9EGQZ7yjAgtx21kbeVZ1aOSVegSKRyxI7hGyDkf4V3YRh7OIFM9bKfosEvxlP2224hngCpov1S70KdeVHF3LhP5noU2GvT80YMZ0CFpsYkzVj0oWnHouXfQYpxVU72pdHISPlwjbVRrqJQLscgVFhcA75hSeJ-Ak0THJpDp0yIPHfIp2irkmL2nScxhZdF9T3KNhMrhKHmfSG5c0dMV1XRmMn7wCy10ewwMN-VYkTbnAPu4dsBXFOe0sxaMfe9WB23yIQZmOHDBTw1cHXX9RZMuBThCAYB9vyzGoCWf7aXAzmYurIOtEI-MuM_FnF2qgzSDsLKoMzBrlCue4LWvsvtBAsk6Eij0LQMBhDm5Md3L8t2Qprmc5WsgFgiBL7UNcGbmNoSLzRyTZDhnPQi9Cnc8ryhCuL9sH7RPHiBJUyKrEbpR3sI4dGnTcRCZSQGhUy7FuJa5LKWbsJYcDbPZ7RTi5jLQC2kcv6B8h9EMhXJngP-05nBr0IO0r5Y0aRe2j5U-WWpyLBDFvwn4LQE5RetCFcBeodAJE2yeYMHHDfVsmp7ioPdF5Lfs-FtloJlib3D_qN5su-R32Kfg',
'https://avatars.mds.yandex.net/i?id=e1fb222c3891394a2d2a71bf6ca1efe92249d1e9-12802892-images-thumbs&n=13',
'https://www.sunhome.ru/i/wallpapers/14/loshadi-v4.orig.jpg'
]

def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

def download_image(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '')[:13] + '.jpg'
    with open(filename, 'wb') as f:
        f.write(response.content)
    end_time = time.time()
    print(f"Изображение {filename} скачано за {end_time - start_time} секунд.")

processes = []
start_time = time.time()

if __name__ == '__main__':
    if len(argv) > 1:
        urls = argv[1:]

    for url in urls:
        process = Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()