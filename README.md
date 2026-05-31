# Colorlink+
#### Autor: Witold Kwidziński

# Spis treści
### 1. Informacje
- Instalacja
- Wykorzystane technologie
- O czym jest aplikacja?
### 2. Zawartość Aplikacji
- Menu główne
- Solve (Generowanie łamigłówek)
- Create (Sprawdzanie łamigłówek)

### 3. Techniczna analiza
- Przetestowane algorytmy
- Algorytm użyty w aplikacji
- Analiza innych algorytmów
- Potencjalne problemy

### 4. Wnioski


# 1. Informacje
## Instalacja
1. Sklonuj repozytorium:

```
git clone https://github.com/witold-kwidzinski-ug/Inteligencja-Obliczeniowa-Projekt.git 
  
cd Inteligencja-Obliczeniowa-Projekt
```
2. Zainstaluj potrzebne paczki:

``` pip install -r requirements.txt ```
3. Uruchom aplikację:

` python main.py `

## Wykorzystane technologie

- Python 3.11
- Pygame
- PyGAD
- Random
- Math
- Collections (deque)

## O czym jest aplikacja?
Głównym celem aplikacji jest umożliwienie generowania i tworzenia łamigłówek typu [Numberlink](https://en.wikipedia.org/wiki/Numberlink).

W skrócie, łamigłówka polega na połączeniu każdej pary punktów tego samego koloru ciągłą ścieżką w taki sposób, aby ścieżki się nie przecinały. Rozwiązanie jest poprawne, gdy wszystkie pary zostaną połączone.

Aby zrealizować cel, przetestowano kilka algorytmów, żeby zoptymalizować znalezienie rozwiązania.

# 2. Zawartość aplikacji
## Menu główne
W Menu głównym dostępne są dwie opcje do wyboru: Solve i Create.

## Solve (Generowanie łamigłówek)
Na początku trzeba wybrać odpowiednie parametry dla łamigłówki. Do wyboru są:
- rozmiar planszy (od 5x5 do 10x10)
- ilość kolorów (od 3 do 10)

Po zatwierdzeniu parametrów tworzona jest unikatowa łamigłówka, którą da się ukończyć.

## Create (Tworzenie łamigłówek)
Po wyborze rozmiaru planszy pokazuje się plansza i możliwe do wykorzystania punkty.
Można dobrowolnie je umieszczać na planszy, ale zawsze muszą się znaleźć pary tego samego koloru.
Po wciśnięciu na przycisk "Verify" wbudowany rozwiązywacz sprawdzi, czy zbudowana łamigłówka jest rozwiązywalna.

# 3. Techniczna analiza
## Przetestowane algorytmy
W ramach eksperymentu przetestowałem 4 algorytmy: DFS (Depth-First Search), GA (Genetic Algorithm), BFS (Breadth-First Search) i SA (Simulated Annealing).
Wydawały się najbardziej ciekawymi i możliwymi do zrealizowania algorytmami do rozwiązywania problemu. 

Każdy algorytm został uruchomiony 5 razy dla losowo wygenerowanych łamigłówek o danym rozmiarze planszy. W tabeli przedstawiono średni czas wykonania oraz liczbę poprawnie rozwiązanych łamigłówek. Oto wyniki:

| Algorytm | 5x5 | 6x6 | 7x7 |
| -------- |-----|-----|-----|
| DFS | 0.0002s (5/5) | 0.001 (5/5) | 0.001 (5/5) |
| GA | 0.0s (0/5) | 0.0s (0/5) | 0.0s (0/5) |
| BFS | 0.0008s (5/5) | 0.017s (4/5) | 2.09s (3/5) |
| SA | 0.0s (0/5) | 0.0s (0/5) | 0.0s (0/5) |

## Algorytm użyty w aplikacji
Spośród czterech algorytmów najlepszy okazał się DFS. Bardzo szybko znajdował rozwiązanie i radził sobie dobrze z coraz większymi planszami. Także udało mu się rozwiązać wszystkie plansze. Głównym powodem są heurestyki dodane do algorytmów:
- sortowanie kolorów według odległości między punktami
- wybór punktu początkowego o największej liczbie sąsiadujących przeszkód
- sprawdzanie osiągalności punktów za pomocą BFS
- preferowanie ruchów zmniejszających odległość od celu

## Analiza innych algorytmów
### BFS
Ten algorytm po DFSie miał najlepsze wyniki. W miare szybko znajdował rozwiązanie, choć czasami zdarzało mu się go nie znaleźć. Problemem tego algorytmu jest jego prędkość przy większych planszach. Ilość czasu i zasobów potrzebna do znalezienia rozwiązania eksponentalnie wzrasta z każdym rozmiarem planszy, przez co coraz bardziej traci na optymalności.

### GA i SA
Algorytmy GA i SA wykorzystywały reprezentację rozwiązania jako listę ruchów dla poszczególnych kolorów. Takie podejście powodowało powstawanie wielu niepoprawnych ścieżek, przez co algorytmy miały trudność ze znalezieniem poprawnego rozwiązania w rozsądnym czasie. W przyszłości można zastosować bardziej zaawansowaną reprezentację stanu lub funkcję oceny uwzględniającą strukturę planszy.
## Potencjalne problemy
### Generator plansz
Algorytm generowania plansz jest bardzo prosty, losuje punkty na planszy i sprawdza czy istnieje rozwiązanie. Przez to bardzo często rozwiązanie nie wymaga przejścia przez wszystkie kafelki. Można dodać konkretne wymagania, żeby stworzyć ciekawsze łamigłówki (np. ilość skrętów dla połączeń), ale w ramach eksperymentu i ciekawszych wyników postanowiłem zaimplementować najprostszy.

### Optymalność algorytmów
Algorytmy DFS i BFS już posiadają dodatkowe flagi, dzięki którym wykrywają złe ścieżki, dzięki czemu działają bardzo szybko. W przyszłości można dodać kolejne warunki, które przyspieszą algorytmy jeszcze bardziej.

# 4. Wnioski

Spośród przetestowanych algorytmów najlepsze wyniki osiągnął DFS. Dzięki zastosowaniu dodatkowych flag i sprawdzania osiągalności punktów końcowych był w stanie szybko znajdować rozwiązania nawet dla plansz o rozmiarze 9x9.

BFS również znajdował poprawne rozwiązania, jednak wraz ze wzrostem rozmiaru planszy jego wymagania pamięciowe i czasowe rosły znacznie szybciej.

Wyniki GA i SA nie oznaczają, że algorytmy te są nieprzydatne dla problemu Numberlink. W ramach projektu zastosowano uproszczoną reprezentację rozwiązania opartą na sekwencjach ruchów, która okazała się niewystarczająca do efektywnego eksplorowania przestrzeni rozwiązań.


W związku z tym w finalnej wersji aplikacji wykorzystano algorytm DFS.