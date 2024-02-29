import requests
from bs4 import BeautifulSoup

def search_images(keyword, num_images):
    url = f'https://www.google.com/search?q={keyword}&tbm=isch'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    images = soup.find_all('img', limit=num_images)
    image_urls = [img['src'] for img in images]
    return image_urls

def send_images(images):
    for index, image_url in enumerate(images):
        # Отправляем изображение пользователю
        print(f"Изображение {index+1}: {image_url}")

keyword = input("Введите ключевую фразу для поиска изображений: ")
num_images = int(input("Введите количество изображений, которое хотите получить: "))

images = search_images(keyword, num_images)
send_images(images)