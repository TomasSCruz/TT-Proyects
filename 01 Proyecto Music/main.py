# main.py

from src.data_preprocessing import load_data, clean_data, clean_data
from src.hypothesis_testing import hip_1, hip_2, hip_3

def main():
    # Cargamos y preprocesamos la tabla
    df = load_data('data/raw/dataset.csv')
    df = replace_wrong_values(df)   
    df = clean_data(df)

    # Ahora probamos las hipótesis
    hip_1(df)
    hip_2(df)
    hip_3(df)


if __name__ == '__main__':
    main()