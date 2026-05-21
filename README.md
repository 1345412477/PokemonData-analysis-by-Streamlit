# Pokémon Data Analysis 🐉

A Streamlit web application for exploring and analyzing Pokémon data. Dive into the world of Pokémon with interactive charts, statistical insights, and comprehensive data visualizations!

## ✨ Features

- **🔐 User Authentication** — Secure login, registration, password reset, and profile management
- **📊 Data Overview** — Browse complete Pokémon dataset with filtering by type, generation, and stats
- **📈 Interactive Charts** — Visualize Pokémon stats distributions, type comparisons, and legendary Pokémon analysis
- **🔍 Statistical Insights** — Average stats, type distribution, legendary counts, and more
- **🎨 Multiple Pages** — Project introduction, charts, and account management pages

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Core language |
| **Streamlit** | Web app framework |
| **Pandas / NumPy** | Data processing |
| **Matplotlib / Seaborn** | Data visualization |
| **Streamlit-Authenticator** | User authentication |
| **YAML** | Configuration management |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/1345412477/PokemonData-analysis-by-Streamlit.git
cd PokemonData-analysis-by-Streamlit

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Edit `config.yaml` to set up user credentials and cookie settings:

```yaml
cookie:
  expiry_days: 30
  key: your_signature_key
  name: your_cookie_name
credentials:
  usernames:
    your_username:
      email: your_email@example.com
      name: Your Name
      password: your_password
```

### Run the App

```bash
streamlit run Home.py
```

Open your browser and go to `http://localhost:8501`

## 📁 Project Structure

```
PokemonData-analysis-by-Streamlit/
├── Home.py              # App entry point & login page
├── pages.py             # Core data analysis & visualization
├── pages/               # Multi-page modules
│   ├── 1_Project Introduction.py
│   ├── 2_Chart.py
│   ├── 3_Thanks.py
│   └── ... (auth pages)
├── config.yaml          # Authentication configuration
├── data/
│   └── Pokemon.csv      # Pokémon dataset
├── image/               # App images & assets
└── requirements.txt     # Python dependencies
```

## 📊 Dataset

The app uses the classic Pokémon dataset containing:
- **Name**, **Type 1 & Type 2**
- **Base Stats**: HP, Attack, Defense, Sp. Atk, Sp. Def, Speed
- **Generation**
- **Legendary** status
- And more!

## 🎯 Use Cases

- Analyze Pokémon stat distributions by type and generation
- Compare offensive vs defensive capabilities
- Identify legendary Pokémon patterns
- Explore type effectiveness and combinations
- Educational tool for learning data analysis with Python & Streamlit

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

> 🐉 **Gotta Analyze 'Em All!** — Built with ❤️ using Streamlit
