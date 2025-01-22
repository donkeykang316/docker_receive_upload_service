from flask import Flask, request, jsonify, render_template
import docker
import uuid
import os
import shutil

app = Flask(__name__)
docker_client = docker.from_env()


# Generate the interface
@app.route('/')
def index():
    return render_template('index.html')

# main function for th service
@app.route('/submit', methods=['POST'])
def build_push():

    # Get the docker user name
    input_dir = request.form.get('input_dir_path')

    # Get the docker user pw
    input_pw = request.form.get('PW_input')

    # Get the uploaded file
    input_file = request.files.get('input_docker_file')
    
    if not input_dir or not input_pw:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        docker_client.login(username=input_dir, password=input_pw)
        print("login success")
    except Exception as e:
        return jsonify({"error": f"Login failed: {str(e)}"}), 400
    
    # file validation 
    if input_file.filename.strip().lower() == "":
        return jsonify({"error": "No selected file"}), 400
    
    if input_file.filename.strip().lower() != "dockerfile":
        return jsonify({"error": "No valid Dockerfile"}), 400
    
    # create temporary directory for storing dockerfile
    tmp_dir = f"./tmp/dockerfile_{uuid.uuid1()}/"
    os.makedirs(tmp_dir)
    dockerfile_path = os.path.join(tmp_dir, input_file.filename)
    print(dockerfile_path)
        
    with open(dockerfile_path, "w") as f:
        f.write(input_file.read().decode("utf-8"))

    # start buidling the image
    image_name = "docker_image_api:latest"
    try:
        image = docker_client.images.build(path=tmp_dir, tag=image_name)

    except Exception as e:
        shutil.rmtree("./tmp/")
        return jsonify({"error": f"{str(e)}"}), 400        
    
    # push the image to the docker registery
    tagged_image = f"{input_dir}/{image_name}"
    docker_client.images.get(image_name).tag(tagged_image)
    try:
        push_logs = {}
        for line in docker_client.images.push(tagged_image, stream=True, decode=True):
            push_logs.update(line)
    except Exception as e:
        shutil.rmtree("./tmp/")
        return jsonify({"error": f"{str(e)}"}), 400
    
    # remove local image
    try:
        docker_client.images.remove(image="docker_image_api:latest", force=True)
        docker_client.images.remove(image=tagged_image, force=True)
        print(f"Image '{image}' removed successfully.")
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400

    #remove the temp directory
    shutil.rmtree("./tmp/")
    
    return push_logs, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)