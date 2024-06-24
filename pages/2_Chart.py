import streamlit as st

from pages import (data_overview,
                   plot_scatter,
                   correlation_heatmap,
                   type_evolution,
                   pokemon_basic_value,
                   plot_pie,boxplot_stats,
                   swarm_legendary,
                   violin_attack,
                   boxplot_attack,
)
def chart():
    PAGES = {
            "Pokemon数据概览":data_overview,
            "不同属性Pokemon防御和攻击对比":plot_scatter,
            "Pokemon属性相关性热图":correlation_heatmap,
            "不同世代Pokemon类型的演变":type_evolution,
            "Pokemon基础数值直方图":pokemon_basic_value,
            "不同类型Pokemon百分比":plot_pie,
            "Pokemon属性的箱线图":boxplot_stats,
            "不同Pokemon类型的总数和传奇状态":swarm_legendary,
            "Pokemon攻击力的小提琴图":violin_attack,
            "Pokemon攻击力的箱线图":boxplot_attack,
        }
    if st.session_state["authentication_status"]:
        page = st.sidebar.radio('Pokemon', list(PAGES.keys()))
        PAGES[page]()
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    chart()