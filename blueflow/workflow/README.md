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
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=axsotra3fb6unvyr)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=axsotra3fb6unvyr) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=axsotra3fb6unvyr) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=xhx21ba8b9zkrwsi)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=xhx21ba8b9zkrwsi) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=xhx21ba8b9zkrwsi) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=o80l14vzwcqn319n)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=o80l14vzwcqn319n) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=o80l14vzwcqn319n) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=v76ea4p79b5adcb2)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=v76ea4p79b5adcb2) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=v76ea4p79b5adcb2) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=7y4xkg7cwtcaejps)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=7y4xkg7cwtcaejps) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=7y4xkg7cwtcaejps) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=89wblg8nvlyxnqd1)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=89wblg8nvlyxnqd1) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=89wblg8nvlyxnqd1) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=o9cok83clvf2ipjf)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=o9cok83clvf2ipjf) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=o9cok83clvf2ipjf) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=ztvr0wbqkzzvazgu)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=ztvr0wbqkzzvazgu) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=ztvr0wbqkzzvazgu) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=258oujtsc1dbm8mi)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=258oujtsc1dbm8mi) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=258oujtsc1dbm8mi) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=7n0a8trexp8hverq)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=7n0a8trexp8hverq) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=7n0a8trexp8hverq) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=oyjzzwfpynui40s0)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=oyjzzwfpynui40s0) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=oyjzzwfpynui40s0) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=i0ddxlkhmr3mvhph)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=i0ddxlkhmr3mvhph) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=i0ddxlkhmr3mvhph) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/notebooks-and-scripts)](https://pypistats.org/packages/notebooks-and-scripts)

built by 🌀 [`blue_options-4.186.1`](https://github.com/kamangir/awesome-bash-cli), based on [`blueflow-4.834.1`](https://github.com/kamangir/notebooks-and-scripts).
