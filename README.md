
## Running the experiments

The code is all present in Google Colab which makes it very simple to run all of the experiments. But diving deeper into the code files, shown below is the way to run the experiments.

```bash
wget http://images.cocodataset.org/zips/train2017.zip -O coco_train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip -O coco_val2017.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip -O coco_ann2017.zip
```

## Reused code
The CLIP model was found in the repository: https://huggingface.co/openai/clip-vit-base-patch32. 

## Modified code

## Original code
The code that was created 

## Datasets 
The datasets that I have utilized for these experiments are COCO and MNIST. The MNIST one was acquired through the use of torchvision as it is one of the provided datasets. COCO was generated from the wget links that are mentioned above in the README.
