import pandas as pd
import seaborn as sns

from tqdm import tqdm
data= pd.read_csv("train.csv")


import seaborn as sns
import matplotlib.pyplot as plt


plt.scatter(data['Age'], data['Balance'])
plt.xlabel('Age')
plt.ylabel('Balance')
plt.savefig('outliers.png')
plt.close()


data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Gender', hue='Exited', palette='Set2')


plt.xticks(ticks=[0, 1], labels=['Female', 'Male'])  
plt.title('Exit Status by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Exited', loc='upper right')
plt.savefig('gender.png')
plt.close()

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='Exited', y='Age', palette='Set2')

plt.xticks(ticks=[0, 1], labels=['Not Exited', 'Exited'])
plt.title('Age Distribution by Exit Status')
plt.xlabel('Exit Status')
plt.ylabel('Age')


plt.savefig('age.png')
plt.close()


plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='IsActiveMember', hue='Exited', palette='Set2')

plt.xticks(ticks=[0, 1], labels=['Inactive', 'Active']) 
plt.title('Exit Status by Membership Activity')
plt.xlabel('Is Active Member')
plt.ylabel('Count')
plt.legend(title='Exited', loc='upper right')

plt.savefig('isactive.png')
plt.close()


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='Exited', y='CreditScore', palette='Set2')

plt.xticks(ticks=[0, 1], labels=['Not Exited', 'Exited'])  
plt.title('Credit Score Distribution by Exit Status')
plt.xlabel('Exit Status')
plt.ylabel('Credit Score')

plt.savefig('creditscore.png')




import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='Exited', y='Tenure', palette='Set2')

plt.xticks(ticks=[0, 1], labels=['Not Exited', 'Exited'])  
plt.title('Tenure Distribution by Exit Status')
plt.xlabel('Exit Status')
plt.ylabel('Tenure (Years)')

plt.savefig('tenure.png')

