import os
import sys

import pygame
import requests

d = {"ll": '39.815543,52.859885',
     "spn": '0.005,0.005',
     "l": "map"}

server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(server, params=d)

if not response:
    print("Ошибка выполнения запроса:")
    print(server)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
