# scripts

[abcli 🪄](https://github.com/kamangir/awesome-bash-cli) [[meta](./meta/)] scripts for [aws batch](https://aws.amazon.com/batch/) jobs and [sagemaker](https://aws.amazon.com/sagemaker/) serving.

> ℹ️ scripts are replaced with `@docker eval - <command>` and `@batch eval - <command>`.


| ![image](https://github.com/kamangir/assets/blob/main/nbs/3x4.jpg?raw=true)                               | ![image](https://github.com/kamangir/assets/blob/main/nbs/mission-patch-00008.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/nbs/train-summary.png?raw=true) ![image](https://github.com/kamangir/assets/blob/main/nbs/predict-00000.png?raw=true) |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [paint-a-sentence](./scripts/paint-a-sentence.sh)                                                         | [mission-patch](./scripts/mission-patch.sh)                                                 | [roofAI-train](./scripts/roofAI-train.sh)                                                                                                                                   |
| https://medium.com/@arash-kamangir/a-cat-walking-under-apple-trees-style-by-stable-diffusion-ab60ece43e2a | https://medium.com/@arash-kamangir/private-mission-patch-%EF%B8%8F-1-0c2eddd79762           | https://arash-kamangir.medium.com/roofai-%EF%B8%8F-on-gpu-6-b02f8f67ed3f                                                                                                    |

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
abcli scripts list|ls \
	[meta|<prefix>]
 . list [meta] scripts.
abcli scripts move|mv \
	<script-name-1> <script-name-2>
 . <script-name-1> -> <script-name-2>
abcli scripts source [cat,dryrun] \
	<script-name> [<args>]
 . source <script-name>.
```

## [paint-a-sentence](./paint-a-sentence.sh)

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

## [mission-patch](./mission-patch.sh)

uses 🛠️ [openai_commands](https://github.com/kamangir/openai_commands) and 🎨 [aiart](https://github.com/kamangir/aiart)

```bash
 > scripts help mission-patch
abcli scripts source cat,dryrun \
	mission-patch \
	[count=<1>,dryrun,height=<1024>,open,width=<1024>,dryrun,~upload,url=<url>] \
	[<object-name>] \
	[<args>]
 . generate mission patches for <url>.
```

## [roofai-train](./roofai-train.sh)

uses 🏛️ [roofai](https://github.com/kamangir/roofai)

```bash
 > scripts help roofai-train
abcli scripts source cat,dryrun \
	roofai-train \
	[order=<2>,*] \
	[<args>]
 . train a roofai semseg model at the <order>
 * [profile=FULL|DECENT|QUICK|DEBUG|VALIDATION,~register,suffix=<suffix>]
```

# meta scripts

- [roofserver](./roofserver/): `create`s model, endpoint config, and config to serve a model on SageMaker. 🔥 `invoke`, `wipe`.