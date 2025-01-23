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

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=c7vzniehta4w2y2b)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=c7vzniehta4w2y2b) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=c7vzniehta4w2y2b) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ta4csieohq3k1g1y)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ta4csieohq3k1g1y) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ta4csieohq3k1g1y) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=8fs7z47i26d3enhf)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=8fs7z47i26d3enhf) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=8fs7z47i26d3enhf) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=9g5py6ecero67hzd)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=9g5py6ecero67hzd) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=9g5py6ecero67hzd) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=qljq1v2hrx3ut1y9)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=qljq1v2hrx3ut1y9) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=qljq1v2hrx3ut1y9) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=xl7xfkbzdc06dlbi)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=xl7xfkbzdc06dlbi) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=xl7xfkbzdc06dlbi) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=569kq62kwslxnrni)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=569kq62kwslxnrni) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=569kq62kwslxnrni) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=1x1s1c8bokz9t7iq)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=1x1s1c8bokz9t7iq) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=1x1s1c8bokz9t7iq) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=s1jgbuexvyysyvxo)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=s1jgbuexvyysyvxo) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=s1jgbuexvyysyvxo) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=3jjb0p3tnaj7jbdz)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=3jjb0p3tnaj7jbdz) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=3jjb0p3tnaj7jbdz) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=3492v4jibrfxe02t)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=3492v4jibrfxe02t) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=3492v4jibrfxe02t) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=2b4kn704nzeapzqw)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=2b4kn704nzeapzqw) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=2b4kn704nzeapzqw) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/notebooks-and-scripts)](https://pypistats.org/packages/notebooks-and-scripts)

built by 🌀 [`blue_options-4.194.1`](https://github.com/kamangir/awesome-bash-cli), based on [`blueflow-4.843.1`](https://github.com/kamangir/notebooks-and-scripts).
