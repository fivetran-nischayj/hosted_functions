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
    startup.download_deps()
    startup.init_files(entry)
    return {
        'message': 'Initialised files successfully'
    }

@app.route('/data', methods=['POST'])
def get_data():
   
    params = request.json 

    from invoker import invoke

    result = invoke(params)

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)