from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': 'Buy Groceries',
        'Description': 'Milk, Pizza, Cheese',
        'Done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'Description': 'Learn Writing Python',
        'Done': False
    }
]
@app.route('/add-data',methods= ['post'])

def AddTask():
    if not request.json:
        return jsonify({
            'status': 'error',
            'Message': 'Please Provide The Data'        
            },404)
    task = {
            'id': tasks[-1]['id']+1,
            'title': request.json['title'],
            'Description': request.json.get('Description',''),
            'Done': False    
    }


    tasks.append(task)

    return jsonify({
        'status': 'success',
        'message': 'Task Added Successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data': tasks
    })    

if (__name__ == '__main__'):
    app.run(debug = True)