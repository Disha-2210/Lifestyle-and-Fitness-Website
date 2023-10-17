# https://youtu.be/bluclMxiUkA
"""
Application that predicts heart disease percentage in the population of a town
based on the number of bikers and smokers. 

Trained on the data set of percentage of people biking 
to work each day, the percentage of people smoking, and the percentage of 
people with heart disease in an imaginary sample of 500 towns.

"""
from pandas import *
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from flask import Flask, request, render_template
import pickle

#import seaborn as sns
#import numpy as np

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('D:/empower_hub/fitness_webapp/models/model.pkl', 'rb'))

#Define the route to be home. 
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory. 
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder. 

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]
    output = round(prediction[0], 2)
    #data = read_csv("heart_data.csv")
    # Your model training code here
    # For demonstration, let's create a simple example
    x = [30.80124571,65.12921517,1.959664531,44.80019562,69.42845368,54.40362555,49.05616196,4.784604202,65.7307883,35.25744894]
    y = [11.76942278,2.854081478,17.17780348,6.816646909,4.062223522,9.550045997,7.62450698,15.85465443,3.06746173,12.09848437]
   # x = data['biking'].tolist()
   # y = data['smoking'].tolist()

    # Create the Matplotlib graph
    plt.plot(x, y)
    plt.xlabel('biking')
    plt.ylabel('heart disease')
    plt.title('Sample Training Plot')
    
    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the bytes buffer to a base64 encoded string
    plot_data = base64.b64encode(buffer.getvalue()).decode()

   # return render_template('index.html', plot_data=plot_data)
  

    

    return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output), plot_data=plot_data)


#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()