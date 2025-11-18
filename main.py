#MapPlot.py
#Name: Macy Dubes
#Date: 11/16/25
#Assignment: Lab 10

#My favorite subject from the list is coffee too so I had to pick it, I have tried almost every coffee spot in Omaha
#import necessary applications
import coffee
import pandas
import matplotlib.pyplot as plt
coffee = coffee.get_coffee()
years = []
scores = []
#Align elements of data to code
for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    #Make sure it doesn't include outliers
    if score != 0:
        years.append(year)
        scores.append(score)
#Create the image
df = pandas.DataFrame({"Year": years, "Score": scores})
print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score')
#Generate the image
plt.savefig("output")
