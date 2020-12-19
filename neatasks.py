#name: jaanki rajababoo
#project: NEA Pre-Release Material - Tiles

#initialising and declaring 1D arrays
Tile_List=['Small Black Granite','Small Grey Marble','Small Powder Blue',
           'Medium Sunset Yellow','Medium Berry Red','Medium Glitter Purple',
           'Large Oak Wood Effect','Large Black Granite','Large Bamboo Effect',
           'Extra-Large White Marble']

PricePerBox=[     19.50,     25.95,     25.75,     12.50,
                  11.00,    52.95,    65.00,     58.98,     85.00,
              62.75]

IdentificationCode=[    0,    1,    2,    3,    4,   5,   6,    7,    8,9]
#setting out the format of what the code will look like when displayed
def Task1():
    print('tiles are sold in boxes, each box covers one square metre')
    Tile_Length = len(Tile_List)
    #this line is the format for the table and the line below it is used to make the table look presentable
    print('{0:30} {1:20} {2:20}'.format('Tile Description','Price per box','Identification Code'))
    print('{0:30} {1:20} {2:20}'.format('----------------','---------------','-------------------'))
    #this uses a for loop and it repeats the code below for the length of the tiles
    for index in range(Tile_Length):
        Idcode=IdentificationCode[index]
        TileDescription=Tile_List[index]
        Priceperbox=PricePerBox[index]
        print('{0:30} {1:^20} {2:^20}'.format(TileDescription,Priceperbox,Idcode))
        
    #asking the user to input the id code, the height and width for their wall
    Idcode = input('Enter the Identification Code:')
    Height = input('Enter the height of your wall:')
    Width = input('Enter the width of your wall:')
    #converting the string into an integer/s 
    Height = int(Height)
    Width = int(Width)
    Idcode = int(Idcode)
    
    #working out the area from the height and width given
    Area = Height*Width
    print('The area of your wall is',Area,'m')

    print('you need',Area,'number of boxes')
    TotalBox = Area*1

    TotalPrice = TotalBox*PricePerBox[Idcode]
    print('the total cost is $',TotalPrice)    
#working out area, how many boxes are needed and the total price
    return
#Task1()

def Task2():
    print('tiles are sold in boxes, each box covers one square metre')
    Tile_Length = len(Tile_List)
    
    #this line is the format for the table and the line below it is used to make the table look presentable
    print('{0:30} {1:20} {2:20}'.format('Tile Description','Price per box','Identification Code'))
    print('{0:30} {1:20} {2:20}'.format('----------------','---------------','-------------------'))
    for index in range(Tile_Length):
        Idcode=IdentificationCode[index]
        TileDescription=Tile_List[index]
        Priceperbox=PricePerBox[index]
        print('{0:30} {1:^20} {2:^20}'.format(TileDescription,Priceperbox,Idcode))

    Idcode = input('Enter the Identification Code:')
    Idcode = int(Idcode)

    TotalWalls = input('enter the total number of walls:')
    TotalWalls = int(TotalWalls)
    
    TotalArea = 0
    for count in range(TotalWalls):
        Height = input('Enter the height of your wall:')
        Width = input('Enter the width of your wall:')
        Height = int(Height)
        Width = int(Width)
        Area = Height*Width
        TotalArea = TotalArea + Area

    
    print('The area of your wall is',TotalArea,'m')

    print('you need',TotalArea,'number of boxes')
    
    #task3
    TotalBox = TotalArea
    WastedTiles = input('Input a percentage for wastage:')
    WastedTiles = int(WastedTiles)
    Wastage = WastedTiles * (WastedTiles / 100)
    TotalBox = TotalBox + Wastage

    Whole = TotalBox // 1
    Remainder = TotalBox%1
    #showing that if the remainder is not equal to 0, to add 1 on to make it a whole number
    if Remainder !=0:
        TotalBox = Whole + 1
        
    #
    TotalPrice = TotalBox*PricePerBox[Idcode]
    print('The area of your wall is',TotalBox,'m')
    print('The amount to boxes you have to buy including wastage is',TotalBox)
    print('the total cost is $',TotalPrice)
    print('the total cost is $',TotalPrice)

    return
Task2()

