import io
from untils.until import *

st.markdown("# Laptop price EDA & Prediction ")
df = pd.read_csv('database/data.csv', encoding='utf-8')
# df = df.drop('Unnamed: 0', axis=1)
# df = df.drop('Unnamed: 0.1', axis=1)

st.header('DataFrame')
st.write(df)

st.header('Data Info')
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

if 'price' in df.columns:
    st.header("1. Price")
    st.markdown('<h4 style="text-align: center;"> Laptop Price Distribution </h4>', unsafe_allow_html=True)

    bins = range(0, int(df['price'].max()) + 1000000, 1000000)
    labels = [f'{i // 1000000}-{(i + 1000000) // 1000000}' for i in bins[:-1]]
    df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels, right=False)
    price_dist = df['price_range'].value_counts().sort_index()

    st.bar_chart(price_dist)

    st.markdown('<h4 style="text-align: center;">Price</h4>', unsafe_allow_html=True)
    st.write(f"**Mean of Price:** {df['price'].mean()}")
    st.write(f"**Median of Price:** {df['price'].median()}")
    st.write(f"**Mode of Price:** {df['price_range'].mode().iloc[0]}")

if 'os' in df.columns:
    st.header("2. OS")
    st.markdown('<h4 style="text-align: center;"> OS and Average price </h4>', unsafe_allow_html=True)

    feature_price_plot(df, 'os')

if 'ram' in df.columns:
    st.header("3. RAM")
    st.markdown('<h4 style="text-align: center;"> Count plot showing the number of RAM capacity </h4>', unsafe_allow_html=True)

    feature_price_plot(df, 'ram')

if 'ram_max' in df.columns:
    st.header("4. RAM MAX")
    st.markdown('<h4 style="text-align: center;"> Count plot showing the number of RAM capacity </h4>', unsafe_allow_html=True)

    feature_price_plot(df, 'ram_max')

if 'vga' in df.columns:
    st.header("5. VGA")
    st.markdown('<h4 style="text-align: center;"> VGA and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'vga')

if 'battery' in df.columns:
    st.header("6. Battery")
    st.markdown('<h4 style="text-align: center;"> Battery and Average price </h4>', unsafe_allow_html=True)

    bins = range(int(df['battery'].min()), int(df['battery'].max()) + 5, 5)
    labels = [f'{i}-{(i + 5)}' for i in bins[:-1]]
    df['battery_range'] = pd.cut(df['battery'], bins=bins, labels=labels, right=False)
    df['battery_range'].value_counts()

    feature_price_plot(df, 'battery_range')

if 'weight' in df.columns:
    st.header("7. Weight")

    st.markdown('<h4 style="text-align: center;"> Weight and Price </h4>', unsafe_allow_html=True)
    df = df.reset_index()

    scatter_weight = alt.Chart(df).mark_point(size=10, color='blue').encode(
        x=alt.X('index:Q', title='Index'),
        y=alt.Y('weight:Q', title='Weight', axis=alt.Axis(titleColor='blue'))
    )

    scatter_price = alt.Chart(df).mark_point(size=10, color='red').encode(
        x=alt.X('index:Q', title='Index'),
        y=alt.Y('price:Q', title='Price', axis=alt.Axis(titleColor='red'))
    )

    combined_chart = alt.layer(scatter_weight, scatter_price).resolve_scale(
        y='independent'
    ).properties(
        width=800,
        height=400,
    )

    st.altair_chart(combined_chart)

    st.markdown('<h4 style="text-align: center;"> Scatter weight and price </h4>', unsafe_allow_html=True)
    scatter = alt.Chart(df).mark_point(size=10, color='blue').encode(
        x = alt.X('weight:Q', title='Weight'),
        y = alt.Y('price:Q', title='Price'),

    ).properties(
        width=800,
        height=400,
    )

    st.altair_chart(scatter, use_container_width=True)

if 'chipset' in df.columns:
    st.header("8. Chipset")
    st.markdown('<h4 style="text-align: center;"> Chipset and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'chipset')

if 'chipset_gen' in df.columns:
    st.header("9. Chipset gen")
    st.markdown('<h4 style="text-align: center;"> Chipset gen and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'chipset_gen')

if 'brand' in df.columns:
    st.header("10. Brand")
    st.markdown('<h4 style="text-align: center;"> Laptop brand and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'brand')

if 'storage_type' in df.columns:
    st.header("11. Storage type")
    st.markdown('<h4 style="text-align: center;"> Storage type and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'storage_type')

if 'storage' in df.columns:
    st.header("12. Storage capacity")

    # st.markdown('<h4 style="text-align: center;"> Storage capacity </h4>', unsafe_allow_html=True)
    # df = df.reset_index()
    # scatter_storage = alt.Chart(df).mark_point(size=10, color='blue').encode(
    #     x=alt.X('index:Q', title='Index'),
    #     y=alt.Y('storage:Q', title='Storage', axis=alt.Axis(titleColor='blue'))
    # )
    #
    # scatter_price = alt.Chart(df).mark_point(size=10, color='red').encode(
    #     x=alt.X('index:Q', title='Index'),
    #     y=alt.Y('price:Q', title='Price', axis=alt.Axis(titleColor='red'))
    # )
    #
    # combined_chart = alt.layer(scatter_storage, scatter_price).resolve_scale(
    #     y='independent'
    # ).properties(
    #     width=800,
    #     height=400,
    # )
    # st.altair_chart(combined_chart)

    feature_price_plot(df, 'storage')

    st.markdown('<h4 style="text-align: center;"> Scatter storage and price </h4>', unsafe_allow_html=True)
    scatter = alt.Chart(df).mark_point(size=10, color='blue').encode(
        y=alt.Y('price:Q', title='Price'),
        x=alt.X('storage:Q', title='Weight')
    ).properties(
        width=800,
        height=400,
    )

    st.altair_chart(scatter)

if 'screen_revolution' in df.columns:
    st.header("13. Screen revolution")
    st.markdown('<h4 style="text-align: center;"> Screen revolution and Average price </h4>', unsafe_allow_html=True)
    feature_price_plot(df, 'screen_revolution')

if 'screen_size' in df.columns:
    st.header("14. Screen size")

    st.markdown('<h4 style="text-align: center;"> Scatter screen size and price </h4>', unsafe_allow_html=True)
    scatter = alt.Chart(df).mark_point(size=10, color='blue').encode(
        y=alt.Y('price:Q', title='Price'),
        x=alt.X('screen_size:Q', title='Screen size')
    ).properties(
        width=800,
        height=400,
    )

    st.altair_chart(scatter)

