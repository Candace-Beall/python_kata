from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello World!</p><h1>Your name is: " + request.args.get('name', 'Jordan') + '</h1>'


@app.route("/dog")
def dog():
    print(request.args)
    html = '''
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <div class="card container shadow m-3">
      <div class="card-body">    
        <form action="/dog" class="form-horizontal">
        <h1>Dog Age Calculator</h1>
        
        <div class="form-group">
            <label for="name" class="col control-label">What Is Your Dog's Name?</label>
            <div class="col-4">
              <input type="text" class="form-control" name="name" placeholder="Name" value="''' + \
           request.args.get('name', '') + '''">
            </div>
        </div>        
        

        <div class="form-group">
            <label for="age" class="col control-label">What Is Your Dog's Age?</label>
            <div class="col-4">
              <input type="number" class="form-control" name="age" placeholder="Age" value="''' + \
           request.args.get('age', '') + '''">
            </div>
        </div>

        <div class="form-group">
          <input type="submit" value="Calculate" class="btn btn-outline-success" />
        </div>
           
        </form>
      </div>
    </div>
    '''

    message = ''

    if 'name' in request.args:
        message += "Your Dog's Name is " + request.args.get('name')

    if 'age' in request.args:
        dog_age = 0

        try:
            dog_age = int(request.args.get('age', 1)) * 7
        except Exception:
            pass

        message += ", its age is " + str(dog_age) + '.'

    # print("Your Dog's Name is " + name + ", its age is " + str(dog_age) + '.')

    if message:
        html += "<h4 class='m-3'>" + message + "</h4>"
    return html
