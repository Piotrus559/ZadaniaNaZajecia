function WyswietlAPI(ktore){
    switch(ktore){
        case 1:
            window.open(window.location.href + "/api");
            break;
        case 2:
            window.open(window.location.href + "/api/bydate");
            break;
        case 3:
            window.open(window.location.href + "/api/avaible");
            break;
        case 4:
            window.open(window.location.href + "/api/last");
            break;
    }
}