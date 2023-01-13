# Release: v2.5.3-rc3
#
# Copyright (c) 2022-2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import time

from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def progress_bar():
  """bloco de interface progress func mix"""

  global window_progress

  window_progress = Tk()
  window_progress.title("DYGTube Downloader")
  window_progress.geometry("400x100")
  # site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window_progress['background'] = '#4E4E4E'
  # False para não responsivo e True para responsivo.
  window_progress.resizable(False, False)
  window_progress.attributes('-alpha', 9.1)

  global progress

  progress = ttk.Progressbar(window_progress, orient=HORIZONTAL,
                             length=300, mode='determinate')

  progress.pack(pady=30)

  progress['value'] = 0
  label = Label(window_progress,
                text="0 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(2)
  progress['value'] = 10
  label = Label(window_progress,
                text="10 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
  progress.update_idletasks()
  progress['value'] = 10

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 50

  label = Label(window_progress,
                text="50 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 60

  label = Label(window_progress,
                text="60 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 70

  label = Label(window_progress,
                text="70 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 80

  label = Label(window_progress,
                text="80 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 90

  label = Label(window_progress,
                text="90 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 100

  label = Label(window_progress,
                text="100 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  label = Label(window_progress,
                text="Dowload Concluído!",
                fg='white',
                bg="#4E4E4E").place(x=140, y=60)