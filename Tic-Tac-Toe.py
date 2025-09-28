import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("520x700")  # was 430x570
        self.root.resizable(False, False)
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.dark_mode = False
        self.leaderboard = {"X": 0, "O": 0, "Draws": 0}
        self.create_widgets()
        self.set_dark_mode()  # Or self.set_light_mode() for light mode by default

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=("Arial Rounded MT Bold", 32, "bold"))
        self.title_label.pack(pady=(18, 0))

        # Frame for the board
        self.board_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.board_frame.pack(pady=25)

        # Game buttons
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text=" ",
                    font=("Arial", 28, "bold"),
                    width=4,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c),
                    bd=0,
                    relief="ridge",
                    bg="#fff"
                )
                btn.grid(row=row, column=col, padx=4, pady=4)
                self.buttons[row][col] = btn

        # Status label
        self.status_label = tk.Label(self.root, text=f"Player X's turn", font=("Arial", 18, "bold"))
        self.status_label.pack(pady=(10, 0))

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=25)

        # Dark mode button
        self.toggle_btn = tk.Button(self.button_frame, text="Enable Dark Mode", command=self.toggle_mode, font=("Arial", 13, "bold"), width=16)
        self.toggle_btn.grid(row=0, column=0, padx=8)

        # Leaderboard button
        self.leaderboard_btn = tk.Button(self.button_frame, text="Show Leaderboard", command=self.show_leaderboard, font=("Arial", 13, "bold"), width=14)
        self.leaderboard_btn.grid(row=0, column=1, padx=8)

        # Reset button
        self.reset_btn = tk.Button(self.button_frame, text="Reset Game", command=self.reset_board, font=("Arial", 13, "bold"), width=12)
        self.reset_btn.grid(row=0, column=2, padx=8)

        # Footer
        self.footer = tk.Label(self.root, text="Enjoy your game!", font=("Arial", 12), fg="#888")
        self.footer.pack(side="bottom", pady=10)

    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if check_winner(self.board, self.current_player):
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.leaderboard[self.current_player] += 1
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif is_full(self.board):
                self.status_label.config(text="It's a draw!")
                self.leaderboard["Draws"] += 1
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(
                    text=f"Player {self.current_player}'s turn"
                )

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")

    def toggle_mode(self):
        if self.dark_mode:
            self.set_light_mode()
        else:
            self.set_dark_mode()

    def set_dark_mode(self):
        self.dark_mode = True
        bg = "#181818"
        fg = "#fff"
        btn_bg = "#232323"
        btn_fg = "#fff"
        active_bg = "#333"
        board_bg = "#222"
        self.root.configure(bg=bg)
        self.title_label.config(bg=bg, fg="#00eaff")
        self.status_label.config(bg=bg, fg="#00eaff")
        self.button_frame.config(bg=bg)
        self.footer.config(bg=bg, fg="#aaa")
        self.toggle_btn.config(text="Enable White Mode", bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.leaderboard_btn.config(bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.reset_btn.config(bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.board_frame.config(bg=board_bg)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(bg=btn_bg, fg=btn_fg, activebackground=active_bg, activeforeground=fg)

    def set_light_mode(self):
        self.dark_mode = False
        bg = "#f0f0f0"
        fg = "#222"
        btn_bg = "#fff"
        btn_fg = "#222"
        active_bg = "#e0e0e0"
        board_bg = "#f0f0f0"
        self.root.configure(bg=bg)
        self.title_label.config(bg=bg, fg="#1e90ff")
        self.status_label.config(bg=bg, fg="#1e90ff")
        self.button_frame.config(bg=bg)
        self.footer.config(bg=bg, fg="#888")
        self.toggle_btn.config(text="Enable Dark Mode", bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.leaderboard_btn.config(bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.reset_btn.config(bg=btn_bg, fg=btn_fg, activebackground=active_bg)
        self.board_frame.config(bg=board_bg)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(bg=btn_bg, fg=btn_fg, activebackground=active_bg, activeforeground=fg)

    def show_leaderboard(self):
        leaderboard_text = (
            f"Leaderboard:\n\n"
            f"Player X Wins: {self.leaderboard['X']}\n"
            f"Player O Wins: {self.leaderboard['O']}\n"
            f"Draws: {self.leaderboard['Draws']}"
        )
        messagebox.showinfo("Leaderboard", leaderboard_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()