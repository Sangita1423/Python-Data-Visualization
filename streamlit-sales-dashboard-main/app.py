# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



from sqlite3 import InterfaceError
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
 
    
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = '10.1.1.142'
    database = 'UNOFINANCE_REPORT' 
    username = 'uno' 
    password = 'devmis123'  
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    # select 26 rows from SQL table to insert in dataframe.
    query = "SELECT * FROM ExpDumpAsonDate_Final_test"
    df = pd.read_sql(query, cnxn)
    #print(df.head(26))


    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["VoucherDt"], format="%H:%M:%S").dt.hour
    #return df
    df["JMDGRPUNIT"] = df["JMDGRPUNIT"] 
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
jmdgrpunit = st.sidebar.multiselect('select:', df["JMDGRPUNIT"].unique())
#st.write('You selected:', jmdgrpunit)
zonegrpunit = st.sidebar.multiselect('select:', df["ZONEGRPUNIT"].unique())
#st.write('You selected:', zonegrpunit)
expsubcategory = st.sidebar.multiselect('select:', df["ExpSubCategoryDescr"].unique())
#st.write('You selected:', expsubcategory)    

df_selection = df.query(
    "JMDGRPUNIT == @jmdgrpunit & ZONEGRPUNIT == @zonegrpunit & ExpSubCategoryDescr ==@expsubcategory"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Amount"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" #* int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Amount"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Amount:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["ZONEGRPUNIT"]).sum()[["Amount"]].sort_values(by="Amount")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x=sales_by_product_line.index,
    y="Amount",
    #orientation="v",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    yaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["ExpSubCategoryDescr"]).sum()[["Amount"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Amount",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
