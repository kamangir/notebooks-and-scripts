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
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=YMLqSsMAlRKXoi7k)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=YMLqSsMAlRKXoi7k) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=gv16UsAiyDiNvjzF)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=gv16UsAiyDiNvjzF) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=viCPR5ABBKelADRo)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=viCPR5ABBKelADRo) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=SHwMLMbAjFJxxMC0)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=SHwMLMbAjFJxxMC0) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=OJn4WI5T30ApCQTP)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=OJn4WI5T30ApCQTP) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=vppoqb5QOWQp8aIQ)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=vppoqb5QOWQp8aIQ) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=CVxWPhk68i9EARjy)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=CVxWPhk68i9EARjy) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=F8YLOnSzYbchxi0y)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=F8YLOnSzYbchxi0y) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=Y2uEqPIrzJcJzn9c)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=Y2uEqPIrzJcJzn9c) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---

to use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with "notebooks_and_scripts" and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).

[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/)

built by 🪄 [`blue_options-4.48.1-abcli-blue-objects-attempt-2-b-2024-09-07-99677`](https://github.com/kamangir/awesome-bash-cli), based on [`notebooks_and_scripts-4.704.1`](https://github.com/kamangir/notebooks-and-scripts).
