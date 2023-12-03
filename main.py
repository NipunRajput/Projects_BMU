import tkinter as tk
from tkinter import ttk, messagebox

class TowerOfHanoiGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tower of Hanoi")

        # Input for number of disks
        self.num_disks_var = tk.IntVar(value=3)
        tk.Label(master, text="Number of Disks:").pack()
        tk.Entry(master, textvariable=self.num_disks_var).pack()

        # Input for number of pegs (towers)
        self.num_pegs_var = tk.IntVar(value=3)
        tk.Label(master, text="Number of Pegs:").pack()
        tk.Entry(master, textvariable=self.num_pegs_var).pack()

        # Setup button
        tk.Button(master, text="Setup Game", command=self.setup_game).pack()

        # Canvas for drawing towers and disks
        self.canvas = tk.Canvas(master, height=300, width=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Dropdown menus for selecting towers
        self.source_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.source_menu = ttk.Combobox(master, textvariable=self.source_var)
        self.destination_menu = ttk.Combobox(master, textvariable=self.destination_var)
        self.source_menu.pack()
        self.destination_menu.pack()

        # Move button
        tk.Button(master, text="Move Disk", command=self.move_disk).pack()

        # Number of moves
        self.moves = 0
        self.moves_label = tk.Label(master, text="Moves: 0")
        self.moves_label.pack()

    def setup_game(self):
        self.num_disks = self.num_disks_var.get()
        self.num_pegs = self.num_pegs_var.get()
        self.towers = [[] for _ in range(self.num_pegs)]
        self.towers[0] = list(reversed(range(1, self.num_disks + 1)))

        self.source_menu['values'] = list(range(self.num_pegs))
        self.destination_menu['values'] = list(range(self.num_pegs))
        self.source_var.set('')
        self.destination_var.set('')

        self.moves = 0
        self.draw_game()

    def draw_game(self, event=None):
        self.canvas.delete("all")
        tower_width = self.canvas.winfo_width() / self.num_pegs
        for i in range(self.num_pegs):
            # Draw tower
            x0 = i * tower_width
            y0 = self.canvas.winfo_height() - 20
            x1 = x0 + tower_width
            y1 = 20
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="gray")

            # Draw disks
            for j, disk in enumerate(self.towers[i]):
                disk_width = disk * 20
                disk_x0 = x0 - disk_width // 2 + 5
                disk_y0 = y0 - (j + 1) * 20
                disk_x1 = x0 + disk_width // 2 + 5
                disk_y1 = y0 - j * 20
                self.canvas.create_rectangle(disk_x0, disk_y0, disk_x1, disk_y1, fill="blue")

        self.moves_label.config(text=f"Moves: {self.moves}")

        # Check for winning condition
        if len(self.towers[-1]) == self.num_disks:
            messagebox.showinfo("You Win!", f"Congratulations! You solved it in {self.moves} moves.")

    def move_disk(self):
        source = int(self.source_var.get())
        destination = int(self.destination_var.get())

        if self.towers[source] and (not self.towers[destination] or self.towers[source][-1] < self.towers[destination][-1]):
            disk = self.towers[source].pop()
            self.towers[destination].append(disk)
            self.moves += 1
            self.draw_game()
        else:
            messagebox.showerror("Invalid Move", "Cannot place a larger disk on a smaller one.")

def main():
    root = tk.Tk()
    root.geometry("600x400")
    TowerOfHanoiGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
