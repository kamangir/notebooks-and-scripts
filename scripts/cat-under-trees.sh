#! /usr/bin/env bash

function cat_unrder_trees() {
    local sentence="a cat walking under apple trees"
    local prefix="cat-under-trees"

    local list_of_artists="Leonardo-da-Vinci,Vincent-van-Gogh,Michelangelo,Gustav-Klimt,Claude-Monet,Paul-Cézanne,Frida-Kahlo,Salvador-Dali,Jackson-Pollock,Johannes-Vermeer,Wassily-Kandinsky,Edvard-Munch,Paul-Gauguin,Pablo-Picasso,Rembrandt,Diego-Velázquez,Henri-Matisse,Andy-Warhol,Edgar-Degas,J.-M.-W.-Turner,Caravaggio"

    local artist
    for artist in $(echo $list_of_artists | tr , " "); do

        local filename=$(python3 -c "print('$artist'.lower().replace(' ','-'))")

        blue_stability generate image \
            ~dryrun \
            $filename \
            - \
            "$sentence style by $(echo $artist | tr - " ")"
    done

    abcli_log "completed."
}

cat_unrder_trees "$@"
