from mmdet.apis import DetInferencer
import json 

# Initialize the DetInferencer
config_path = "/home/luunvt/WORK_DIR/fisheye/src/mmdetection/work_dirs/faster-rcnn_r101_fpn_2x_coco_28_02_2024/faster-rcnn_r101_fpn_2x_coco.py"
weight_path = "/home/luunvt/WORK_DIR/fisheye/src/mmdetection/work_dirs/faster-rcnn_r101_fpn_2x_coco_28_02_2024/epoch_20.pth"
inferencer = DetInferencer(model=config_path, weights=weight_path, device='cuda:0')

# Perform inference
res = inferencer('/home/luunvt/WORK_DIR/fisheye/data/Fisheye8K_all_including_train&test/test/images/camera1_A_0.png')

with open("prediction.json", "w") as outfile: 
    json.dump(res, outfile)