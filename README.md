# notebooks & scripts

Repository of research [notebooks](#notebooks) and [scripts](#scripts).

## [notebooks](./notebooks/)

```bash
 > notebooks help
abcli notebooks \
	[open] \
	[<notebook>] \
	[<args>]
 . open ./notebook.ipynb.
abcli notebooks build \
	[<notebook>]
 . build model-2023-12-02-20-01-08-54634/notebook.ipynb.
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

- [Semantic segmentation](./notebooks/semseg).

## [scripts](./scripts/)

```bash
 > scripts help
abcli scripts cat \
	<script-name>
 . cat <script-name>.
abcli scripts code \
	<script-name>
 . code <script-name>.
abcli scripts help \
	[<script-name>]
 . help <script-name>.
abcli scripts list \
	[<prefix>]
 . list scripts.
abcli scripts move|mv \
	<script-name-1> <script-name-2>
 . <script-name-1> -> <script-name-2>
abcli scripts source [cat,dryrun] \
	<script-name> [<args>]
 . source <script-name>.
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

## [mission-patch](./scripts/mission-patch.sh)

uses 🛠️ [openai](https://github.com/kamangir/openai) and 🎨 [aiart](https://github.com/kamangir/aiart)

```bash
 > scripts help mission-patch
abcli scripts source cat,dryrun \
	mission-patch \
	[count=<1>,dryrun,height=<1024>,open,width=<1024>,dryrun,~upload,url=<url>] \
	[<object-name>] \
	[<args>]
 . generate mission patches for <url>.
```

## [roofAI-train](./scripts/roofAI-train.sh)

uses 🏛️ [roofAI](https://github.com/kamangir/roofAI)

```bash
 > scripts help roofAI-train
abcli scripts source cat,dryrun \
	roofAI-train \
	[order=<2>,*] \
	[<args>]
 . train a roofAI semseg model at the <order>
 * [profile=FULL|DECENT|QUICK|DEBUG|VALIDATION,~register,suffix=<suffix>]
```

---

| ![image]()                                        | ![image](https://github.com/kamangir/assets/blob/main/nbs/mission-patch-00008.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/nbs/train-summary.png?raw=true) ![image](https://github.com/kamangir/assets/blob/main/nbs/predict-00000.png?raw=true) |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [paint-a-sentence](./scripts/paint-a-sentence.sh) | [mission-patch](./scripts/mission-patch.sh)                                                 | [roofAI-train](./scripts/roofAI-train.sh)                                                                                                                                   |
| xxx                                               | https://medium.com/@arash-kamangir/private-mission-patch-%EF%B8%8F-1-0c2eddd79762           | https://arash-kamangir.medium.com/roofai-%EF%B8%8F-on-gpu-6-b02f8f67ed3f                                                                                                    |
