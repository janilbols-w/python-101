# install python in a Pure linux device (cmd)

```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

ln -s /usr/bin/python3.6 /usr/bin/python
```

