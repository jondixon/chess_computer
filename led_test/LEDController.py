
def AR2STRIP(row,col):
    if row % 2 == 0:
        return row*8+col
    else:
        return row*8+7-col


class LEDController:


    leds = []

    def __init__(self):
        self.resetLEDs()


    def resetLEDs(self):
        for i in range(0,64):
            self.leds.append(' ')

    def printLEDs(self):
        print('  +-----------------+')
        for i in range(7,-1,-1):
            print(str(i+1) + ' | ', end='')

            for j in range(0,8):
                print(self.leds[AR2STRIP(i,j)] + ' ',end='')
            print('|')
        print('  +-----------------+')
        print('    A B C D E F G H')
    
    #def addTestMove(self, move):
        



