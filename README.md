**#ZAŁOŻENIA**  
Oto wizualizacja pierwszych 100 milionów miejsc liczby pi  


**#JAK DZIAŁA**  

#Przy kompresji 6:  
Bierzemy sobie część liczby pi np: 314159  
Następnie dzielimy na 3 pakiety: 31 41 69 i przeskalowujemy je do 255, daje to: 80 106 152  
Czyli:  
Red = 80  
Green = 106  
Blue = 152  

I robimy tak dla każdego piksela  

#WZÓR  
wzór na skalowanie w kompresji 3:  
[round((c / 10) * 255) for c in colorDane]  
  

#Przy kompresji 3:  
Robimy to samo ale zamiast robić pakiety po 2 liczby robimy po 1 np: 3 1 4 zamiast 31 41 69  


**#DALSZE INFO**  
utworzono o 4.09.2026 18.02

**#STORYTIME**  
nudziło mi się na historii i informatyce i jakoś ten pomysł powstał  
