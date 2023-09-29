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

```bash
 > scripts help vanwatch/ingest-and-analyze.sh

abcli scripts source ingest-and-analyze \
	[cat,count=<-1>,dryrun,upload] \
	[<object-name>] \
	[<args>]
 . ingest from traffic cameras and analyze.
 ```

## [paint-a-sentence](./scripts/paint-a-sentence.sh)

uses [blue stability](https://github.com/kamangir/blue-stability).

```bash
 > scripts help paint-a-sentence

abcli scripts source paint-a-sentence \
	[cat,count=<-1>] \
	[<object-name>] \
	["a cat walking under apple trees"] \
	[]
 . paint a sentence by different artists.
21 artists(s): Andy-Warhol,Caravaggio,Claude-Monet,Diego-Velázquez,Edgar-Degas,Edvard-Munch,Frida-Kahlo,Gustav-Klimt,Henri-Matisse,J.-M.-W.-Turner,Jackson-Pollock,Johannes-Vermeer,Leonardo-da-Vinci,Michelangelo,Pablo-Picasso,Paul-Cézanne,Paul-Gauguin,Rembrandt,Salvador-Dali,Vincent-van-Gogh,Wassily-Kandinsky
```