#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import sys


try:
    filei = sys.argv[1]
except IndexError:
    pass
else:
    root = Tk()
    root.configure(bg="black")
    root.title("Logger")
    frame1 = Frame(root)
    frame1.configure(bg="black",width=800,height=800)

    frame2 = Frame(root)
    frame2.configure(bg="black")

    issueTitleVar = StringVar()
    vulnUrlVar = StringVar()
    dataVar = StringVar()
    impactVar = StringVar()
    pjVar = StringVar()

    titleLabel = Label(frame1, text="Reporter", fg="white", bg="black", font=("Verdana",25,"bold"))

    issueNum = Label(frame1, text="Issue No  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    issueEnt =  Spinbox(frame1, from_=1, to=1000, width=8, highlightcolor="blue")

    pjLabel = Label(frame1, text="Project  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    pjEnt = Entry(frame1, textvariable=pjVar, fg="cyan", bg="black", width=25, font=("Aerial",10,"bold"), highlightcolor="blue")

    issueTitle = Label(frame1, text="Issue Title  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    issueTitleEnt = Entry(frame1, textvariable=issueTitleVar, fg="cyan", bg="black", width=100, font=("Aerial",10,"bold"), highlightcolor="blue")

    vulnUrl = Label(frame1, text="Endpoint  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    vulnUrlEnt = Entry(frame1, textvariable=vulnUrlVar, fg="cyan", bg="black", width=100, font=("Aerial",10,"bold"), highlightcolor="blue")

    methodLabel = Label(frame1, text="HTTP method  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    methodComboBox = ttk.Combobox(frame1, values=["","GET","POST","PUT","PATCH","HEAD","TRACE","OPTIONS","DELETE"], width=8)

    dataLabel = Label(frame1, text="Request data  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    dataEnt = Text(frame1, fg="cyan", bg="black", width=60, height=8, font=("Aerial",10,"bold"), highlightcolor="blue")

    impactLabel = Label(frame1, text="Impact  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    impactEnt = Entry(frame1, textvariable=impactVar, fg="cyan", bg="black", width=100, font=("Aerial",10,"bold"), highlightcolor="blue")

    dayLabel = Label(frame1, text="Day  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    daySpinBox = Spinbox(frame1, from_=1, to=31, width=5, highlightcolor="blue")

    monthLabel = Label(frame1, text="Month  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    monthSpinBox = Spinbox(frame1, from_=1, to=12, width=5, highlightcolor="blue")

    yearLabel = Label(frame1, text="Year  ", fg="lime", bg="black", font=("Aerial",15,"bold"))
    yearSpinBox = Spinbox(frame1, from_=2025, to=2070, width=5, highlightcolor="blue")

    resultLabel = Label(frame2, text="Output", fg="lime", bg="black", font=("Aerial",15,"bold"))
    resultText = Text(frame2, width=100, height=40, fg="cyan", bg="black", highlightcolor="blue")

    def add():
        sIssueNo = issueEnt.get()
        sTitle = issueTitleVar.get()
        sPj = pjVar.get()
        sMethod = methodComboBox.get()
        sVulnUrl = vulnUrlVar.get()
        sData = dataEnt.get(0.0,END).strip()
        sImpact = impactVar.get()
        sDay = daySpinBox.get()
        sMonth = monthSpinBox.get()
        sYear = yearSpinBox.get()
        dataText = f"#{sPj}_issueNo_{sIssueNo}\n{sTitle}\nVulnerable endpoint : {sVulnUrl}\nHTTP method         : {sMethod}\nRequest data        : {sData}\nImpact              : {sImpact}\nDate                : {sDay}/{sMonth}/{sYear}\n----------------------------------------------------------------------\n"
        logfile = open(f"{filei}","a")
        logfile.write(dataText)
        impactEnt.delete(0,END)
        dataEnt.delete(0.0,END)
        vulnUrlEnt.delete(0,END)
        issueTitleEnt.delete(0,END)
        resultText.insert(0.0,dataText)

    writeButton = Button(frame1, text="Write", fg="white", bg="black", font=("Aerial",20,"bold"), width=10, height=2, command=add, activebackground="lime", activeforeground="black")

    frame1.pack(pady=80,side=LEFT,padx=10)
    frame2.pack(pady=80,side=RIGHT,padx=30)
    titleLabel.grid( row=0, column=0, columnspan=2, padx=5)
    pjLabel.grid( row=1, column=0, sticky="e")
    pjEnt.grid( row=1, column=1, sticky="w")
    issueNum.grid( row=2, column=0, sticky="e")
    issueEnt.grid( row=2, column=1, sticky="w")
    issueTitle.grid( row=3, column=0, sticky="e")
    issueTitleEnt.grid( row=3, column=1, sticky="w")
    vulnUrl.grid( row=4, column=0, sticky="e")
    vulnUrlEnt.grid( row=4, column=1, sticky="w")
    methodLabel.grid( row=5, column=0, sticky="e")
    methodComboBox.grid( row=5, column=1, sticky="w")
    dataLabel.grid( row=6, column=0, sticky="e")
    dataEnt.grid( row=6, column=1, sticky="w")
    impactLabel.grid( row=7, column=0, sticky="e")
    impactEnt.grid( row=7, column=1, sticky="w")
    dayLabel.grid( row=8, column=0, sticky="e")
    daySpinBox.grid( row=8, column=1, sticky="w")
    monthLabel.grid( row=9, column=0, sticky="e")
    monthSpinBox.grid( row=9, column=1, sticky="w")
    yearLabel.grid( row=10, column=0, sticky="e")
    yearSpinBox.grid( row=10, column=1, pady=10, sticky="w")
    writeButton.grid( row=11, column=0, columnspan=2)
    resultLabel.grid( row=0, column=0, pady=10)
    resultText.grid( row=1, column=0, pady=10)

    for widget in frame1.winfo_children():
        widget.grid_configure(pady=10)

    root.mainloop()
