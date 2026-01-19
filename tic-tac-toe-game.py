# Tic Tac Toe in der Konsole

from typing import List, Optional
import sys

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"
WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Reihen
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Spalten
    (0, 4, 8), (2, 4, 6)              # Diagonalen
]


def print_board(board: List[str]) -> None:
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def print_index_board() -> None:
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(board: List[str]) -> Optional[str]:
    """Gibt X oder O zurück falls ein Gewinner existiert sonst None."""
    for a, b, c in WINNING_COMBOS:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    return all(field != EMPTY for field in board) and check_winner(board) is None


def get_move(board: List[str], player: str) -> int:
    """
    Fragt den Spieler nach einem Zug
    Eingaben: 1-9 für Feld q zum Beenden
    Gibt Index 0-8 zurück
    """
    while True:
        raw = input(f"Spieler {player}, wähle ein Feld (1-9) oder 'q' zum Beenden: ").strip().lower()
        if raw == "q":
            print("Spiel wird beendet.")
            sys.exit(0)
        if not raw.isdigit():
            print("Ungültige Eingabe, bitte eine Zahl eingeben.")
            continue
        move = int(raw) - 1
        if move < 0 or move > 8:
            print("Bitte eine Zahl von 1 bis 9 eingeben.")
        elif board[move] != EMPTY:
            print("Feld ist schon belegt, bitte anderes wählen.")
        else:
            return move


def play_game() -> None:
    board: List[str] = [EMPTY] * 9
    current_player = PLAYER_X

    print("Willkommen bei Tic Tac Toe!")
    print("Felder sind so nummeriert:")
    print_index_board()

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Spieler {winner} hat gewonnen!")
            break

        if is_draw(board):
            print_board(board)
            print("Unentschieden!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


def main() -> None:
    while True:
        play_game()
        again = input("Nochmal spielen? (j/n, q=Beenden): ").strip().lower()
        if again == "q" or again == "n":
            print("Auf Wiedersehen.")
            break
        if again != "j":
            print("Ungültige Eingabe, verwende 'j' oder 'n'.")


if __name__ == "__main__":
    main()