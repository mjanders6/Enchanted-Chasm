class Player:

    def __init__(self):
        self.status = ''
        self.cell = ()



    def set_players(MASTER_OBSTACLES):
        cell.master_obs = {key: tuple(value) for key, value in MASTER_OBSTACLES.items()}
        for cells in cell.all:
            for key, value in cell.master_obs.items():
                if value == (cells.x, cells.y):
                    cells.is_mine = True
                    cells.status = key
                    if key == 'H':
                        cells.cell_btn_object.configure(text=key)
                        for i in cells.surrounded_cells:
                            i.cell_btn_object.configure(state='normal')

