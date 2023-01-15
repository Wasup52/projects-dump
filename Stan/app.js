xhr = $.ajax({
    url: '/?type=476',
    type: 'post',
    data: {
        requete: 'tempsreel_submit',
        requete_val: ({
            arret: arret,
            arret_name: arret_name,
            ligne_id: ligne_id,
            ligne_omsid: ligne_omsid,
            numlignepublic: numlignepublic,
            color:color,
            background:background,
            libelle:libelle
        })
    },