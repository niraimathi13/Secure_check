import streamlit as st
import pandas as pd
import mysql.connector
import datetime
#DATABASE CONNECTION
def creating_connection():
    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='digital',
        )
        return mydb
    except Exception as e:
        st.error(f"DATABASE CONNECTION ERROR:{e}")
        return None
    
#FETCHING THE DATA FROM THE DATABASE
def fetching_of_data(query):
    mydb=creating_connection()
    if mydb:
        try:
                cursor=mydb.cursor()
                cursor.execute(query)
                RESULT=cursor.fetchall()
                columns=[desc[0] for desc in cursor.description] 
                df=pd.DataFrame(RESULT,columns=columns)
                
                return df
        finally:
            mydb.close()
    else:
        return pd.DataFrame()
query="select * from digital.ledger"
data=fetching_of_data(query)
if 'stop_time' in data.columns:
     def format_stop_time(x):
        if pd.isnull(x):
            return None
        elif isinstance(x,datetime.time):
            return x.strftime('%H:%M:%S')
        elif isinstance(x,datetime.timedelta):
            total_seconds=int(x.total_seconds())
            hours=total_seconds//3600
            minutes=(total_seconds%3600)//60
            seconds=total_seconds%60
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        elif isinstance(x,str):
            return x[:8]  
        else:
            return str(x)[:8]  
data['stop_time']=data['stop_time'].apply(format_stop_time)
    
#STREAMLITE APP TITLE
st.set_page_config(page_title="SECURECHECK POLICE DASHBOARD",layout="wide")

#SIDEBAR FOR NAVIGATION
st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["INTRODUCTION OF THE PROJECT","FULL TABLE","KEY METRICES","ADVANCED INSIGHTS","PREDICT OUTCOME AND VIOLATION"])

#                       *********************Page 1-INTRODUCTION************************
if page=="INTRODUCTION OF THE PROJECT":
    st.title(" 👮🏻‍♂️ DIGITAL LEDGER FOR POLICE POST LOGS")
    st.image(r"C:\Users\nirai\Downloads\tag.jpg")
    st.subheader("📊 Streamlit app for creating beautiful dashboards 💎")
    st.write("""
    This project aims to build an SQL-based check post database with a Python-powered dashboard for real-time insights and alerts.
    
    **FEATURES**
    --🖥️ Easy dashboard built with the Streamlit
    --🗃️ Uses SQL to store and manage data automatically
    --🌐 One system for all the check posts
    --🧠 Help to analyze crime and check post activity
    --📊 Shows the report instantly

    """)

#                       ************Page 2-FULL TABLE******************
elif page=='FULL TABLE':
    st.header("🧾 OVERVIEW OF THE POLICE LOGS")
    
    st.dataframe(data,use_container_width=True)

#                         **************Page 3-KEY METRICES****************
elif page=='KEY METRICES':
    st.header("📊 KEY MATRICES")
    column1,column2,column3,column4=st.columns(4)
    with column1:
        total_stops=data.shape[0]
        st.metric("TOTAL POLICE STOPS",total_stops)
    with column2:
         arrests=data[data['stop_outcome'].str.contains("arrest",case=False,na=False)].shape[0]
         st.metric("TOTAL ARREST",arrests)
    with column3:
         warnings=data[data['stop_outcome'].str.contains("warning",case=False,na=False)].shape[0]
         st.metric("TOTAL WARNINGS",warnings)
    with column4:
        drug_related=data[data['drugs_related_stop']==1].shape[0]
        st.metric("DRUG RELATED STOPS",drug_related)
         
#                   **************Page 4-ADVANCED INSIGHTS****************
elif page=='ADVANCED INSIGHTS':
    st.header("🔥ADVANCED INSIGHTS")
    selecting_the_query=st.selectbox("Select the query to run",[
         "Top 10 vehicle number related to drug related stop",
         "Frequently searched vehicle",
         "Driver age group having high arrest rate",
         "Gender distribution of driver stopped in each country",
         "Gender and race combination having highest arrest rate",
         "Time of the day having most traffic stop",
         "Average stop duration for different violation",
         "Are the stops during the night are more likely to lead to arrests",
         "Violation most associated with search or arrest",
         "Violation most common among young driver (i.e) less than 25",
         "Violation that rarely result in search or arrest",
         "Country reporting the highest rate of drug related stops",
         "Arrest rate by country and violation",
         "Country having most stop with search conducted",
         "Top 5 violation with highest arrest rate",
         "Driver demographic[Age,Gender,Race] by country",
         "Violation with high search and arrest rate",
         "Number of stops by year,month,hour of the day",
         "Driver violation trend based on race & age",
         "Yearly breakdown of stops and arrests by country"])
    maping_of_query={
         "Top 10 vehicle number related to drug related stop":"""select vehicle_number,count(*) as count from digital.ledger where drugs_related_stop=TRUE group by vehicle_number order by count desc limit 10""",
         "Frequently searched vehicle":"""select vehicle_number,count(*) as most_frequent_search_count from digital.ledger where search_conducted =TRUE group by vehicle_number order by most_frequent_search_count desc limit 15""",
         "Driver age group having high arrest rate":"""select case when driver_age between 18 and 25 then '18-25' when driver_age between 26 and 35 then '26-35' when driver_age between 36 and 45 then '36-45' when driver_age between 46 and 60 then '46-60' else '60+' end as age_group,count(*) as total_stops,count(case when is_arrested =TRUE then 1 end) as arrests,round(count(case when is_arrested =TRUE then 1 end)/count(*)*100.0,2) as arrest_rate from digital.ledger group by age_group order by arrest_rate desc limit 1""",
         "Gender distribution of driver stopped in each country":"""select country_name,count(case when driver_gender='M' then 1 end) as MALE,count(case when driver_gender='F' then 1 end) as FEMALE from digital.ledger group by country_name""",
         "Gender and race combination having highest arrest rate":"""select driver_race,driver_gender,round(count(case when search_conducted =TRUE then 1 end)/count(*)*100.0, 2) as search_rate from digital.ledger group by driver_race, driver_gender order by search_rate DESC limit 1""",
         "Time of the day having most traffic stop":"""select hour(str_to_date(stop_time,'%H:%i')) as hour_of_the_day,count(*) as stop_count from digital.ledger group by hour_of_the_day order by stop_count DESC limit 1""",
         "Average stop duration for different violation":"""select violation,avg(case when stop_duration = '0-15 Min' then 7.5 when stop_duration = '16-30 Min' then 23 when stop_duration = '30+ Min' then 35 END) as average_stop_duration from digital.ledger group by violation""",
         "Are the stops during the night are more likely to lead to arrests":"""select case when hour(str_to_date(stop_time,'%H:%i'))>=18 or hour(str_to_date(stop_time,'%H:%i'))<6 then 'NIGHT' else 'DAY' end as stop_period,count(*) as total_stops,count(case when is_arrested=TRUE then 1 end) as arrests,round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2) as arrest_rate_percent from digital.ledger group by stop_period""",
         "Violation most associated with search or arrest":"""select violation,count(case when search_conducted=TRUE then 1 end) as count_of_the_search,count(case when is_arrested=TRUE then 1 end) as count_of_the_arrest,round(count(case when search_conducted=TRUE then 1 end)/count(*)*100.0,2) as search_rate,round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2) as arrest_rate,greatest(round(count(case when search_conducted=TRUE then 1 end)/count(*)*100.0,2),round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2)) as maximum_arrest_or_search_rate from digital.ledger group by violation order by maximum_arrest_or_search_rate desc limit 1""",
         "Violation most common among young driver (i.e) less than 25":"""select violation,count(*) as counts_of_driver from digital.ledger where driver_age<25 group by violation order by counts_of_driver desc limit 1""",
         "Violation that rarely result in search or arrest":"""select violation,count(case when search_conducted=TRUE then 1 end) as count_of_the_search,count(case when is_arrested=TRUE then 1 end) as count_of_the_arrest,round(count(case when search_conducted=TRUE then 1 end)/count(*)*100.0,2) as search_rate,round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2) as arrest_rate,least(round(count(case when search_conducted=TRUE then 1 end)/count(*)*100.0,2),round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2)) as rarely_arrest_or_search_rate from digital.ledger group by violation order by rarely_arrest_or_search_rate asc limit 1""",
         "Country reporting the highest rate of drug related stops":"""select country_name,count(*) as tot_counts,round(count(case when drugs_related_stop=TRUE then 1 end)/count(*)*100.0,2) as drugs_related_stop_rates from digital.ledger group by country_name order by drugs_related_stop_rates desc limit 1""",
         "Arrest rate by country and violation":"""select country_name,violation,count(*) as tot_count,round(count(case when is_arrested=TRUE then 1 end)/count(*)*100.0,2) as arrest_rate from digital.ledger group by country_name,violation""",
         "Country having most stop with search conducted":"""select country_name,count(case when search_conducted=TRUE then 1 end) as no_of_counts from digital.ledger group by country_name order by no_of_counts desc limit 1""",
         "Top 5 violation with highest arrest rate":"""select violation,count(*) as total,round(count(case when is_arrested=TRUE then 1 end)/count(*)*100,2) as arrest_rate from digital.ledger group by violation order by arrest_rate desc limit 5""",
         "Driver demographic[Age,Gender,Race] by country":"""select country_name,count(*) as tot_driver,count(case when driver_gender='M' then 1 end) as Male_driver,count(case when driver_gender='F' then 1 end) as Female_driver,count(case when driver_race='Asian' then 1 end) as Asian_driver,count(case when driver_race='Black' then 1 end) as Black_driver,count(case when driver_race='Hispanic' then 1 end) as Hispanic_driver,count(case when driver_race='Other' then 1 end) as Other_people,count(case when driver_race ='White' then 1 end) as White_driver,count(case when driver_age<30 then 1 end) as less_than_thirty,count(case when driver_age between 30 and 50 then 1 end) as between_thirty_and_fifty,count(case when driver_age>50 then 1 end) as greater_than_fifty from digital.ledger group by country_name""",
         "Violation with high search and arrest rate":"""select * from(select distinct violation,count(*) over(partition by violation) as total_stops,sum(case when search_conducted=TRUE then 1 else 0 end) over(partition by violation) as total_searches,sum(case when is_arrested=TRUE then 1 else 0 end) over(partition by violation) as total_arrests,round(avg(case when search_conducted=TRUE then 1 else 0 end) over(partition by violation)*100,2) as search_rate_percent,round(avg(case when is_arrested=TRUE then 1 else 0 end) over(partition by violation)*100,2) as arrest_rate_percent from digital.ledger)as sub where search_rate_percent>20 or arrest_rate_percent>20 order by search_rate_percent desc,arrest_rate_percent desc""",
         "Number of stops by year,month,hour of the day":"""select year(str_to_date(stop_date,'%Y-%m-%d')) as STOP_YEAR,month(str_to_date(stop_date,'%Y-%m-%d')) as STOP_MONTH,hour(str_to_date(stop_time,'%H:%i')) as STOP_HOUR,count(*) as total_stops from digital.ledger group by STOP_YEAR,STOP_MONTH,STOP_HOUR order by STOP_YEAR,STOP_MONTH,STOP_HOUR""",
         "Driver violation trend based on race & age":"""select age_info.age_group,r.driver_race,count(*) as total_violations from digital.ledger r join(select distinct driver_age,case when driver_age between 16 and 25 then '16-25' when driver_age between 26 and 35 then '26-35' when driver_age between 36 and 50 then '36-50' when driver_age>50 then '51+' else 'Unknown' end as age_group from digital.ledger)as age_info on r.driver_age=age_info.driver_age group by age_info.age_group, r.driver_race order by age_info.age_group, r.driver_race""",
         "Yearly breakdown of stops and arrests by country":"""select stats.stop_year,stats.country_name,stats.total_stops,stats.total_arrests,round(total_arrests/NULLIF(total_stops*100.0,0), 2)as arrest_rate_percent,sum(total_arrests) over(partition by country_name order by stop_year) as cumulative_arrests from(select year(str_to_date(stop_date,'%Y-%m-%d'))as stop_year,country_name,count(*) as total_stops,count(if(is_arrested,1,NULL))as total_arrests from digital.ledger group by stop_year,country_name)as stats order by stats.country_name,stats.stop_year"""
    }
    if st.button("Run the query 🛩️"):
        output=fetching_of_data(maping_of_query[selecting_the_query])
        if not output.empty:
            st.write(output)
        else:
            st.warning("NO RESULTS FOUND 🔍")

#                          ************Page 4- PREDICT OUTCOME AND VIOLATION*****************
elif page == 'PREDICT OUTCOME AND VIOLATION':
    st.header("☄️ PREDICT THE OUTCOME AND VIOLATION")
    with st.form("form"):
        stop_date=st.date_input("STOP DATE")
        time_str=st.text_input("STOP TIME (HH:MM:SS)",value="12:00:00")
        try:
          stop_time=datetime.datetime.strptime(time_str,"%H:%M:%S").time()
        except ValueError:
           st.error("Invalid time format. Use HH:MM:SS")
           stop_time=None
        driver_gender=st.selectbox("DRIVER GENDER",["female", "male"])
        driver_age=st.number_input("DRIVER AGE",min_value=18,max_value=80)
        violation=st.selectbox("VIOLATION",["Seatbelt","Speeding","Signal","DUI","Other"])
        search_conducted=st.selectbox("SEARCH CONDUCTED",["0", "1"])
        stop_outcome=st.selectbox("STOP OUTCOME",["Ticket","Arrest","Warning"])
        stop_duration=st.selectbox("STOP DURATION",data['stop_duration'].dropna().unique())
        drugs_related_stop=st.selectbox("DRUG RELATED",["0", "1"])
        timestamp =pd.Timestamp.now()
        submit=st.form_submit_button("PREDICT THE STOP OUTCOME AND VIOLATION 🌟")
    if submit:
        filter_data = data[
            (data['driver_gender']==driver_gender) &
            (data['driver_age']==driver_age) &
            (data['search_conducted']==int(search_conducted)) &
            (data['stop_duration']==stop_duration) &
            (data['drugs_related_stop']==drugs_related_stop)&
            (data['violation']==violation)&
            (data['stop_outcome']==stop_outcome)
        ]
        searching="A search was conducted" if int(search_conducted) else "No search was conducted"
        drug_txt="was drugs related" if int(drugs_related_stop) else "was not drug related"
        pronoun="he" if driver_gender=="male" else "she"
        
        st.markdown(f"""
        🚗 A {driver_age}-year-old {driver_gender} driver was stopped for **{violation}** at **{stop_time.strftime('%I:%M %p')}**.  
        {searching}, and {pronoun} received a **{stop_outcome}**.  
        The stop lasted **{stop_duration}** and {drug_txt}.
        """)

 
         