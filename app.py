# from flask import Flask, render_template, request
# from datetime import datetime as dt
# import pickle

# # Load the pickle model
# model = pickle.load(open("models/model_rf.pkl","rb"))

# # Constants for scaling
# MEAN_TOTAL_VOLUME = 850644.0130089321
# STD_TOTAL_VOLUME = 3453545.3553994815
# MEAN_TOTAL_BAGS = 239639.20205983886
# STD_TOTAL_BAGS = 986242.3992164129
# MEAN_SMALL_BAGS = 182194.68669570936
# STD_SMALL_BAGS = 746178.5149617859

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form data
#         date = request.form.get('date')
#         total_volume = float(request.form.get('total_volume'))
#         total_bag = float(request.form.get('total_bag'))
#         small_bags = float(request.form.get('small_bags'))
#         large_bags = float(request.form.get('large_bags', 0))  # Default to 0 if missing
#         xlarge_bags = float(request.form.get('xlarge_bags', 0))  # Default to 0 if missing
#         type = request.form.get('type')
#         region = request.form.get('region')

#         # Add prefix to region and convert to lowercase
#         region_key = "region_" + region.lower() if region else None

#         # Scale numerical features
#         scaled_total_volume = (total_volume - MEAN_TOTAL_VOLUME) / STD_TOTAL_VOLUME
#         scaled_total_bag = (total_bag - MEAN_TOTAL_BAGS) / STD_TOTAL_BAGS
#         scaled_small_bags = (small_bags - MEAN_SMALL_BAGS) / STD_SMALL_BAGS

#         # Extract date features
#         date_obj = dt.strptime(date, '%Y-%m-%d')
#         month = date_obj.month
#         quarter = (month - 1) // 3 + 1  # Calculate quarter
#         year = date_obj.year

#         regions = [
#             'region_atlanta', 'region_baltimorewashington', 'region_boise',
#             'region_boston', 'region_buffalorochester', 'region_california',
#             'region_charlotte', 'region_chicago', 'region_cincinnatidayton',
#             'region_columbus', 'region_dallasftworth', 'region_denver',
#             'region_detroit', 'region_grandrapids', 'region_greatlakes',
#             'region_harrisburgscranton', 'region_hartfordspringfield',
#             'region_houston', 'region_indianapolis', 'region_jacksonville',
#             'region_lasvegas', 'region_losangeles', 'region_louisville',
#             'region_miamiftlauderdale', 'region_midsouth', 'region_nashville',
#             'region_neworleansmobile', 'region_newyork', 'region_northeast',
#             'region_northernnewengland', 'region_orlando', 'region_philadelphia',
#             'region_phoenixtucson', 'region_pittsburgh', 'region_plains',
#             'region_portland', 'region_raleighgreensboro', 'region_richmondnorfolk',
#             'region_roanoke', 'region_sacramento', 'region_sandiego',
#             'region_sanfrancisco', 'region_seattle', 'region_southcarolina',
#             'region_southcentral', 'region_southeast', 'region_spokane',
#             'region_stlouis', 'region_syracuse', 'region_tampa', 'region_totalus',
#             'region_west', 'region_westtexnewmexico'
#         ]

#         # Set the selected region to True in the dictionary
#         region_dict = {region: False for region in regions}  
#         if region_key and region_key in region_dict: 
#             region_dict[region_key] = True  

#         features = [scaled_total_volume,scaled_total_bag,scaled_small_bags,large_bags,xlarge_bags,type,year,month,quarter]

#         # Your initial list of features


#         features.extend(regions.values())

#         return render_template(
#             "index.html",
#             # date=date,
#             # total_volume=total_volume,
#             # total_bag=total_bag,
#             # small_bags=small_bags,
#             # large_bags=large_bags,
#             # xlarge_bags=xlarge_bags,
#             # type=type,
#             # region=region_key,
#             # scaled_total_volume=scaled_total_volume,
#             # scaled_total_bag=scaled_total_bag,
#             # scaled_small_bags=scaled_small_bags,
#             # month=month,
#             # quarter=quarter,
#             # year=year,
#             # region_dict=region_dict
#             features=features
#         )  
#     except Exception as e:
#         return render_template("index.html", error=str(e))

# if __name__ == "__main__":
#     app.run(debug=True)






# from flask import Flask, render_template, request
# import numpy as np
# from datetime import datetime as dt
# import pickle

# # Load the pickle model
# model = pickle.load(open("models/model_rf.pkl", "rb"))

# # Constants for scaling
# MEAN_TOTAL_VOLUME = 850644.0130089321
# STD_TOTAL_VOLUME = 3453545.3553994815
# MEAN_TOTAL_BAGS = 239639.20205983886
# STD_TOTAL_BAGS = 986242.3992164129
# MEAN_SMALL_BAGS = 182194.68669570936
# STD_SMALL_BAGS = 746178.5149617859

# app = Flask(__name__)


# @app.route('/')
# def main_page():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form data
#         date = request.form.get('date')
#         total_volume = float(request.form.get('total_volume'))
#         total_bag = float(request.form.get('total_bag'))
#         small_bags = float(request.form.get('small_bags'))
#         large_bags = float(request.form.get('large_bags', 0))  # Default to 0 if missing
#         xlarge_bags = float(request.form.get('xlarge_bags', 0))  # Default to 0 if missing
#         type = request.form.get('type')
#         region = request.form.get('region')

#         # Add prefix to region and convert to lowercase
#         region_key = "region_" + region.lower() if region else None

#         # Scale numerical features
#         scaled_total_volume = (total_volume - MEAN_TOTAL_VOLUME) / STD_TOTAL_VOLUME
#         scaled_total_bag = (total_bag - MEAN_TOTAL_BAGS) / STD_TOTAL_BAGS
#         scaled_small_bags = (small_bags - MEAN_SMALL_BAGS) / STD_SMALL_BAGS

#         # Extract date features
#         date_obj = dt.strptime(date, '%Y-%m-%d')
#         month = date_obj.month
#         quarter = (month - 1) // 3 + 1  # Calculate quarter
#         year = date_obj.year

#         regions = [
#             'region_atlanta', 'region_baltimorewashington', 'region_boise',
#             'region_boston', 'region_buffalorochester', 'region_california',
#             'region_charlotte', 'region_chicago', 'region_cincinnatidayton',
#             'region_columbus', 'region_dallasftworth', 'region_denver',
#             'region_detroit', 'region_grandrapids', 'region_greatlakes',
#             'region_harrisburgscranton', 'region_hartfordspringfield',
#             'region_houston', 'region_indianapolis', 'region_jacksonville',
#             'region_lasvegas', 'region_losangeles', 'region_louisville',
#             'region_miamiftlauderdale', 'region_midsouth', 'region_nashville',
#             'region_neworleansmobile', 'region_newyork', 'region_northeast',
#             'region_northernnewengland', 'region_orlando', 'region_philadelphia',
#             'region_phoenixtucson', 'region_pittsburgh', 'region_plains',
#             'region_portland', 'region_raleighgreensboro', 'region_richmondnorfolk',
#             'region_roanoke', 'region_sacramento', 'region_sandiego',
#             'region_sanfrancisco', 'region_seattle', 'region_southcarolina',
#             'region_southcentral', 'region_southeast', 'region_spokane',
#             'region_stlouis', 'region_syracuse', 'region_tampa', 'region_totalus',
#             'region_west', 'region_westtexnewmexico'
#         ]

#         # Set the selected region to True in the dictionary
#         region_dict = {region: False for region in regions}  
#         if region_key and region_key in region_dict: 
#             region_dict[region_key] = True  

#         # Create the features list
#         features = [scaled_total_volume, scaled_total_bag, scaled_small_bags, large_bags, xlarge_bags, type, year, month, quarter]

#         ft = [np.array(features)]
#         prediction = model.predict(ft)

        
#         features.extend(region_dict.values())

#         return render_template(
#             "index.html",
#             prediction=prediction
#         )  
#     except Exception as e:
#         return render_template("index.html", error=str(e))

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import numpy as np
# from datetime import datetime as dt
# import pickle

# # Load the pickle model
# model = pickle.load(open("models/model_rf.pkl", "rb"))

# # Constants for scaling
# MEAN_TOTAL_VOLUME = 850644.0130089321
# STD_TOTAL_VOLUME = 3453545.3553994815
# MEAN_TOTAL_BAGS = 239639.20205983886
# STD_TOTAL_BAGS = 986242.3992164129
# MEAN_SMALL_BAGS = 182194.68669570936
# STD_SMALL_BAGS = 746178.5149617859

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form data
#         date = request.form.get('date')
#         total_volume = float(request.form.get('total_volume'))
#         total_bag = float(request.form.get('total_bag'))
#         small_bags = float(request.form.get('small_bags'))
#         large_bags = float(request.form.get('large_bags', 0))  # Default to 0 if missing
#         xlarge_bags = float(request.form.get('xlarge_bags', 0))  # Default to 0 if missing
#         type = request.form.get('type')  # "Conventional" or "Organic"
#         region = request.form.get('region')

#         # Add prefix to region and convert to lowercase
#         region_key = "region_" + region.lower() if region else None

#         # Scale numerical features
#         scaled_total_volume = (total_volume - MEAN_TOTAL_VOLUME) / STD_TOTAL_VOLUME
#         scaled_total_bag = (total_bag - MEAN_TOTAL_BAGS) / STD_TOTAL_BAGS
#         scaled_small_bags = (small_bags - MEAN_SMALL_BAGS) / STD_SMALL_BAGS

#         # Extract date features
#         date_obj = dt.strptime(date, '%Y-%m-%d')
#         month = date_obj.month
#         quarter = (month - 1) // 3 + 1  # Calculate quarter
#         year = date_obj.year

#         regions = [
#             # 'region_albany',
#             'region_atlanta', 'region_baltimorewashington', 'region_boise',
#             'region_boston', 'region_buffalorochester', 'region_california',
#             'region_charlotte', 'region_chicago', 'region_cincinnatidayton',
#             'region_columbus', 'region_dallasftworth', 'region_denver',
#             'region_detroit', 'region_grandrapids', 'region_greatlakes',
#             'region_harrisburgscranton', 'region_hartfordspringfield',
#             'region_houston', 'region_indianapolis', 'region_jacksonville',
#             'region_lasvegas', 'region_losangeles', 'region_louisville',
#             'region_miamiftlauderdale', 'region_midsouth', 'region_nashville',
#             'region_neworleansmobile', 'region_newyork', 'region_northeast',
#             'region_northernnewengland', 'region_orlando', 'region_philadelphia',
#             'region_phoenixtucson', 'region_pittsburgh', 'region_plains',
#             'region_portland', 'region_raleighgreensboro', 'region_richmondnorfolk',
#             'region_roanoke', 'region_sacramento', 'region_sandiego',
#             'region_sanfrancisco', 'region_seattle', 'region_southcarolina',
#             'region_southcentral', 'region_southeast', 'region_spokane',
#             'region_stlouis', 'region_syracuse', 'region_tampa', 'region_totalus',
#             'region_west', 'region_westtexnewmexico'
#         ]

#         # Set the selected region to True in the dictionary
#         region_dict = {region: 0 for region in regions}  # Default all to 0
#         if region_key and region_key in region_dict:
#             region_dict[region_key] = 1  # Set the selected region to 1

#         if(type=="conventional"):
#             type = 0
#         else:
#             type = 1

#         # Create the feature list
#         features = [scaled_total_volume, scaled_total_bag, scaled_small_bags, large_bags, xlarge_bags, type, year, month, quarter]
#         features.extend(region_dict.values())
        

#         # Predict the result
#         prediction = model.predict([features])  # Ensure features is in the right shape
#         price = round(prediction[0],2)
#         return render_template(
#             "index.html",
#             Date=date_obj,
#             price = price  # Assuming the model returns a 1D array or scalar
#         )

#     except Exception as e:
#         return render_template("index.html", error=str(e))

# if __name__ == "__main__":
#     app.run(debug=True)








from flask import Flask, render_template, request
import numpy as np
from datetime import datetime as dt
import pickle

# Load the pickle model
model = pickle.load(open("models/model_rf.pkl", "rb"))

# Constants for scaling
MEAN_TOTAL_VOLUME = 850644.0130089321
STD_TOTAL_VOLUME = 3453545.3553994815
MEAN_TOTAL_BAGS = 239639.20205983886
STD_TOTAL_BAGS = 986242.3992164129
MEAN_SMALL_BAGS = 182194.68669570936
STD_SMALL_BAGS = 746178.5149617859

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        date = request.form.get('date')
        total_volume = float(request.form.get('total_volume'))
        total_bag = float(request.form.get('total_bag'))
        small_bags = float(request.form.get('small_bags'))
        large_bags = float(request.form.get('large_bags', 0))  # Default to 0 if missing
        xlarge_bags = float(request.form.get('xlarge_bags', 0))  # Default to 0 if missing
        type = request.form.get('type')  # "Conventional" or "Organic"
        region = request.form.get('region')

        # Add prefix to region and convert to lowercase
        region_key = "region_" + region.lower() if region else None

        # Scale numerical features
        scaled_total_volume = (total_volume - MEAN_TOTAL_VOLUME) / STD_TOTAL_VOLUME
        scaled_total_bag = (total_bag - MEAN_TOTAL_BAGS) / STD_TOTAL_BAGS
        scaled_small_bags = (small_bags - MEAN_SMALL_BAGS) / STD_SMALL_BAGS

        # Extract date features
        date_obj = dt.strptime(date, '%Y-%m-%d')
        month = date_obj.month
        quarter = (month - 1) // 3 + 1  # Calculate quarter
        year = date_obj.year

        # List of possible regions
        regions = [
            'region_atlanta', 'region_baltimorewashington', 'region_boise',
            'region_boston', 'region_buffalorochester', 'region_california',
            'region_charlotte', 'region_chicago', 'region_cincinnatidayton',
            'region_columbus', 'region_dallasftworth', 'region_denver',
            'region_detroit', 'region_grandrapids', 'region_greatlakes',
            'region_harrisburgscranton', 'region_hartfordspringfield',
            'region_houston', 'region_indianapolis', 'region_jacksonville',
            'region_lasvegas', 'region_losangeles', 'region_louisville',
            'region_miamiftlauderdale', 'region_midsouth', 'region_nashville',
            'region_neworleansmobile', 'region_newyork', 'region_northeast',
            'region_northernnewengland', 'region_orlando', 'region_philadelphia',
            'region_phoenixtucson', 'region_pittsburgh', 'region_plains',
            'region_portland', 'region_raleighgreensboro', 'region_richmondnorfolk',
            'region_roanoke', 'region_sacramento', 'region_sandiego',
            'region_sanfrancisco', 'region_seattle', 'region_southcarolina',
            'region_southcentral', 'region_southeast', 'region_spokane',
            'region_stlouis', 'region_syracuse', 'region_tampa', 'region_totalus',
            'region_west', 'region_westtexnewmexico'
        ]

        # Set the selected region to True in the dictionary
        region_dict = {region: 0 for region in regions}  # Default all to 0
        if region_key and region_key in region_dict:
            region_dict[region_key] = 1  # Set the selected region to 1

        if type == "conventional":
            type = 0
        else:
            type = 1

        # Create the feature list
        features = [scaled_total_volume, scaled_total_bag, scaled_small_bags, large_bags, xlarge_bags, type, year, month, quarter]
        features.extend(region_dict.values())

        # Predict the result
        prediction = model.predict([features])  # Ensure features is in the right shape
        
        # Make sure the prediction is correctly handled (ensure it's numeric)
        price = round(prediction[0], 2)  # Round the first prediction value to 2 decimal places
        
        # Return the result to the user
        return render_template(
            "index.html",
            Date=date_obj,
            price=price  # Pass the rounded price for display
        )

    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)










## from flask import Flask, render_template
## from flask_sqlalchemy import SQLAlchemy
#from flask import Flask, render_template
## from flask_sqlalchemy import SQLAlchemy
## from datetime import datetime
#
#app = Flask(__name__)
#
## app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avacado.db'
#
## app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#
## db = SQLAlchemy(app)
#
#
## class Avocado(db.Model):
##     sno = db.Column(db.Integer, primary_key=True, autoincrement=True)  # autoincrement
##     Date = db.Column(db.DateTime)
##     Total_Volume = db.Column(db.Float)
##     Total_Bags = db.Column(db.Float)
##     Small_bags = db.Column(db.Float)
##     Large_bags = db.Column(db.Float)
##     X_Large_bags = db.Column(db.Float)
##     Type = db.Column(db.String(25))
##     Region = db.Column(db.String(25))
#
#     
#
#@app.route('/')# ,methods=['GET','POST']
#def main_page():
#    # date_obj = datetime.strptime("12/11/2012", "%d/%m/%Y")
#    # Avocado_check = Avocado(Date=date_obj,
#    #                         Total_Volume = 45,
#    #                         Total_Bags = 345,
#    #                         Small_bags = 123,
#    #                         Large_bags = 234,
#    #                         X_Large_bags = 543,
#    #                         Type = "Conventional",
#    #                         Region = "New York")
#    # db.session.add(Avocado_check)
#    # db.session.commit()
#    return render_template('index.html')
#
#@app.route('/predict',methods=['POST'])
#def predict():
#    return render_template("index.html")
#
#if __name__=="__main__":
#    app.run(debug=True)
#