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
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=OaoW4eECGcj1wXp9)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=OaoW4eECGcj1wXp9) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=tQu11gF4RukdHXIJ)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=tQu11gF4RukdHXIJ) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=UwNs9ZWwIZMdDUGz)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=UwNs9ZWwIZMdDUGz) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=sPDgYGS5Ad7lUlI1)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=sPDgYGS5Ad7lUlI1) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=8nBcX1VqLwZeKY7H)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=8nBcX1VqLwZeKY7H) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=niYA4BA9uHUADnYj)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=niYA4BA9uHUADnYj) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=6UdG03KabKqx8ZE0)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=6UdG03KabKqx8ZE0) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=huzgb6Po0HEOI9pM)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=huzgb6Po0HEOI9pM) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=f7Z7lTyduY1tuc6U)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=f7Z7lTyduY1tuc6U) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/notebooks-and-scripts)](https://pypistats.org/packages/notebooks-and-scripts)

built by 🌀 [`blue_options-4.124.1`](https://github.com/kamangir/awesome-bash-cli), based on [`notebooks_and_scripts-4.746.1`](https://github.com/kamangir/notebooks-and-scripts).
