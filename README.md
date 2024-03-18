# Installation
MMDetection works on Linux, Windows, and macOS. It requires Python 3.7+, CUDA 9.2+, and PyTorch 1.8+.

1. Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html).
2. Create a conda environment and activate it.
```bash
conda create --name openmmlab python=3.8.18 -y
conda activate openmmlab
```
3. Install PyTorch following [official instructions](https://pytorch.org/get-started/locally/), e.g.

On GPU platforms:
```bash
conda install pytorch torchvision -c pytorch
```

On CPU platforms:
```bash
conda install pytorch torchvision cpuonly -c pytorch
```

4. Install [MMEngine](https://github.com/open-mmlab/mmengine) and [MMCV](https://github.com/open-mmlab/mmcv) using [MIM](https://github.com/open-mmlab/mim).
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv==2.1.0"
```

5. Install MMDetection.
```bash
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
# "-v" means verbose, or more output
# "-e" means installing a project in editable mode,
# thus any local modifications made to the code will take effect without reinstallation.
```

# Result
| Model | Backbone | AP_0.5_0.95 | AP_0.5 | AP_S | AP_M | AP_L | F1 | Config | Download |
| ------ |:-------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|:----------------------:|
| Faster R-CNN | ResNet101+FPN | 0.1655 | 0.2887 | 0.1043 | 0.2219 | 0.3041 | 0.1962 | [config](https://drive.google.com/file/d/1cKF3iFt67XU_e3wqI9XBW4TqJQsP5osH/view?usp=drive_link) | [model](https://drive.google.com/file/d/1CvPknKVzF9U1ezjQQ_y5z58JdVPLLPLH/view?usp=drive_link) |
| Faster R-CNN | ReResNet50+ReFPN | 0.2955 | 0.4738 | 0.1817 | 0.4113 | 0.4449 | 0.2783 | [config](https://drive.google.com/file/d/1QVu-niO-ZNFiEb6_iTxJW0DCk1seLm2c/view?usp=sharing) | [model](https://drive.google.com/file/d/1fNyYheY9ALldg1-uFIoaLIIp2CoRr2qU/view?usp=sharing) |
| Retinanet | ResNet101+FPN | 0.1754 | 0.2690 | 0.0712 | 0.2935 | 0.3260 | 0.2788 | [config](https://drive.google.com/file/d/1fkOPq2Gm364WGE81V6puoawJxF7Fy46e/view?usp=sharing) | [model](https://drive.google.com/file/d/1HUrZlUuXQm716p3v6cFKJZHQG7eJOI7A/view?usp=sharing) |
| Retinanet | ReResNet50+ReFPN | 0.2829 | 0.4556 | 0.1515 | 0.4103 | 0.4539 | 0.1764 | [config](https://drive.google.com/file/d/105OrHoJWPPlgukGcGktA6OMUHhcOFNfr/view?usp=sharing) | [model](https://drive.google.com/file/d/1UwkGbzlAbxOZEb3qVWUkZoRsUrsk66Nu/view?usp=sharing) |