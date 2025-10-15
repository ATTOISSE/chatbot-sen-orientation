# 🇸🇳 Senegal Orientation Chatbot

## 🧠 Projet de Chatbot d'Orientation Scolaire et Professionnelle pour le Sénégal

Ce projet vise à créer un agent conversationnel intelligent basé sur la technologie **RAG (Retrieval-Augmented Generation)** et un **Modèle de Langage Local (LLM)** pour fournir aux étudiants, parents et professionnels des informations précises et à jour sur les formations, les établissements et les opportunités d'orientation au Sénégal.

Le projet est entièrement conteneurisé à l'aide de **Docker** et **Docker Compose**, utilisant **Streamlit** pour l'interface utilisateur et **Ollama** pour le modèle de langage local.

***

## 🛠️ Architecture du Projet

Le système est décomposé en plusieurs services conteneurisés et suit une architecture modulaire :

| Composant | Technologie(s) | Rôle |
| :--- | :--- | :--- |
| **Backend / API** | Python, FastAPI (Optionnel), SQLAlchemy | Logique métier, gestion de la base de données, exécution des scripts d'ingestion. |
| **Chatbot Core** | LangChain  | Implémentation du RAG (Retrieval, Embeddings, Chains, Agents). |
| **Interface Utilisateur** | Streamlit | Application web interactive pour l'interface de chat et l'administration. |
| **LLM (Modèle de Langage)** | Ollama | Serveur pour héberger et servir un modèle de langage local (ex: Llama3, Mistral, Gemma). |
| **Base de Données** | PostgreSQL (via Docker) | Stockage des données structurées (formations, établissements, etc.). |
| **Vector Store** | ChromaDB | Stockage des embeddings de la documentation d'orientation. |

### Structure des Répertoires Clés

chatbot-sen-orientation/
├── config/             # Paramètres de configuration (settings, prompts)
├── data/               # Données brutes et traitées (documentation, vector store)
├── src/                # Cœur de la logique métier (RAG, DB, LLM)
├── streamlit_app/      # Code de l'interface utilisateur Streamlit
├── api/                # Code de l'API FastAPI (si utilisée)
├── docker/             # Dockerfiles et configurations Nginx
├── docker-compose.yml  # Orchestration de l'environnement de développement
└── scripts/            # Scripts d'initialisation et de maintenance

***

## ⚙️ Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre machine :

1.  **Git**
2.  **Docker**
3.  **Docker Compose** (souvent inclus avec Docker Desktop)

***

## 🚀 Démarrage Rapide (Environnement de Développement)

Suivez ces étapes pour lancer l'application localement.

### 1. Cloner le dépôt et préparer l'environnement

```bash
# Clonez le dépôt
git clone <URL_DE_VOTRE_DEPOT>
cd senegal-orientation-chatbot

# Copiez le fichier d'environnement
cp .env.example .env

# ⚠️ MODIFIEZ .env
# Remplissez les variables d'environnement nécessaires (ports, URLs de DB, LLM_MODEL)
2. Lancer les Services Docker
La commande suivante va construire les images, télécharger le modèle Ollama spécifié dans docker-compose.yml et démarrer tous les conteneurs (DB, Ollama, Backend, Streamlit).

Bash

docker-compose up --build -d
3. Initialiser la Base de Données et Ingestions des Données
Une fois les services lancés, vous devez initialiser la base de données et ingérer les données initiales pour le RAG.

Bash

# Exécute la migration de la DB (création des tables)
docker-compose exec backend python scripts/init_database.py

# Ingestion des données (chargement, découpage et création des embeddings)
# Assurez-vous d'avoir des fichiers de données dans data/raw/ avant d'exécuter ceci.
docker-compose exec backend python scripts/ingest_data.py
4. Accéder à l'Application
L'interface Streamlit est maintenant accessible.

Interface Chatbot : Ouvrez votre navigateur et accédez à http://localhost:8501

💻 Développement
Services et Ports
Service	Port	Description
streamlit	8501	Interface utilisateur principale.
ollama	11434	Point d'accès au modèle de langage.
backend	8000	API FastAPI (si utilisée).
db	5432	Base de données PostgreSQL.

Exporter vers Sheets
Commandes Utiles
Commande	Description
docker-compose down	Arrête et supprime les conteneurs, les réseaux et les volumes anonymes.
docker-compose restart [service]	Redémarre un service spécifique (ex: backend ou streamlit).
docker-compose logs -f	Affiche les logs de tous les services en temps réel.
docker-compose exec backend bash	Ouvre un shell dans le conteneur du backend pour le débogage.
docker-compose exec backend python scripts/update_vectors.py	Met à jour le vector store après l'ajout de nouvelles données.

Exporter vers Sheets
🌐 Déploiement en Production
Pour le déploiement en production, utilisez le fichier docker-compose.prod.yml qui inclut Nginx pour la gestion des proxys.

Bash

# Lancer en mode production
docker-compose -f docker-compose.prod.yml up --build -d
*(Note: La configuration de Nginx dans docker/nginx.conf doit être adaptée à votre nom de domaine et à la gestion des certificats SSL.)

🧪 Tests Unitaires
Le projet utilise pytest pour les tests unitaires et d'intégration.

Pour exécuter les tests à l'intérieur du conteneur backend :

```bash
docker-compose exec backend pytest tests/
