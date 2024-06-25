### Enviroment 

The repo is working with cuda 11.8

1-Install miniconda on linux

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

2-After installation init miniconda

```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

3-Restart the terminal

4-Clone the repo 

```bash
git clone https://github.com/Reynold97/YOLOv10-crowd-recog.git
```

5-Go to folder

```bash
cd YOLOv10-crowd-recog
```

6-Create env with conda 

```bash
conda create -p ./env python=3.10 -y
```

7-Activate enviroment

```bash
conda activate ./env
```

8-Install YOLOv10

```bash
pip install -q git+https://github.com/THU-MIG/yolov10.git
```

9-Other complementary packages 
-> Roboflow for training datasets datasets 
-> Supervision for visualization 

```bash
pip install -q supervision roboflow 
```

10-Download models

```bash
mkdir -p weights
```

```bash
wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt -P weights
```

To work with the results find more details in ultralytics docs

https://docs.ultralytics.com/modes/predict/#working-with-results

https://docs.ultralytics.com/reference/engine/results/

https://docs.ultralytics.com/modes/predict/#boxes

https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes
