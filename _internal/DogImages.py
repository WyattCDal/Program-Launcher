#DogImages.py displays a random image of a dog everytime the user clicks.
#Version: 1
#██████╗░░█████╗░░██████╗░██╗███╗░░░███╗░█████╗░░██████╗░███████╗░██████╗░░░██████╗░██╗░░░██╗
#██╔══██╗██╔══██╗██╔════╝░██║████╗░████║██╔══██╗██╔════╝░██╔════╝██╔════╝░░░██╔══██╗╚██╗░██╔╝
#██║░░██║██║░░██║██║░░██╗░██║██╔████╔██║███████║██║░░██╗░█████╗░░╚█████╗░░░░██████╔╝░╚████╔╝░
#██║░░██║██║░░██║██║░░╚██╗██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░░╚═══██╗░░░██╔═══╝░░░╚██╔╝░░
#██████╔╝╚█████╔╝╚██████╔╝██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗██████╔╝██╗██║░░░░░░░░██║░░░
#╚═════╝░░╚════╝░░╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
#█▄▄ █▄█ ▀   █░█░█ █▄█ ▄▀█ ▀█▀ ▀█▀   █▀▄ ▄▀█ █░░
#█▄█ ░█░ ▄   ▀▄▀▄▀ ░█░ █▀█ ░█░ ░█░   █▄▀ █▀█ █▄▄ 

from requests import*
from graphics import*

def fetchAndSave():

    from PIL import Image
    from io import BytesIO
    
    url= "https://dog.ceo/api/breeds/image/random"
    response= get(url)
    data= response.json()

    image_url = data["message"]

    image_response = get(image_url)
    image = Image.open(BytesIO(image_response.content))

    image.save("dog_image.gif")

def main():
    
    win = GraphWin("Dog Pictures", 800, 500)
    win.setCoords(0,0,200,200)

    background = Image(Point(100,100), "background.gif").draw(win)

    image = Point(100,100)

    for i in range(50):
        
        win.getMouse()
        
        image.undraw()
        fetchAndSave()
        image = Image(Point(100,100), "dog_image.gif").draw(win)

main()
