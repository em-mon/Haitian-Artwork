import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import cv2
import extcolors

from colormap import rgb2hex

# -- Resize Image --
input_name = "haitian_art.jpeg"

#Output size
output_width = 900
img = Image.open(input_name)

wpercent = (output_width / float (img.size[0]))
output_height = int((float(img.size[1])*float(wpercent)))

img = img.resize((output_width, output_height), Image.Resampling.LANCZOS)

#Save resized image
resize_name = 'resize_' + input_name
img.save(resize_name)

#Read image
plt.figure(figsize = (9, 9))
img_url = resize_name
img = plt.imread(img_url)
plt.imshow(img)
plt.axis('off')
plt.show()

# -- Extract Colors --
colors_x = extcolors.extract_from_path(img_url, tolerance = 24, limit = 11)
colors_x
print(colors_x)

# #A function that converts RGB codes into HEX codes
# def rgb_to_hex(input):
#     colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
#     df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
#     df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]

#     #Conversions
#     df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
#                           int(i.split(", ")[1]),
#                           int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
#     df = pd.DataFrame(zip(df_color_up, df_percent), columns = ['c_code','occurence'])
#     return df

# df_color = rgb_to_hex(colors_x)
# df_color

# # -- Visualize Result --
# list_color = list(df_color['c_code'])
# list_precent = [int(i) for i in list(df_color['occurence'])]
# text_c = [c + ' ' + str(round(p*100/sum(list_precent),1)) +'%' for c, p in zip(list_color,
#                                                                                list_precent)]
# #Create donute chart
# fig, ax = plt.subplots(figsize=(90,90),dpi=10)
# wedges, text = ax.pie(list_precent,
#                       labels= text_c,
#                       labeldistance= 1.05,
#                       colors = list_color,
#                       textprops={'fontsize': 120, 'color':'black'}
#                      )
# plt.setp(wedges, width=0.3)
# plt.setp(wedges, width=0.36)

# ax.set_aspect("equal")
# fig.set_facecolor('white')
# plt.show()

# # -- Make Color Palette --
# #Create background color
# fig, ax = plt.subplots(figsize=(192,108),dpi=10)
# fig.set_facecolor('white')
# plt.savefig('bg.png')
# plt.close(fig)

# #Create color palette
# bg = plt.imread('bg.png')
# fig = plt.figure(figsize=(90, 90), dpi = 10)
# ax = fig.add_subplot(1,1,1)

# x_posi, y_posi, y_posi2 = 320, 25, 25
# for c in list_color:
#     if  list_color.index(c) <= 5:
#         y_posi += 125
#         rect = patches.Rectangle((x_posi, y_posi), 290, 115, facecolor = c)
#         ax.add_patch(rect)
#         ax.text(x = x_posi+360, y = y_posi+80, s = c, fontdict={'fontsize': 150})
#     else:
#         y_posi2 += 125
#         rect = patches.Rectangle((x_posi + 800, y_posi2), 290, 115, facecolor = c)
#         ax.add_artist(rect)
#         ax.text(x = x_posi+1160, y = y_posi2+80, s = c, fontdict={'fontsize': 150})
        
# ax.axis('off')
# plt.imshow(bg)
# plt.tight_layout()

# img = mpimg.imread('<photo location/name>')
# bg = plt.imread('bg.png')

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(160,120), dpi = 10)

# #donut plot
# wedges, text = ax1.pie(list_precent,
#                       labels= text_c,
#                       labeldistance= 1.05,
#                       colors = list_color,
#                       textprops={'fontsize': 160, 'color':'black'})
# plt.setp(wedges, width=0.3)

# #add image in the center of donut plot
# imagebox = OffsetImage(img, zoom=2.3)
# ab = AnnotationBbox(imagebox, (0, 0))
# ax1.add_artist(ab)

# #color palette
# x_posi, y_posi, y_posi2 = 160, -170, -170
# for c in list_color:
#     if list_color.index(c) <= 5:
#         y_posi += 180
#         rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor = c)
#         ax2.add_patch(rect)
#         ax2.text(x = x_posi+400, y = y_posi+100, s = c, fontdict={'fontsize': 190})
#     else:
#         y_posi2 += 180
#         rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor = c)
#         ax2.add_artist(rect)
#         ax2.text(x = x_posi+1400, y = y_posi2+100, s = c, fontdict={'fontsize': 190})

# ax2.axis('off')
# fig.set_facecolor('white')
# plt.imshow(bg)       
# plt.tight_layout()

# def exact_color(input_image, resize, tolerance, zoom):
#     #background
#     bg = 'bg.png'
#     fig, ax = plt.subplots(figsize=(192,108),dpi=10)
#     fig.set_facecolor('white')
#     plt.savefig(bg)
#     plt.close(fig)
    
#     #resize
#     output_width = resize
#     img = Image.open(input_image)
#     if img.size[0] >= resize:
#         wpercent = (output_width/float(img.size[0]))
#         hsize = int((float(img.size[1])*float(wpercent)))
#         img = img.resize((output_width,hsize), Image.ANTIALIAS)
#         resize_name = 'resize_'+ input_image
#         img.save(resize_name)
#     else:
#         resize_name = input_image
    
#     #crate dataframe
#     img_url = resize_name
#     colors_x = extcolors.extract_from_path(img_url, tolerance = tolerance, limit = 13)
#     df_color = rgb_to_hex(colors_x)
    
#     #annotate text
#     list_color = list(df_color['c_code'])
#     list_precent = [int(i) for i in list(df_color['occurence'])]
#     text_c = [c + ' ' + str(round(p*100/sum(list_precent),1)) +'%' for c, p in zip(list_color, list_precent)]
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(160,120), dpi = 10)
    
#     #donut plot
#     wedges, text = ax1.pie(list_precent,
#                            labels= text_c,
#                            labeldistance= 1.05,
#                            colors = list_color,
#                            textprops={'fontsize': 150, 'color':'black'})
#     plt.setp(wedges, width=0.3)

#     #add image in the center of donut plot
#     img = mpimg.imread(resize_name)
#     imagebox = OffsetImage(img, zoom=zoom)
#     ab = AnnotationBbox(imagebox, (0, 0))
#     ax1.add_artist(ab)
    
#     #color palette
#     x_posi, y_posi, y_posi2 = 160, -170, -170
#     for c in list_color:
#         if list_color.index(c) <= 5:
#             y_posi += 180
#             rect = patches.Rectangle((x_posi, y_posi), 360, 160, facecolor = c)
#             ax2.add_patch(rect)
#             ax2.text(x = x_posi+400, y = y_posi+100, s = c, fontdict={'fontsize': 190})
#         else:
#             y_posi2 += 180
#             rect = patches.Rectangle((x_posi + 1000, y_posi2), 360, 160, facecolor = c)
#             ax2.add_artist(rect)
#             ax2.text(x = x_posi+1400, y = y_posi2+100, s = c, fontdict={'fontsize': 190})

#     fig.set_facecolor('white')
#     ax2.axis('off')
#     bg = plt.imread('bg.png')
#     plt.imshow(bg)       
#     plt.tight_layout()
#     return plt.show()
