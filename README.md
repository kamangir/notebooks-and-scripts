# notebooks & scripts

Repository of research [notebooks](#notebooks) and [scripts](#scripts).

## [notebooks](./notebooks/)

```bash
 > notebooks help
📜 notebooks & scripts-4.4.1
📜 notebooks & scripts for experiments and aws batch jobs.

abcli notebooks \
	[open] \
	[<notebook>] \
	[<args>]
 . open ./notebook.ipynb.
abcli notebooks build \
	[<notebook>]
 . build vancouver-watching-test-v1/notebook.ipynb.
abcli notebooks connect \
	<1-2-3-4> [setup]
 . [setup and] connect to jupyter notebook on ec2:1-2-3-4.
abcli notebooks host \
	[setup]
 . [setup and] host jupyter notebook on ec2.
abcli notebooks touch \
	[<notebook>]
 . touch ./<notebook>.ipynb.
```

- [Semantic segmentation](./semseg).

## [scripts](./scripts/)

```bash
 > scripts help
📜 notebooks & scripts-4.4.1
📜 notebooks & scripts for experiments and aws batch jobs.

abcli scripts list
 . list scripts.
abcli scripts source \
	[<script-name>] \
	<args>
 . source <script-name>.sh
```

## [vanwatch](./scripts/vanwatch/)

uses [Vancouver Watching 🌈](https://github.com/kamangir/Vancouver-Watching).

TBA

## [paint-a-cat](./scripts/paint-a-cat.sh)

uses [blue stability](https://github.com/kamangir/blue-stability).

TBA