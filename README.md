# 📜 notebooks & scripts

📜 [notebooks](./notebooks) and [scripts](./scripts) for ai experiments and aws batch jobs.

```bash
pip install notebooks-and-scripts
```

🔷 [scripts](#scripts) 🔷 [ukraine-timemap](#ukraine-timemap-) 🇺🇦 🔷 [workflow](#workflow) 🔷

---

## scripts

scripts are maintained as legacy and are replaced with `@docker eval - <command>`.

| ![image](https://github.com/kamangir/assets/blob/main/nbs/3x4.jpg?raw=true)                               | ![image](https://github.com/kamangir/assets/blob/main/nbs/mission-patch-00008.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/nbs/train-summary.png?raw=true) ![image](https://github.com/kamangir/assets/blob/main/nbs/predict-00000.png?raw=true) |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [paint-a-sentence](./scripts/paint-a-sentence.sh)                                                         | [mission-patch](./scripts/mission-patch.sh)                                                 | [roofAI-train](./scripts/roofAI-train.sh)                                                                                                                                   |
| https://medium.com/@arash-kamangir/a-cat-walking-under-apple-trees-style-by-stable-diffusion-ab60ece43e2a | https://medium.com/@arash-kamangir/private-mission-patch-%EF%B8%8F-1-0c2eddd79762           | https://arash-kamangir.medium.com/roofai-%EF%B8%8F-on-gpu-6-b02f8f67ed3f                                                                                                    |

also: [`sagesemseg`](./scripts/sagesemseg/).

---

## ukraine-timemap 🇺🇦

[`ukraine-timemap`](./notebooks_and_scripts/.abcli/ukraine-timemap/) ingests the [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json), and generates a `geojson`, a QGIS project, and more.

download the latest ingested object: [ukraine-timemap.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/ukraine_timemap.tar.gz).

```bash
 > ukraine_timemap help
ukraine_timemap browse \
	[dataset|github]
 . browse ukraine-timemap.
ukraine_timemap ingest \
	[dryrun,~upload] \
	[-|<object-name>] \
	[--verbose 1]
 . ingest the latest dataset from https://github.com/bellingcat/ukraine-timemap.
```

example use,

```
@select ukraine-timemap-$(@@timestamp)
ukraine_timemap ingest - . --verbose 1
@open . QGIS
@publish tar .
```

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/ingest_log.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true)

more: https://arash-kamangir.medium.com/%EF%B8%8F-openai-experiments-93-bf0cee062693

---

## workflow

also home to [`workflow`](./notebooks_and_scripts/workflow/generic.py), an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of bash commands on aws batch.

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

---

[![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/)

To use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with `nbs` and follow [these instructions](https://github.com/kamangir/blue-plugin/blob/main/SageMaker.md).
