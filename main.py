import requests
import json
from tkinter import *
import tkinter .font as font

window = Tk()

# Window Config
window.title('COVID19 Info')
window.geometry('570x400')

def get_country_info():
    url = 'https://api.covid19api.com/summary'
    response = requests.request("GET",url)

    #Get Data from API and store in json
    data = json.loads(response.text)

    # Get Index for Country
    searchcountry = txt.get()

    def get_country_index(country):
        for index,item in enumerate(data['Countries']):
            if item['Country'] == country:
                return index

    countryid = get_country_index(searchcountry)

    #Get New New Confirmed & Total Confirmed
    totalconfirmed = data['Countries'][countryid]['TotalConfirmed']
    total_deaths = data['Countries'][countryid]['TotalDeaths']
    total_recovered = data['Countries'][countryid]['TotalRecovered']

    covid_msg = f'\n       Coronavirus Cases :{totalconfirmed}\nDeaths : {total_deaths}\nRecovered : {total_recovered}'

    # Return covid msg to gui
    output_text.set(covid_msg)


#covid_image = PhotoImage(file="covid.png")
#banner = Label(image= covid_image)
#banner.grid(column=7, row=4, columnspan=2)

my_font = font.Font(family='Helvetica', size=25, weight ='bold')
mainlabel = Label(window, text='COVID TRACKER')
mainlabel['font']=my_font
mainlabel.grid(column=7, row=7,columnspan=2)

# Create Label
my_font1 = font.Font(family='Helvetica', size=14)
lbl = Label(window, text='Enter Country:')
lbl['font']=my_font1
lbl.grid(column=6, row=8, sticky=E)

# Create Entry Field
my_font2 = font.Font(family='Helvetica', size=11)
txt = Entry(window, width=30)
txt['font']=my_font2
txt.grid(column=7, row=8, sticky=W)

# Create Button
my_font3 = font.Font(family='Helvetica', size=11)
btn = Button(window, text='Get Information', command=get_country_info)
btn['font']=my_font3
btn.grid(column=15,row=8, sticky=W)

# Display Output
output_text = StringVar()
my_font4 = font.Font(family='Helvetica', size=17)
lbl_output = Label(window, textvariable=output_text)
lbl_output['font']=my_font4
lbl_output.grid(column=6,columnspan=2, row=9, sticky=W)

window.mainloop()