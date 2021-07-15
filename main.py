from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import json

# Doan ma khoi tao server
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>hello !<h1>'

# Khai bao ham xu ly request trainning
@app.route('/genetic-algorithm', methods=['GET'])
@cross_origin()
def Genetic_Algorithm():
# xử lý tại đây
    

       
#tạo dữ liệu mẫu để test
    list = []
    list.append( SimulationResult('Home 1',  8.523, 8.178, 8.070, 7.814, 7.885, 7.922))
    list.append( SimulationResult('Home 2',  7.949, 5.999, 5.844, 5.831, 6.075, 5.893 ))
    list.append( SimulationResult('Home 3', 8.054, 6.354, 6.340, 6.395, 6.311, 6.501  ))
    list.append( SimulationResult('Home 4', 10.864, 7.130, 7.196, 7.021, 7.153, 7.162 ))
    list.append( SimulationResult('Home 5',  7.173, 6.266, 6.107, 6.141, 6.095, 6.193 ))
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;

class SimulationResult: 
    def __init__(self,home, survey,ind_1,ind_2,ind_3,ind_4,ind_5): 
        self.home = home 
        self.survey = survey
        self.ind_1 = ind_1
        self.ind_2 = ind_2
        self.ind_3 = ind_3
        self.ind_4 = ind_4
        self.ind_5 = ind_5


# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True)
    