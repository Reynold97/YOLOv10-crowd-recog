### Requirements (Windows)

Create env with conda 

```bash
conda create -p ./env python=3.10 -y
```

Activate enviroment

```bash
conda activate ./env
```

Install YOLOv10

```bash
pip install -q git+https://github.com/THU-MIG/yolov10.git
```

Other complementary packages 
-> Roboflow for training datasets datasets 
-> Supervision for visualization 

```bash
pip install -q supervision roboflow
```

