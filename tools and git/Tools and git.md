1. Utwórz katalog o nazwie data w arpdatapl7
2. Utwórz pusty plik o nazwie backup.txt
3. Za pomocą vim/vi utwórz plik o nazwie imiona.txt i wpisz kilka imion do pliku (minimum 2)
4. Zapisz zmiany
5. Wyświetl tylko ostatnie 2 imiona.
6. Skopiuj trzy pierwsze imiona z imiona.txt do pliku backup.txt
7. Utwórz katalog o nazwie test, a w nim data
8. Skopiuj plik imiona.txt do data, a backup.txt do test/data
9. Zmień nazwę pliki imiona.txt w katalogu data na names.txt
10. Dodaj kolejne imiona do names.txt
11. Porównaj names.txt z imiona.txt
12. Skopiuj nowe linijki z names.txt do backup.txt



  152  mkdir data
  153  touch backup.txt
  154  vim imiona.txt
  155  cat imiona.txt
  156  tail -n 2 imiona.txt
  157  ls
  158  head -n 3 imiona.txt > backup.txt
  159  cat backup.txt
  160  mkdir test
  161  cd test
  162  mkdir data
  163  cd ..
  164  ls test
  165  ls -l
  166  cp imiona.txt ./data/
  167  cp backup.txt ./test/data/
  168  mv ./data/imiona.txt ./data/names.txt
  169  ls data
  170  vim ./data/names.txt
  171  cat ./data/names.txt
  172  ls
  173  diff imiona.txt ./data/names.txt
  174  tail -n 3 ./data/names.txt
  175  tail -n 3 ./data/names.txt >> backup.txt
  176  cat backup.txt



**Ładniejszy format git log:**  

git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

**Aby zastąpić klasyczne git log powyższym:**  

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

**i używać:**  

git lg
git lg -p

**Jak pracować ze zdalnym repozytorium:**  

1. [Git - Praca ze zdalnym repozytorium](https://git-scm.com/book/pl/v2/Podstawy-Gita-Praca-ze-zdalnym-repozytorium)

**Oraz dwa kompletne tutoriale z GITa po polsku!:**  

1. [Git tutorial | stash, rebase, commit, merge, checkout, push i clone - StormIT.pl &#x1f47d; &#x1f47e; &#x1f916;](https://stormit.pl/git/)
2. [git - prosty przewodnik - nic skomplikowanego!](https://rogerdudler.github.io/git-guide/index.pl.html)
