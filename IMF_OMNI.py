import pandas as pd
import numpy as np
from datetime import datetime,timedelta
df = pd.read_csv('omni2_2017.dat', sep='\s+', header=None, skiprows=0)
df.columns = [ 'year',  'day',  'hour',  'Bartels_rotation_no',  'IMF_Spacecraft_ID',  'SW_plasma_Spacecraft_ID',
              '#pts_IMF_avg',  '#pts_in_plasma_avg','B_avg',  'B', 'Lat_angle', 'long_angle', 'Bx', 
              'By_GSE', 'Bz_GSE','By_GSM', 'Bz_GSM','sigma|B|','sigma_B', 'sigma|Bx|', 'sigma|By|', 'sigma|Bz|',
              'proton_temp', 'proton_density', 'plasma_flow_speed', 'plasma_flow_long_angle',
              'plasma_flow_lat_angle', 'NaNp', 'Flow_pressure', 'sigma_T', 'sigma_N', 'sigma_V', 'sigma_phi_V',
              'sigma_theta_V', 'sigma_Na/Np','electric_field', 'plasma_beta', 'alfven_no', 'Kp', 'R', 'DST_index',
              'AE_index', '43', '44', '45', '46', '47', '48', '49', 'ap_index','f10.7_index', 'PC(N)', 'AL_index', 'AU_index','Magnetosonic_mach_no']

df = df.drop(['43','44','45','46','47','48','49'],axis=1)

flag=True

slider_ranges = {'day':(1,max(df['day'])),'hour':(0,23), 'Bartels_rotation_no':(2502,2515),'B_avg':(0.50,27.30),'B':(0.20,24.90),
					'Bx':(-12.0,13.0),'By_GSE':(-14.40,19.80),'Bz_GSE':(-23.6,18.1),'By_GSM':(-14.20,18.10),
					'Bz_GSM':(-24.20,17.80),'NaNp':(0.001,0.372),'electric_field':(-7.73,16.77),'Kp':(0.00,83.0),
					'DST_index':(-142.0,59.0),'AE_index':(12.0,1271.0)
                }
unknown = {'day':999,'hour':99,'Bartels_rotation_no':9999,'B_avg':999.9,'B':999.9,'Bx':999.9,'By_GSE':999.9,'Bz_GSE':999.9,
			'By_GSM':999.9,'Bz_GSM':999.9,'NaNp':9.999,'electric_field':999.99,'Kp':99,'DST_index':99999,'AE_index':9999
          }
step_value={'day':1,'hour':1, 'Bartels_rotation_no':1,'B_avg':0.1,'B':0.1,'Bx':0.1,'By_GSE':0.1,
			'Bz_GSE':0.1,'By_GSM':0.1,'Bz_GSM':0.1,'NaNp':0.001,'electric_field':0.01,'Kp':1,'DST_index':1,'AE_index':1
            }

from bokeh.plotting import figure, curdoc
from bokeh.io import output_notebook, show
from bokeh.models import HoverTool,Slider,Select, ColumnDataSource
from bokeh.layouts import column , row
from bokeh.models.widgets.sliders import DateRangeSlider, RangeSlider
from datetime import datetime
from bokeh.palettes import Set2

source = ColumnDataSource(data={
    'x':df[(df['day']<unknown['day']) & (df['DST_index']<unknown['DST_index'])]['day'],
    'y':df[(df['day']<unknown['day']) & (df['DST_index']<unknown['DST_index'])]['DST_index'],
    'day':df[(df['day']<unknown['day']) & (df['DST_index']<unknown['DST_index'])]['day'],
    'hour':df[(df['day']<unknown['day']) & (df['DST_index']<unknown['DST_index'])]['hour']
})

def year_update(attr,old,new):
    global flag
    global df
    flag=False
    curdoc().title = "Loading data..."
    plot.title.text = "Loading data..."
    year = year_select.value
    file_name = 'omni2_'+year+'.dat'
    df = pd.read_csv(file_name, sep='\s+', header=None, skiprows=0)
    df.columns = [ 'year',  'day',  'hour',  'Bartels_rotation_no',  'IMF_Spacecraft_ID',  'SW_plasma_Spacecraft_ID',
              '#pts_IMF_avg',  '#pts_in_plasma_avg','B_avg',  'B', 'Lat_angle', 'long_angle', 'Bx', 
              'By_GSE', 'Bz_GSE','By_GSM', 'Bz_GSM','sigma|B|','sigma_B', 'sigma|Bx|', 'sigma|By|', 'sigma|Bz|',
              'proton_temp', 'proton_density', 'plasma_flow_speed', 'plasma_flow_long_angle',
              'plasma_flow_lat_angle', 'NaNp', 'Flow_pressure', 'sigma_T', 'sigma_N', 'sigma_V', 'sigma_phi_V',
              'sigma_theta_V', 'sigma_Na/Np','electric_field', 'plasma_beta', 'alfven_no', 'Kp', 'R', 'DST_index',
              'AE_index', '43', '44', '45', '46', '47', '48', '49', 'ap_index','f10.7_index', 'PC(N)', 'AL_index', 'AU_index','Magnetosonic_mach_no']

    df = df.drop(['43','44','45','46','47','48','49'],axis=1)
    slider_ranges = {'day':(1,max(df['day']))}
    for x in label_options:
        try:
            slider_ranges[x]=(min(df[df[x]<unknown[x]][x]),max(df[df[x]<unknown[x]][x]))
        except:
            slider_ranges[x]=(min(df[x]),max(df[x]))

    date_range_slider.start = slider_ranges['day'][0]
    date_range_slider.end = slider_ranges['day'][1]
    date_range_slider.value = slider_ranges['day']

    Bartels_rotation_no_slider.start = slider_ranges['Bartels_rotation_no'][0]
    Bartels_rotation_no_slider.end = slider_ranges['Bartels_rotation_no'][1]
    Bartels_rotation_no_slider.value = slider_ranges['Bartels_rotation_no']

    B_avg_slider.start = slider_ranges['B_avg'][0]
    B_avg_slider.end = slider_ranges['B_avg'][1]
    B_avg_slider.value = slider_ranges['B_avg']

    B_slider.start = slider_ranges['B'][0]
    B_slider.end = slider_ranges['B'][1]
    B_slider.value = slider_ranges['B']

    Bx_slider.start = slider_ranges['Bx'][0]
    Bx_slider.end = slider_ranges['Bx'][1]
    Bx_slider.value = slider_ranges['Bx']

    By_GSE_slider.start = slider_ranges['By_GSE'][0]
    By_GSE_slider.end = slider_ranges['By_GSE'][1]
    By_GSE_slider.value = slider_ranges['By_GSE']

    Bz_GSE_slider.start = slider_ranges['Bz_GSE'][0]
    Bz_GSE_slider.end = slider_ranges['Bz_GSE'][1]
    Bz_GSE_slider.value = slider_ranges['Bz_GSE']

    By_GSM_slider.start = slider_ranges['By_GSM'][0]
    By_GSM_slider.end = slider_ranges['By_GSM'][1]
    By_GSM_slider.value = slider_ranges['By_GSM']

    Bz_GSM_slider.start = slider_ranges['Bz_GSM'][0]
    Bz_GSM_slider.end = slider_ranges['Bz_GSM'][1]
    Bz_GSM_slider.value = slider_ranges['Bz_GSM']

    NaNp_slider.start = slider_ranges['NaNp'][0]
    NaNp_slider.end = slider_ranges['NaNp'][1]
    NaNp_slider.value = slider_ranges['NaNp']

    electric_field_slider.start = slider_ranges['electric_field'][0]
    electric_field_slider.end = slider_ranges['electric_field'][1]
    electric_field_slider.value = slider_ranges['electric_field']

    Kp_slider.start = slider_ranges['Kp'][0]
    Kp_slider.end = slider_ranges['Kp'][1]
    Kp_slider.value = slider_ranges['Kp']

    DST_index_slider.start = slider_ranges['DST_index'][0]
    DST_index_slider.end = slider_ranges['DST_index'][1]
    DST_index_slider.value = slider_ranges['DST_index']

    AE_index_slider.start = slider_ranges['AE_index'][0]
    AE_index_slider.end = slider_ranges['AE_index'][1]
    AE_index_slider.value = slider_ranges['AE_index']

    new_data = {
        'x':df[df['DST_index']<unknown['DST_index']]['day'],
        'y':df[df['DST_index']<unknown['DST_index']]['DST_index'],
        'day':df[df['DST_index']<unknown['DST_index']]['day'],
        'hour':df[df['DST_index']<unknown['DST_index']]['hour']
    }

    source.data = new_data

    curdoc().title = "IMF data "+year
    plot.title.text = "DST V/S day"
    flag=True


def update_plot(attr,old,new):
    global flag
    global df
    if(flag):
        x = x_axis.value
        y = y_axis.value
        plot.xaxis.axis_label = x
        plot.yaxis.axis_label = y
        plot.title.text = x + ' V/S ' + y

        mask = (df['day']<=date_range_slider.value[1]) & (df['day']>=date_range_slider.value[0])
        mask = mask & (df['hour']<=hour_range_slider.value[1]) & (df['hour']>=hour_range_slider.value[0])
        mask = mask & (((df['Bartels_rotation_no']<=Bartels_rotation_no_slider.value[1]) & (df['Bartels_rotation_no']>=Bartels_rotation_no_slider.value[0])) | (df['Bartels_rotation_no']==unknown['Bartels_rotation_no']))
        mask = mask & (((df['B_avg']<=B_avg_slider.value[1]) & (df['B_avg']>=B_avg_slider.value[0])) | (df['B_avg']==unknown['B_avg']))
        mask = mask & (((df['B']<=B_slider.value[1]) & (df['B']>=B_slider.value[0])) | (df['B']==unknown['B']))
        mask = mask & (((df['Bx']<=Bx_slider.value[1]) & (df['Bx']>=Bx_slider.value[0])) | (df['Bx']==unknown['Bx']))
        mask = mask & (((df['By_GSE']<=By_GSE_slider.value[1]) & (df['By_GSE']>=By_GSE_slider.value[0])) | (df['By_GSE']==unknown['By_GSE']))
        mask = mask & (((df['Bz_GSE']<=Bz_GSE_slider.value[1]) & (df['Bz_GSE']>=Bz_GSE_slider.value[0])) | (df['Bz_GSE']==unknown['Bz_GSE']))
        mask = mask & (((df['By_GSM']<=By_GSM_slider.value[1]) & (df['By_GSM']>=By_GSM_slider.value[0])) | (df['By_GSM']==unknown['By_GSM']))
        mask = mask & (((df['Bz_GSM']<=Bz_GSM_slider.value[1]) & (df['Bz_GSM']>=Bz_GSM_slider.value[0])) | (df['Bz_GSM']==unknown['Bz_GSM']))
        mask = mask & (((df['NaNp']<=NaNp_slider.value[1]) & (df['NaNp']>=NaNp_slider.value[0])) | (df['NaNp']==unknown['NaNp']))
        mask = mask & (((df['electric_field']<=electric_field_slider.value[1]) & (df['electric_field']>=electric_field_slider.value[0])) | (df['electric_field']==unknown['electric_field']))
        mask = mask & (((df['Kp']<=Kp_slider.value[1]) & (df['Kp']>=Kp_slider.value[0])) | (df['Kp']==unknown['Kp']))
        mask = mask & (((df['DST_index']<=DST_index_slider.value[1]) & (df['DST_index']>=DST_index_slider.value[0])) | (df['DST_index']==unknown['DST_index']))
        mask = mask & (((df['AE_index']<=AE_index_slider.value[1]) & (df['AE_index']>=AE_index_slider.value[0])) | (df['AE_index']==unknown['AE_index']))

        mask = mask & (df[x]!=unknown[x])
        mask = mask & (df[y]!=unknown[y])

        new_data = {
            'x':df[mask][x],
            'y':df[mask][y],
            'day':df[mask]['day'],
            'hour':df[mask]['hour']
        }
        source.data = new_data

year_options=[]
for i in range(1963,2019):
	year_options.append(str(i))

year_select = Select(title='Year',value='2017',options=year_options)

label_options = ['hour','Bartels_rotation_no','B_avg','B','Bx','By_GSE','Bz_GSE','By_GSM','Bz_GSM','NaNp',
                 'electric_field','DST_index','Kp','AE_index']

slider_labels = ['day','hour','Bartels_rotation_no','B_avg','B','Bx','By_GSE','Bz_GSE','By_GSM','Bz_GSM','NaNp',
                 'electric_field','DST_index','Kp','AE_index']

x_axis = Select(title='X-axis label',value='day',options=["day"]+label_options)
y_axis = Select(title='Y-axis label',value='DST_index',options=label_options)

hover = HoverTool(tooltips=[('x','@x'),('y','@y'),('day','@day'),('Hour','@hour')])


date_range_slider = RangeSlider(title="Day", 
                                    start=slider_ranges['day'][0],
                                    end=slider_ranges['day'][1],
                                    value=(slider_ranges['day']),
                                    step = step_value['day'])

hour_range_slider = RangeSlider(title='Hour range',
                                start=slider_ranges['hour'][0],
                                end=slider_ranges['hour'][1],
                                step=step_value['hour'],
                                value=(slider_ranges['hour']))

Bartels_rotation_no_slider = RangeSlider(title="Bartel's rotation number",start=slider_ranges['Bartels_rotation_no'][0],
                                         end=slider_ranges['Bartels_rotation_no'][1],
                                         step=step_value['Bartels_rotation_no'],
                                         value=slider_ranges['Bartels_rotation_no'])

B_avg_slider = RangeSlider(title="Average B",
                          start=slider_ranges['B_avg'][0],
                          end=slider_ranges['B_avg'][1],
                          value=slider_ranges['B_avg'],
                           step=step_value['B_avg'])

B_slider = RangeSlider(title="Magnitude of B",
                      start=slider_ranges['B'][0],
                      end=slider_ranges['B'][1],
                      value=slider_ranges['B'],
                      step=step_value['B'])

Bx_slider = RangeSlider(title="Bx (GSE GSM)",
                       start=slider_ranges['Bx'][0],
                       end=slider_ranges['Bx'][1],
                       value=slider_ranges['Bx'],
                       step=step_value['Bx'])

By_GSE_slider = RangeSlider(title="By (GSE)",
                           start=slider_ranges['By_GSE'][0],
                           end=slider_ranges['By_GSE'][1],
                           value=slider_ranges['By_GSE'],
                           step=step_value['By_GSE'])

Bz_GSE_slider = RangeSlider(title="Bz (GSE)",
                           start=slider_ranges['Bz_GSE'][0],
                           end=slider_ranges['Bz_GSE'][1],
                           value=slider_ranges['Bz_GSE'],
                           step=step_value['Bz_GSE'])

By_GSM_slider = RangeSlider(title="By (GSM)",
                           start=slider_ranges['By_GSM'][0],
                           end=slider_ranges['By_GSM'][1],
                           value=slider_ranges['By_GSM'],
                           step=step_value['By_GSM'])

Bz_GSM_slider = RangeSlider(title="Bz (GSM)",
                           start=slider_ranges['Bz_GSM'][0],
                           end=slider_ranges['Bz_GSM'][1],
                           value=slider_ranges['Bz_GSM'],
                           step=step_value['Bz_GSM'])

NaNp_slider = RangeSlider(title="Na/Np",
                         start=slider_ranges['NaNp'][0],
                         end=slider_ranges['NaNp'][1],
                         value=slider_ranges['NaNp'],
                         step=step_value['NaNp'])

electric_field_slider = RangeSlider(title="Electric Field",
                                   start=slider_ranges['electric_field'][0],
                                   end=slider_ranges['electric_field'][1],
                                   step=step_value['electric_field'],
                                   value=slider_ranges['electric_field'])

Kp_slider = RangeSlider(title="Kp",
                       start=slider_ranges['Kp'][0],
                       end=slider_ranges['Kp'][1],
                       value=slider_ranges['Kp'],
                       step=step_value['Kp'])

DST_index_slider = RangeSlider(title="DST index",
                              start=slider_ranges['DST_index'][0],
                              end=slider_ranges['DST_index'][1],
                              value=slider_ranges['DST_index'],
                              step=step_value['DST_index'])

AE_index_slider = RangeSlider(title="AE index",
                             start=slider_ranges['AE_index'][0],
                             end=slider_ranges['AE_index'][1],
                             value=slider_ranges['AE_index'],
                             step=step_value['AE_index'])


plot = figure(title='DST V/S Bz',x_axis_label='DST',y_axis_label='Bz_GSM')
plot.circle(x='x',y='y',alpha=0.2,color='blue',hover_fill_color='red',hover_alpha=1.0,source=source)
plot.add_tools(hover)

layout = row(column([year_select,date_range_slider,hour_range_slider,Bartels_rotation_no_slider,B_avg_slider,B_slider,Bx_slider,By_GSE_slider,Bz_GSE_slider,By_GSM_slider,Bz_GSM_slider,NaNp_slider,electric_field_slider,DST_index_slider]),
             column([row([x_axis,y_axis]),plot,row([Kp_slider,AE_index_slider])]))

sliders = [date_range_slider,hour_range_slider,Bartels_rotation_no_slider,B_avg_slider,B_slider,Bx_slider,By_GSE_slider,Bz_GSE_slider,
			By_GSM_slider,Bz_GSM_slider,NaNp_slider,electric_field_slider,DST_index_slider,Kp_slider,AE_index_slider]


year_select.on_change('value',year_update)
x_axis.on_change('value',update_plot)
y_axis.on_change('value',update_plot)
for x in sliders:
	x.on_change('value',update_plot)


curdoc().add_root(layout)
curdoc().title = "IMF data 2017"