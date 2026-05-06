from pyscript import document, display
import matplotlib.pyplot as plt

days = []
absences = []

def displaying(event):
    day = document.getElementById("day").value
    absence = document.getElementById("absence").value

    if day == "" or absence == "":
        display("Please fill all fields.", target="plot")
        return

    absences.append(int(absence))
    days.append(day)

    plt.clf()
    plt.plot(days, absences, marker="o")
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid(True)

    display(plt, target="plot", append=False)