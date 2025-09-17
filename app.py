import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# App Title
st.title("📊 Data Visualization Explorer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Dataset")
    st.dataframe(df.head())

    # Visualization type
    vis_type = st.selectbox("Select Visualization Type", ["1D Plot", "2D Plot", "3D Plot", "Heatmap"])

    # 1D Visualization (Histogram / Boxplot)
    if vis_type == "1D Plot":
        column = st.selectbox("Select a Column", df.columns)
        plot_type = st.radio("Select Plot Type", ["Histogram", "Boxplot"])

        fig, ax = plt.subplots()
        if plot_type == "Histogram":
            sns.histplot(df[column], kde=True, ax=ax)
        else:
            sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)

    # 2D Visualization (Scatter / Line)
    elif vis_type == "2D Plot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        plot_type = st.radio("Select Plot Type", ["Scatter", "Line"])

        fig, ax = plt.subplots()
        if plot_type == "Scatter":
            sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        else:
            sns.lineplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)

    # 3D Visualization (Scatter3D)
    elif vis_type == "3D Plot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        z_col = st.selectbox("Select Z-axis", df.columns)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(df[x_col], df[y_col], df[z_col], c='blue', marker='o')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_zlabel(z_col)
        st.pyplot(fig)

    # Heatmap (Correlation Matrix)
    elif vis_type == "Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

else:
    st.info("👆 Please upload a CSV file to start visualization.")
