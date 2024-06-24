import streamlit as st

st.title('致谢')
# 定义首行缩进的CSS样式
custom_css = """
<style>
.indent {
    text-indent: 2em;
    margin-left: 0;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<p class="indent">经过我们的不懈努力，Pokemon数据分析终于接近了尾声。在此，我们首先要感谢王家老师。'
            '王家老师无论是在课程学习上，还是在学术研究上，亦或是是在项目实践中，都给予了我们很大的帮助，'
            '这些影响都将会使我们受益终身。没有王家老师的谆谆教海和悉心指导就不会有我们这么多的成长，'
            '更不会有此次项目的圆满完成。另外，要感谢同学们，在学习和实践中我们都一起探讨和交流，'
            '也从他们身上学到了很多。最后，借此机会，还要感谢家人们的支持，他们在我们的学业和未来中付出了很多心血，'
            '我们努力的最大动力也都来自于他们。</p>',
            unsafe_allow_html=True)
st.image('https://www.pokemon.cn/play/resources/pokedex/img/pm/0783062d0d860b8ae7d8e859241a700359c4d981.png', width=450)
