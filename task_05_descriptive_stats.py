import pandas as pd
import matplotlib.pyplot as plt


player_data = {
    "Player": ["Emma Tyrrell", "Olivia Adamson", "Emma Ward", "Natalie Smith", "Payton Rowley",
               "Maddy Baxter", "Savannah Sweitzer", "Emma Muchnick", "Joely Caramelli",
               "Gracie Britton", "Meghan Rode", "Kaci Benoit", "Katie Goodale",
               "Mackenzie Rich", "Coco Vandiver", "Ryann Banks", "Katelyn Mashewske",
               "Bianca Chevarie", "Carlie Desimone", "Lauren Call", "Tate Paulson",
               "Evan Johnston", "Chloe Bethea-Jones", "Gwenna Gentle", "Izzy Lahah",
               "Ella Blesi", "Faith Wooters", "Julia Basciano", "Ana Horvit"],
    "G":  [70, 58, 44, 44, 23, 30, 24, 14, 11, 7, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "A":  [22, 25, 37, 10, 15, 6, 9, 13, 3, 4, 1, 0, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "GB": [21, 12, 10, 11, 5, 14, 8, 15, 10, 1, 3, 2, 43, 4, 19, 0, 12, 40, 2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    "DC": [6, 6, 0, 36, 0, 14, 0, 20, 1, 0, 0, 0, 47, 0, 2, 0, 23, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df_players = pd.DataFrame(player_data)
df_players["PTS"] = df_players["G"] + df_players["A"]


schedule_data = {
    "Date": ["Feb 10","Feb 14","Feb 17","Feb 24","Mar 02","Mar 05","Mar 09","Mar 16","Mar 19","Mar 23",
             "Mar 27","Mar 30","Apr 02","Apr 06","Apr 13","Apr 18","Apr 23","Apr 26","Apr 28","May 12",
             "May 16","May 24"],
    "Opponent": ["#1 Northwestern","Army","#9 Maryland","#2 Notre Dame","Duke","Stony Brook","Virginia Tech",
                 "#9 North Carolina","UAlbany","#9 Virginia","#7 Loyola","Louisville","Cornell","Pittsburgh",
                 "Clemson","#6 Boston College","Louisville","#6 Virginia","Boston College","#14 Stony Brook",
                 "#6 Yale","Boston College"],
    "Result": ["L","W","Lot","W","W","Lot","W","W","W","W","W","W","W","W","W","Lot","W","W","L","W","W","L"],
    "Score": ["15-18","18-7","8-9","16-14","15-8","12-13","15-5","20-5","20-11","15-14","16-13","22-12",
              "17-4","16-7","15-6","10-11","17-8","19-4","8-15","15-10","19-9","7-10"],
    "Attendance": [933,1077,2097,482,1976,1264,178,2982,1062,871,1238,1902,86,1350,1067,4337,268,0,1049,1052,887,4308]
}

df_schedule = pd.DataFrame(schedule_data)
df_schedule[["Goals_For", "Goals_Against"]] = df_schedule["Score"].str.split("-", expand=True).astype(int)



# Top 5 Goal Scorers
top5_scorers = df_players.nlargest(5, "G")
plt.figure(figsize=(8, 5))
plt.bar(top5_scorers["Player"], top5_scorers["G"], color="skyblue")
plt.title("Top 5 Goal Scorers (2024)")
plt.xlabel("Player")
plt.ylabel("Goals")
plt.xticks(rotation=30, ha="right")
for i, v in enumerate(top5_scorers["G"]):
    plt.text(i, v + 1, str(v), ha="center")
plt.show()

# Team Totals
team_totals = {
    "Goals": df_players["G"].sum(),
    "Assists": df_players["A"].sum(),
    "Points": df_players["PTS"].sum(),
    "Ground Balls": df_players["GB"].sum(),
    "Draw Controls": df_players["DC"].sum()
}

plt.figure(figsize=(8, 5))
plt.bar(team_totals.keys(), team_totals.values(), color=["skyblue", "purple", "green", "orange", "red"])
plt.title("Team Totals (2024)")
plt.ylabel("Total")
for i, v in enumerate(team_totals.values()):
    plt.text(i, v + 3, str(v), ha="center")
plt.show()

# Goals For vs Goals Against
plt.figure(figsize=(12, 6))
plt.plot(df_schedule["Date"], df_schedule["Goals_For"], label="Goals For", marker="o")
plt.plot(df_schedule["Date"], df_schedule["Goals_Against"], label="Goals Against", marker="x")
plt.xticks(rotation=45)
plt.title("Goals For vs Goals Against (Game by Game)")
plt.xlabel("Game Date")
plt.ylabel("Goals")
plt.legend()
plt.grid(alpha=0.5)
plt.show()

# Attendance Trend
plt.figure(figsize=(12, 6))
plt.plot(df_schedule["Date"], df_schedule["Attendance"], color="green", marker="o")
plt.title("Attendance Trend (2024)")
plt.xlabel("Game Date")
plt.ylabel("Attendance")
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.show()
