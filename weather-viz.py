# import math
import sys
import csv
import math
import numpy as np
import matplotlib.pyplot as plt  # pip3 install matplotlib
import matplotlib.markers as markers
from matplotlib.lines import Line2D

# --------------------------------------------------------------------------------
# INPUT
# --------------------------------------------------------------------------------
def read_csv(path):
    try:
        with open(path, "r", newline='') as f:
            reader = csv.DictReader(f, fieldnames=['month', 'px1'], delimiter=',')
            data = [{'month':round(float(row['month'])), 'px1':float(row['px1'])} for row in reader]
            return data
    except OSError as e:
        print('[*] OSError:', e)
        raise

def build_path(region, area):
    if type(region) is not str or type(area) is not str:
        print('[*] ERROR: Region & Area must be a string.')
        raise
    elif not region.isalpha():
        print('[*] ERROR: Region must be an alphabet.')
        raise

    filename = "-".join([region.lower(), area.lower()])
    extension = "csv"
    filenameWithExtension = ".".join([filename, extension])
    filepath = "/".join([".", "dataset", filenameWithExtension])
    assert filepath.startswith("./dataset")
    return filepath

# --------------------------------------------------------------------------------
# HELPERS: GET MONTH / PX1 VALUES FROM INPUT
# --------------------------------------------------------------------------------
def get_month(data):
    month_dict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return [month_dict[dictionary['month']] for dictionary in data]

def get_px1(data):
    return [dictionary['px1'] for dictionary in data]

# --------------------------------------------------------------------------------
# HELPERS: CALC DIFF BTW TWO LISTS
# --------------------------------------------------------------------------------
def calc_px1_diff(px1_list_subtrahend, px1_list_minuend):
    if type(px1_list_subtrahend) is not list or type(px1_list_minuend) is not list:
        print('[*] ERROR: The two parameters must be in list type.')
        raise
    elif len(px1_list_subtrahend) != len(px1_list_minuend):
        print('[*] ERROR: The two lists must have the same length.')
        raise
    return [px1_list_subtrahend[idx] - px1_list_minuend[idx] for idx in range(len(px1_list_subtrahend))]

# --------------------------------------------------------------------------------
# HELPERS: CALC POINT VOLUME BASED ON DIFF
# --------------------------------------------------------------------------------
def calc_px1_point_volume_based_on(px1_list_diff):
    if type(px1_list_diff) is not list:
        print('[*] ERROR: The parameter must be in list type.')
        raise
    return [(diff*20)**2 for diff in px1_list_diff] # handle negative number via power of 2

def compute_px1_shape_volume_based_on(px1_list_diff):
    if type(px1_list_diff) is not list:
        print('[*] ERROR: The parameter must be in list type.')
        raise
    return ["o" if diff >= 0 else "_" for diff in px1_list_diff]
    
# --------------------------------------------------------------------------------
# VISUALIZING
# --------------------------------------------------------------------------------
def add_single_scatter_point(ax, x, y, volume, color, marker, alpha=0.5):
    diff = math.sqrt(volume)/15 # used for highlighting diff >= 1.0 during experiments before.
    if color == "#ffcc55" and x in ["Aug", "Sep", "Oct", "Nov"]:
        ax.scatter([x], [y], s=[volume], c=color, marker=marker, alpha=alpha, edgecolors='red', linewidths=6)
    elif color == "#ff7f0e" and x in ["Aug"]:
        ax.scatter([x], [y], s=[volume], c=color, marker=marker, alpha=alpha, edgecolors='red', linewidths=6)
    else:
        ax.scatter([x], [y], s=[volume], c=color, marker=marker, alpha=alpha)
    pass

# --------------------------------------------------------------------------------
# OUTPUT (WRITE IMAGE)
# --------------------------------------------------------------------------------
    
# --------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # (A) read csv
    data_RegionA_AreaRural = read_csv(build_path('a', 'rural'))
    data_RegionA_AreaUrban = read_csv(build_path('a', 'urban'))
    data_RegionB_AreaRural = read_csv(build_path('b', 'rural'))
    data_RegionB_AreaUrban = read_csv(build_path('b', 'urban'))
    data_RegionC_AreaRural = read_csv(build_path('c', 'rural'))
    data_RegionC_AreaUrban = read_csv(build_path('c', 'urban'))
    data_RegionD_AreaRural = read_csv(build_path('d', 'rural'))
    data_RegionD_AreaUrban = read_csv(build_path('d', 'urban'))

    # (B1) retrieve month values
    month_RegionA_AreaRural = get_month(data_RegionA_AreaRural)
    month_RegionA_AreaUrban = get_month(data_RegionA_AreaUrban)
    month_RegionB_AreaRural = get_month(data_RegionB_AreaRural)
    month_RegionB_AreaUrban = get_month(data_RegionB_AreaUrban)
    month_RegionC_AreaRural = get_month(data_RegionC_AreaRural)
    month_RegionC_AreaUrban = get_month(data_RegionC_AreaUrban)
    month_RegionD_AreaRural = get_month(data_RegionD_AreaRural)
    month_RegionD_AreaUrban = get_month(data_RegionD_AreaUrban)

    # (B2) retrieve px1 values
    px1_RegionA_AreaRural = get_px1(data_RegionA_AreaRural)
    px1_RegionA_AreaUrban = get_px1(data_RegionA_AreaUrban)
    px1_RegionB_AreaRural = get_px1(data_RegionB_AreaRural)
    px1_RegionB_AreaUrban = get_px1(data_RegionB_AreaUrban)
    px1_RegionC_AreaRural = get_px1(data_RegionC_AreaRural)
    px1_RegionC_AreaUrban = get_px1(data_RegionC_AreaUrban)
    px1_RegionD_AreaRural = get_px1(data_RegionD_AreaRural)
    px1_RegionD_AreaUrban = get_px1(data_RegionD_AreaUrban)

    # (C) calculate rural & urban differences
    px1_RegionA_AreaUrbanRuralDiff = calc_px1_diff(px1_RegionA_AreaUrban, px1_RegionA_AreaRural)
    px1_RegionB_AreaUrbanRuralDiff = calc_px1_diff(px1_RegionB_AreaUrban, px1_RegionB_AreaRural)
    px1_RegionC_AreaUrbanRuralDiff = calc_px1_diff(px1_RegionC_AreaUrban, px1_RegionC_AreaRural)
    px1_RegionD_AreaUrbanRuralDiff = calc_px1_diff(px1_RegionD_AreaUrban, px1_RegionD_AreaRural)

    # (D1) compute volume 
    px1_RegionA_Volume = calc_px1_point_volume_based_on(px1_RegionA_AreaUrbanRuralDiff)
    px1_RegionB_Volume = calc_px1_point_volume_based_on(px1_RegionB_AreaUrbanRuralDiff)
    px1_RegionC_Volume = calc_px1_point_volume_based_on(px1_RegionC_AreaUrbanRuralDiff)
    px1_RegionD_Volume = calc_px1_point_volume_based_on(px1_RegionD_AreaUrbanRuralDiff)

    # (D2) compute shape based on the diff 
    px1_RegionA_Shape = compute_px1_shape_volume_based_on(px1_RegionA_AreaUrbanRuralDiff)
    px1_RegionB_Shape = compute_px1_shape_volume_based_on(px1_RegionB_AreaUrbanRuralDiff)
    px1_RegionC_Shape = compute_px1_shape_volume_based_on(px1_RegionC_AreaUrbanRuralDiff)
    px1_RegionD_Shape = compute_px1_shape_volume_based_on(px1_RegionD_AreaUrbanRuralDiff)

    # (D3) colors
    regionA_Color = "#ffcc55"
    regionB_Color = "#ff7f0e"
    regionC_Color = "#2ca02c"
    regionD_Color = "#1f77b4"

    # (E1) setup
    fig, ax = plt.subplots(1, 1, figsize=(10,10))
    # ax.set_facecolor('#eeeeee')

    # (E2) draw scatter plot
    [add_single_scatter_point(ax, x=month_RegionA_AreaUrban[idx], y=px1_RegionA_AreaUrban[idx], volume=px1_RegionA_Volume[idx], color=regionA_Color, marker=px1_RegionA_Shape[idx]) for idx in range(len(month_RegionA_AreaUrban))]
    [add_single_scatter_point(ax, x=month_RegionB_AreaUrban[idx], y=px1_RegionB_AreaUrban[idx], volume=px1_RegionB_Volume[idx], color=regionB_Color, marker=px1_RegionB_Shape[idx]) for idx in range(len(month_RegionB_AreaUrban))]
    [add_single_scatter_point(ax, x=month_RegionC_AreaUrban[idx], y=px1_RegionC_AreaUrban[idx], volume=px1_RegionC_Volume[idx], color=regionC_Color, marker=px1_RegionC_Shape[idx]) for idx in range(len(month_RegionC_AreaUrban))]
    [add_single_scatter_point(ax, x=month_RegionD_AreaUrban[idx], y=px1_RegionD_AreaUrban[idx], volume=px1_RegionD_Volume[idx], color=regionD_Color, marker=px1_RegionD_Shape[idx]) for idx in range(len(month_RegionD_AreaUrban))]
    

    # (E3) Rectangle Boxes / Blur


    # (E4) Legends, Axis, & Titles
    legend_elements  = [
        Line2D(range(1), range(1), color='white', markerfacecolor=regionA_Color, markersize=10, marker='o', alpha=0.5, label="Region A"),
        Line2D(range(1), range(1), color='white', markerfacecolor=regionB_Color, markersize=10, marker='o', alpha=0.5, label="Region B"),
        Line2D(range(1), range(1), color='white', markerfacecolor=regionC_Color, markersize=10, marker='o', alpha=0.5, label="Region C"),
        Line2D(range(1), range(1), color='white', markerfacecolor=regionD_Color, markersize=10, marker='o', alpha=0.5, label="Region D"),
        Line2D(range(1), range(1), color='white', markerfacecolor='gray', markersize=10, marker='o', alpha=0.5, label="Px1 in Urban > Px1 in Rural"),
        Line2D(range(1), range(1), color='gray', linewidth=0.1, markerfacecolor='gray', markersize=10, marker='_', alpha=0.5, label="Px1 in Urban < Px1 in Rural"),
        Line2D(range(1), range(1), color='white', markerfacecolor='gray', markersize=5, marker='o', alpha=0.5, label="Small Urban-Rural Diff."),
        Line2D(range(1), range(1), color='white', markerfacecolor='gray', markersize=15, marker='o', alpha=0.5, label="Large Urban-Rural Diff."),
    ]

    ax.legend(handles=legend_elements, loc='lower right')
    plt.title("Px1 Value in Urban Area Among Four Regions")
    plt.xlabel("Month")
    plt.ylabel("Px1 Value in Urban Area")

    # (E5) Show!
    plt.show()