from mmdet.apis import DetInferencer
import json 
import os

# Initialize the DetInferencer
CONFIG_PATH = "/home/luunvt/WORK_DIR/fisheye/src/mmdetection/work_dirs/retinanet_r101_fpn_2x_16_03_2024/retinanet_r101_fpn_2x.py"
WEIGHT_PATH = "/home/luunvt/WORK_DIR/fisheye/src/mmdetection/work_dirs/retinanet_r101_fpn_2x_16_03_2024/epoch_17.pth"
IMAGE_FOLDER_PATH = "/home/luunvt/WORK_DIR/fisheye/data/images"
OUT_DIR = "/home/luunvt/WORK_DIR/fisheye/src/mmdetection/work_dirs/retinanet_r101_fpn_2x_16_03_2024/outputs_test_images/"
PREDS_JSON_PATH = f'{OUT_DIR}/preds'
VIS_IMG_PATH = f'{OUT_DIR}/vis'
FILE_PATH = f'{OUT_DIR}/res.json'

def get_image_Id(img_name):
    img_name = img_name.split('.png')[0]
    sceneList = ['M', 'A', 'E', 'N']
    cameraIndx = int(img_name.split('_')[0].split('camera')[1])
    sceneIndx = sceneList.index(img_name.split('_')[1])
    frameIndx = int(img_name.split('_')[2])
    imageId = int(str(cameraIndx)+str(sceneIndx)+str(frameIndx))
    return imageId

if __name__ == '__main__':
    '''
    INFERENCE
    '''
    inferencer = DetInferencer(model=CONFIG_PATH, weights=WEIGHT_PATH, device='cuda:0')
    res = inferencer(IMAGE_FOLDER_PATH, out_dir=OUT_DIR, no_save_pred=False)
    
    '''
    GENERATE JSON
    '''
    imgs_name = os.listdir(VIS_IMG_PATH)
    preds_json = os.listdir(PREDS_JSON_PATH)

    final_results = []
    for Img_name in imgs_name:
        img_id = get_image_Id(img_name=Img_name)
        json_path = PREDS_JSON_PATH + '/' + Img_name.split('.')[0] + '.json'
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        labels = data['labels']
        scores = data['scores']
        bboxes = data['bboxes']

        for lb, sc, bb in zip(labels, scores, bboxes):
            if (sc < 0.7): continue
            x_top_left, y_top_left, x_bot_right, y_bot_right = bb
            tmp_dict = {
                "image_id": img_id,
                "category_id": lb,
                # Convert format 
                #    [x_top_left, y_top_left, x_bottom_right, y_bottom_right] 
                # to [x_top_left, y_top_left, w, h]
                "bbox": [x_top_left, y_top_left, x_bot_right-x_top_left, y_bot_right-y_top_left],
                "score": sc
            }
            final_results.append(tmp_dict)

    with open(FILE_PATH, 'w') as json_file:
        json.dump(final_results, json_file)

    print("Done!")