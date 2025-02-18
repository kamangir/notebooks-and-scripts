# 📜 blueflow

📜 `blueflow` for workflow management on [aws batch](https://aws.amazon.com/batch/) and more.

```bash
pip install blueflow
```

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [aws_batch](./runners/aws_batch.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=mi4rfj83b7yqieuc)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=mi4rfj83b7yqieuc) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-a-bc-d/workflow.gif?raw=true&random=mi4rfj83b7yqieuc) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=iwsk1qgdnx9d9hp8)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=iwsk1qgdnx9d9hp8) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-hourglass/workflow.gif?raw=true&random=iwsk1qgdnx9d9hp8) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=kuidlbmvv9ouh8c6)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=kuidlbmvv9ouh8c6) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce/workflow.gif?raw=true&random=kuidlbmvv9ouh8c6) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=xkw6v8iop4m7lw83)](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=xkw6v8iop4m7lw83) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/aws_batch-map-reduce-large/workflow.gif?raw=true&random=xkw6v8iop4m7lw83) |
| [generic](./runners/generic.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=peipfgvlutuvz8e5)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=peipfgvlutuvz8e5) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-a-bc-d/workflow.gif?raw=true&random=peipfgvlutuvz8e5) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=x26ncfwlgx53krys)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=x26ncfwlgx53krys) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-hourglass/workflow.gif?raw=true&random=x26ncfwlgx53krys) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=zmnkmd6t2zet9u3f)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=zmnkmd6t2zet9u3f) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce/workflow.gif?raw=true&random=zmnkmd6t2zet9u3f) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=jwdt32ab3f8dn9nv)](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=jwdt32ab3f8dn9nv) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/generic-map-reduce-large/workflow.gif?raw=true&random=jwdt32ab3f8dn9nv) |
| [local](./runners/local.py) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=li5geidfku8yeupt)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=li5geidfku8yeupt) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-a-bc-d/workflow.gif?raw=true&random=li5geidfku8yeupt) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=zshj68lzhyobdl2n)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=zshj68lzhyobdl2n) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-hourglass/workflow.gif?raw=true&random=zshj68lzhyobdl2n) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=iq10m4iqaw4xdn9y)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=iq10m4iqaw4xdn9y) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce/workflow.gif?raw=true&random=iq10m4iqaw4xdn9y) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=3vv4syu9sjicefax)](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=3vv4syu9sjicefax) [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/local-map-reduce-large/workflow.gif?raw=true&random=3vv4syu9sjicefax) |

💡 example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).


---


[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/blueflow.svg)](https://pypi.org/project/blueflow/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/blueflow)](https://pypistats.org/packages/blueflow)

built by 🌀 [`blue_options-4.223.1`](https://github.com/kamangir/awesome-bash-cli), based on 📜 [`blueflow-4.853.1`](https://github.com/kamangir/notebooks-and-scripts).

---

used to be [`notebooks-and-scripts`](https://pypi.org/project/notebooks-and-scripts/).
