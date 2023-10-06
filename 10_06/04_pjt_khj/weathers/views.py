from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
# Create your views here.

plt.switch_backend('Agg')

csv_path = 'weathers/data/austin_weather.csv'
df = pd.read_csv(csv_path)

def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'problem1.html', context)

import matplotlib.dates as mdates




def problem2(request):
    df.loc[:,'Date'] = pd.to_datetime(df.loc[:,'Date'])
    x = df.loc[:,'Date']
    y1 = df.loc[:,'TempHighF']
    y2 = df.loc[:,'TempAvgF']
    y3 = df.loc[:,'TempLowF']
    fig = plt.subplots(figsize=(10,6))
    plt.clf()
    plt.plot(x,y1, label = 'High Temperature')
    plt.plot(x,y2, label = 'Average Temperature')
    plt.plot(x,y3, label = 'Low Temperature')
    plt.title('Temperature Variation')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')
    plt.grid(True)
    plt.legend()
    
    buffer = BytesIO()
    
    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }
    
    return render(request, 'problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])

    Month_temperature = df.groupby(df['Date'].dt.to_period('M'))[['TempHighF', 'TempAvgF', 'TempLowF']].mean()

    fig = plt.subplots(figsize=(10,6))
    plt.clf()
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempHighF'], label='Max Temperature')
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempAvgF'], label='Mean Temperature')
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempLowF'], label='Min Temperature')


    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.gca().xaxis.get_major_ticks()[0].label.set_visible(False)
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    # plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=8))
    plt.grid(visible=True)
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend(loc='lower right')

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()


    context = {

        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)
    df = df.replace({'Events' : ' '}, 'No Events') 
    

    df['Event_Separated'] = df['Events'].str.split(' , ')


    event_counts = df['Event_Separated'].explode().value_counts()
    plt.clf()

    plt.bar(event_counts.index, event_counts.values)

    plt.grid(visible=True)
    plt.xlabel('Events')
    plt.ylabel('Counts')
    plt.title('Event Counts')

    buffer = BytesIO()

    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'problem4.html', context)