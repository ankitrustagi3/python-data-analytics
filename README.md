
## Running the experiments

The code is all present in Google Colab which makes it very simple to run all of the experiments. There are two code files that store all of the work that I did (both the reimplementation and further implementation). The names of the two code files are: Reimplementation.ipynb and Transformer.ipynb. As I mentioned before, these notebooks are present in Google Colab which means that if one wanted to run the experiments, then they would just have to sequentially run the tasks in the notebook.  


## Reused code
The CLIP model was found in the repository: https://huggingface.co/openai/clip-vit-base-patch32. In addition, Sections 1-4 of the Reimplementation notebook are present in the GitHub repository: https://github.com/RahmadSadli/COCO_Dataset_Loader/blob/main/Custom_Loading_COCO.ipynb. 

## Modified code
The CLIP model is present in the repository that I mentioned above. As mentioned in the findings of my second paper, the use of CLIP model was utilized on a variety of datasets. I decided to modify the code by first applying it to the COCO dataset and then also visualizing the results in a heatmap. The future steps of this project will be to get the training loop of the CLIP model working and also the collation function of the COCO datasetloader. 

## Original code
The code that was created by me in the Transformer.ipynb. In this code file, I have created a fundamental transformer model with the layers of encoding, decoding, and linear. 

## Datasets 
The datasets that I have utilized for these experiments are COCO and MNIST. The MNIST one was acquired through the use of torchvision as it is one of the provided datasets. COCO was generated from the wget links that are mentioned above in the README (the link to the datasets is: http://images.cocodataset.org).
