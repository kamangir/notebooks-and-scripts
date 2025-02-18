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
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=t9rj2acdusw6gox4)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=t9rj2acdusw6gox4) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=t9rj2acdusw6gox4) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ksk87c40gwmqd2n3)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ksk87c40gwmqd2n3) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=ksk87c40gwmqd2n3) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=w4vevmacz8u9nxti)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=w4vevmacz8u9nxti) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=w4vevmacz8u9nxti) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=n81ttvza8zblma2k)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=n81ttvza8zblma2k) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=n81ttvza8zblma2k) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=3ixcujlk8zpnq0qp)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=3ixcujlk8zpnq0qp) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=3ixcujlk8zpnq0qp) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=z8q6j1kg05f7djr1)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=z8q6j1kg05f7djr1) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=z8q6j1kg05f7djr1) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=v90wihyctvi8kqrg)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=v90wihyctvi8kqrg) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=v90wihyctvi8kqrg) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=8b4yjyjsn7yqn0jo)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=8b4yjyjsn7yqn0jo) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=8b4yjyjsn7yqn0jo) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=z2powif7a9nk4ndj)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=z2powif7a9nk4ndj) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=z2powif7a9nk4ndj) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=fk00inf1br20tej2)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=fk00inf1br20tej2) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=fk00inf1br20tej2) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=27croei8es98zyeo)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=27croei8es98zyeo) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=27croei8es98zyeo) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=pcxm5ods5xyifkj8)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=pcxm5ods5xyifkj8) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=pcxm5ods5xyifkj8) |

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef)

---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/notebooks-and-scripts)](https://pypistats.org/packages/notebooks-and-scripts)

built by 🌀 [`blue_options-4.223.1`](https://github.com/kamangir/awesome-bash-cli), based on [`blueflow-4.850.1`](https://github.com/kamangir/notebooks-and-scripts).
