import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os


def clean_data(stock_data):
    clean = stock_data['Adj Close']
    return clean


def get_date(data):
    data = StringVar()
    data = date.get()
    year, month, day = data.split(",")
    return int(year), int(month), int(day)


def graph():
    print(str(var1), str(var2))
    ticker = entry1.get()
    print(ticker)
    year, month, day = get_date(date)
    start = dt.datetime(year, month, day)
    end = dt.date.today()
    df = web.DataReader(ticker, 'yahoo', start, end)
    df_clean = clean_data(df)
    style.use('ggplot')
    plt.subplots(figsize=(12, 8))
    plt.plot(df_clean, label=ticker)
    if var1.get() == 1:
        short = df_clean.rolling(window=30).mean()
        plt.plot(short, label='30 day average')
    if var2.get() == 1:
        long = df_clean.rolling(window=90).mean()
        plt.plot(long, label='90 day average')
    if var3.get() == 1:
        long = df_clean.rolling(window=180).mean()
        plt.plot(long, label='180 day average')
    plt.xlabel('Date')
    plt.ylabel('Adj Close')
    plt.legend()
    plt.show()


root = tk.Tk()
root.title("Stock Analyzer")
root.resizable(0, 0)
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label2 = tk.Label(root, text='Stock Data Analyzer')
label2.config(font=('helvetica', 16), bg="white")
canvas.create_window(350, 100, window=label2)

var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='30 Day Rolling Average', variable=var1, onvalue=1, offvalue=0, bg="white")
canvas.create_window(350, 270, window=c1)

var2 = tk.IntVar()
c2 = tk.Checkbutton(root, text='90 Day Rolling Average', variable=var2, onvalue=1, offvalue=0, bg="white")
canvas.create_window(350, 300, window=c2)

var3 = tk.IntVar()
c3 = tk.Checkbutton(root, text='180 Day Rolling Average', variable=var3, onvalue=1, offvalue=0, bg="white")
canvas.create_window(352, 330, window=c3)

label_stock_ticker = tk.Label(root, text='Enter Stock Ticker Symbol')
canvas.create_window(350, 140, window=label_stock_ticker)
label_stock_ticker.config(font=('helvetica', 9), bg="white")
button = tk.Button(root, text="Open Stock", padx=10, pady=5, fg="white", bg="#263D42", command=graph)
button_quit = tk.Button(root, text="Exit Program", padx=10, pady=5, fg="white", bg="#263D42", command=root.quit)
canvas.create_window(350, 200, window=button)
canvas.create_window(342, 600, window=button_quit)
label_date = tk.Label(root, text='Start Date (YYYY, MM, DD)')
label_date.config(font=('helvetica', 9), bg="white")
canvas.create_window(350, 370, window=label_date)

date = tk.Entry(root)
canvas.create_window(350, 390, window=date)

entry1 = tk.Entry(root)
canvas.create_window(350, 160, window=entry1)

root.mainloop()


