# Projekt Wykrywania Spamów

## Opis

Projekt Wykrywania Spamów to aplikacja API, która pozwala na klasyfikację czy tekst jest przypadkowym ciągiem znaków czy
nie.

## Instalacja

### Wymagania

- Python 3.8 lub wyższy
- pip

### Kroki

1. Sklonuj repozytorium na swoją lokalną maszynę.
2. Przejdź do katalogu projektu.
3. Zainstaluj wymagane zależności za pomocą pip:
    ```bash
    pip install -r requirements.txt
    ```

## Użycie

Aby skorzystać z wersji demonstracyjnej aplikacji API, musisz wysłać żądanie do adresu URL, pod którym jest hostowana
Twoja aplikacja. W Twoim przypadku, jeśli Twoja aplikacja jest hostowana na `sm-spam-detector.itech4.pl` i masz
trasę `/predict` w swojej aplikacji Flask, możesz uzyskać do niej dostęp w następujący sposób:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"texts": ["example text"]}' http://sm-spam-detector.itech4.pl/predict
```

W odpowiedzi otrzymasz JSON-a z kluczem `predictions`, który zawiera listę przewidywanych etykiet dla każdego tekstu.

## Rozwój

Jeśli chcesz rozwijać ten projekt, sklonuj repozytorium na swoją lokalną maszynę i zainstaluj wymagane zależności za
pomocą pip:

```bash
pip install -r requirements.txt
```

Następnie możesz zacząć rozwijać projekt, dodając nowe funkcje, poprawiając istniejące lub naprawiając błędy.

## Zasada działania

Projekt wykorzystuje różne algorytmy uczenia maszynowego do klasyfikacji czy tekst jest przypadkowym ciągiem znaków czy
nie.
W projekcie wykorzystano następujące algorytmy:

- CountVectorizer()
    - jest techniką przetwarzania języka naturalnego, która przekształca tekst na wektory liczbowe. Każde
      słowo w tekście jest traktowane jako cecha i liczba wystąpień tego słowa w tekście jest wartością cechy.
- MultinomialNB()
    - to implementacja algorytmu Naive Bayes dla cech wielomianowych. Jest to popularny algorytm do
      klasyfikacji tekstu, który działa na zasadzie "naiwnego" założenia o niezależności cech.

## Plan rozwoju

W przyszłości planujemy dodać więcej funkcji, takich jak możliwość personalizacji filtrów spamu przez użytkowników,
lepsze raportowanie i analizę wyników klasyfikacji oraz wsparcie dla większej liczby języków.

## FAQ

### Jak mogę skonfigurować swoje filtry spamu?

W tej chwili filtry spamu są predefiniowane i nie można ich dostosować. Pracujemy nad dodaniem tej funkcji w przyszłych wydaniach.

### Czy mogę użyć tego systemu do innych celów niż wykrywanie spamu?

Tak, możesz użyć tego systemu do innych celów niż wykrywanie spamu. Wystarczy, że zmienisz dane treningowe i dostosujesz
algorytmy klasyfikacji do swoich potrzeb.

## Autorzy

- [Patryk Rusak](https://www.linkedin.com/in/patryk-rusak/)
- [Maksymilian Zbroja](https://www.linkedin.com/in/maksymilian-zbroja/)
- [Szymon Warda](https://www.linkedin.com/in/szymon-warda-9a30ab289/)

## Licencja

[MIT](https://choosealicense.com/licenses/mit/)