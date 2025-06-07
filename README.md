Here is the updated and **fully detailed** `README.md` reflecting the latest changes in your project — specifically the error fix related to clusters with missing subtype values and overall robustness improvement.

---

````markdown
# 🧬 Cancer Subtype Discovery using Unsupervised Learning

An interactive **bioinformatics dashboard** built using **Streamlit** for discovering cancer subtypes via unsupervised machine learning on gene expression data. It supports visualization, clustering, and statistical summarization, making it ideal for **transcriptomics research**, **educational use**, and **portfolio demonstration**.

---

## 🚀 Run the App Locally

```powershell
# Replace with your environment path
& "C:\Users\ekramah\AppData\Roaming\Python\Python310\Scripts\streamlit.exe" run "F:\cancer-subtype-discovery\cancer-subtype-discovery\app.py"
````

---

## 📁 Project Structure

```
cancer-subtype-discovery/
│
├── app.py                     # Main Streamlit dashboard
├── requirements.txt           # Dependencies list
├── data/                      # Sample gene expression files
├── report/                    # Generated PDF summaries (optional)
├── notebooks/                 # Exploratory notebooks (optional)
├── docs/                      # Static site or publication pages
└── README.md                  # You're reading it
```

---

## 🛠️ Features

| Feature                    | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| 📁 CSV Upload              | Upload gene expression matrix (genes × samples, .csv format)                |
| 📊 PCA + KMeans Clustering | Visualize sample clusters, Silhouette Score, and PCA explained variance     |
| 🔁 t-SNE / 🔀 UMAP         | Explore nonlinear projections for cluster separation                        |
| 📉 Expression Heatmap      | Heatmap of top-expressed genes across samples (hierarchical clustering)     |
| ⚙️ Variance Filter         | Filter genes by variance for noise reduction                                |
| 🔍 Subtype Summary Table   | Match detected clusters with majority-known subtypes using safe aggregation |
| 📤 Export Options          | Save cluster results and visualizations                                     |
| 🧾 PDF Report Generator    | Export clustering summary and visuals (optional feature)                    |

> 🧠 **New Update (June 2025)**: The code now safely handles empty subtype groups when summarizing cluster labels. Missing subtype info will return `None` instead of crashing.

---

## 🖼️ Interface Snapshots

Here are some screenshots of the application's interface:

### Screenshot 1
![Screenshot 1](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%201.png)

### Screenshot 2
![Screenshot 2](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%202025-06-07%20040123.png)

### Screenshot 3
![Screenshot 3](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%202025-06-07%20040513.png)

### Screenshot 4
![Screenshot 4](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%205.png)

### Screenshot 5
![Screenshot 5](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%206.png)

### Screenshot 6
![Screenshot 6](https://github.com/itsEkramah/cancer-subtype-discovery/raw/main/interface%20images/Screenshot%207.png)

---

## 📦 Installation

### Install via `pip`

```bash
pip install -r requirements.txt
```

### OR install manually:

```bash
pip install streamlit pandas scikit-learn matplotlib seaborn umap-learn
```

---

## ⚙️ How to Use

1. **Launch the App**

   ```bash
   streamlit run app.py
   ```

2. **Visit Localhost**
   Open your browser: `http://localhost:8501`

3. **Upload CSV File**
   Format:

   * Rows = genes (e.g., `TP53`, `BRCA1`)
   * Columns = samples (e.g., `Sample_1`, `Sample_2`)
   * Values = expression levels (e.g., TPM, RPKM, log2 Counts)

4. **Explore the Tabs**

   * PCA & KMeans clustering
   * t-SNE / UMAP projections
   * Heatmap of filtered genes
   * Subtype cluster matching

5. **Download Outputs**

   * `.csv` file with cluster labels
   * Optional: PDF summary with visualizations

---

## 🧪 Sample Files for Testing

| File Name                    | Description                             |
| ---------------------------- | --------------------------------------- |
| `gene_expression_test_1.csv` | Clean matrix, 50 samples × 10,000 genes |
| `subtypes_test_1.csv`        | Sample-to-subtype mapping               |

*You can use GSE25066 from GEO: download its Series Matrix, clean it, and save as CSV.*

---
---

## 🎯 Educational Objectives

* Learn unsupervised clustering (KMeans, UMAP, t-SNE)
* Apply dimensionality reduction to omics data
* Develop GUI-based analysis pipelines for biology
* Practice good coding habits and data handling in bioinformatics

---

## 📜 License

MIT License — Free for academic and commercial use with attribution.

---

## 👨‍💻 Author & Contact

**Muhammad Ekramah**
Bioinformatics | Machine Learning | Research Automation

📫 Connect on:

* GitHub: [itsEkramah](https://github.com/itsEkramah)
* LinkedIn: [Muhammad Ekramah](https://linkedin.com/in/itsEkramah)

---

```
