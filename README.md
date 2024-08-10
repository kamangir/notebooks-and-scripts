# 📜 notebooks & scripts

📜 [notebooks](./notebooks) and [scripts](./scripts) for ai experiments and aws batch jobs.

```bash
pip install notebooks-and-scripts
```

|   |   |
| --- | --- |
| 📜[`workflow`](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow) [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/hourglass/workflow.gif?raw=true)](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow) an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/). | 📜[`scripts`](https://github.com/kamangir/notebooks-and-scripts/tree/main/scripts) [![image](https://github.com/kamangir/assets/blob/main/nbs/3x4.jpg?raw=true)](https://github.com/kamangir/notebooks-and-scripts/tree/main/scripts) legacy mechanisms replaced with `@docker eval - <command>` and `@batch eval - <command>`. |

---

[![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/)

To use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with `nbs` and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).

---
built by [`abcli-9.192.1-current`](https://github.com/kamangir/awesome-bash-cli), based on [`notebooks_and_scripts-4.620.1`](https://github.com/kamangir/notebooks-and-scripts).
