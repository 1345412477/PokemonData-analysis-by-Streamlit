# 1. 主页配置
- 导入必要的库：Streamlit, streamlit_authenticator, seaborn, matplz`otlib, Pandas, numpy, yaml。
- 设置Streamlit主页配置，包括登录和标题。
```python
import streamlit as st
import streamlit_authenticator as stauth
import yaml

from streamlit_authenticator.utilities.exceptions import (CredentialsError,ForgotError,LoginError,RegisterError,ResetError,UpdateError) 

with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

#初始化认证器
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

def main():
    # 创建侧边栏登录
    try:
        authenticator.login()
    except LoginError as e:
        st.sidebar.error(e)


    # 根据登录状态显示页面
    if st.session_state["authentication_status"]:
        st.balloons()
        st.sidebar.success(f'Logged in as {st.session_state["name"]}')
        col1, col2 = st.columns([3, 1])
        with col1:
            st.title('登陆成功！')
            st.title(f'欢迎{st.session_state["name"]}!')
        with col2:
            st.image('image/1.gif',width=150)
        st.image('https://www.pokemon.cn/play/resources/pokedex/img/pm/2fd12098f15628cce80d411e090189aeb7d758ff.png',width=400)

    elif st.session_state["authentication_status"] == False:
        st.sidebar.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.sidebar.warning('Please enter your username and password')

def save():
    with open('config.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)

if __name__ == '__main__':
    main()
```
# 2. Streammlit认证系统
- 通过 Streamlit 应用程序实现一个基本的用户认证系统，包括登录、注册、密码重置等功能。
- 准备配置文件 `config.yaml`，包含用户凭证和 cookie 设置
## 1. `config.yaml`文件
```yml
cookie:
  expiry_days: 30
  key: some_signature_key
  name: some_cookie_name
credentials:
  usernames:
    th:
      email: 1345412477@qq.com
      failed_login_attempts: 0
      logged_in: false
      name: Tang Heng
      password: qqq
    wt:
      email: 2726234495@qq.com
      failed_login_attempts: 0
      logged_in: false
      name: Wu Tao
      password: qqq
      email: 980259394@qq.com
      failed_login_attempts: 0
      logged_in: false
      name: Wu Yuhao
      password: qqq
pre-authorized:
  emails:
  - melsby@gmail.com
```
## 2. 忘记密码
```python
import streamlit as st
from Home import save ,authenticator

from streamlit_authenticator.utilities.exceptions import (ForgotError) 

def forgot_pwd():
    try:
        (username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password) = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.success('New password sent securely')
            st.write(new_random_password)
            save()
        elif not username_of_forgotten_password:
            st.error('Username not found')
    except ForgotError as e:
        st.error(e)
         
if __name__ == '__main__':
    forgot_pwd()
```
## 2.用户注册
```python
import streamlit as st

from Home import save,authenticator
from streamlit_authenticator.utilities.exceptions import (RegisterError) 

def registration():
    try:
        (email_of_registered_user,
            username_of_registered_user,
            name_of_registered_user) = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            save()
    except RegisterError as e:
        st.error(e)
        
if __name__ == '__main__':
    registration()
```
## 3. 密码随机重置
```python
import streamlit as st

from Home import save ,authenticator
from streamlit_authenticator.utilities.exceptions import (CredentialsError,ResetError)

#密码重置
def reset_pwd():
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"]):
                st.success('Password modified successfully')
                save()
        except ResetError as e:
            st.error(e)
        except CredentialsError as e:
            st.error(e)
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    reset_pwd()
```
## 4. 更新用户信息
```python
import streamlit as st

from Home import save ,authenticator
from streamlit_authenticator.utilities.exceptions import (UpdateError) 


#更新用户信息
def update_user_details():
    if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state["username"]):
                st.success('Entries updated successfully')
                save()
        except UpdateError as e:
            st.error(e)
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    update_user_details()
```
## 5. 退出登录
```python
import streamlit as st

from Home import authenticator

def logout():
    if st.session_state["authentication_status"]:
        authenticator.logout()
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    logout()
```
# 3. Pokemon.csv数据表格视图
- 定义chart页面所有视图及其交互功能。
- 根据Pokemon.csv提供数据进行数据分析。
```python
import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')
def pre_data():
    df = pd.read_csv('data/Pokemon.csv') 
    df.columns = df.columns.str.upper().str.replace('_', '')
    df = df.set_index("NAME")
    df.index = df.index.str.replace(".*(?=Mega)","")
    df= df.drop(['#'],axis=1)
    df['TYPE 2'].fillna(df['TYPE 1'],inplace=True)
    return df

def filter_data_by_types(df, types):
    """定义数据筛选功能"""
    return df[df['TYPE 1'].isin(types) | df['TYPE 2'].isin(types)] # 筛选出指定类型的数据

def generate_statistics(df):
    """定义生成数据统计功能"""
    statistics = {}                               # 初始化统计信息字典
    statistics['总数'] = df.shape[0]             # 计算宝可梦的总数
    statistics['平均攻击力'] = df['ATTACK'].mean() # 计算平均攻击力
    statistics['平均防御力'] = df['DEFENSE'].mean() # 计算平均防御力
    statistics['平均速度'] = df['SPEED'].mean()   # 计算平均速度
    statistics['Pokemon类型分布'] = df['TYPE 1'].value_counts().to_dict() # 计算宝可梦类型分布
    statistics['平均HP'] = df['HP'].mean()       # 计算平均HP
    statistics['平均特攻'] = df['SP. ATK'].mean() # 计算平均特攻
    statistics['平均特防'] = df['SP. DEF'].mean() # 计算平均特防
    statistics['平均代数'] = df['GENERATION'].mean() # 计算平均代数
    statistics['传奇的数量'] = df['LEGENDARY'].sum() # 计算传奇宝可梦的数量
    return statistics                             # 返回统计信息字典

def show_statistics(statistics):
    """定义显示数据统计的功能"""
    st.subheader("数据统计")                     # 显示子标题'数据统计'
    st.write(f"Pokemon总数：{statistics['总数']}")   # 显示宝可梦总数
    st.write(f"平均攻击力：{statistics['平均攻击力']:.2f}") # 显示平均攻击力
    st.write(f"平均防御力：{statistics['平均防御力']:.2f}") # 显示平均防御力
    st.write(f"平均速度：{statistics['平均速度']:.2f}")   # 显示平均速度
    st.write(f"平均HP: {statistics['平均HP']:.2f}")      # 显示平均HP
    st.write(f"平均特攻：{statistics['平均特攻']:.2f}")  # 显示平均特攻
    st.write(f"平均特防：{statistics['平均特防']:.2f}")  # 显示平均特防
    st.write(f"平均代数：{statistics['平均代数']:.2f}")  # 显示平均代数
    st.write(f"传奇的数量：{statistics['传奇的数量']}")   # 显示传奇宝可梦的数量
    st.subheader("Pokemon类型分布")             # 显示子标题'宝可梦类型分布'
    type_distribution = statistics['Pokemon类型分布'] # 获取宝可梦类型分布
    num_columns = 4                              # 设置每行显示的列数
    num_types = len(type_distribution)           # 获取类型总数
    num_rows = (num_types + num_columns - 1) // num_columns # 计算需要的行数
    for i in range(num_rows):                    # 遍历每一行
        row_start = i * num_columns              # 当前行的起始索引
        row_end = min(row_start + num_columns, num_types) # 当前行的结束索引
        type_subset = list(type_distribution.items())[row_start:row_end] # 当前行的类型子集
        row_strings = [f"{type_}: {count}" for type_, count in type_subset] # 生成当前行的字符串列表
        st.write(" | ".join(row_strings))         # 将当前行的字符串列表连接并显示
```
## 1. Pokemon数据概览
```python
def data_overview():
    st.title("Pokemon数据概览")    
    
    show_all_data = st.checkbox("显示所有数据")    # 显示复选框，是否显示所有数据
    if show_all_data:
        st.write(df)                              # 如果选中，显示所有数据
    else:
        num_rows = st.number_input("显示前 N 行数据", min_value=1, max_value=len(df), value=10) # 显示数值输入框
        st.write(df.head(num_rows))               # 显示前N行数据
    
    types = df['TYPE 1'].unique().tolist()        # 获取所有宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types) # 显示多选框选择类型
    filtered_df = filter_data_by_types(df, selected_types) # 筛选出选中类型的数据
    
    st.write(f"选择的类型：{selected_types}")     # 显示选中的类型
    st.write(filtered_df)                         # 显示筛选后的数据
    
    st.subheader("编辑数据")                     # 显示子标题'编辑数据'
    index_to_edit = st.number_input("选择要编辑的数据行索引", min_value=0, max_value=len(filtered_df)-1, value=0) # 显示数值输入框选择索引
    if st.button("编辑"):                         # 显示编辑按钮
        edited_data = {}                          # 初始化字典存储编辑后的数据
        for column in filtered_df.columns:        # 遍历每一列
            edited_value = st.text_input(f"编辑 {column}", value=str(filtered_df.iloc[index_to_edit][column])) # 显示文本输入框
            edited_data[column] = edited_value    # 将编辑后的数据存入字典
        try:
            for key in edited_data:                # 遍历编辑后的数据
                filtered_df.at[index_to_edit, key] = edited_data[key] # 更新DataFrame中的数据
            st.success("数据已成功编辑。")         # 显示成功消息
        except Exception as e:                    # 捕获异常
            st.error(f"编辑数据时出现错误：{e}")    # 显示错误消息
    
    st.subheader("已编辑的数据")                 # 显示子标题'已编辑的数据'
    st.write(filtered_df)                         # 显示编辑后的数据
    
    st.subheader("下载数据")                     # 显示子标题'下载数据'
    csv = filtered_df.to_csv(index=False).encode('utf-8') # 将筛选后的数据转换为CSV格式
    st.download_button(label="点击下载文件", data=csv, file_name='filtered_data.csv', mime='text/csv') # 显示下载按钮

    if st.button("生成数据概要"):                 # 显示生成数据概要按钮
        st.toast('Ready!', icon = "🥞")
        statistics = generate_statistics(filtered_df) # 生成数据统计
        show_statistics(statistics)               # 显示数据统计
```
## 2.不同属性Pokemon防御和攻击对比
```python
def plot_scatter():
    st.title("不同属性Pokemon防御和攻击对比")    
    
    pk_type1 = st.selectbox("选择你要对比的第一种类型的Pokemon",df['TYPE 1'].unique())
    pk_type2 = st.selectbox("选择你要对比的第二种类型的Pokemon",df['TYPE 1'].unique())
    fire=df[(df['TYPE 1']==pk_type1) | ((df['TYPE 2'])==pk_type1)] #fire contains all fire pokemons
    water=df[(df['TYPE 1']==pk_type2) | ((df['TYPE 2'])==pk_type2)] #all water pokemins
    plt.scatter(fire.ATTACK.head(50),fire.DEFENSE.head(50),color='Red',label=pk_type1 ,marker="*",s=50) #scatter 
    plt.scatter(water.ATTACK.head(50),water.DEFENSE.head(50),color='Blue',label=pk_type2 ,s=25)
    plt.xlabel("ATTACK")
    plt.ylabel("DEFENCE")
    plt.legend()
    fig=plt.gcf() #get the current figure using .gcf()
    fig.set_size_inches(12,6) #set the size for the figure
    st.pyplot(plt)
    st.header('Code:')
```
## 3. Pokemon属性相关性热图
```python
def correlation_heatmap():
    st.title("Pokemon属性相关性热图") 
    
    types = df['TYPE 1'].unique().tolist()  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types)  # 显示多选框让用户选择类型
    filtered_df = filter_data_by_types(df, selected_types)  # 根据选中的类型筛选数据
    df_numeric = filtered_df.select_dtypes(include=np.number)  # 筛选出数值类型的数据
    
    fig, ax = plt.subplots(figsize=(10, 6))  # 创建一个新的指定尺寸的Matplotlib图形和轴
    sns.heatmap(df_numeric.corr(), annot=True, ax=ax)  # 绘制热图
    st.pyplot(fig)  # 在Streamlit网页上显示图表
    st.header('Code:')
```
## 4. 不同世代Pokemon类型的演变
```python
def type_evolution():
    st.title("不同世代Pokemon类型的演变") 
    
    all_types = sorted(set(df['TYPE 1'].unique().tolist() + df['TYPE 2'].unique().tolist()))  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择要查看的Pokemon类型', all_types, default=all_types[:5])  # 显示多选框让用户选择类型
    
    if selected_types:  # 如果选中了类型
        # 筛选出选择的类型数据
        df_selected = df[(df['TYPE 1'].isin(selected_types)) | (df['TYPE 2'].isin(selected_types))]
        df_selected['Type'] = df_selected.apply(lambda x: x['TYPE 1'] if x['TYPE 1'] in selected_types else x['TYPE 2'], axis=1)  # 新增一列"Type"
        type_counts = df_selected.groupby(['GENERATION', 'Type']).size().reset_index(name='counts')  # 计算每一代每种类型的数量
        chart_type = st.selectbox("选择图表类型", ["折线图", "柱状图"])  # 显示选择框选择图表类型

        fig, ax = plt.subplots(figsize=(12, 6))  # 创建一个新的指定尺寸的Matplotlib图形和轴
        for pokemon_type in selected_types:  # 遍历每一个选中类型
            data = type_counts[type_counts['Type'] == pokemon_type]  # 筛选出当前类型的数据
            if chart_type == "折线图":  # 如果选择折线图
                ax.plot(data['GENERATION'], data['counts'], label=pokemon_type)  # 绘制折线图
            elif chart_type == "柱状图":  # 如果选择柱状图
                ax.bar(data['GENERATION'], data['counts'], label=pokemon_type)  # 绘制柱状图

        ax.set_xlabel('GENERATION')  # 设置X轴标签为"世代"
        ax.set_ylabel('COUNTS')  # 设置Y轴标签为"数量"
        ax.legend()  # 显示图例
        st.pyplot(fig)  # 在Streamlit网页上显示图表
    else:  # 如果未选中任何类型
        st.warning("请选择至少一个Pokemon类型以显示图表。")  # 显示警告信息
```
## 5. Pokemon基础数值直方图
```python
def pokemon_basic_value():
    st.title("Pokemon基础数值直方图") 
    
    col = st.selectbox("显示的数据列：",["ATTACK","DEFENSE","SPEED"])
    bins=range(0,200,40) #they act as containers
    plt.hist(df[col],bins,histtype="bar",rwidth=1.2,color='blue') #hist() is used to plot a histogram
    plt.xlabel(col) #set the xlabel name
    plt.ylabel('Count') #set the ylabel name
    plt.axvline(df[col].mean(),linestyle='dashed',color='red') #draw a vertical line showing the average 
    st.pyplot(plt)
    st.header('Code:')
```
## 6. 不同类型Pokemon百分比
```python
def plot_pie():
    st.title("不同类型Pokemon百分比") 
    
    labels = 'Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Other'
    sizes = [112, 98, 70, 69, 57, 52, 44, 44, 175]
    colors = ['#33E6CC', '#FFFAFA', '#7FFF00', 'Coral', '#FA8072', '#A9A9A9', '#B399FF', '#A0522D', '#6495ED']
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0.1) # only "explode" the 3rd slice 
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
     autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title("Percentage of Different Types of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    st.pyplot(plt)
    st.header('Code:')
```
## 7. Pokemon属性的箱线图
```python
def boxplot_stats():
    st.title("Pokemon属性的箱线图")  # 设置页面标题为"宝可梦属性的箱线图"
    
    types = df['TYPE 1'].unique().tolist()  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types)  # 显示多选框让用户选择类型
    filtered_df = filter_data_by_types(df, selected_types)  # 根据选中的类型筛选数据
    st.subheader("选择显示的属性")  # 显示子标题"选择显示的属性"
    attributes = st.multiselect('选择要显示的属性', df.columns.tolist(), default=df.columns.tolist())  # 多选框让用户选择属性
    filtered_df = filtered_df[attributes]  # 筛选出选择的属性数据

    fig, ax = plt.subplots(figsize=(15, 5))  # 创建一个新的指定尺寸的Matplotlib图形和轴
    sns.boxplot(data=filtered_df.drop(['GENERATION', 'TOTAL'], axis=1, errors='ignore'), ax=ax)  # 绘制箱线图
    ax.set_ylim(0, 300)  # 设置Y轴范围
    st.pyplot(fig)  # 在Streamlit网页上显示图表
```
## 8. 不同Pokemon类型的总数和传奇状态
```python
def swarm_legendary():
    st.title("不同Pokemon类型的总数和传奇状态")  # 设置页面标题为"不同宝可梦类型的总数和传奇状态"
    
    types = df['TYPE 1'].unique().tolist()  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types)  # 显示多选框让用户选择类型
    filtered_df = filter_data_by_types(df, selected_types)  # 根据选中的类型筛选数据
    
    fig, ax = plt.subplots(figsize=(12, 6))  # 创建一个新的指定尺寸的Matplotlib图形和轴
    top_types = filtered_df['TYPE 1'].value_counts()[:10]  # 获取选择的前10个类型
    df1 = filtered_df[filtered_df['TYPE 1'].isin(top_types.index)]  # 筛选出前10个类型的数据
    sns.swarmplot(x='TYPE 1', y='TOTAL', data=df1, hue='LEGENDARY', ax=ax)  # 绘制Swarmplot散点图
    ax.axhline(df1['TOTAL'].mean(), color='red', linestyle='dashed')  # 绘制平均值的水平线
    st.pyplot(fig)  # 在Streamlit网页上显示图表
    st.header('Code:')
```
## 9. Pokemon攻击力的小提琴图
```python
def violin_attack():
    st.title("Pokemon攻击力的小提琴图")  # 设置页面标题为"宝可梦攻击力的小提琴图"
    
    types = df['TYPE 1'].unique().tolist()  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types)  # 显示多选框让用户选择类型
    filtered_df = filter_data_by_types(df, selected_types)  # 根据选中的类型筛选数据
    st.subheader("选择显示的攻击范围")  # 显示子标题"选择显示的攻击范围"
    attack_min, attack_max = st.slider("选择攻击范围", 0, 200, (0, 200))  # 显示滑动条选择攻击范围
    filtered_df = filtered_df[(filtered_df["ATTACK"] >= attack_min) & (filtered_df["ATTACK"] <= attack_max)]  # 筛选出攻击范围内的数据
    
    fig, ax = plt.subplots(figsize=(20, 10))  # 创建一个新的指定尺寸的Matplotlib图形和轴
    sns.violinplot(x="TYPE 1", y="ATTACK", data=filtered_df, ax=ax)  # 绘制小提琴图
    ax.set_ylim(0, 200)  # 设置Y轴范围
    st.pyplot(fig)  # 在Streamlit网页上显示图表
    st.header('Code:')
```
## 10. Pokemon攻击力的箱线图
```python
def boxplot_attack():
    st.title("Pokemon攻击力的箱线图")  # 设置页面标题为"宝可梦攻击力的箱线图"

    types = df['TYPE 1'].unique().tolist()  # 获取所有独特的宝可梦类型
    selected_types = st.multiselect('选择Pokemon类型进行查看', types, default=types)  # 显示多选框让用户选择类型

    if not selected_types:  # 如果未选择任何类型
        st.warning('请至少选择一个Pokemon类型进行查看。')  # 显示警告信息
        return
    
    # 根据选中的类型筛选数据
    filtered_df = filter_data_by_types(df, selected_types)
    st.subheader("选择显示的攻击范围")  # 显示子标题"选择显示的攻击范围"
    attack_min, attack_max = st.slider("选择攻击范围", 0, 200, (0, 200))  # 显示滑动条选择攻击范围
    filtered_df = filtered_df[(filtered_df["ATTACK"] >= attack_min) & (filtered_df["ATTACK"] <= attack_max)]  # 筛选出攻击范围内的数据

    if filtered_df.empty:  # 如果筛选后数据为空
        st.warning('根据选择的条件，未找到符合条件的Pokemon。')  # 显示警告信息
        return

    color = st.color_picker('选择箱线图的颜色', '#00f900')  # 显示颜色选择器选择箱线图的颜色
    fig, ax = plt.subplots(figsize=(15, 5))  # 创建一个新的指定尺寸的Matplotlib图形和轴
    sns.boxplot(x="TYPE 1", y="ATTACK", data=filtered_df, ax=ax, palette=[color for _ in range(len(selected_types))])  # 绘制箱线图
    ax.set_ylim(0, 200)  # 设置Y轴范围
    st.pyplot(fig)  # 在Streamlit网页上显示图表
    st.header('Code:')


df = pre_data()
```