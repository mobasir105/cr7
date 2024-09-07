import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import io

plt.style.use('ggplot')

st.set_page_config(page_title="UR CRISTIAND RONALDO",layout='wide')
st.sidebar.title("📈 UR CRISTIAND Analytics ")
st.sidebar.image("cr71.png",use_column_width=True)

sections =["Introduction", 
"Basic Exploration", 
"Goals per Competition", 
"Goals per Season", 
"Goals per Club", 
"Goals per Playing Position", 
"Goals per Game Minute", 
"Goals per Type", 
"Scoreline After Goals",
"Opponents", 
"Favorite Opponents", 
"Assists", 
"Goals per Venue"
]
Selections = st.sidebar.radio("Navigate ", sections)

def load_data():
    df = pd.read_csv('data.csv')
    return df
df = load_data()

if Selections == 'Introduction':
    st.title("⚽ cr7 extensive eda and analytics")
    st.subheader(" Life and Career:")
    st.image("cr71.png")

    # st.write("""
    # **Cristiano Ronaldo dos Santos Aveiro** is a Portuguese professional footballer who plays as a forward for Al-Nassr and captains the Portugal national team.
    
    # - **Current team**: Al-Nassr (#7 / Forward)
    # - **Born**: February 5, 1985 (age 39 years), Funchal, Portugal
    # - **Height**: 1.87 m
    # - **Partner**: Georgina Rodríguez (2017–)
    # - **Salary**: 26.52 million GBP (2022)
    # - **Children**: Cristiano Ronaldo Jr., Alana Martina, Eva Maria, Mateo Ronaldo
    # """)

    st.write('''


### Early Life and Career:
- **Born:** February 5, 1985, in Funchal, Madeira, Portugal.
- **Youth Career:** Ronaldo started playing football at a young age, joining local teams like Andorinha and Nacional before moving to the prestigious Sporting CP academy.
  
### Club Career Highlights:
1. **Sporting CP:** Ronaldo’s performances at Sporting CP attracted the attention of major European clubs.
   
2. **Manchester United (2003-2009):**  
   - He signed with Manchester United in 2003, where he won his first **Ballon d'Or** in 2008.
   - Ronaldo was instrumental in helping Manchester United win multiple **Premier League titles** and the **UEFA Champions League** in 2008.
  
3. **Real Madrid (2009-2018):**  
   - Ronaldo's move to Real Madrid for a then-world record fee of €94 million in 2009 was a turning point.
   - At Real, Ronaldo became the club's all-time top scorer, netting over 450 goals.
   - He won **four Champions League titles** with Real Madrid and multiple **La Liga** titles.
   - During this period, Ronaldo won four additional **Ballon d'Or awards**, bringing his total to five.
  
4. **Juventus (2018-2021):**
   - Ronaldo transferred to Juventus in 2018, winning two **Serie A** titles and continuing to perform at the highest level.

5. **Manchester United Return (2021-2022):**
   - Ronaldo returned to Manchester United for a second spell in 2021, adding more goals to his career tally but amid team struggles.

6. **Al-Nassr (2023-Present):**  
   - Ronaldo signed with Saudi Arabian club Al-Nassr in a high-profile move, making him one of the highest-paid athletes in the world.

### International Career:
- **Portugal National Team:**
   - Ronaldo has been the captain of the Portuguese national team for several years.
   - He led Portugal to victory in the **UEFA Euro 2016**, their first major international trophy.
   - Ronaldo also helped Portugal win the **UEFA Nations League** in 2019.
   - He is Portugal's all-time top scorer and one of the highest goal-scorers in international football history.

### Playing Style and Achievements:
- **Position:** Forward/Winger.
- **Strengths:** Known for his speed, strength, heading ability, and powerful shooting, Ronaldo is an elite finisher.
- **Goal-scoring:** Ronaldo is one of the highest goal-scorers in football history, with over 800 career goals for club and country.
- **Records:**
   - Most goals in the UEFA Champions League.
   - First player to score in five different World Cup tournaments.
   - All-time top scorer for Real Madrid and Portugal.

### Personal Life:
- **Partner:** Georgina Rodríguez, with whom he has several children, including **Cristiano Ronaldo Jr.** (born in 2010), **Alana Martina** (born in 2017), and twins **Eva Maria** and **Mateo** (born in 2017 via surrogacy).
- **Philanthropy:** Ronaldo is known for his charitable work, including donations to hospitals, children's charities, and his regular contributions to causes in his home country.

### Legacy:
Ronaldo's relentless work ethic, combined with his natural talent, has made him a global icon. He has continuously pushed the limits of football, setting records and winning titles at every level. His rivalry with Lionel Messi has defined a footballing generation, with debates often centered around who is the greatest of all time.

       

 ''')


elif Selections =='Basic Exploration':
    st.subheader("Basic Exploration")
    st.write("#### Data Snapshot")
    st.dataframe(df.head())

# <class 'pandas.core.frame.DataFrame'>
    # st.write("## info")
    # buffer = io.StringIO()
    # df.info(buf = buffer)
    # s= buffer.getvalue()
    # st.text(s)


    st.write("### Describe")
    st.dataframe(df.describe())

    # st.dataframe(df['Type'].unique())
    


elif Selections == "Goals per Competition":
    st.subheader("🏆 Goals per Competition")
    fig = px.histogram(df, x = 'Competition', color='Club', title = "Goals per Competition", height=500,        hover_name = "Club", hover_data=['Competition', 'Club'])
    st.plotly_chart(fig)
    st.write("### Competition Goal Counts")
    st.dataframe(df.Competition.value_counts())


elif Selections == "Goals per Season":
    st.subheader("📅 Goals per Season")
    fig = px.histogram(df, x = 'Season', color='Club', title = "Goals per Season", 
                 height=500,hover_name = "Club", hover_data=['Season', 'Club'])
    st.plotly_chart(fig)


elif Selections == "Goals per Club":
    st.subheader("🏅 Goals per Club")
    fig1 = px.histogram(df, x = 'Club', color='Season', title = "Goals per Club - Season", 
                 height=500,hover_name = "Season", hover_data=['Competition', 'Season', 'Club'])
    fig2 = px.histogram(df, x = 'Club', color='Competition', title = "Goals per Club - Competition", 
                 height=500,hover_name = "Competition", hover_data=['Competition', 'Season', 'Club'])
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)    

elif Selections == "Goals per Playing Position":
    st.subheader("⚽ Goals per Playing Position")
    fig = px.histogram(df, x = 'Playing_Position', color='Club', title = "Goals per Playing Position", 
                 height=500,hover_name = "Club", hover_data=['Playing_Position','Competition', 'Season', 'Club'])
    st.plotly_chart(fig)

elif Selections == "Goals per Game Minute":
    st.subheader("⏰ Goals per Game Minute")
    df['Minute'] = df['Minute'].str.extract('(\d+)', expand=False).fillna(0).astype(int)
    bins = [0,15,30,45,60,75,90,105,120]
    labels = ['0-15', '15-30', '30-45', '45-60','60-75', '75-90', '90-105','105-120']
    df['Minute_Bin'] = pd.cut(df['Minute'], bins = bins, labels=labels, right=False)
    fig = px.histogram(df, x = 'Minute_Bin', title = "Goals per Game Minute", color = 'Club', height=500)
    st.plotly_chart(fig)


elif Selections == "Goals per Type":
    st.subheader("🏹 Goals per Type")
    fig = px.histogram(df, x = 'Type', title = "Goals per Typee", color = 'Club', height=500)
    st.plotly_chart(fig)

elif Selections == "Scoreline After Goals":
    st.subheader("🔢 Scoreline After Goals")
    top_20_scores = df['At_score'].value_counts().nlargest(20).index
    df_top_20 = df[df['At_score'].isin(top_20_scores)]

    fig, ax = plt.subplots(figsize=(15,7))
    sns.countplot(x='At_score', data=df_top_20, order = top_20_scores, ax = ax)
    ax.set_title("Top 20 Scoresheets after Scoring", fontsize = 20)
    st.pyplot(fig)

elif Selections == "Opponents":
    st.subheader("🆚 Opponents")
    top_20_opponent = df['Opponent'].value_counts().nlargest(20).index
    df_top_20 = df[df['Opponent'].isin  (top_20_opponent)]
    fig, ax = plt.subplots(figsize=(30,10))
    sns.countplot(x='Opponent', data = df_top_20, order = top_20_opponent, ax=ax)
    ax.set_title("Goal per Opponents", fontsize = 20)
    st.pyplot(fig)

elif Selections == "Favorite Opponents":
    st.subheader("❤️ Favorite Opponents", )
    fig, ax = plt.subplots(figsize=(15,7))
    fav_opponents_df = df['Opponent'].value_counts()[df['Opponent'].value_counts()>15]
    sns.countplot(x='Opponent', data = df[df['Opponent'].isin(fav_opponents_df.index)], order = fav_opponents_df.index, ax=ax)
    ax.set_title("Favorite Opponents", fontsize = 20)
    st.pyplot(fig)

elif Selections == "Assists":
    st.subheader("🤝 Assists")

    top_10_assist = df['Goal_assist'].value_counts().nlargest(10).index

    df_top_10 = df[df['Goal_assist'].isin(top_10_assist)]

    fig, ax = plt.subplots(figsize=(15,7))

    sns.countplot(x = 'Goal_assist', data = df_top_10, order = top_10_assist, ax = ax)

    ax.set_title("Top 10 Assists", fontsize = 20)

    st.pyplot(fig)

elif Selections == "Goals per Venue":
    st.subheader("🏟️ Goals per Venue")
    fig, ax = plt.subplots(figsize = (15,7))
    sns.countplot(x = 'Venue', data = df, order = df['Venue'].value_counts().index, ax = ax)
    ax.set_title("Goal Per Venue", fontsize = 20)
    st.pyplot(fig)