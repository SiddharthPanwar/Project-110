import csv
import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
 
df = pd.read_csv('data.csv')
data = df["articles"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return(mean)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["articles"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode = "lines",name="Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean Of Sampling Distribution : ",mean)

setup()
population_mean = statistics.mean(data)
print("The Mean Of The Population : ",population_mean)
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
        
    std_dev = statistics.stdev(mean_list)
    print("Standard Deviation Of Your Mean : ",std_dev)

standard_deviation()