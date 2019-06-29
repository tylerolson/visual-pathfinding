from grid import Grid
import tkinter as tk

HEIGHT = 600
WIDTH = 800

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
main_grid = Grid(15, canvas, )


decrease_size_button = tk.Button(root, text="Decrease Grid Size", command=main_grid.decrease_size)
increase_size_button = tk.Button(root, text="Increase Grid Size", command=main_grid.increase_size)


def mouse_click(event):
    grid_x = int(event.x / main_grid.size)
    grid_y = int(event.y / main_grid.size)
    print(grid_x, grid_y)
    canvas.itemconfig("grid_sqaure_" + str(grid_x) + "_" + str(grid_y), fill='red')


canvas.bind("<Button-1>", mouse_click)

canvas.pack()
decrease_size_button.pack()
increase_size_button.pack()
root.mainloop()