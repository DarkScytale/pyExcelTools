import xlrd
from xlutils.copy import copy
import xlwt

data = ('aqua', 'black', 'blue', 'blue_gray', 'bright_green', 'brown', 'coral', 'cyan_ega',
    'dark_blue', 'dark_blue_ega', 'dark_green', 'dark_green_ega', 'dark_purple', 'dark_red',
    'dark_red_ega', 'dark_teal', 'dark_yellow', 'gold', 'gray_ega', 'gray25', 'gray40', 'gray50',
    'gray80', 'green', 'ice_blue', 'indigo', 'ivory', 'lavender', 'light_blue', 'light_green',
    'light_orange', 'light_turquoise', 'light_yellow', 'lime', 'magenta_ega', 'ocean_blue',
    'olive_ega', 'olive_green', 'orange', 'pale_blue', 'periwinkle', 'pink', 'plum', 'purple_ega',
    'red', 'rose', 'sea_green', 'silver_ega', 'sky_blue', 'tan', 'teal', 'teal_ega', 'turquoise',
    'violet', 'white', 'yellow',)

wb = xlwt.Workbook()
ws = wb.add_sheet("Colors")

idx = 0
for color in data:
    ws.write(idx, 1, color, xlwt.easyxf("pattern:pattern solid, fore_colour %s"%color))
    idx += 1

wb.save("buildColorFile.xls")