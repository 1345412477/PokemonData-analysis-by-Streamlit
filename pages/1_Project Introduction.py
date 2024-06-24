import streamlit as st
import pandas as pd

st.snow()
st.image('image/2.gif')
st.title('项目介绍')

st.subheader('Pokemon数据分析项目介绍')
custom_css = """
<style>
.indent {
    text-indent: 2em;
    margin-left: 0;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<p class="indent">随着信息技术的飞速发展，数据分析已成为当今各领域至关重要的手段。本次研究是基于streamlit的数据分析网站的应用，'
            '通过对大量相关数据的收集、整理和深入挖掘，运用多种数据分析方法和工具，揭示数据背后隐藏的模式、趋势和关系。研究结果表明，'
            '数据分析能够为决策提供有力支持，有效提升业务效率和竞争力，帮助企业和组织更好地理解市场动态、客户需求以及内部运营状况，'
            '同时为科学研究、社会管理等方面带来了新的机遇和突破，具有广泛的应用前景和重要的实践价值。</p>',
            unsafe_allow_html=True)

st.subheader('以下是此项目的成员及分工')
df = pd.DataFrame(
{
"姓名": ['唐珩', '吴涛', '吴宇皓'],
"年龄": [20, 20, 20],
"学号":["2022402050326","2022402050328","2022402050323"],
"分工": ["分配任务，完成项目整体框架及核心部分，对项目报告进行指导。",
        "完成项目的整体及报告部分，提出意见，确保页面的美观。", 
        "对完成的页面进行全面测试。收集测试过程中发现的问题，协助成员进行问题的修复。"]
}
)

st.dataframe(df)
