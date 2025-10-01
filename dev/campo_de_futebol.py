KM2_PARA_M2 = 1_000_000
AREA_CAMPO_M2 = 100 * 60
area_desvastada_Km2 = float(input("Digite a área desvastada em Km²: "))
area_total_desmatada_m2 = area_desvastada_Km2 * (1000**2)
area_campo_futebol = area_total_desmatada_m2 / AREA_CAMPO_M2
print(f"A área desmatada {area_desvastada_Km2:,.2f} km² equivale a {area_campo_futebol:,.2f} campos de futebol.")

