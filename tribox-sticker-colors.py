#!/usr/bin/env python3

from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import LabColor, sRGBColor

# Fetched on 2015-01-20 from store.tribox.com
colors = [
    {'rgb': (255,255,255), 'id': 10,  'name': '010 : White'},
    {'rgb': (255,172,0),   'id': 20,  'name': '020 : Golden Yellow'},
    {'rgb': (255,208,48),  'id': 21,  'name': '021 : Yellow'},
    {'rgb': (255,228,48),  'id': 22,  'name': '022 : Light Yellow'},
    {'rgb': (255,237,151), 'id': 23,  'name': '023 : Cream'},
    {'rgb': (255,248,0),   'id': 25,  'name': '025 : Brimstone Yellow'},
    {'rgb': (155,11,40),   'id': 30,  'name': '030 : Dark Red'},
    {'rgb': (194,23,23),   'id': 31,  'name': '031 : Red'},
    {'rgb': (234,27,27),   'id': 32,  'name': '032 : Light Red'},
    {'rgb': (255,102,0),   'id': 35,  'name': '035 : Pastel Orange'},
    {'rgb': (92,25,117),   'id': 40,  'name': '040 : Violet'},
    {'rgb': (226,63,158),  'id': 41,  'name': '041 : Pink'},
    {'rgb': (213,164,224), 'id': 42,  'name': '042 : Lilac'},
    {'rgb': (100,90,209),  'id': 43,  'name': '043 : Lavender'},
    {'rgb': (255,159,232), 'id': 45,  'name': '045 : Soft Pink'},
    {'rgb': (26,55,114),   'id': 50,  'name': '050 : Dark Blue'},
    {'rgb': (0,91,230),    'id': 52,  'name': '052 : Azure Blue'},
    {'rgb': (31,163,244),  'id': 53,  'name': '053 : Light Blue'},
    {'rgb': (32,183,175),  'id': 54,  'name': '054 : Turquoise'},
    {'rgb': (135,232,204), 'id': 55,  'name': '055 : Mint'},
    {'rgb': (108,189,255), 'id': 56,  'name': '056 : Ice Blue'},
    {'rgb': (0,66,192),    'id': 57,  'name': '057 : Traffic Blue'},
    {'rgb': (26,66,34),    'id': 60,  'name': '060 : Dark Green'},
    {'rgb': (13,130,83),   'id': 61,  'name': '061 : Green'},
    {'rgb': (0,149,58),    'id': 62,  'name': '062 : Light Green'},
    {'rgb': (147,205,61),  'id': 63,  'name': '063 : Lime-Tree Green'},
    {'rgb': (66,201,63),   'id': 64,  'name': '064 : Yellow Green'},
    {'rgb': (13,153,153),  'id': 66,  'name': '066 : Turquoise Blue'},
    {'rgb': (7,70,160),    'id': 67,  'name': '067 : Blue'},
    {'rgb': (10,10,10),    'id': 70,  'name': '070 : Black'},
    {'rgb': (150,152,150), 'id': 71,  'name': '071 : Grey'},
    {'rgb': (229,229,229), 'id': 72,  'name': '072 : Light Grey'},
    {'rgb': (81,81,81),    'id': 73,  'name': '073 : Dark Grey'},
    {'rgb': (186,186,186), 'id': 74,  'name': '074 : Middle Grey'},
    {'rgb': (183,135,78),  'id': 81,  'name': '081 : Light Brown'},
    {'rgb': (58,30,12),    'id': 80,  'name': '080 : Brown'},
    {'rgb': (234,211,173), 'id': 82,  'name': '082 : Beige'},
    {'rgb': (188,89,0),    'id': 83,  'name': '083 : Nut Brown'},
    {'rgb': (44,65,255),   'id': 86,  'name': '086 : Brilliant Blue'},
    {'rgb': (168,168,167), 'id': 90,  'name': '090 : Silver'},
    {'rgb': (191,161,34),  'id': 91,  'name': '091 : Gold'},
    {'rgb': (160,109,36),  'id': 92,  'name': '092 : Copper'},
    {'rgb': (107,12,35),   'id': 312, 'name': '312 : Burgundy'},
    {'rgb': (255,133,0),   'id': 395, 'name': '395 : Pumpkin'},
    {'rgb': (46,15,132),   'id': 404, 'name': '404 : Purple'},
    {'rgb': (0,18,96),     'id': 518, 'name': '518 : Steel Blue'},
    {'rgb': (16,91,62),    'id': 613, 'name': '613 : Forest Green'},
    {'rgb': (255,0,136),   'id': 991, 'name': 'Pink'},
    {'rgb': (255,50,0),    'id': 992, 'name': 'Red'},
    {'rgb': (255,91,0),    'id': 993, 'name': 'Orange'},
    {'rgb': (255,167,0),   'id': 994, 'name': 'Light Orange'},
    {'rgb': (255,255,0),   'id': 995, 'name': 'Yellow'},
    {'rgb': (0,255,30),    'id': 996, 'name': 'Green'},
    {'rgb': (0,106,255),   'id': 997, 'name': 'Blue'}
]


# Converts RGB to Lab and adds to the global dictionary.
def add_lab_field():
    global colors
    for c in colors:
        rgb = sRGBColor(c['rgb'][0], c['rgb'][1], c['rgb'][2], True)
        #print(rgb)
        lab = convert_color(rgb, LabColor)
        #print(lab)
        c['lab'] = lab.get_value_tuple();


# Outputs Delta E between any two colors to the CSV file.
def output_csv():
    f = open('delta-e-cie2000.csv', 'w')

    # header
    line = ','
    for c in colors:
        line += str(c['id']) + ','
    f.write(line + "\n")

    # body
    for c1 in colors:
        line = str(c1['id']) + ','
        lab1 = LabColor(c1['lab'][0], c1['lab'][1], c1['lab'][2])
        for c2 in colors:
            if c1['id'] == c2['id']:
                line += '-1,'
            else:
                lab2 = LabColor(c2['lab'][0], c2['lab'][1], c2['lab'][2])
                line += str(delta_e_cie2000(lab1, lab2)) + ','
        f.write(line + "\n")
    f.close()


# Outputs Delta E between any two colors to the HTML file.
def output_html():
    f = open('delta-e-cie2000.html', 'w')
    f.write('<table>')

    # header
    line = '<thead><tr><th></th>'
    for c in colors:
        rgb = sRGBColor(c['rgb'][0], c['rgb'][1], c['rgb'][2], True)
        line += '<th style="background-color:' + rgb.get_rgb_hex() + ';">' + str(c['id']) + '</th>'
    f.write(line + '</tr></thead>')

    # boody
    f.write('<tbody>')
    for c1 in colors:
        rgb = sRGBColor(c1['rgb'][0], c1['rgb'][1], c1['rgb'][2], True)
        line = '<tr><th style="background-color:' + rgb.get_rgb_hex() + ';">' + str(c1['id']) + '</th>'
        lab1 = LabColor(c1['lab'][0], c1['lab'][1], c1['lab'][2])
        for c2 in colors:
            if c1['id'] == c2['id']:
                line += '<td>--</td>'
            else:
                lab2 = LabColor(c2['lab'][0], c2['lab'][1], c2['lab'][2])
                line += '<td>' + str(round(delta_e_cie2000(lab1, lab2), 2)) + '</td>'
        f.write(line + '</td>')
    f.write('</tbody>')
    f.write('</table>')
    f.close()

if __name__ == '__main__':
    # Converts RGB to Lab and adds to the dictionary.
    add_lab_field()
    # Some output functions.
    output_csv()
    output_html()
