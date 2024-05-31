import os

class Game():
    def __init__(self,player_1_name:str="player1",player_2_name:str="player2") -> None:
        self.table=self.init_table()
        self.player_1_name=player_1_name if player_1_name!="" else "player1"
        self.player_2_name=player_2_name if player_2_name!="" else "player2"
        self.player_1="X"
        self.player_2="O"
        self.win_player_1=False
        self.win_player_2=False

    @staticmethod
    def init_table():
        return {
            "1": {"1": " ", "2": " ", "3": " "},
            "2": {"1": " ", "2": " ", "3": " "},
            "3": {"1": " ", "2": " ", "3": " "}
        }

    def add_move(self,row:int,column:int,player:int):
        if self.table[str(row)][str(column)]==" ":
            printable=self.player_1 if player==1 else self.player_2
            self.table[str(row)][str(column)]=printable
            return True
        else: return False

    def print_table(self):
        line_moves=[]
        line_move=""
        for row in self.table.values():
            for column in row.values():
                line_move+=f"|   {column}   "
            line_moves.append(f"{line_move}|")
            line_move=""
        line ="".join("|\t" for _ in range(4))
        line_divition=" ".join("_" if _%4!=0 else "+" for _ in range(13))
        line_movies_int=0
        line_moves_count=0
        for _ in range(1,10):
            line_moves_count+=1
            if line_moves_count==2:
                print(line_moves[line_movies_int])
                line_movies_int+=1
            else:
                print(line)
            if _%3==0 and _!=9:
                print(line_divition)
                line_moves_count=0



def wellcome():
    print("Bienvenido al juego del gato")

def start_game():
    return Game(input("Ingresa el nombre del jugador 1: "),input("Ingresa el nombre del jugador 1: "))



if __name__=="__main__":
    wellcome()
    game=Game(player_1_name="Anais",player_2_name="Ivanna")
    game.add_move(1,2,1)
    game.print_table()

