import pandas as pd 
import matplotlib.pyplot as plt

try:
    df = pd.read_csv(r'finanzas2020[1].csv',sep='\t')
except:
    print('El fichero no existe.')
else:
    meses = list(df.columns)

    if len(meses) == 12:
        columna_vacía = False
        for mes in meses:
            if df[mes].empty:
                columna_vacía = True
                break

        if not columna_vacía:
            gastos_por_mes = []
            ingresos_por_mes = []

            for mes in meses:
                gastos = 0
                ingresos = 0
                for i in df[mes]:
                    try:
                        if int(i) < 0:
                            gastos += int(i)
                        else:
                            ingresos += int(i)
                    except:
                        continue
                gastos_por_mes.append(abs(gastos))
                ingresos_por_mes.append(ingresos)

            mayores_gastos = gastos_por_mes[0]
            mayores_ingresos = ingresos_por_mes[0]
            mes_mayores_gastos = meses[0]
            mes_mayores_ingresos = meses[0]
            for mes, gastos, ingresos in zip(meses,gastos_por_mes,ingresos_por_mes):
                if gastos > mayores_gastos:
                    mayores_gastos = gastos
                    mes_mayores_gastos = mes 
                if ingresos > mayores_ingresos:
                    mayores_ingresos = ingresos 
                    mes_mayores_ingresos = mes 

            print(f'El mes en que más se ha gastado ha sido {mes_mayores_gastos}.')
            print(f'El mes en que más se ha ahorrado ha sido {mes_mayores_ingresos}.')

            media_gastos = round(sum(gastos_por_mes) / 12)
            print(f'La media anual de gastos ha sido {media_gastos}.')

            gasto_total = sum(gastos_por_mes)
            print(f'El gasto anual total ha sido {gasto_total}.')

            ingresos_totales = sum(ingresos_por_mes)
            print(f'Los ingresos anuales totales han sido {ingresos_totales}.')

            plt.plot(meses,ingresos_por_mes)
            plt.xlabel('Mes')
            plt.ylabel('Ingresos')
            plt.title('Evolución de los ingresos a lo largo del año')
            plt.show()
        else:
            print('El fichero no debe contener columnas vacías.')       
    else:
        print('El fichero debe tener 12 columnas, una para cada mes del año.')