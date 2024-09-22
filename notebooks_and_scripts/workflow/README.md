# 📜 workflow

an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands with dependencies on [aws batch](https://aws.amazon.com/batch/), and a few other compute resources.

```bash
 > workflow help
workflow create \
	pattern=a-bc-d|hourglass|map-reduce,~upload \
	.|<job-name> \
	[--publish_as <public-object-name>]
 . create a <pattern> workflow.
workflow monitor \
	~download,node=<node>,publish_as=<public-object-name>,~upload \
	.|<job-name>
 . monitor workflow.
workflow submit \
	~download,dryrun,to=aws_batch|generic|local,~upload \
	.|<job-name>
 . submit workflow.
```

example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).

|   |   |   |   |
| --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) |
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=5zinpXZ2kK8Cs0jn)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=5zinpXZ2kK8Cs0jn) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=Og3q4dX2nmBAnyoA)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=Og3q4dX2nmBAnyoA) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=axD9ipNuI1t3p7yK)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=axD9ipNuI1t3p7yK) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=wALm1KyKZLbAUAFi)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=wALm1KyKZLbAUAFi) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=RKlx5nQIjSEinUdu)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=RKlx5nQIjSEinUdu) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=a0DOPGXkMgExcfVG)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=a0DOPGXkMgExcfVG) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=Aravz9pEYgHNn4NF)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=Aravz9pEYgHNn4NF) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=g8z49dmvYEjiux9N)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=g8z49dmvYEjiux9N) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=DifnnooswtoxlzKj)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=DifnnooswtoxlzKj) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---

to use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with "notebooks_and_scripts" and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).

[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/)

built by 🌀 [`blue_options-4.76.1-abcli-current`](https://github.com/kamangir/awesome-bash-cli), based on [`notebooks_and_scripts-4.722.1`](https://github.com/kamangir/notebooks-and-scripts).
