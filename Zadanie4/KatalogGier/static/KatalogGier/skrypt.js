async function ZdobadzDane() {
    const url = window.location.href + "/api"
    try {
        const response = await fetch(url);
        if (!response.ok){
            throw new Error('Repsonse status: ${response.status}');
        }
        const result = await response.json();
        console.log(result);
        WyswietlenieWynikow(result.items);
    }
    catch(blad){
        console.error(blad.massage);
    }
}

function WyswietlenieWynikow(Wyniki){
    Tekst = "";
    for (let i in Wyniki){
    }
    document.getElementById("WyswietlaczDanych").innerHTML = Tekst;
}

function WyswietlAPI(){
    window.open(window.location.href + "/api");
}