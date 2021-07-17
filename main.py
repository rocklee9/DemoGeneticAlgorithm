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
    list.append( SimulationResult('Home 1',  85.590, 1.894, 86.490, 1.894, 86.757, 1.818, 86.257, 1.840, 86.599, 1.815))
    list.append( SimulationResult('Home 2',  109.691, 1.830, 109.366, 1.801, 109.482, 1.785, 111.616, 1.762, 109.334, 1.817 ))
    list.append( SimulationResult('Home 3', 125.364, 2.011, 125.176, 2.025, 125.939, 2.058, 125.693, 2.049, 125.476, 2.052  ))
    list.append( SimulationResult('Home 4', 111.498, 1.703, 111.440, 1.738, 111.423, 1.717, 111.798, 1.697, 111.948, 1.704 ))
    list.append( SimulationResult('Home 5',  250.488, 2.496, 252.655, 2.416, 253.488, 2.350, 253.488, 2.346, 251.776, 2.430 ))
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;

class SimulationResult: 
    def __init__(self,home,cost_1,flat_1,cost_2,flat_2,cost_3,flat_3,cost_4,flat_4,cost_5,flat_5): 
        self.home = home 
        self.cost_1 = cost_1
        self.cost_2 = cost_2
        self.cost_3 = cost_3
        self.cost_4 = cost_4
        self.cost_5 = cost_5
        self.flat_1 = flat_1
        self.flat_2 = flat_2
        self.flat_3 = flat_3
        self.flat_4 = flat_4
        self.flat_5 = flat_5
        
# xử lý các api khác

@app.route('/electrical-appliances', methods=['GET'])
@cross_origin()
def Electrical_Appliances():

    list = []
    list.append( Electrical('Refrigerator',  1, 0.1, 288, 'ND-NI'))
    list.append( Electrical('D. Freezer',  2, 0.06, 288, 'ND-NI'))
    list.append( Electrical('Oven',  3, 2.0, 14, 'D-NI'))
    list.append( Electrical('Iron',  4, 2.4, 13, 'D-I'))
    
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;
    
class Electrical: 
    def __init__(self,name,id,power,period,type): 
        self.id = id
        self.name = name
        self.power = power
        self.period = period
        self.type = type
        
@app.route('/home', methods=['GET'])
@cross_origin()
def Home():

    list = []
    list.append( Home('Home 1',  1))
    list.append( Home('Home 2',  2))
    list.append( Home('Home 3',  3))
    list.append( Home('Home 4',  4))
    
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;
    
class Home: 
    def __init__(self,name,id): 
        self.id = id
        self.name = name
        

        
@app.route('/electrical-appliances/home/<id>', methods=['GET'])
@cross_origin(id)
def Electrical_Appliances_Home(id):
    print(id)
    list = []
    list.append( AppliancesHome('Refrigerator',  1,1))
    list.append( AppliancesHome('Refrigerator 1',  2,1))
    list.append( AppliancesHome('Refrigerator 2',  3,1))
    list.append( AppliancesHome('Refrigerator 3',  4,1))
    
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;
    
class AppliancesHome: 
    def __init__(self,name,id,number): 
        self.number = number 
        self.id = id
        self.name = name
        
@app.route('/genetic-algorithm/home', methods=['GET'])
@cross_origin(id)
def genetic_Algorithm_Home():
    id = request.args.get('id', None) 
    number = request.args.get('number', None)
    print(id)
    print(number)
    list = []
    for x in range(int(number)):
        list.append( GeneticAlgorithmHome(1.2,  85.59))
    
    
    with open('twitterData.json', 'w') as outfile:
     json_string = json.dumps([ob.__dict__ for ob in list])
    return json_string;
    
class GeneticAlgorithmHome: 
    def __init__(self,flat,cost): 
        self.flat = flat 
        self.cost = cost
        

# Thuc thi server
if __name__ == '__main__':
    app.run(debug=True)
    