import streamlit as st
import plotly.graph_objects as go

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================
st.set_page_config(
    page_title="Soma de uma PG Infinita",
    page_icon="🍫",
    layout="wide"
)

# ============================================
# CSS PERSONALIZADO
# ============================================
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1.05rem;
        color: #555;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .concept-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.2rem;
        border-left: 4px solid #e74c3c;
        margin-bottom: 1rem;
    }
    .step-box {
        background: #fff8e1;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# FUNÇÃO DE PLOTAGEM (BARRA GEOMÉTRICA)
# ============================================
def plot_barra_pg(n_passos):
    fig = go.Figure()
    
    # Cores chamativas para cada pedaço da PG
    cores = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#e91e63', '#34495e', '#d35400', '#16a085']
    
    pos_atual = 0.0
    soma_parcial = 0.0
    
    # Desenhando os blocos da barra de tamanho 1
    for i in range(n_passos):
        tamanho = 1.0 / (2 ** (i + 1))
        soma_parcial += tamanho
        cor = cores[i % len(cores)]
        
        # Adiciona o retângulo representando o pedaço da PG
        fig.add_trace(go.Bar(
            x=[tamanho],
            y=['Barra Total (Valor = 1)'],
            orientation='h',
            base=pos_atual,
            marker=dict(color=cor, line=dict(color='white', width=1.5)),
            text=f"1/{2**(i+1)}",
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(color='white', size=13, family="Arial Black"),
            hovertemplate=f"Passo {i+1}<br>Fração: 1/{2**(i+1)} ({tamanho:.4f})<br>Soma acumulada: {soma_parcial:.4f}<extra></extra>",
            showlegend=False
        ))
        pos_atual += tamanho

    # Espaço restante que falta para fechar o número 1
    falta = 1.0 - soma_parcial
    if falta > 0.00001:
        # CORREÇÃO AQUI: Removido o parâmetro 'dash' que causava incompatibilidade no go.Bar
        fig.add_trace(go.Bar(
            x=[falta],
            y=['Barra Total (Valor = 1)'],
            orientation='h',
            base=pos_atual,
            marker=dict(color='#ecf0f1', line=dict(color='#bdc3c7', width=1)),
            text=f"Falta ({falta:.3f})" if falta > 0.05 else "",
            textposition='inside',
            hoverinfo='skip',
            showlegend=False
        ))

    fig.update_layout(
        barmode='stack',
        xaxis=dict(range=[0, 1.05], dtick=0.1, gridcolor='#e0e0e0'),
        yaxis=dict(showticklabels=False),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=20, r=20, t=30, b=20),
        height=200
    )
    return fig, soma_parcial

# ============================================
# TÍTULO E MENU LATERAL
# ============================================
st.markdown('<div class="main-title">🍫 O Paradoxo da Soma Infinita</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Como a soma de infinitas frações pode resultar em um número inteiro?</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Controles da Simulação")
    n_passos = st.slider("Quantidade de divisões (Passos da PG)", 1, 10, 4, step=1)
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.9rem; color: #555;">
        <b>A Regra da PG:</b><br>
        Primeiro termo ($a_1$) = 1/2<br>
        Razão ($q$) = 1/2<br><br>
        A cada passo, pegamos a metade do que sobrou da barra!
    </div>
    """, unsafe_allow_html=True)

# ============================================
# CONTEÚDO PRINCIPAL
# ============================================
st.markdown("""
<div class="concept-card">
    <b>O Paradoxo de Zenão Visualizado:</b> Imagine que você tem uma barra de chocolate de <b>tamanho 1</b>. 
    Você come metade (1/2). Depois, come a metade do que sobrou (1/4). Depois a metade do resto (1/8), e assim por diante, 
    <b>para todo o sempre (infinitas vezes)</b>. Será que o chocolate acaba? O gráfico abaixo prova que sim!
</div>
""", unsafe_allow_html=True)

col_graf, col_calc = st.columns([2, 1])

with col_graf:
    fig, soma_atual = plot_barra_pg(n_passos)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div style="text-align: center; font-size: 1.2rem; margin-top: 10px;">
        Soma acumulada após <b>{n_passos}</b> passos: <b style="color: #27ae60;">{soma_atual:.6f}</b>
    </div>
    """, unsafe_allow_html=True)

with col_calc:
    st.subheader("🧮 A Matemática por Trás")
    
    st.markdown("""
    <div style="font-size: 1.05rem; line-height: 1.8;">
        Fórmula da Soma Infinita:
        $$ S = \\frac{a_1}{1 - q} $$
        
        Substituindo os valores ($a_1 = \\frac{1}{2}$ e $q = \\frac{1}{2}$):
        $$ S = \\frac{\\frac{1}{2}}{1 - \\frac{1}{2}} = \\frac{\\frac{1}{2}}{\\frac{1}{2}} = \\mathbf{1} $$
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Seção interativa extra: Outro gerador de inteiro (ex: resultado 2)
st.subheader("✨ E se quisermos que o resultado seja 2?")
st.markdown("Basta mudar o primeiro termo! Se começarmos com **1**, e formos somando as metades ($1 + 1/2 + 1/4 + 1/8 + \dots$), a soma total fechará exatamente em **2**.")

col_ex1, col_ex2 = st.columns([1, 2])
with col_ex1:
    a1_ex = st.slider("Escolha o 1º termo (a₁)", 0.5, 2.0, 1.0, step=0.5)
    razao_ex = 0.5
    soma_total_ex = a1_ex / (1 - razao_ex)
    st.markdown(f"**Soma Limite (Infinitita):** <span style='font-size: 1.4rem; color: #e74c3c;'><b>{soma_total_ex:.1f}</b></span> (Número Inteiro!)", unsafe_allow_html=True)

with col_ex2:
    st.markdown("""
    <div class="step-box">
        <b>Por que isso é fascinante para os alunos?</b><br>
        Isso quebra a intuição inicial de que <i>"somar infinitas coisas faz o número explodir para o infinito"</i>. 
        Se os termos decrescem rápido o suficiente (razão entre 0 e 1), o infinito cabe perfeitamente dentro de um número inteiro finito!
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.85rem; padding: 1rem;">
    🍫 <b>Matemática Visual</b> — Mostrando que o infinito pode caber em um número inteiro.
</div>
""", unsafe_allow_html=True)
