#! usr/bin/python
"""
This app is to help calculate an estimated quote for time required by a number of workers to complete main tasks and other tasks.
"""

import tkinter as tk

class Application(tk.Frame):

    def createLayout(self):
        self.columnconfigure(2)

    def quote_calc(self):
        calcToString = 0

        numOfWorkStations = 2 # stations are used by the worker by necessary for a portion of worker
        # TODO portion is hardcoded below, but considering allowing user to edit

        mainWorkTimePerTask = 30
        otherWorkTimePerTask = 15

        try:
            numOfWorkers = 1

            NUMOFMAINTASKS = int(self.NUMOFMAINTASKS.get())
            NUMOFOTHERTASKS = int(self.NUMOFOTHERTASKS.get())
            numOfWorkers = int(self.NUMOFWORKERS.get())

            mainWorkTimePerTaskPerWorker = 0.4*mainWorkTimePerTask # work time without station
            mainWorkTimePerTaskPerStation = 0.6*mainWorkTimePerTask # work time at station

            totalWorkTimeNeededByWorker = mainWorkTimePerTaskPerWorker * NUMOFMAINTASKS
            totalWorkTimeNeededAtStation = mainWorkTimePerTaskPerStation * NUMOFMAINTASKS

            workCalculation = ((totalWorkTimeNeededByWorker + (otherWorkTimePerTask * NUMOFOTHERTASKS))/numOfWorkers)+(totalWorkTimeNeededAtStation/numOfWorkStations)
            complexCalcHours = str(int(workCalculation/60))
            complexCalcMins = str(int(workCalculation%60))
            outputString = str(complexCalcHours + 'h & ' + complexCalcMins + 'm')


            self.WORKTIMECALC.configure(text=outputString)

        except:
            if numOfWorkers<1:
                self.WORKTIMECALC.configure(text='no workers = no work!')
            else:
                self.WORKTIMECALC.configure(text='Whole Numbers ONLY.')

    def createWidgets(self):

        self.QUITBUTTON = tk.Button(self, text='Quit',command=self.quit)
        self.QUITBUTTON.grid(columnspan=2, row=4)

        self.LABELDISPLA = tk.Label(self, text='Main Work Tasks:')
        self.LABELDISPLA.grid(column=0, row=0)

        self.NUMOFMAINTASKS = tk.Entry(self)
        self.NUMOFMAINTASKS.grid(column=1, row=0)

        self.LABELOTHER = tk.Label(self, text='Other Work Tasks:')
        self.LABELOTHER.grid(column=0, row=1)

        self.NUMOFOTHERTASKS = tk.Entry(self)
        self.NUMOFOTHERTASKS.grid(column=1, row=1)

        self.LABELWORKERS = tk.Label(self, text="Worker's Present:")
        self.LABELWORKERS.grid(column=0, row=2)

        self.NUMOFWORKERS = tk.Entry(self)
        self.NUMOFWORKERS.grid(column=1, row=2)

        self.CALC = tk.Button(self, text='Calculate', command=self.quote_calc)
        self.CALC.grid(column=0,row=3)

        self.WORKTIMECALC = tk.Label(self, text='Time to Quote:')
        self.WORKTIMECALC.grid(column=1, row=3)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.createLayout()
        self.createWidgets()

app = Application()
app.master.title('Work Time Needed Quote')
app.mainloop()
