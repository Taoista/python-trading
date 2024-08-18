import yfinance as yf
import matplotlib.pyplit as plt

def main():

    datos = yf.Ticker("MSFT").history(period="1y")

    precio = datos['Close']
    volumen = datos['Volume']

    print(datos)
    print(precio)

# def obtener_precio():
#     return False

if __name__ == "__main__":
    main()