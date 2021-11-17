
# provision compute instance in OCI; E4 flex shape preferred
# deploy into a private subnet, you can expose publically via API-GW
# move verifier_cli.py and verifier_flask.py to compute instance

# From compute insance install dependencies
sudo yum update -y
sudo pip3 install --upgrade pip
pip3 install deepface

# disable firewall
sudo systemctl stop firewalld
sudo systemctl disable firewalld
sudo systemctl mask --now firewalld

# drop some images on the compute VM and test that everything works by running the CLI test

# start the Flask server; by default it listens on port 5000
nohup python3 verifier_flask.py > server.out &

# hook up an API-GW instance to the compute VM on port 5000
# make sure the API-GW is configured for CORS support for *.oraclecloud.com

# test with client file by uploading ~/client/index.html to object storage and running from there
