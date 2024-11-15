```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu "1" -- "1" Ruutu
    Vankila "1" -- "1" Ruutu
    Sattuma "3" -- "1" Ruutu
    Yhteismaa "3" -- "1" Ruutu
    Sijainti "1" -- "1" Vankila
    Sijainti "1" -- "1" Aloitusruutu
    Toiminto "1" -- "m" Ruutu
    Kortti "1" -- "m" Toiminto
    Sattuma "1" -- "1" Kortti
    Yhteismaa "1" -- "1" Kortti
    Katu "m" -- "1" Ruutu
    Katu "1" -- "4" Talo
    Katu "1" -- "1" Hotelli
    Katu "1" -- "2" Toiminto




    

```
