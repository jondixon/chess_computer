from stockfish import Stockfish
from ChessBoard import ChessBoard


sf = Stockfish()
cb = ChessBoard()


while not cb.isGameOver():
    cb.addTextMove(raw_input('Move: '))

    cb.printBoard()

    if cb.isGameOver():
        print "white wins"
        break


    sf.set_position(cb.getAllTextMoves(ChessBoard.AN))
    cb.addTextMove(sf.get_best_move())

    cb.printBoard()




