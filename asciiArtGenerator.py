from pathlib import Path
from PIL import Image
ascii_chars =  ['#', '@', '%', '&', 'M', 'W', 
                '$', '8', 'B', 'H', 'Q', 'E', 'Z', 'N', 'A', 'V', 'X', 
                'U', '0', 'O', 'C', '7', '1', '3', '2', 'r', 'c', 'x', 'o', 'a', 
                's', 'n', 'u', '!', '-', '~', ';', ':', ',', '"', "'", '.']



def asciiArt(imagePath,outputWidth=100):
    img = Image.open(imagePath).convert('L')
    width,height = img.size
    aspectRatio = height/width
    outputHeight = int(outputWidth*aspectRatio)
    Resizedimg = img.resize((outputWidth,outputHeight))
    pixels = list(Resizedimg.getdata())
    asciiArt = ''
    for i in range(len(pixels)):
        if i % outputWidth == 0:
            asciiArt += '\n'
        asciiArt+= ascii_chars[pixels[i]//len(ascii_chars)]

    return asciiArt
    
def saveAsciiArt(asciiart,filename):
    filename = str(filename).split(".")
    print(filename)
    with open(f'{filename[0]}AsciiArt.txt','w') as f:
        for chunk in asciiart:
            f.write(chunk)

if __name__ == "__main__":
    filename = input("Enter filename with extension\n> ")

    imagePath = Path.cwd()/filename




    ASCIIart = asciiArt(imagePath,outputWidth=300)

    saveAsciiArt(ASCIIart,filename)
    