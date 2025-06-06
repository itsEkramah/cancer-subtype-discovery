
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.metrics import adjusted_rand_score, confusion_matrix
import openai
import os
from dotenv import load_dotenv

# Optional: use umap if available
try:
    import umap
    UMAP_AVAILABLE = True
except ImportError:
    UMAP_AVAILABLE = False

st.set_page_config(layout="wide")
st.title("🧬 Advanced Cancer Subtype Discovery & Visualization Tool")

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Upload input files
expr_file = st.sidebar.file_uploader("Upload Gene Expression Matrix (.csv)", type=["csv"])
subtype_file = st.sidebar.file_uploader("Upload Known Subtypes (.csv)", type=["csv"])
min_var = st.sidebar.slider("Filter genes by minimum variance", 0.0, 2.0, 0.2)
k = st.sidebar.slider("Number of Clusters (KMeans)", 2, 10, 3)

# Utility: volcano plot (mocked here with random data)
def plot_volcano(df):
    fig, ax = plt.subplots()
    ax.scatter(df['log2FC'], df['-log10pval'], alpha=0.6, color='gray')
    ax.axhline(y=-np.log10(0.05), color='red', linestyle='--')
    ax.axvline(x=1, color='green', linestyle='--')
    ax.axvline(x=-1, color='green', linestyle='--')
    ax.set_title("Volcano Plot (Simulated)")
    ax.set_xlabel("log2 Fold Change")
    ax.set_ylabel("-log10 p-value")
    return fig

if expr_file:
    df = pd.read_csv(expr_file, index_col=0)
    df = df.loc[df.var(axis=1) > min_var]
    data = df.T

    st.write("📊 Dataset Summary")
    st.write(f"Shape: {data.shape}")
    st.dataframe(df.var(axis=1).sort_values(ascending=False).head(5))

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"], index=data.index)

    # KMeans
    kmeans = KMeans(n_clusters=k, random_state=42)
    pca_df["Cluster"] = kmeans.fit_predict(pca_df)

    tabs = st.tabs(["📌 PCA", "🔁 t-SNE", "🔀 UMAP", "📉 Heatmap", "🌋 Volcano Plot", "📊 Subtype Evaluation", "🤖 GPT Summary"])

    with tabs[0]:
        st.subheader("PCA Cluster Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="Cluster", palette="Set2", ax=ax)
        st.pyplot(fig)

    with tabs[1]:
        st.subheader("t-SNE Plot")
        tsne = TSNE(n_components=2, random_state=42, perplexity=10)
        tsne_result = tsne.fit_transform(data)
        tsne_df = pd.DataFrame(tsne_result, columns=["tSNE1", "tSNE2"], index=data.index)
        tsne_df["Cluster"] = pca_df["Cluster"]
        fig, ax = plt.subplots()
        sns.scatterplot(data=tsne_df, x="tSNE1", y="tSNE2", hue="Cluster", palette="Set2", ax=ax)
        st.pyplot(fig)

    with tabs[2]:
        st.subheader("UMAP Plot")
        if UMAP_AVAILABLE:
            reducer = umap.UMAP(random_state=42)
            umap_result = reducer.fit_transform(data)
            umap_df = pd.DataFrame(umap_result, columns=["UMAP1", "UMAP2"], index=data.index)
            umap_df["Cluster"] = pca_df["Cluster"]
            fig, ax = plt.subplots()
            sns.scatterplot(data=umap_df, x="UMAP1", y="UMAP2", hue="Cluster", palette="Set2", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("UMAP is not installed. Run `pip install umap-learn` to enable.")

    with tabs[3]:
        st.subheader("Top Gene Heatmap")
        try:
            top_genes = df.var(axis=1).sort_values(ascending=False).head(50).index
            fig = sns.clustermap(df.loc[top_genes], cmap="vlag", figsize=(10, 8))
            st.pyplot(fig.fig)
        except Exception as e:
            st.error(f"Heatmap error: {e}")

    with tabs[4]:
        st.subheader("Volcano Plot (Simulated)")
        mock_df = pd.DataFrame({
            'log2FC': np.random.randn(df.shape[0]),
            '-log10pval': -np.log10(np.random.rand(df.shape[0]))
        })
        fig = plot_volcano(mock_df)
        st.pyplot(fig)

    with tabs[5]:
        if subtype_file:
            subtype_df = pd.read_csv(subtype_file)
            if "Sample" in subtype_df.columns and "Subtype" in subtype_df.columns:
                subtype_df = subtype_df.set_index("Sample")
                merged = pca_df.join(subtype_df)

                true_labels = merged["Subtype"].astype("category").cat.codes
                pred_labels = merged["Cluster"]
                ari = adjusted_rand_score(true_labels, pred_labels)

                st.write(f"🎯 Adjusted Rand Index (ARI): `{ari:.2f}`")
                cm = confusion_matrix(true_labels, pred_labels)
                st.write("🔁 Confusion Matrix")
                st.dataframe(pd.DataFrame(cm))

                # Safe aggregation
                def majority_subtype(x):
                    vc = x.value_counts()
                    return vc.index[0] if not vc.empty else "Unknown"

                summary_table = merged.groupby("Cluster")["Subtype"].agg(majority_subtype)
                match_pct = merged.groupby("Cluster").apply(
                    lambda x: (x["Subtype"] == x["Subtype"].value_counts().idxmax()).mean() * 100 if not x["Subtype"].value_counts().empty else 0
                )

                st.write("📋 Subtype Match Summary")
                st.dataframe(pd.DataFrame({
                    "Majority Subtype": summary_table,
                    "Match %": match_pct.round(2),
                    "Samples in Cluster": merged["Cluster"].value_counts().sort_index()
                }))
            else:
                st.warning("Subtype CSV must have columns: 'Sample', 'Subtype'")
        else:
            st.info("Upload known subtypes to evaluate clustering accuracy")

    with tabs[6]:
        if subtype_file:
            st.subheader("ChatGPT-Generated Cancer Subtype Explanations")
            subtype_df = pd.read_csv(subtype_file)
            if "Subtype" in subtype_df.columns:
                unique_subtypes = subtype_df["Subtype"].dropna().unique().tolist()
                if st.button("🔍 Generate Subtype Summary"):
                    prompt = "Explain these cancer subtypes in plain language for a bioinformatics student: " + ", ".join(unique_subtypes)
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": prompt}],
                            max_tokens=500,
                            temperature=0.5
                        )
                        summary_text = response["choices"][0]["message"]["content"]
                        st.success("Subtype Summary Generated:")
                        st.markdown(summary_text)
                    except Exception as e:
                        st.error(f"ChatGPT Error: {e}")
            else:
                st.warning("Subtype column not found in uploaded file.")
        else:
            st.info("Upload subtype file to enable ChatGPT explanation.")
else:
    st.info("Upload gene expression data (.csv) to begin analysis.")
