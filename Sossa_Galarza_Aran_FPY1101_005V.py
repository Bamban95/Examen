import csv
import random
import statistics
import pandas as pd


empleados = ['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez']


def asignar_sueldos_aleatorios():
    for empleado in empleados:
        empleado['sueldo'] = random.randint(300000, 2500000)
    print("Se han asignado los  sueldos aleatorios a los Trabajadores.")


def clasificar_sueldos():
    bajos, medios, altos = [], [], []
    for empleado in empleados:
        sueldo = empleado['sueldo']
        if sueldo < 800000:
            bajos.append(empleado)
        elif sueldo <= 2000000:
            medios.append(empleado)
        else:
            altos.append(empleado)
   
    print("\nSueldos menores a $800,000 TOTAL: {}".format(len(bajos)))
    print("{:<20} {:<20} {:<20}".format("Nombre empleado","Sueldo"))
    for emp in bajos:
        print("{:<20} {:<20} ${:<20,.1f}".format(emp['nombre'], emp['sueldo']))
   
    print("\nSueldos entre $800,000 y $2,000,000 TOTAL: {}".format(len(medios)))
    print("{:<20} {:<20} {:<20}".format("Nombre empleado", "Sueldo"))
    for emp in medios:
        print("{:<20} {:<20} ${:<20,.1f}".format(emp['nombre'], emp['sueldo']))
   
    print("\nSueldos mayores a $2,000,000 TOTAL: {}".format(len(altos)))
    print("{:<20} {:<20} {:<20}".format("Nombre empleado", "Sueldo"))
    for emp in altos:
        print("{:<20} {:<20} ${:<20,.1f}".format(emp['nombre'], emp['sueldo']))
   
    total_sueldos = sum(emp['sueldo'] for emp in empleados)
    print("\nTOTAL SUELDOS: ${:,.1f}".format(total_sueldos))




def ver_estadisticas():
    sueldos = [emp['sueldo'] for emp in empleados]
    sueldo_promedio = statistics.mean(sueldos)
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    print(f"\nSueldo promedio: ${sueldo_promedio:,.1f}")
    print(f"Sueldo mas alto: ${sueldo_maximo:,.1f}")
    print(f"Sueldo mas bajo: ${sueldo_minimo:,.1f}")


def reporte_sueldos():
    data = []
    for empleado in empleados:
        sueldo = empleado['sueldo']
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        data.append([empleado['nombre'], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
   
    df = pd.DataFrame(data, columns=["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
    df = df.sort_values(by="Sueldo Base", ascending=False)


    df["Sueldo Base"] = df["Sueldo Base"].apply(lambda x: f"${x:,.1f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    df["Descuento Salud"] = df["Descuento Salud"].apply(lambda x: f"${x:,.1f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    df["Descuento AFP"] = df["Descuento AFP"].apply(lambda x: f"${x:,.1f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    df["Sueldo Liquido"] = df["Sueldo Liquido"].apply(lambda x: f"${x:,.1f}".replace(',', 'X').replace('.', ',').replace('X', '.'))


    df.to_csv('reporte_sueldos.csv', index=False)
    print("\nReporte de sueldos generado.")
    print(df.to_string(index=False))


    print("\nPrimeras filas del reporte:")
    print(df.head().to_string(index=False))




def main():
    while True:
        print("\nMenu Empresarial:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir")
        opc = input("Seleccione una opcion: ")
       
        try:
            if opc == '1':
                asignar_sueldos_aleatorios()
            elif opc == '2':
                clasificar_sueldos()
            elif opc == '3':
                ver_estadisticas()
            elif opc == '4':
                reporte_sueldos()
            elif opc == '5':
                print("Finalizando Programa...")
                print("Desarrollado por Aran Sossa Galarza")
                print("RUT 24.609.198-6")
                break
            else:
                print("Opcion no valida, intente de nuevo.")
        except Exception as e:
            print(f"Ocurrio un error: {e}")


if __name__ == "__main__":
    main()