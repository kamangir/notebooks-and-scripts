# 📜 workflow

[`workflow`](./notebooks_and_scripts/workflow/generic.py), an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/).

```bash
 > workflow help
workflow create \
	pattern=a-bc-d|hourglass,~upload \
	-|<job-name> \
	<command-line>
 . create a <pattern> workflow.
workflow monitor \
	~download,~upload \
	.|<job-name>
 . monitor workflow.
workflow submit \
	~download,dryrun,to=aws_batch|generic|local|localflow,~upload \
	.|<job-name>
 . submit workflow.
```

```bash
@select - open
workflow create pattern=hourglass .
workflow submit to=aws_batch
@watch - @download
```

from https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef

| [`a-bc-d`](./notebooks_and_scripts/workflow/patterns/a-bc-d.dot) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/a-bc-d/workflow.gif?raw=true) | [`hourglass`](./notebooks_and_scripts/workflow/patterns/hourglass.dot) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/hourglass/workflow.gif?raw=true) | [`map-reduce`](./notebooks_and_scripts/workflow/patterns/map-reduce.dot) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/map-reduce/workflow.gif?raw=true) |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/a-bc-d/workflow.gif?raw=true)                                                              | ![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/hourglass/workflow.gif?raw=true)                                                                    | ![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/map-reduce/workflow.gif?raw=true)                                                                      |