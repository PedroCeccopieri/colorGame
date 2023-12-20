red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (224,150,0)
brown = (74,36,0)
pink = (252,15,192)
purple = (128,0,128)
white = (255,255,255)
black = (0,0,0)

colorList = [red,green,blue,yellow,orange,brown,pink,purple,white,black]

allLanguages = sorted(['portuguese','indonesian','english','japanese','chinese','arabic','hindi','spanish','french'])

def loadLanguages(selectedLanguages):
    global languages, names

    if (True not in selectedLanguages):
        languages = ['english']
    else:
        languages = [allLanguages[i] for i in range(len(allLanguages)) if (selectedLanguages[i])]
    names = []

    for i in languages:
         names.append(getNames(i))

def getNames(language):

    with open(f'colors/{language}.txt', encoding='utf-8') as f:

            if (language == 'arabic'): return [i[::-1].replace('\n', '') for i in f]
            else: return [i.replace('\n', '') for i in f]

def setColors(colors):

    colors = [i if (i != '') else '0' for i in colors]
    
    for i in range(0,len(colors),3):
        colorList[i // 3] = (int(colors[i]),int(colors[i+1]),int(colors[i+2]))