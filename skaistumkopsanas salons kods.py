class Skaistumkopsana:
    def __init__(self,
                 pakalpojuma_kategorija: str = "",
                 pakalpojuma_nosaukums: str = "",
                 pakalpojuma_atlaide: Any = "0%",
                 pakalpojuma_cena: float = 0.0):
        self.Pakalpojuma_kategorija: str = pakalpojuma_kategorija
        self.Pakalpojuma_nosaukums: str = pakalpojuma_nosaukums
        self.Pakalpojuma_atlaide: str = str(pakalpojuma_atlaide) if pakalpojuma_atlaide is not None else "0%"
        self.Pakalpojuma_cena: float = float(pakalpojuma_cena or 0.0)
        self.Laiks_pieejams: bool = True
        self.Klients_vards: str = ""
        self.Klients_uzvards: str = ""
        self.Klients_pk: str = ""
        self.Klients_tel_numurs: str = ""
        self.Pakalpojuma_datums: str = ""
        self.Pakalpojuma_sakuma_laiks: str = ""
        self.Pakalpojuma_beigu_laiks: str = ""
        
    def no_detalam(self, pak_kategorija: str, pak_nosaukums: str, atlaide: Any, cena: float):
        self.Pakalpojuma_kategorija = pak_kategorija
        self.Pakalpojuma_nosaukums = pak_nosaukums
