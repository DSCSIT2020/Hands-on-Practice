# Hands-on-Practice
# Developer Student Clubs - Siliguri Institute Of Technology
# Prasun Roy - https://github.com/PRASUNR0Y

from tkinter import *

root = Tk()
root.geometry("460x260")
root.title("Covid-19 Tracker")

def shwdata():
    import matplotlib.patches as mpatches
    from covid import Covid
    from matplotlib import pyplot as plt

    covid = Covid(source="worldometers")
    case = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    root.update()
    countries = data.get()
    country_names = countries.strip()
    country_names = country_names.replace(" ", ",")
    country_names = country_names.split(",")

    for x in country_names:
        case.append(covid.get_status_by_country_name(x))

    for y in case:
        confirmed.append(y["confirmed"])
        active.append(y["active"])
        deaths.append(y["deaths"])
        recovered.append(y["recovered"])
    confirmed_patch = mpatches.Patch(color='red', label='Confirmed')
    recovered_patch = mpatches.Patch(color='green', label='Recovered')
    active_patch = mpatches.Patch(color='blue', label='Active')
    deaths_patch = mpatches.Patch(color='yellow', label='Deaths')
    plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

    for x in range(len(country_names)):
        plt.bar(country_names[x], confirmed[x], color='red')
        if recovered[x] > active[x]:
            plt.bar(country_names[x], recovered[x], color='green')
            plt.bar(country_names[x], active[x], color='blue')
        else:
            plt.bar(country_names[x], active[x], color='blue')
            plt.bar(country_names[x], recovered[x], color='green')
        plt.bar(country_names[x], deaths[x], color='yellow')

    plt.title('Current COVID-19 Cases')
    plt.xlabel('Country Name')
    plt.ylabel('Cases(in millions)')
    plt.show()


Label(root, text="Enter all countries names\n for whom you want to get\n COVID-19 data", font="Consolas 14 bold").pack()
Label(root, text="Enter Country Name : (Seperate country names using comma or space)").pack()
data = StringVar()
data.set("Enter Here")
entry = Entry(root, textvariable=data, width=45).pack()
Button(root, text="Go", command=shwdata).pack()
root.mainloop()
