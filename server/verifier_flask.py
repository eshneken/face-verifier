from flask import Flask, jsonify, request, make_response
from deepface import DeepFace
import argparse

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>What do you want?  Take a hike!</h1>'

@app.route('/verify', methods=['POST'])
def verify():

	algorithm = "VGG-Face"
	req = request.get_json(force=True)

	if "img1" in list(req.keys()):
	    img1 = "data:image/," + req['img1']
	if "img2" in list(req.keys()):
	    img2 = "data:image/," + req['img2']
	if "algorithm" in list(req.keys()):
		algorithm = req['algorithm']

	resp_obj = jsonify({'success': False})

	try:
		resp_obj = DeepFace.verify(img1, img2, algorithm)
	except Exception as err:
		resp_obj = jsonify({'success': False, 'error': str(err)}), 205

	return resp_obj, 200

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-p', '--port',
		type=int,
		default=5000,
		help='Port of serving api')
	args = parser.parse_args()
	app.run(host='0.0.0.0', port=args.port)