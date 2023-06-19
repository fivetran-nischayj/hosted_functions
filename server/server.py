from flask import Flask, request



app = Flask(__name__)

@app.route('/init', methods=['POST'])
def initialise():
    '''
    Request body: 
    {
        "github_token": <key>,
        "repo": <repo>
        "path": <path>,
        "entry": <entry>
    }
    '''

    params = request.json
    print(params)
    github_token, repo, path, entry = params['github_token'], params['repo'], params['path'], params['entry']

    import startup
    startup.fetch_files(github_token, repo, path)
    startup.init_files(entry)
    return {
        'message': 'Initialised files successfully'
    }

@app.route('/data', methods=['POST'])
def get_data():
    # Call the handle method inside function.py with the request body params
    # Assumes that the handle method is defined in the function.py file

    # Extract params from the request body
    params = request.json  # Assuming the request body is in JSON format

    # Import the handler method from the function.py file
    from invoker import invoke

    # Call the handle method and pass the params
    result = invoke(params)

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)