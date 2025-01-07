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
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=pRFiRBFJvQ4vRerM)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=pRFiRBFJvQ4vRerM) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=pRFiRBFJvQ4vRerM) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ZVBO3e10eRxtH9P3)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ZVBO3e10eRxtH9P3) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ZVBO3e10eRxtH9P3) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=yNUYjFfUkqfnG3S7)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=yNUYjFfUkqfnG3S7) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=yNUYjFfUkqfnG3S7) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=XdumP1z0DM2S1rXm)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=XdumP1z0DM2S1rXm) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=XdumP1z0DM2S1rXm) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=XWQGYlv3BRDOhxBY)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=XWQGYlv3BRDOhxBY) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=XWQGYlv3BRDOhxBY) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=1zb7koE4rFc27cNk)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=1zb7koE4rFc27cNk) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=1zb7koE4rFc27cNk) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=H3exyNvnRagkRZYB)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=H3exyNvnRagkRZYB) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=H3exyNvnRagkRZYB) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=SjKUkg3bXvv3le5k)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=SjKUkg3bXvv3le5k) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=SjKUkg3bXvv3le5k) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=hOXBOY3bDTs0GgZw)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=hOXBOY3bDTs0GgZw) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=hOXBOY3bDTs0GgZw) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=Z2t9cjhMdAcoISIa)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=Z2t9cjhMdAcoISIa) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=Z2t9cjhMdAcoISIa) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=R79ohaqxDl1qMgff)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=R79ohaqxDl1qMgff) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=R79ohaqxDl1qMgff) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=kPoxtOSt0Pkm77s2)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=kPoxtOSt0Pkm77s2) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=kPoxtOSt0Pkm77s2) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/notebooks-and-scripts)](https://pypistats.org/packages/notebooks-and-scripts)

built by 🌀 [`blue_options-4.175.1`](https://github.com/kamangir/awesome-bash-cli), based on [`blueflow-4.829.1`](https://github.com/kamangir/notebooks-and-scripts).
