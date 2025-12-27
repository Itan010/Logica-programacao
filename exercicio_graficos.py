import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configurações visuais
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Carregar os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Visualizar as primeiras linhas e informações do dataset
print("=== PRIMEIRAS LINHAS DO DATASET ===")
print(df.head())
print("\n" + "="*60)

print("\n=== INFORMAÇÕES DO DATASET ===")
print(df.info())
print("\n" + "="*60)

print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df.describe())
print("\n" + "="*60)

print("\n=== VERIFICANDO VALORES NULOS ===")
print(df.isnull().sum())
print("\n" + "="*60)

# Análise exploratória das colunas
print("\n=== ANÁLISE DAS COLUNAS ===")
for col in df.columns:
    print(f"\nColuna: {col}")
    print(f"Tipo: {df[col].dtype}")
    print(f"Valores únicos: {df[col].nunique()}")
    if df[col].dtype in ['int64', 'float64']:
        print(f"Média: {df[col].mean():.2f}")
        print(f"Mediana: {df[col].median():.2f}")

# 1. GRÁFICO DE HISTOGRAMA
plt.figure(figsize=(15, 12))

# Supondo que temos colunas numéricas como 'valor_total', 'quantidade', 'idade_cliente', etc.
# Vou usar exemplos baseados em dados típicos de e-commerce

# Verificar quais colunas numéricas estão disponíveis
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"Colunas numéricas disponíveis: {numeric_cols}")

# Criar histogramas para as principais colunas numéricas
if len(numeric_cols) >= 3:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    for i, col in enumerate(numeric_cols[:4]):
        ax = axes[i // 2, i % 2]
        ax.hist(df[col].dropna(), bins=30, edgecolor='black', alpha=0.7)
        ax.set_title(f'Distribuição de {col}', fontsize=14, fontweight='bold')
        ax.set_xlabel(col)
        ax.set_ylabel('Frequência')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('histogramas_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

# 2. GRÁFICO DE DISPERSÃO
plt.figure(figsize=(12, 8))

if len(numeric_cols) >= 2:
    # Usar as duas primeiras colunas numéricas para dispersão
    x_col, y_col = numeric_cols[0], numeric_cols[1]

    plt.scatter(df[x_col], df[y_col], alpha=0.6, c='steelblue', edgecolor='black')
    plt.title(f'Relação entre {x_col} e {y_col}', fontsize=16, fontweight='bold')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)

    # Adicionar linha de tendência
    z = np.polyfit(df[x_col].dropna(), df[y_col].dropna(), 1)
    p = np.poly1d(z)
    plt.plot(df[x_col].sort_values(), p(df[x_col].sort_values()), "r--", alpha=0.8)

    plt.savefig('dispersao_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

#  3. MAPA DE CALOR (CORRELAÇÃO)
plt.figure(figsize=(12, 10))

if len(numeric_cols) > 1:
    # Calcular matriz de correlação
    correlation_matrix = df[numeric_cols].corr()

    # Criar mapa de calor
    sns.heatmap(correlation_matrix,
                annot=True,
                cmap='coolwarm',
                center=0,
                fmt='.2f',
                linewidths=1,
                square=True,
                cbar_kws={"shrink": 0.8})

    plt.title('Mapa de Calor - Correlação entre Variáveis',
              fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)

    plt.savefig('mapa_calor_correlacao.png', dpi=300, bbox_inches='tight')
    plt.show()

#  4. GRÁFICO DE BARRA
plt.figure(figsize=(14, 8))

# Verificar colunas categóricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"Colunas categóricas disponíveis: {categorical_cols}")

if categorical_cols:
    # Usar a primeira coluna categórica para gráfico de barras
    cat_col = categorical_cols[0]

    # Contar frequência das categorias (pegar top 10 se houver muitas)
    value_counts = df[cat_col].value_counts().head(10)

    bars = plt.bar(range(len(value_counts)), value_counts.values,
                   color=plt.cm.Set3(np.arange(len(value_counts))))

    plt.title(f'Distribuição de {cat_col}', fontsize=16, fontweight='bold')
    plt.xlabel(cat_col)
    plt.ylabel('Contagem')
    plt.xticks(range(len(value_counts)),
               [str(x)[:15] + '...' if len(str(x)) > 15 else str(x)
                for x in value_counts.index],
               rotation=45, ha='right')

    # Adicionar valores nas barras
    for i, v in enumerate(value_counts.values):
        plt.text(i, v + 0.01 * max(value_counts.values),
                 str(v), ha='center', fontweight='bold')

    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('grafico_barras_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

#  5. GRÁFICO DE PIZZA
plt.figure(figsize=(12, 10))

if categorical_cols:
    # Usar outra coluna categórica ou a mesma para pizza
    if len(categorical_cols) > 1:
        cat_col_pizza = categorical_cols[1]
    else:
        cat_col_pizza = categorical_cols[0]

    # Pegar top 5 categorias para pizza
    value_counts_pizza = df[cat_col_pizza].value_counts().head(5)

    # Criar gráfico de pizza
    colors = plt.cm.Pastel1(np.arange(len(value_counts_pizza)))
    wedges, texts, autotexts = plt.pie(value_counts_pizza.values,
                                       labels=value_counts_pizza.index,
                                       colors=colors,
                                       autopct='%1.1f%%',
                                       startangle=90,
                                       textprops={'fontsize': 10})

    # Melhorar aparência
    plt.title(f'Proporção de {cat_col_pizza} (Top 5)',
              fontsize=16, fontweight='bold', pad=20)

    # Ajustar textos
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')

    plt.axis('equal')  # Garantir que seja um círculo
    plt.savefig('grafico_pizza_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

#  6. GRÁFICO DE DENSIDADE
plt.figure(figsize=(14, 8))

if len(numeric_cols) >= 1:
    # Criar subplots para múltiplas densidades
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    for i, col in enumerate(numeric_cols[:4]):
        ax = axes[i]

        # Gráfico de densidade
        sns.kdeplot(data=df[col].dropna(),
                    ax=ax,
                    fill=True,
                    alpha=0.6,
                    linewidth=2)

        # Adicionar linha da média
        mean_val = df[col].mean()
        ax.axvline(mean_val, color='red', linestyle='--',
                   label=f'Média: {mean_val:.2f}')

        ax.set_title(f'Densidade de {col}', fontsize=12, fontweight='bold')
        ax.set_xlabel(col)
        ax.set_ylabel('Densidade')
        ax.legend()
        ax.grid(True, alpha=0.3)

    # Remover eixos vazios se necessário
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.suptitle('Gráficos de Densidade - Distribuição das Variáveis',
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('densidade_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

#  7. GRÁFICO DE REGRESSÃO
plt.figure(figsize=(12, 8))

if len(numeric_cols) >= 2:
    # Escolher duas variáveis para regressão
    x_col_reg, y_col_reg = numeric_cols[0], numeric_cols[1]

    # Criar gráfico de regressão com seaborn
    sns.regplot(x=x_col_reg, y=y_col_reg, data=df,
                scatter_kws={'alpha': 0.6, 'edgecolor': 'black'},
                line_kws={'color': 'red', 'linewidth': 2},
                ci=95)  # Intervalo de confiança de 95%

    plt.title(f'Regressão Linear: {y_col_reg} vs {x_col_reg}',
              fontsize=16, fontweight='bold')
    plt.xlabel(x_col_reg)
    plt.ylabel(y_col_reg)
    plt.grid(True, alpha=0.3)

    # Calcular e mostrar estatísticas de regressão
    x_vals = df[x_col_reg].dropna()
    y_vals = df[y_col_reg].dropna()

    if len(x_vals) > 1 and len(y_vals) > 1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_vals, y_vals)

        # Adicionar texto com estatísticas
        stats_text = (f'Equação: y = {slope:.2f}x + {intercept:.2f}\n'
                      f'R² = {r_value ** 2:.3f}\n'
                      f'p-valor = {p_value:.4f}')

        plt.text(0.05, 0.95, stats_text,
                 transform=plt.gca().transAxes,
                 fontsize=10,
                 verticalalignment='top',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.savefig('regressao_ecommerce.png', dpi=300, bbox_inches='tight')
    plt.show()

#  ANÁLISE DETALHADA
print("\n" + "=" * 60)
print("ANÁLISE DETALHADA DOS DADOS DE E-COMMERCE")
print("=" * 60)

# Análise de insights principais
print("\nPRINCIPAIS INSIGHTS:")
print("-" * 40)

# 1. Análise de correlações fortes
if len(numeric_cols) > 1:
    print("\n1. CORRELAÇÕES SIGNIFICATIVAS:")
    corr_matrix = df[numeric_cols].corr()
    for i in range(len(numeric_cols)):
        for j in range(i + 1, len(numeric_cols)):
            corr_value = corr_matrix.iloc[i, j]
            if abs(corr_value) > 0.5:  # Correlação moderada/forte
                print(f"   • {numeric_cols[i]} vs {numeric_cols[j]}: {corr_value:.3f}")

# 2. Análise de distribuição
print("\n2. DISTRIBUIÇÃO DAS VARIÁVEIS:")
for col in numeric_cols[:3]:
    skewness = df[col].skew()
    if abs(skewness) > 1:
        print(f"   • {col}: Distribuição assimétrica (skewness: {skewness:.2f})")
    else:
        print(f"   • {col}: Distribuição relativamente simétrica (skewness: {skewness:.2f})")

# 3. Valores atípicos
print("\n3. DETECÇÃO DE VALORES ATÍPICOS:")
for col in numeric_cols[:3]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    if len(outliers) > 0:
        print(f"   • {col}: {len(outliers)} valores atípicos detectados "
              f"({len(outliers) / len(df) * 100:.1f}% dos dados)")

# 4. Recomendações baseadas nos dados
print("\n4. RECOMENDAÇÕES PARA ANÁLISE:")
print("   • Focar nas variáveis com maior correlação para modelos preditivos")
print("   • Investigar valores atípicos para entender comportamentos excepcionais")
print("   • Considerar transformações para variáveis muito assimétricas")
print("   • Analisar categorias dominantes para estratégias de marketing")

# Salvar resumo das análises
analysis_summary = {
    'total_registros': len(df),
    'total_colunas': len(df.columns),
    'colunas_numericas': len(numeric_cols),
    'colunas_categoricas': len(categorical_cols),
    'dados_faltantes': df.isnull().sum().sum(),
    'percentual_faltantes': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
}

print("\n" + "=" * 60)
print("RESUMO ESTATÍSTICO DO DATASET")
print("=" * 60)
for key, value in analysis_summary.items():
    if 'percentual' in key:
        print(f"{key.replace('_', ' ').title()}: {value:.2f}%")
    else:
        print(f"{key.replace('_', ' ').title()}: {value}")

print("\nGráficos salvos como:")
print("1. histogramas_ecommerce.png")
print("2. dispersao_ecommerce.png")
print("3. mapa_calor_correlacao.png")
print("4. grafico_barras_ecommerce.png")
print("5. grafico_pizza_ecommerce.png")
print("6. densidade_ecommerce.png")
print("7. regressao_ecommerce.png")
