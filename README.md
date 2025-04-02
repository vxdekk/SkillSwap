# Projekt "SkillSwap"

**SkillSwap** je spletna aplikacija za izmenjavo veščin, ki omogoča uporabnikom, da se povežejo in učijo drug od drugega. Aplikacija bo uporabljala naslednje tehnologije:

- **Python (Flask)** za strežnik
- **HTML, CSS, JavaScript** za uporabniški vmesnik
- **JSON datoteke** za shranjevanje podatkov

## Koraki razvoja

1. **Postavitev Flask strežnika**  
   Inicializacija Flask aplikacije in konfiguracija poti za prikaz strani (npr. index, registracija, iskanje).

2. **Ustvarjanje osnovnih HTML strani**  
   - **index.html**: Glavna stran
   - **register.html**: Registracija uporabnika
   - **search.html**: Iskanje partnerjev za učenje

3. **Registracija uporabnika**  
   Obrazec za vnos imena, veščin, želja in Discord username-a. Podatki se shranijo v **users.json**.

4. **Prikaz in iskanje uporabnikov**  
   Branje podatkov iz **users.json** in filtriranje po ponujenih veščinah.

5. **Povezovanje uporabnikov**  
   Prikaz kontaktnih podatkov (Discord username) in možnost filtriranja glede na jezik, lokacijo (kasnejše nadgradnje).

6. **Dodatne funkcije (nadgradnje)**  
   - Ocene in pregledi uporabnikov
   - Sistem značk (npr. "Zanesljiv učitelj")
   - Možnost direktnega klepeta znotraj aplikacije

# Prednosti in slabosti projekta "SkillSwap"

## Prednosti

- **Enostavna izmenjava veščin**: Uporabniki lahko hitro najdejo partnerje za učenje na podlagi svojih veščin in želja.
- **Prilagodljivo iskanje**: Napreden sistem iskanja in filtriranja uporabnikov po različnih kriterijih, kot so veščine, jezik, lokacija in posebne zahteve.
- **Povezovanje uporabnikov**: Preko kontaktnih podatkov (Discord username) se lahko uporabniki hitro povežejo in začnejo z izmenjavo veščin.
- **Ocene in pregledi uporabnikov**: Sistem ocen omogoča večjo varnost in zaupanje med uporabniki, saj lahko preverijo izkušnje drugih.
- **Enostavno shranjevanje podatkov**: Uporaba **JSON datotek** omogoča preprost in pregleden način shranjevanja uporabniških podatkov.
- **Nadgradnje**: Možnost kasnejših nadgradenj, kot so sistem značk in direktni klepet znotraj aplikacije.

## Slabosti

- **Omejena funkcionalnost**: Trenutna različica omogoča le osnovne funkcije, kot so registracija in iskanje uporabnikov, brez naprednejših možnosti, kot so video klici ali integracija z drugimi platformami.
- **Pomanjkanje napredne varnosti**: Ker se podatki trenutno shranjujejo v **JSON datotekah**, ni vgrajenega naprednega sistema za zaščito in šifriranje podatkov, kar bi lahko predstavljalo varnostno tveganje.
- **Nizka prilagodljivost v uporabniškem vmesniku**: Trenutno aplikacija ponuja osnovni uporabniški vmesnik, ki bi lahko bil izboljšan z bolj naprednim dizajnom ali odzivnimi funkcijami za različne naprave.
- **Omejena uporabniška baza**: Ker je aplikacija odvisna od uporabnikov, ki jo aktivno uporabljajo, lahko začetna faza razvoja pripelje do omejene baze uporabnikov, kar zmanjša možnosti za iskanje partnerjev.
- **Odvisnost od zunanjih orodij**: Povezovanje preko Discorda ali drugih zunanjih platform pomeni, da so uporabniki odvisni od teh orodij za komunikacijo, kar lahko omeji fleksibilnost aplikacije.


Aplikacija omogoča enostavno iskanje in izmenjavo veščin ter kasnejše nadgradnje za boljšo izkušnjo uporabnikov.
