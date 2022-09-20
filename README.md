# Python-Data-Visualization

# Website
 
https://stackoverflow.com/questions/67120765/how-to-create-dependent-dropdownlist-in-python-and-streamlit
https://github.com/uMehliseli/Allocation_Tool
with st.sidebar: #1st filter                                     
    FirstFilter = st.mulitiselect(default=df["FirstColumn"].unique())   

df2 = df.query("FirstColumn == @FirstFilter")

with st.sidebar: #2nd filter                                  
    SecondFilter = st.multiselect(deafult=df2["SecondCoulmn"].unique()

df3 = df2.query("SecondColumn == @SecondFilter")

with st.sidebar: #3rd filter*                                       
    ThirdFilter = st.multiselect(default=df3["ThirdColumn"].unique()
