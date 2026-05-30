import numpy as np
from sklearn.linear_model
import LinearRegression
Import matplotlib.pyplot as plt

#Sample data:Area (Sq ft), Price(K Kes)
X = np.array([[1000],[1500],[2000],[2500],[3000]]) #Area
y = np.array([5,7,10,12,15] #Price (M Kes)

             #Train Model
             model = LinearRegression()
             model.fit(x,y)

             #Predict price for 2200 sq ft
             area = np.array([[2200]])
             predicted_price = model.predict(area)
             print(f"Predicted price : {predicted_price[0]:.2f} M Kes")

             #Plot
             plt.scatter(x,y)
             plt.plot(x, model.predict(x), color='red')
             plt.show()
