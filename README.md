# Installation
MMDetection works on Linux, Windows, and macOS. It requires Python 3.7+, CUDA 9.2+, and PyTorch 1.8+.

1. Download and install Miniconda from the official website.
2. Create a conda environment and activate it.
```bash
conda create --name openmmlab python=3.8 -y
conda activate openmmlab
```
3. Install PyTorch following official instructions, e.g.

On GPU platforms:
```bash
conda install pytorch torchvision -c pytorch
```

On CPU platforms:
```bash
conda install pytorch torchvision cpuonly -c pytorch
```

4. Install MMEngine and MMCV using MIM.
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
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