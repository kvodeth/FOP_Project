import matplotlib.pyplot as plt

# Setting labels for items in Chart
Employee = ['Roshni', 'Shyam', 'Priyanshi',
            'Harshit', 'Anmol']
Employee1 = ['Matt', "Ashley", "Travis", 'Laura', 'Ashley']


# Setting size in Chart based on
# given values
Salary = [40000, 50000, 70000, 54000, 44000]
Salary1 = [40000, 50000, 70000, 54000, 44000]

# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
          '#ADFF2F', '#FFA500']
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(
    10, 10))  # ax1,ax2 refer to your two pies
# Pie Chart
ax1.pie(Salary, colors=colors, labels=Employee,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
ax1.set_title('Gender Composition in 2016')
ax2.pie(Salary1, colors=colors, labels=Employee1,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
ax2.set_title('Gender Composition in 2016')


# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

# Displaying Chart
plt.show()
