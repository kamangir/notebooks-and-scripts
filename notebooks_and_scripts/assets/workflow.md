# 📜 workflow

[`workflow`](./notebooks_and_scripts/workflow/generic.py), an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/).

```bash
 > workflow help
workflow create \
	pattern=a-bc-d|hourglass|map-reduce,~upload \
	.|<job-name>
 . create a <pattern> workflow.
workflow monitor \
	~download,node=<node>,publish_as=<public-object-name>,~upload \
	.|<job-name>
 . monitor workflow.
workflow submit \
	~download,dryrun,to=aws_batch|generic|local|localflow,~upload \
	.|<job-name>
 . submit workflow.
```

## example use

```bash
@select - open
workflow create pattern=hourglass .
workflow submit to=aws_batch
@watch - @download
```

from https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-54-e49117dc69ef

--table--

---

--signature--