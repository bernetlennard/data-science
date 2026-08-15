import statistics


def calculate(modell):

    modell.sort()


    
    mittelwert = statistics.mean(modell)

    # 2. Median (entspricht dem 2. Quartil / 50 %-Quantil)
    median = statistics.median(modell)

    # 3. Quartile berechnen (n=4 teilt die Daten in 4 Teile -> 3 Schnittpunkte: Q1, Q2, Q3)
    quartile = statistics.quantiles(modell, n=4, method='inclusive')
    q1, q2, q3 = quartile

    print(f"Mittelwert: {mittelwert:.2f}")
    print(f"Unterers Quartil (Q1): {q1}")
    print(f"Median (Q2): {median} (oder über quantiles: {q2})")
    print(f"Oberes Quartil (Q3): {q3}")

modell_a = [54.8, 57.4, 55.3, 53.4, 52.6, 55.5, 52.4, 55.7, 57.0, 54.6]
modell_b = [45.2, 70.1, 52.3, 58.1, 69.5, 37.5, 55.4, 49.7, 46.6, 90.2]

print("Modell A")
calculate(modell_a)
print("Modell B")
calculate(modell_b)