from stockfish import Stockfish
from ChessBoard import ChessBoard
from LEDController import LEDController

sf = Stockfish()
cb = ChessBoard()
led = LEDController()


while not cb.isGameOver():

    cb.printBoard()
    #led.printLEDs()

    move = input('Move: ')
    cb.addTextMove(move)
    #led.addTextMove(move)

    cb.printBoard()
    #led.printLEDs()

    if cb.isGameOver():
        print( "white wins")
        break


    sf.set_position(cb.getAllTextMoves(ChessBoard.AN))
    cb.addTextMove(sf.get_best_move())

    cb.printBoard()




