# Datos completos desde cuartos hasta la final de Champions 2022
champions_2022 = {
    "cuartos de final": {
        "Resultados": [
            {
                "visitante": "Manchester City",
                "Local": "Atlético de Madrid",
                "Resultado": "1-0",
                "tarjetas": {
                    "rojas": "1",
                    "amarillas": "3"
                }
            },
            {
                "visitante": "Chelsea",
                "Local": "Real Madrid",
                "Resultado": "1-3",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "2"
                }
            },
            {
                "visitante": "Bayern Munich",
                "Local": "Villarreal",
                "Resultado": "1-0",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "4"
                }
            },
            {
                "visitante": "Benfica",
                "Local": "Liverpool",
                "Resultado": "1-3",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "3"
                }
            }
        ]
    },
    "semifinal": {
        "Resultados": [
            {
                "visitante": "Manchester City",
                "Local": "Real Madrid",
                "Resultado": "3-4",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "5"
                }
            },
            {
                "visitante": "Villarreal",
                "Local": "Liverpool",
                "Resultado": "2-3",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "4"
                }
            }
        ]
    },
    "final": {
        "Resultados": [
            {
                "visitante": "Liverpool",
                "Local": "Real Madrid",
                "Resultado": "0-1",
                "tarjetas": {
                    "rojas": "0",
                    "amarillas": "4"
                }
            }
        ]
    }
}

# Mostrar resultados y campeón
campeon = None

for fase, datos in champions_2022.items():
    print(f"\n{fase.upper()}")
    print("=" * 30)
    
    for partido in datos["Resultados"]:
        visitante = partido["visitante"]
        local = partido["Local"]
        resultado = partido["Resultado"]
        rojas = partido["tarjetas"]["rojas"]
        amarillas = partido["tarjetas"]["amarillas"]
        
        goles_local, goles_visitante = map(int, resultado.split('-'))
        if goles_local > goles_visitante:
            ganador = local
        elif goles_visitante > goles_local:
            ganador = visitante
        else:
            ganador = "Empate"
        
        print(f"Partido: {local} vs {visitante}")
        print(f"  Resultado: {resultado}")
        print(f"  Ganador: {ganador}")
        print(f"  Tarjetas Rojas: {rojas}")
        print(f"  Tarjetas Amarillas: {amarillas}")
        print("-" * 30)

        # Guardar el campeón al final
        if fase == "final":
            campeon = ganador

# Mostrar campeón
if campeon:
    print(f"\n🏆 CAMPEÓN DE LA CHAMPIONS 2022: {campeon.upper()} 🏆")
