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
| Faster R-CNN| ResNet101+FPN | 0.1655 | 0.2887 | 0.1043 | 0.2219 | 0.3041 | - | [config](https://drive.google.com/file/d/1cKF3iFt67XU_e3wqI9XBW4TqJQsP5osH/view?usp=drive_link) | [model](https://drive.google.com/file/d/1CvPknKVzF9U1ezjQQ_y5z58JdVPLLPLH/view?usp=drive_link) |
| Faster R-CNN| ReResNet101+ReFPN | - | - | - | - | - | - | - | - |