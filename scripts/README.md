# scripts

[abcli 🚀](https://github.com/kamangir/awesome-bash-cli) [[meta](./meta/)] scripts for [aws batch](https://aws.amazon.com/batch/) jobs and [sagemaker](https://aws.amazon.com/sagemaker/) serving.

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

## [@vanwatch](./vanwatch_meta/)

[Vancouver Watching 🌈](https://github.com/kamangir/Vancouver-Watching) + AWS Batch.

```bash
@vanwatch ingest \
	batch,dryrun \
	area=<area>,count=<-1>,dryrun,gif,model=<model-id>,~process,publish,~upload \
	-|<object-name> \
	[<args>]
 . vanwatch ingest, defaults to vancouver x 10.
@vanwatch process \
	batch,dryrun \
	count=<count>,~download,gif,model=<model-id>,publish,~upload \
	.|all|<object-name> \
	[<args>]
 . vanwatch process <object-name>.
```

## [sagesemseg](./sagesemseg/)

[Semantic Segmentation on AWS Sagemaker](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb).

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

## [roofAI-train](./roofAI-train.sh)

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

# meta scripts

- [roofserver](./roofserver/): `create`s model, endpoint config, and config to serve a model on SageMaker. 🔥 `invoke`, `wipe`.
