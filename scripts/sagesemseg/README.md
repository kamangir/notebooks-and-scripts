# Semantic Segmentation on AWS Sagemaker

Based on [Semantic Segmentation on AWS Sagemaker](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb), uses [roofAI.semseg.sagemaker](https://github.com/kamangir/roofAI/tree/main/roofAI/semseg/sagemaker).

```bash
 > sagesemseg help
sagesemseg cache_dataset \
	[dataset=pascal-voc,suffix=<v1>,rm]
 . cache dataset.
sagesemseg train \
	[dryrun,~upload] \
	[test|<dataset-object-name>] \
	[-|<model-object-name>] \
	[--deploy 0] \
	[--delete_endpoint 0] \
	[--epochs 10] \
	[--instance_type ml.p3.2xlarge]
 . <dataset-object-name> -train-> <model-object-name>.
sagesemseg upload_dataset \
	[dataset=pascal-voc,suffix=<v1>] \
	[dryrun,suffix=<v1>] \
	[--count <count>]
 . upload dataset to SageMaker for training.
```
