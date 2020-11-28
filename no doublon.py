from tkinter import *
from tkinter import filedialog

class Nodoublon:

    def suppressionDoublon(self, file):
        l = []
        with open(file) as f:
            for line in f:
                l.append(line.replace("\n",""))
        l2 = []
        for e in l:
            if l.count(e) < 2:
                l2.append(e)


        with open(f"{file.replace('.txt','')}-convert.txt", "w") as f:
            for e in l2:
                f.write(f"{e}\n")
        return


    def getfile(self):
        self.filename = filedialog.askopenfilename()

    def start(self):
        fenetre = Tk()
        fenetre.title("Supression des Doublons totale")
        fenetre.geometry("150x50")


        bouton_getfiles = Button(fenetre, text="Get Files", command=self.getfile)
        bouton_getfiles.pack()

        bouton_go = Button(fenetre, text="Go!", command=lambda: self.suppressionDoublon(self.filename))
        bouton_go.pack()

        fenetre.mainloop()

if __name__ == '__main__':
    Nodoublon().start()
