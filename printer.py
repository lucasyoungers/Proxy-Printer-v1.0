#!/usr/local/bin/python3

"""
This program is designed to print proxies of custom Pokémon cards. To use, place the image files, either png or jpg, in the folder, then run the file using python3 with PIL and fpdf installed via pip3.
"""

import os
import pathlib
from math import ceil
from time import time
from PIL import Image
from fpdf import FPDF

def my_round(x, base=10):
  return base * ceil(x / base)

def get_files():
  path = pathlib.Path().resolve()
  files = os.listdir(path)
  files = [f"{path}/{file}" for file in files if file[-4:] in (".png", ".jpg")]
  return files

def print_files(files):
  pdf = FPDF(orientation="P", unit="in", format="Letter")

  for i in range(0, len(files)):
    if i % 9 == 0:
      pdf.add_page()
    x = 0.53 + 2.49 * (i % 3)
    if (i + 1) % 9 in (1, 2, 3):
      y = 0.3
    elif (i + 1) % 9 in (4, 5, 6):
      y = 0.3 + 3.47
    elif (i + 1) % 9 in (7, 8, 9):
      y = 0.3 + 3.47 * 2
    pdf.image(files[i], x, y, 2.48, 3.46)
  
  pdf.output(f"Proxy-{round(time() * 1000)}.pdf")

def main():
  files = get_files()
  print_files(files)

if __name__ == "__main__":
  main()
