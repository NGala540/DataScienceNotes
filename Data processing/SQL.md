# Feature Engeneering

przeteważanie surowych danych w celu uzyskania cech które poprawią nam model (np. zamiana time na dzni tygodnia)

# Relacyjne bazy danych

posiadają relacje między bazami, np. wypożyczenia i samochody, 

<b>
Primary key
</b>
- musi być unikalny ale nie koniecznie między tabelami, nie może się skończyć

**Foreign key** - primary key innej tabeli, wrzucamy wszędzie tam gdzie jest sens dowiązać inne tabela (np. Książka - Autor)



**Rodzaje relacji**

- jeden do jednego - jeden rekord tabeli A jest powiązany z jednym rekordem tabeli B (np. jedna osoba -> jedno prawojazdy)

- jeden do wielu - jeden rekord tabeli A może być powiązany z wieloma rekordami tabeli B (np. jeden klient -> wiele zazmówień)

- wiele do wielu - analogicznie, tylko z wykorzystaniem tabeli pomocniczej (np. Autor -> Książka/Autor <- Książka)
  
  

**Zasady projektowania tabel**

1. Określeie celu - odczyt vs zapis, wdłuż czy wszerz

2. Unikanie duplikowania danych - dodatkowe tabely etc.

3. Atomowość informacji - jak najmniejsza ilość informacji w ramach jednej komórki (np. rozbijanie adresu, wartość tranzakcji i waluta)

4. Multiplikowanie odwołań - rozbijanie wzdłóż (np. jeden produkt = jeden wiersz, przy zamówieniu), przydatne do uzyskiwania potrzebnych informacji

5. Unikanie pustych pól - puste komórki też ważą , lepiej wykorzystać dodatkową tabelę (np. kolumna/tabela Uwagi)
   
   

**Ciekawostki**

- Archiwizuje się dane przenosząc je do serwisu tańszego do utrzymania
  
  

# SQL

język zapytań, nie programowania, pod spodem jest c++, implementacje najbardziej różnią się UI i niuansami ale łatwo jest przełożyć między sobą 



**Rodzaje zadań**

- Definiowanie danych

- Manipulacja i modyfikowanie

- Kontrola dostępu

- Zarządzanie grupami zapytań

Dla Data Scientistów głównie SELECT, resztą zajmują się administratorzy i inżynierowie danych, inne statmenty są ograne przez interfejs



**DDL = Data Definition Language**

```sql
CREATE TABLE produkt(
    id INTEGER
    Nazwa VARCHAR(20)
    Producent VARCHAR(25)
)
```

Nazwy nie mogą kończyć się znakiem spacji, być nazwami specjalnymi itd.

Atrybuty:

- PRIMARY KEY

- NOT NULL

- AUTO_INCREMENT

- UNIQUE

_Są jeszcze inne przydatne komendy/ atrybuty w inernecie (Alter, Drop, Truncate)_

Klucze obce:

```sql
CREATE TABLE produkt(
    id INTEGER PRIMARY KEY,
    Nazwa VARCHAR(20),
    Producent VARCHAR(25),
    CONSTRAINT producentID_fk FOREIGN KEY (ProducentId)
REFERENCES Producent(Id)
)
```

ALTER  - można dodać klucz obcy w istniejącej tabeli



**Język modyfikacji danych**

- INSERT - dodanie wartości

- UPDATE - aktualizacja wartości

- DELETE - usuwanie wartości

- SELECT - pobieranie danych z tabeli

_Istnieją aliasy, operatory logiczne i równości również słowne oraz zapytania zagnieżdżone_

_Where odpala się przy kązdym wierszu, więc nested jest drogi obliczeniowo_

_Limit nie zmniejsza złożoności obliczeniowej zapytania_



**Język kontroli dostępu**

- GRANT - dodaje uprawnienia, również do operacji

- REVOKE - odbiera uprawnienia



**Łączenie w bazach danych**

w jaki sposób łączyć - odpowiedni join, jeśli nazwy kolumn się powtarzają, potrzebujemy odwołania do odpowiedniej tabeli

![Isn't SQL A left join B, just A? - Stack Overflow](https://i.stack.imgur.com/4zjxm.png)

- INNER JOIN = JOIN

- W całej kwerendzie najpierw przebiega proces łączenia



# SQLAlchemy

Biblioteka Pythona do używania SQL,

Dwie warstwy:

- Core - pozwala łączyć się z bazą (daje API)

- ORM - mapowanie obiektowo-relacyjne

| ORM                       | SQL                                                   |
|:-------------------------:|:-----------------------------------------------------:|
| proste zapytania          | bardziej złożone operacje                             |
| dostęp do wielu bibliotek | wykorzystanie pełnego potencjału silnika bazodanowego |

**Połączenie z bazą** 

1. import sqlalchemy

2. create_engine + adres + echo (pozwala monitorować co się dzieje), ostrożnie z loginem i hasłem

3.  przypisanie do jakiegoś obiektu



**Podstawy ORMa**

każdą tabelę musimy opisać klasą, dodająć do tabeli tworzymy objekt tej klasy w ramach sesji później commitujemy zmiany



# Serializacja plików

ujednolicanie plików, plik zajmuje mniej miejsca, standaryzacja przy przenoszeniu/udostępnianiu - łatwiej wymieniać dane, konwersja w strumien bajtów objektu ale też np. modelu

**Pickle (nested data)**

biblioteka pickle: 

_serializacja_: pickle.dumps(dict)

 _deserialzacja_: pickle.loads(serial_dict)



# Pandas Profiling

generuje automatyczny raport umożliwiający explorację danych

```python
from pandas_profiling import ProfileReport

# Generate the Profiling Report
profile = ProfileReport(df, 
                        title="Titanic Dataset",
                        html={'style': {'full_width': True}}, 
                        sort="None")

# Save to file
profile.to_file('report.html')
```

_Warto zwrócić uwagę na dodatkowe atrybuty min. interakcja_

mamy:

- Ogólny opis danych

- Ostrzeżenia

- Opis kolumn

- Szczegóły

- Ogólnie dojebany raport



# API

Application programming interface - pozwala na czerpanie danych z innych serwisów (a także do komunikacji?), możemy pobierać dane w określonej formie

JSON - typ pliku, przypomina słownik, na podstawie JS

XML - stabilniejszy niż JSON, stosuje zagnieżdżenia

request - biblioteka pozwalająca, z poziomu pythona, odpytywać API

_Przykład w prezce - dane giełdowe_


