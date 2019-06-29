import time


class Grid:
    def __init__(self, scale, size, root, canvas, canvas_width, canvas_height):
        self.scale = scale
        self.size = size
        self.root = root
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.flood_speed = 0
        self.clear_array()

    def increase_scale(self):
        self.scale += 5
        self.draw()

    def decrease_scale(self):
        if self.scale > 10:
            self.scale -= 5
            self.draw()

    def change_color(self, x, y, color):
        self.array[x, y] = color
        self.draw()

    def clear_array(self):
        self.array = {(i, j): "white" for i in range(self.size) for j in range(self.size)}
        self.draw()

    def flood(self, x, y, target, replacement):
        if x < 0 or x == self.size or y < 0 or y == self.size:
            return
        if self.array[x, y] == replacement:
            return
        elif self.array[x, y] != target:
            return
        else:
            self.change_color(x, y, replacement)

        self.root.update_idletasks()

        self.flood(x - 1, y, target, replacement)
        self.flood(x + 1, y, target, replacement)
        self.flood(x, y - 1, target, replacement)
        self.flood(x, y + 1, target, replacement)
        return

    def draw(self):
        self.canvas.delete("all")
        grid_width = round(self.canvas_width / self.scale)
        grid_height = round(self.canvas_height / self.scale)
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(self.scale * i + 1, self.scale * j + 1, self.scale * (i + 1) + 1, self.scale * (j + 1) + 1, tags="grid_sqaure_" + str(i) + "_" + str(j), fill=self.array[i, j])
