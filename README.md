# Python-Data-Visualization

# Code

http://10.1.1.122/MobileServiceLiveAudit/mbservice.asmx/MBGetPythonData?P_Action=JMD&P_JMD= &P_ZONE= &P_UNIT='
'GU1-CHENNAI BUSINESS ZONE GROUP UNIT'

#from cProfile import label
#from sqlite3 import InterfaceError
import time

start_time = time.time()
import pandas as pd  # pip install pandas openpyxl

import plotly.express as px  # pip install plotly-express

import streamlit as st  # pip install streamlit

import pyodbc

#import sqlalchemy as sal

#from sqlalchemy import create_engine

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

@st.cache

def get_y_vars(action, variables_j,variables_z):

    server = '10.1.1.142'

    database = 'UNOFINANCE_REPORT'

    username = 'uno'

    password = 'devmis123'  

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    cursor = cnxn.cursor()

    # select 26 rows from SQL table to insert in dataframe.

    if(action=="JMD"):

        query = "select JMDGRPUNIT , sum(amount) Amount  from  ExpDumpAsonDate_Final_test  where JMDGRPUNIT is not null group by JMDGRPUNIT;"

    if(action=="ZONE"):

        query = "select ZONEGRPUNIT , sum(amount) Amount from  ExpDumpAsonDate_Final_test where ZONEGRPUNIT is not null and JMDGRPUNIT in("+variables_j+") and isnull(ZONEGRPUNIT,'') <> '' group by ZONEGRPUNIT;"

        #query = "select ZONEGRPUNIT , sum(amount) from  ExpDumpAsonDate_Final_test  where ZONEGRPUNIT is not null group by ZONEGRPUNIT;"

    if(action=="UNIT"):

        query = "select UnitShrtDescr , sum(amount) Amount from  ExpDumpAsonDate_Final_test where ZONEGRPUNIT is not null and JMDGRPUNIT in("+variables_j+")   and ZONEGRPUNIT in("+variables_z+") group by UnitShrtDescr;"

        #query = "select ZONEGRPUNIT , sum(amount) from  ExpDumpAsonDate_Final_test  where ZONEGRPUNIT is not null group by ZONEGRPUNIT;"
    
    df = pd.read_sql(query, cnxn)

    return df

ds_jmd = get_y_vars("JMD","null","null")

jmdgrpunit = st.sidebar.multiselect(

    "Select the JMD:",
    
    options=ds_jmd["JMDGRPUNIT"].unique(),

    default=None

)
ds_selection_jmd = ds_jmd.query(

    "JMDGRPUNIT == @jmdgrpunit"
)
str=""

for x in jmdgrpunit:

    #st.write('You have selected:' , x)

    str = str + "'"+ x +"',"
if(len(str)==0):
    str = "'''"
st.write(len(str))

strlen =len(str)-1

finstr =str[0:strlen]

ds_zone = get_y_vars("ZONE",finstr,"null")

#COUNTRIES_SELECTED = st.multiselect('Select countries', jmdgrpunit)

#mask_countries = ds['JMDGRPUNIT'].isin(jmdgrpunit)

#st.write('You have selected:', jmdgrpunit)
#st.write(ds["ZONEGRPUNIT"])
zonegrpunit = st.sidebar.multiselect(

    "Select the ZONE:",

    options=ds_zone["ZONEGRPUNIT"].unique(),

    default=ds_zone["ZONEGRPUNIT"].unique(),

)
ds_selection_zone = ds_zone.query(

    "ZONEGRPUNIT ==@zonegrpunit"
)
str1=""

for x in zonegrpunit:

    #st.write('You have selected:' , x)

    str1 = str1 + "'"+ x +"',"
if(len(str1)==0):
    str1 = "'''"
st.write(len(str))

strlen =len(str1)-1    

finstr1 =str1[0:strlen]

#st.write('You have selected:', finstr1)

ds_unit = get_y_vars("UNIT",finstr,finstr1)

unit = st.sidebar.multiselect(

    "Select the UNIT:",

    options=ds_unit["UnitShrtDescr"].unique(),

    default=ds_unit["UnitShrtDescr"].unique()

)
ds_selection_unit = ds_unit.query(

    "UnitShrtDescr ==@unit"

)
st.sidebar.header("Please Filter Here:")
#st.write(ds_jmd)
 
sales_by_product_line = (
    ds_selection_jmd.groupby(by=["JMDGRPUNIT"]).sum()[["Amount"]] 
)
fig_product_sales = px.bar(
    sales_by_product_line,
    y="Amount",
    x=sales_by_product_line.index,
    orientation="v",
    title="<b>JMD VS AMOUNT</b>",
    #color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    yaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_product_sales)

#CHART FOR ZONE AND AMOUNT 
sales_by_hour =(
     ds_selection_zone.groupby(by=["ZONEGRPUNIT"]).sum()[["Amount"]] 
)
fig_hourly_sales = px.bar(
    sales_by_hour,
    y="Amount",
    x=sales_by_hour.index,
    orientation="v",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)
st.plotly_chart(fig_hourly_sales)

 

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute




https://www.youtube.com/watch?v=mTsZL-VmRVE





python -m pip install --upgrade pip                          # update python
python -m pip install django                                        # django installation
django-admin                                                                    # start Django admin panel                          
ls                                                                                             # list of 
django-admin startproject projectname                 # create Project
python manage.py makemigrations                         # make migrations for project
python manage.py migrate
python manage.py runserver                                     #run on server
python manage.py startapp appname                    # To create new app
python manage.py createsuperuser                        # create admin, username, password in Django


Installing virtualenv
pip install virtualenv                                                       #install virtual environment
virtualenv –version                                                       #Test your installation
virtualenv virtualenv-name                                               #create a virtual environment
virtualenv-name\scripts\activate                                   # activate virtual en




https://www.webslesson.info/2017/05/json-dynamic-dependent-select-box-using-jquery-and-ajax.html
