# 📜 notebooks & scripts

📜 [notebooks](./notebooks) and [scripts](./scripts) for ai experiments and aws batch jobs.

```bash
pip install notebooks-and-scripts
```

|   |   |
| --- | --- |
| 📜[`workflow`](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow) [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/hourglass/workflow.gif?raw=true)](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow) an abstraction to run mixed-type (cpu/gpu/...) [DAG](https://networkx.org/documentation/stable/reference/classes/digraph.html)s of commands on [aws batch](https://aws.amazon.com/batch/), and a few other compute resources. | 📜[`scripts`](https://github.com/kamangir/notebooks-and-scripts/tree/main/scripts) [![image](https://github.com/kamangir/assets/blob/main/nbs/3x4.jpg?raw=true)](https://github.com/kamangir/notebooks-and-scripts/tree/main/scripts) legacy mechanisms replaced with `@docker eval - <command>` and `@batch eval - <command>`. |

---

to use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with "notebooks_and_scripts" and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).

[![pylint](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/notebooks-and-scripts/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/notebooks-and-scripts.svg)](https://pypi.org/project/notebooks-and-scripts/)

built by 🌀 [`blue_options-4.105.1`](https://github.com/kamangir/awesome-bash-cli), based on [`notebooks_and_scripts-4.734.1`](https://github.com/kamangir/notebooks-and-scripts).
