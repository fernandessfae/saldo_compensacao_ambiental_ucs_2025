import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def is_dataframe(dataframe: pd.DataFrame) -> bool:
    return isinstance(dataframe, pd.DataFrame)

def exist_column_in_dataframe(
        dataframe: pd.DataFrame, column_name: str) -> bool:
    if column_name in dataframe.columns:
        return True
    return False

def is_integer(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def ensure_directory_exists(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
        return None
    return None

def generate_bar_chart_plot_top(df: pd.DataFrame, column: str,
                                number_top: str, title: str,
                                name_file: str) -> None:
    if not is_dataframe(df):
        print('Data is not a dataframe.')
        return None
    
    if not exist_column_in_dataframe(df, column):
        print('Column does not exist in dataframe.')
        return None
    
    if not is_integer(number_top):
        print('Number of top elements is not an integer.')
        return None
    
    top_count = df[column].value_counts().nlargest(int(number_top))
    df_top = pd.DataFrame(
        {column.capitalize(): top_count.index, 'Count': top_count.values})
    plt.figure(figsize=(15, 6))

    ensure_directory_exists('readme_images')

    sns.barplot(x='Count', y=column.capitalize(), data=df_top,
                palette='viridis', hue=column.capitalize(), legend=False)
    plt.title(title, loc='center', fontsize=20, fontweight='bold')
    plt.xlabel('Contagem')
    plt.ylabel(column.capitalize())
    plt.tight_layout()
    image_path: str = f'readme_images/{column.lower().replace(" ", "_")}_{name_file}.jpg'
    plt.savefig(image_path, dpi=300, bbox_inches="tight")
    return None


if __name__ == "__main__":

    df_ucs_compensation: pd.DataFrame = pd.read_excel(
        'data/recurso_compensacao_ambiental_ucs_2025.xlsx')

    #print(df_ucs_compensation.tail())

    # Remove rows with NaN values in 'Gerência Regional' column
    df_ucs_compensation.dropna(subset=['Gerência Regional'], inplace=True)

    print(df_ucs_compensation.tail())

    print(df_ucs_compensation.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        df_ucs_compensation.value_counts(
            subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(
        df_ucs_compensation, 'Unidade de Conservação impactada',
        '10','As 10 Unidades de Conservação que mais receberam empreendimentos',
        'brasil')

    print(
        df_ucs_compensation.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(df_ucs_compensation.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(df_ucs_compensation["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(df_ucs_compensation.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()

    generate_bar_chart_plot_top(df_ucs_compensation, 'Gerência Regional',
        '5','As gerências regionais que mais receberam empreendimentos',
        'brasil')
    
    # Separate dataframes for each 'Gerência Regional'
    gr1 = df_ucs_compensation.loc[
        df_ucs_compensation['Gerência Regional'] == 'GR1']
    gr2 = df_ucs_compensation.loc[
        df_ucs_compensation['Gerência Regional'] == 'GR2']
    gr3 = df_ucs_compensation.loc[
        df_ucs_compensation['Gerência Regional'] == 'GR3']
    gr4 = df_ucs_compensation.loc[
        df_ucs_compensation['Gerência Regional'] == 'GR4']
    gr5 = df_ucs_compensation.loc[
        df_ucs_compensation['Gerência Regional'] == 'GR5']

    # Data analysis for GR1    
    print(gr1.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        gr1.value_counts(subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(gr1, 'Unidade de Conservação impactada',
        '10', 'As 10 Unidades de Conservação que mais receberam empreendimentos na GR1',
        'gr1')

    print(gr1.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(gr1.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(gr1["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(gr1.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()

    # Data analysis for GR2
    print(gr2.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        gr2.value_counts(subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(gr2, 'Unidade de Conservação impactada',
        '10', 'As 10 Unidades de Conservação que mais receberam empreendimentos na GR2',
        'gr2')

    print(gr2.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(gr2.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(gr2["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(gr2.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()
    
    # Data analysis for GR3
    print(gr3.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        gr3.value_counts(subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(gr3, 'Unidade de Conservação impactada',
        '10', 'As 10 Unidades de Conservação que mais receberam empreendimentos na GR3',
        'gr3')

    print(gr3.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(gr3.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(gr3["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(gr3.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()

    # Data analysis for GR4
    print(gr4.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        gr4.value_counts(subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(gr4, 'Unidade de Conservação impactada',
        '10', 'As 10 Unidades de Conservação que mais receberam empreendimentos na GR4',
        'gr4')

    print(gr4.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(gr4.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(gr4["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(gr4.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()

    # Data analysis for GR5
    print(gr5.value_counts(
        subset='Unidade de Conservação impactada'))
    print()

    print(
        gr5.value_counts(subset='Unidade de Conservação impactada').nlargest(10))
    print()

    generate_bar_chart_plot_top(gr5, 'Unidade de Conservação impactada',
        '10', 'As 10 Unidades de Conservação que mais receberam empreendimentos na GR5',
        'gr5')

    print(gr5.value_counts(subset='Empreendimento').nlargest(10))
    print()

    print(gr5.value_counts(subset='Ação de aplicação'))
    print()

    print('Total compensação ambiental (R$): '\
          f'{round(gr5["Saldo Disponível (R$)"].sum(), 2)}')
    print()
    
    print(gr5.groupby('Unidade de Conservação impactada')[
        'Saldo Disponível (R$)'].sum().nlargest(10))
    print()