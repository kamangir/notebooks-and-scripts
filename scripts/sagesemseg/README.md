# Semantic Segmentation on AWS Sagemaker

Based on [Semantic Segmentation on AWS Sagemaker](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb).

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

## dataset structure

same reference,... directory structure...,

```bash
root
|-train/
|-train_annotation/
|-validation/
|-validation_annotation/
```

... images in the `_annotation` directory are ... indexed PNG files ... `[0, 1 ... c-1, 255]` for ... `c` class[es] ... `255` ... 'ignore' ... any mode that is a [recognized standard](https://pillow.readthedocs.io/en/3.0.x/handbook/concepts.html#concept-modes) [and] ... read as integers ...
