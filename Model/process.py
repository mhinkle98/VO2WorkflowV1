from enum import Enum
# from PySide6.QtCore import QAbstractItemModel

class Process():
    dataTypes = {
        "SPUT", "Sputtering and Annealing",
        "TRANS", "Transition",
        "ELLIP", "Ellipsometry"
        "TEMPSPEC", "Temperature Dependent Spectrometry",
        "LITH", "Lithography",
        "ETCH", "Etching",
        "EXC", "Excess Processes"
    }

    colors = {
        "GREEN", "#00FF00",
        "RED", "#FF0000",
        "GREY", "#808080"
    }
    
    color = colors["GREY"]
    name = "Process Name"
    dataType = "EXC"

    def __init__(self, dataType: str):
        """Enter the name of the data type: SPUT, TRANS, ELLIP, TEMPSPEC, LITH, ETCH, EXC"""
        # super().__init__()
        
        self.dataType = dataType

        match self.dataType:
            case "SPUT":
                self.name = self.dataTypes["SPUT"]
                self.picture = ""
                self.notes = ""
            case "TRANS":
                self.name = self.dataTypes["NAME"]
                self.picture = ""
                self.notes = ""
                self.result: bool = None # was the transition good?
            case "ELLIP":
                self.name = self.dataTypes["ELLIP"]
                self.numTrials = 0
                self.graphs = []
                self.data = []
                self.notes = []
            case "TEMPSPEC":
                self.name = self.dataTypes["TEMPSPEC"]
                self.VisData = [] # nested list? ([Temp, file])?
                self.IRData = [] # nested list? ([Temp, file])?
                self.result: bool = None # was this a good transition?
            case "ETCH":
                self.name = self.dataTypes["ETCH"]
                self.notes = ""
                self.data = []
