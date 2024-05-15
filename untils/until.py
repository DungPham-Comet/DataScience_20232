import streamlit as st
import pandas as pd
import altair as alt

def feature_price_plot(df, feature=''):
    if feature in df.columns:
        feature_count = df[feature].value_counts().reset_index()
        feature_count.columns = [feature, 'frequency']

        feature_price = df.groupby(feature)['price'].mean().reset_index()
        feature_price.columns = [feature, 'average_price']

        combined_df = pd.merge(feature_count, feature_price, on=feature)

        sorted_feature = combined_df.sort_values(by='average_price')[feature]

        base = alt.Chart(combined_df).encode(
            x=alt.X(feature + ':N', sort=list(sorted_feature), title=feature.title())
        )

        bar = base.mark_bar(color='blue').encode(
            y=alt.Y('frequency:Q', axis=alt.Axis(title='Frequency', titleColor='blue'))
        )

        line = base.mark_line(color='red', strokeWidth=3).encode(
            y=alt.Y('average_price:Q', axis=alt.Axis(title='Average Price', titleColor='red'))
        )

        points = base.mark_point(color='red', size=50).encode(
            y=alt.Y('average_price:Q', axis=None)
        )

        chart = alt.layer(bar, line, points).resolve_scale(
            y='independent'
        ).properties(
            width=800,
            height=500,
        )

        st.altair_chart(chart)
