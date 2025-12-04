import time

def sekundnik(czas_w_sekundach):
    for pozostało in range(czas_w_sekundach,0,-1):
        print(f"Pozostało {pozostało} sekund")
        time.sleep(1)  # pauza 1 sekunda
    print("Czas minął!")

sek = int(input("Podaj sekundnik: "))
sekundnik(sek)