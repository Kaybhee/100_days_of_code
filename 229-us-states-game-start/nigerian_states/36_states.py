import pandas as pd
dat_dic = {
    "states":["Abia","Adamawa", "Akwa Ibom", "Anambra","Bauchi","Bayelsa","Benue", "Borno", "Cross river", "Delta","Ebonyi","Edo","Ekiti", "Enugu", "Gombe","Imo", "Jigawa","Kaduna", "Kano", "Kastina","Kebbi", "Kogi","Kwara","Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo","Plateau","Rivers", "Sokoto","Taraba", "Yobe","Zamfara"],
        "X":  [-54.0, 194.0, -35.0, -92.0, 92.0, -138.0,0.0,235.0,-2.0,-135.0,-36.0,-138.0,-175.0,-68.0,128,-86.0,42.0,-48.0,-11.0,-60.0,-235.0,-102.0,-151.0,-279.0,-30.0,-156.0,-282,-201,-212,-265,43,-96,-174,102,140,-127],
        "Y":  [-181.0, 23.0, -224.0, -153.0, 82.0, -223.0,-88.0,151.0,-162.0,-186.0,-144.0,-124.0,-72.0,-134.0,77,-189.0,167.0,74.0,140.0,179,152.0,-72.0,37.0,-138.0,-29.0,48.0,-114,-128,-84,-48,2,-218,218,-58,175,160]
}
df = pd.DataFrame(dat_dic)
df.to_csv(r"C:\Users\intern2\Videos\100_days_of_code\229-us-states-game-start")
print(df)
